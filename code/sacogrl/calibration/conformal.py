from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class ConformalResult:
    value: float
    radius: float
    lower_bound: float
    reject: bool


class SplitConformalVerifier:
    def __init__(self, alpha: float, soc_value: float) -> None:
        self.alpha = alpha
        self.soc_value = soc_value
        self.scores: np.ndarray | None = None
        self.radius: float = 0.0

    def fit(self, predicted: np.ndarray, realized: np.ndarray) -> None:
        if predicted.shape != realized.shape:
            raise ValueError("predicted and realized must have equal shape")
        scores = predicted - realized
        self.scores = scores
        n = len(scores)
        if n == 0:
            raise ValueError("calibration set is empty")
        q = min(1.0, (1.0 - self.alpha) * (1.0 + 1.0 / n))
        self.radius = float(np.quantile(scores, q, method="higher"))

    def evaluate(self, fqe: float, dr: float, wis: float) -> ConformalResult:
        value = (float(fqe) + float(dr) + float(wis)) / 3.0
        lower = value - self.radius
        return ConformalResult(value, self.radius, lower, lower < self.soc_value)


class CalibrationReweighter:
    def __init__(self, floor: float = 0.25, ceiling: float = 4.0) -> None:
        self.floor = floor
        self.ceiling = ceiling

    def weights(self, groups: np.ndarray) -> np.ndarray:
        unique, counts = np.unique(groups, return_counts=True)
        total = float(len(groups))
        table = {
            int(g): total / (len(unique) * float(c)) for g, c in zip(unique, counts, strict=False)
        }
        return np.array(
            [min(self.ceiling, max(self.floor, table[int(g)])) for g in groups], dtype=np.float32
        )
