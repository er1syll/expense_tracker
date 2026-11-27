import argparse
import csv
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Calculate expenses by category and month from a CSV file."
    )
    parser.add_argument(
        "filepath",
        type=Path,
        help="Path to the UTF-8 CSV file with expenses",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    # Now use args.filepath instead of 'expense_tracker/expenses.csv'
    with open(args.filepath, mode="r", encoding="utf-8", newline="") as expen:
        csv_reader = csv.reader(expen)
        for row in csv_reader:
            print(row)


if __name__ == "__main__":
    main()