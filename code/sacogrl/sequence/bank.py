from collections import defaultdict

import numpy as np

from sacogrl.patient.features import FeatureProjector
from sacogrl.patient.schemas import PatientMonth, TrajectoryBatch


class SequenceBank:
    def __init__(
        self, rows: list[PatientMonth], history: int, state_dim: int, gamma: float = 0.95
    ) -> None:
        self.rows = rows
        self.history = history
        self.state_dim = state_dim
        self.gamma = gamma
        self.projector = FeatureProjector(state_dim)
        self.by_patient: dict[str, list[PatientMonth]] = defaultdict(list)
        for row in rows:
            self.by_patient[row.patient_id].append(row)
        for values in self.by_patient.values():
            values.sort(key=lambda x: x.month)
        self.index: list[tuple[str, int]] = []
        for pid, months in self.by_patient.items():
            for i in range(max(0, len(months) - 1)):
                self.index.append((pid, i))

    def __len__(self) -> int:
        return len(self.index)

    def sample(self, batch_size: int, seed: int | None = None) -> TrajectoryBatch:
        rng = np.random.default_rng(seed)
        chosen = rng.integers(0, len(self.index), size=batch_size)
        states = np.zeros((batch_size, self.history, self.state_dim), dtype=np.float32)
        next_states = np.zeros_like(states)
        actions = np.zeros(batch_size, dtype=np.int64)
        rewards = np.zeros(batch_size, dtype=np.float32)
        dones = np.zeros(batch_size, dtype=np.float32)
        groups = np.zeros(batch_size, dtype=np.int64)
        weights = np.ones(batch_size, dtype=np.float32)
        for j, idx in enumerate(chosen):
            pid, pos = self.index[int(idx)]
            months = self.by_patient[pid]
            now = months[pos]
            states[j] = self.projector.encode_history(months[: pos + 1], self.history)
            next_states[j] = self.projector.encode_history(months[: pos + 2], self.history)
            actions[j] = now.action
            rewards[j] = self.projector.reward(now, 1.0, 0.30, 0.20)
            dones[j] = float(pos + 2 >= len(months))
            groups[j] = now.race_group
            weights[j] = now.weight
        return TrajectoryBatch(states, actions, rewards, next_states, dones, groups, weights)
