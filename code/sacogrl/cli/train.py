import argparse

from sacogrl.training.trainer import train_from_config


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    summary = train_from_config(args.config)
    print(
        f"steps={summary.steps} final_loss={summary.final_loss:.6f} checkpoint={summary.checkpoint}"
    )


if __name__ == "__main__":
    main()
