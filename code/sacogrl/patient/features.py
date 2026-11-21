import math
from collections.abc import Sequence

import numpy as np

from sacogrl.patient.schemas import FIELD_ORDER, PatientMonth


class FeatureProjector:
    def __init__(self, state_dim: int) -> None:
        self.state_dim = state_dim

    def encode_month(self, item: PatientMonth) -> np.ndarray:
        raw = np.array([float(getattr(item, name)) for name in FIELD_ORDER], dtype=np.float32)
        scaled = raw.copy()
        scaled[0] = (scaled[0] - 70.0) / 12.0
        scaled[7] = math.log1p(max(float(scaled[7]), 0.0))
        scaled[10] = scaled[10] / 10.0
        scaled[11] = scaled[11] / 10.0
        scaled[12] = scaled[12] / 4.0
        out = np.zeros(self.state_dim, dtype=np.float32)
        n = min(len(scaled), self.state_dim)
        out[:n] = scaled[:n]
        for i in range(n, self.state_dim):
            out[i] = math.sin((i + 1) * 0.07 + float(item.month) * 0.11)
        return out

    def encode_history(self, months: Sequence[PatientMonth], history: int) -> np.ndarray:
        if history <= 0:
            raise ValueError("history must be positive")
        selected = list(months)[-history:]
        arr = np.zeros((history, self.state_dim), dtype=np.float32)
        offset = history - len(selected)
        for i, item in enumerate(selected):
            arr[offset + i] = self.encode_month(item)
        return arr

    def reward(self, item: PatientMonth, w_rfs: float, w_ae: float, w_adherence: float) -> float:
        return w_rfs * item.rfs_event - w_ae * item.ae_event + w_adherence * item.adherence
