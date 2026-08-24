"""Example descriptive script.

Demonstrates the two rules that matter most in this repository:

1. Paths are derived from a single ROOT variable, never hardcoded.
2. Inputs come from data/, outputs go to output/<same subfolder as this script>.

Run from anywhere:
    python code/descriptive/summaryStats.py
"""

from pathlib import Path

import pandas as pd

# --- paths ------------------------------------------------------------------
# This file is at <root>/code/descriptive/summaryStats.py, so the repo root is
# two levels up. Everything else is built from ROOT.
ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
OUTPUT = ROOT / "output" / "descriptive"
INTERMEDIATE = ROOT / "intermediate" / "descriptive"


def load_sample() -> pd.DataFrame:
    """Load the input table.

    In a real project this reads from DATA. Here we build a tiny frame in memory
    so the script runs without the Dropbox junctions being set up.
    """
    infile = DATA / "sample.csv"
    if infile.exists():
        return pd.read_csv(infile)

    print(f"{infile} not found - using built-in demo data instead.")
    return pd.DataFrame(
        {
            "prefecture": ["Tokyo", "Osaka", "Aichi", "Fukuoka"],
            "population": [14_000_000, 8_800_000, 7_500_000, 5_100_000],
            "employment": [8_200_000, 4_400_000, 3_900_000, 2_600_000],
        }
    )


def main() -> None:
    df = load_sample()

    stats = df.describe().transpose()
    print(stats)

    OUTPUT.mkdir(parents=True, exist_ok=True)
    outfile = OUTPUT / "summaryStats.csv"
    stats.to_csv(outfile)
    print(f"Wrote {outfile}")


if __name__ == "__main__":
    main()
