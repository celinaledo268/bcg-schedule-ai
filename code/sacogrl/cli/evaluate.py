import argparse

from sacogrl.evaluation.evaluate import evaluate_from_config


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--checkpoint", default=None)
    args = parser.parse_args()
    summary = evaluate_from_config(args.config, args.checkpoint)
    message = (
        f"value={summary.value:.6f} "
        f"ci=({summary.interval_low:.6f},{summary.interval_high:.6f}) "
        f"fairness_flag={summary.fairness_flag} "
        f"delta_auroc={summary.delta_auroc:.6f}"
    )
    print(message)


if __name__ == "__main__":
    main()
