from dataclasses import dataclass

import numpy as np
import torch

from sacogrl.audit.fairness import FairnessAudit
from sacogrl.audit.rules import ThresholdRuleCompiler
from sacogrl.calibration.conformal import SplitConformalVerifier
from sacogrl.registry.actions import ScheduleAction, soc_action


@dataclass(frozen=True)
class MonthDecision:
    action: ScheduleAction
    lower_bound: float
    fairness_flag: bool
    rule_text: str


class MonthlyOrchestrator:
    def __init__(
        self,
        verifier: SplitConformalVerifier,
        auditor: FairnessAudit,
        compiler: ThresholdRuleCompiler,
        soc_value: float,
    ) -> None:
        self.verifier = verifier
        self.auditor = auditor
        self.compiler = compiler
        self.soc_value = soc_value

    def decide(
        self,
        month: int,
        latent: np.ndarray,
        q_values: np.ndarray,
        ope_values: tuple[float, float, float],
        group_stats: tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray],
        clinical: np.ndarray,
    ) -> MonthDecision:
        candidate = int(np.argmax(q_values))
        result = self.verifier.evaluate(*ope_values)
        action = soc_action(month) if result.reject else ScheduleAction(candidate)
        y_true, y_score, y_pred, groups = group_stats
        fair, _ = self.auditor.flag(y_true, y_score, y_pred, groups)
        rule = self.compiler.explain(latent, clinical, int(action))
        return MonthDecision(action, result.lower_bound, fair, rule.text)

    def decide_from_model(
        self,
        month: int,
        states: torch.Tensor,
        model: torch.nn.Module,
        group_stats: tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray],
        clinical: np.ndarray,
    ) -> MonthDecision:
        model.eval()
        with torch.no_grad():
            z, q, v = model(states)
        latent = z[0].detach().cpu().numpy()
        q_values = q[0].detach().cpu().numpy()
        value = float(v[0].detach().cpu())
        return self.decide(month, latent, q_values, (value, value, value), group_stats, clinical)
