from dataclasses import dataclass

import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_text


@dataclass(frozen=True)
class RuleDecision:
    text: str
    agreement: float


class ThresholdRuleCompiler:
    def __init__(self, depth: int) -> None:
        self.depth = depth
        self.tree = DecisionTreeClassifier(max_depth=depth, random_state=1337)
        self.feature_names = ["latent_0", "latent_1", "eortc", "g3_ae", "month"]
        self.ready = False

    def fit(self, latent: np.ndarray, clinical: np.ndarray, actions: np.ndarray) -> None:
        x = np.concatenate([latent[:, :2], clinical], axis=1)
        self.tree.fit(x, actions)
        self.ready = True

    def explain(self, latent: np.ndarray, clinical: np.ndarray, action: int) -> RuleDecision:
        if not self.ready:
            text = "rule_unavailable_until_compiler_fit"
            return RuleDecision(text, 0.0)
        x = np.concatenate([latent[:2], clinical]).reshape(1, -1)
        pred = int(self.tree.predict(x)[0])
        agreement = float(pred == int(action))
        tree_text = export_text(self.tree, feature_names=self.feature_names, max_depth=self.depth)
        first = tree_text.splitlines()[0] if tree_text.splitlines() else "tree_empty"
        return RuleDecision(first, agreement)
