import numpy as np
from sacogrl.audit.fairness import FairnessAudit
from sacogrl.calibration.conformal import SplitConformalVerifier
from sacogrl.registry.synthetic import SyntheticCohort
from sacogrl.sequence.bank import SequenceBank


def test_sequence_bank_shapes() -> None:
    rows = SyntheticCohort(4, 8, seed=4).build()
    bank = SequenceBank(rows, history=6, state_dim=12)
    batch = bank.sample(5, seed=8)
    assert batch.states.shape == (5, 6, 12)
    assert batch.next_states.shape == (5, 6, 12)


def test_conformal_lower_bound() -> None:
    verifier = SplitConformalVerifier(alpha=0.1, soc_value=0.45)
    verifier.fit(np.array([0.5, 0.6, 0.7]), np.array([0.48, 0.59, 0.67]))
    result = verifier.evaluate(0.55, 0.56, 0.54)
    assert result.lower_bound <= result.value


def test_fairness_flag_runs() -> None:
    y = np.array([0, 1, 0, 1, 0, 1])
    s = np.array([0.1, 0.9, 0.2, 0.7, 0.3, 0.8])
    p = (s > 0.5).astype(int)
    g = np.array([0, 0, 1, 1, 2, 2])
    flag, stats = FairnessAudit().flag(y, s, p, g)
    assert isinstance(flag, bool)
    assert "delta_auroc" in stats
