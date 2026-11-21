import torch
import torch.nn.functional as F


class CQLLoss:
    def __init__(self, gamma: float, alpha: float) -> None:
        self.gamma = gamma
        self.alpha = alpha

    def __call__(
        self,
        q: torch.Tensor,
        next_q: torch.Tensor,
        actions: torch.Tensor,
        rewards: torch.Tensor,
        dones: torch.Tensor,
        weights: torch.Tensor,
    ) -> tuple[torch.Tensor, dict[str, float]]:
        chosen = q.gather(1, actions.view(-1, 1)).squeeze(1)
        target = rewards + self.gamma * next_q.max(dim=1).values * (1.0 - dones)
        td = F.mse_loss(chosen, target.detach(), reduction="none")
        conservative = torch.logsumexp(q, dim=1) - chosen
        loss = ((td + self.alpha * conservative) * weights).mean()
        return loss, {
            "td": float(td.mean().detach().cpu()),
            "cql": float(conservative.mean().detach().cpu()),
        }


class IQLLoss:
    def __init__(self, tau: float = 0.7, beta: float = 3.0) -> None:
        self.tau = tau
        self.beta = beta

    def expectile(self, diff: torch.Tensor) -> torch.Tensor:
        weight = torch.where(diff > 0, self.tau, 1.0 - self.tau)
        return weight * diff.pow(2)

    def value_loss(self, q: torch.Tensor, v: torch.Tensor) -> torch.Tensor:
        return self.expectile(q.max(dim=1).values.detach() - v).mean()

    def advantage_weights(self, q: torch.Tensor, v: torch.Tensor) -> torch.Tensor:
        adv = q.max(dim=1).values - v
        return torch.exp(self.beta * adv).clamp(max=100.0)


def reward_tensor(
    rfs: torch.Tensor,
    ae: torch.Tensor,
    adherence: torch.Tensor,
    w_rfs: float,
    w_ae: float,
    w_adherence: float,
) -> torch.Tensor:
    return w_rfs * rfs - w_ae * ae + w_adherence * adherence
