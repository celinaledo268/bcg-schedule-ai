from dataclasses import dataclass
from pathlib import Path
from typing import Any

import torch
from torch.optim import AdamW

from sacogrl.ops.runtime import atomic_torch_save, resolve_config, set_seed
from sacogrl.policy.losses import CQLLoss
from sacogrl.policy.networks import AgenticPolicy
from sacogrl.registry.loading import RegistryLoader
from sacogrl.sequence.bank import SequenceBank


@dataclass(frozen=True)
class TrainSummary:
    steps: int
    final_loss: float
    checkpoint: str


class Trainer:
    def __init__(self, cfg: dict[str, Any]) -> None:
        self.cfg = cfg
        set_seed(int(cfg["seed"]))
        patient = cfg["patient"]
        model_cfg = cfg["model"]
        rl = cfg["rl"]
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = AgenticPolicy(
            int(patient["state_dim"]),
            int(model_cfg["transformer_width"]),
            int(model_cfg["transformer_depth"]),
            int(model_cfg["transformer_heads"]),
            int(model_cfg["latent_dim"]),
            int(model_cfg["action_hidden"]),
            int(rl["action_count"]),
        ).to(self.device)
        self.target = AgenticPolicy(
            int(patient["state_dim"]),
            int(model_cfg["transformer_width"]),
            int(model_cfg["transformer_depth"]),
            int(model_cfg["transformer_heads"]),
            int(model_cfg["latent_dim"]),
            int(model_cfg["action_hidden"]),
            int(rl["action_count"]),
        ).to(self.device)
        self.target.load_state_dict(self.model.state_dict())
        self.loss_fn = CQLLoss(float(rl["gamma"]), float(rl["cql_alpha"]))
        self.opt = AdamW(
            self.model.parameters(),
            lr=float(cfg["training"]["lr"]),
            weight_decay=float(cfg["training"].get("weight_decay", 0.0)),
        )
        rows = RegistryLoader(
            cfg["paths"].get("registry_csv"), patients=64, months=int(patient["horizon_months"])
        ).load()
        self.bank = SequenceBank(
            rows, int(patient["history_months"]), int(patient["state_dim"]), float(rl["gamma"])
        )

    def step(self, idx: int) -> float:
        tr = self.cfg["training"]
        batch = self.bank.sample(int(tr["batch_size"]), seed=int(self.cfg["seed"]) + idx)
        states = torch.tensor(batch.states, device=self.device)
        next_states = torch.tensor(batch.next_states, device=self.device)
        actions = torch.tensor(batch.actions, device=self.device)
        rewards = torch.tensor(batch.rewards, device=self.device)
        dones = torch.tensor(batch.dones, device=self.device)
        weights = torch.tensor(batch.weights, device=self.device)
        _, q, _ = self.model(states)
        with torch.no_grad():
            _, next_q, _ = self.target(next_states)
        loss, _ = self.loss_fn(q, next_q, actions, rewards, dones, weights)
        torch.autograd.backward(loss)
        torch.nn.utils.clip_grad_norm_(self.model.parameters(), float(tr.get("grad_clip", 1.0)))
        self.opt.step()
        self.opt.zero_grad(set_to_none=True)
        if (idx + 1) % int(tr.get("target_update", 2000)) == 0:
            self.target.load_state_dict(self.model.state_dict())
        return float(loss.detach().cpu())

    def run(self) -> TrainSummary:
        steps = int(self.cfg["training"]["steps"])
        final = 0.0
        for idx in range(steps):
            final = self.step(idx)
        ckpt_dir = Path(str(self.cfg["paths"]["checkpoint_dir"]))
        ckpt = ckpt_dir / "latest.pt"
        atomic_torch_save(
            {"model": self.model.state_dict(), "seed": int(self.cfg["seed"]), "config": self.cfg},
            ckpt,
        )
        return TrainSummary(steps, final, str(ckpt))


def train_from_config(path: str | Path) -> TrainSummary:
    return Trainer(resolve_config(path)).run()
