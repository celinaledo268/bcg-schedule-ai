import numpy as np
from sklearn.metrics import roc_auc_score


class FairnessAudit:
    def __init__(self, auroc_gap: float = 0.05, eod_gap: float = 0.10) -> None:
        self.auroc_gap = auroc_gap
        self.eod_gap = eod_gap

    def auroc_by_group(
        self, y_true: np.ndarray, y_score: np.ndarray, groups: np.ndarray
    ) -> dict[int, float]:
        out: dict[int, float] = {}
        for g in sorted(set(int(x) for x in groups)):
            mask = groups == g
            if len(np.unique(y_true[mask])) < 2:
                out[g] = float("nan")
            else:
                out[g] = float(roc_auc_score(y_true[mask], y_score[mask]))
        return out

    def equal_opportunity(
        self, y_true: np.ndarray, y_pred: np.ndarray, groups: np.ndarray
    ) -> dict[int, float]:
        out: dict[int, float] = {}
        for g in sorted(set(int(x) for x in groups)):
            mask = (groups == g) & (y_true == 1)
            out[g] = float(y_pred[mask].mean()) if mask.any() else float("nan")
        return out

    def flag(
        self, y_true: np.ndarray, y_score: np.ndarray, y_pred: np.ndarray, groups: np.ndarray
    ) -> tuple[bool, dict[str, float]]:
        aucs = [v for v in self.auroc_by_group(y_true, y_score, groups).values() if not np.isnan(v)]
        eods = [
            v for v in self.equal_opportunity(y_true, y_pred, groups).values() if not np.isnan(v)
        ]
        auroc_delta = float(max(aucs) - min(aucs)) if aucs else 0.0
        eod_delta = float(max(eods) - min(eods)) if eods else 0.0
        return auroc_delta > self.auroc_gap or eod_delta > self.eod_gap, {
            "delta_auroc": auroc_delta,
            "eod": eod_delta,
        }


def bootstrap_interval(
    values: np.ndarray, seed: int = 1337, draws: int = 1000
) -> tuple[float, float]:
    rng = np.random.default_rng(seed)
    means = np.zeros(draws, dtype=np.float32)
    n = len(values)
    for i in range(draws):
        idx = rng.integers(0, n, size=n)
        means[i] = float(values[idx].mean())
    return float(np.quantile(means, 0.025)), float(np.quantile(means, 0.975))
