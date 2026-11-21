from typing import cast

import torch
from torch import nn


class ConstraintTransformer(nn.Module):
    def __init__(self, state_dim: int, width: int, depth: int, heads: int, latent_dim: int) -> None:
        super().__init__()
        self.input = nn.Linear(state_dim, width)
        layer = nn.TransformerEncoderLayer(
            width, heads, width * 4, dropout=0.1, batch_first=True, activation="gelu"
        )
        self.encoder = nn.TransformerEncoder(layer, depth)
        self.norm = nn.LayerNorm(width)
        self.out = nn.Linear(width, latent_dim)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        h = self.input(x)
        z = self.encoder(h)
        return cast(torch.Tensor, self.out(self.norm(z[:, -1])))


class ScheduleQNetwork(nn.Module):
    def __init__(self, latent_dim: int, hidden: int, actions: int) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(latent_dim, hidden),
            nn.GELU(),
            nn.LayerNorm(hidden),
            nn.Linear(hidden, hidden),
            nn.GELU(),
            nn.Linear(hidden, actions),
        )

    def forward(self, z: torch.Tensor) -> torch.Tensor:
        return cast(torch.Tensor, self.net(z))


class ValueHead(nn.Module):
    def __init__(self, latent_dim: int, hidden: int) -> None:
        super().__init__()
        self.net = nn.Sequential(nn.Linear(latent_dim, hidden), nn.SiLU(), nn.Linear(hidden, 1))

    def forward(self, z: torch.Tensor) -> torch.Tensor:
        return cast(torch.Tensor, self.net(z).squeeze(-1))


class AgenticPolicy(nn.Module):
    def __init__(
        self,
        state_dim: int,
        width: int,
        depth: int,
        heads: int,
        latent_dim: int,
        hidden: int,
        actions: int,
    ) -> None:
        super().__init__()
        self.encoder = ConstraintTransformer(state_dim, width, depth, heads, latent_dim)
        self.q = ScheduleQNetwork(latent_dim, hidden, actions)
        self.value = ValueHead(latent_dim, hidden)

    def forward(self, states: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
        z = self.encoder(states)
        return z, self.q(z), self.value(z)

    def act(self, states: torch.Tensor) -> torch.Tensor:
        _, q, _ = self.forward(states)
        return q.argmax(dim=-1)
