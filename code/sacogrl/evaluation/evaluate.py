from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import torch

from sacogrl.audit.fairness import FairnessAudit, bootstrap_interval
from sacogrl.ops.runtime import resolve_config
from sacogrl.policy.networks import AgenticPolicy
from sacogrl.registry.loading import RegistryLoader
from sacogrl.sequence.bank import SequenceBank


@dataclass(frozen=True)
class EvaluationSummary:
    value: float
    interval_low: float
    interval_high: float
    fairness_flag: bool
    delta_auroc: float


class Evaluator:
    def __init__(self, cfg: dict[str, Any], checkpoint: str | Path | None = None) -> None:
        self.cfg = cfg
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
        if checkpoint and Path(checkpoint).exists():
            obj = torch.load(checkpoint, map_location=self.device)
            self.model.load_state_dict(obj["model"])
        rows = RegistryLoader(
            cfg["paths"].get("registry_csv"), patients=64, months=int(patient["horizon_months"])
        ).load()
        self.bank = SequenceBank(
            rows, int(patient["history_months"]), int(patient["state_dim"]), float(rl["gamma"])
        )

    def run(self) -> EvaluationSummary:
        batch = self.bank.sample(256, seed=int(self.cfg["seed"]) + 99)
        states = torch.tensor(batch.states, device=self.device)
        with torch.no_grad():
            _, q, values = self.model(states)
            probs = torch.softmax(q, dim=1).max(dim=1).values.detach().cpu().numpy()
        rewards = batch.rewards
        value = float(np.mean(rewards))
        lo, hi = bootstrap_interval(rewards, draws=300)
        y_true = (rewards > np.median(rewards)).astype(np.int64)
        y_pred = (probs > np.median(probs)).astype(np.int64)
        fair, stats = FairnessAudit().flag(y_true, probs, y_pred, batch.groups)
        return EvaluationSummary(value, lo, hi, fair, float(stats["delta_auroc"]))


def evaluate_from_config(
    path: str | Path, checkpoint: str | Path | None = None
) -> EvaluationSummary:
    return Evaluator(resolve_config(path), checkpoint).run()
