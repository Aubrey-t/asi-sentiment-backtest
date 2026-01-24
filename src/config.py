"""Configuration placeholders for data paths and constants."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = ROOT / "data" / "raw"
DATA_INTERIM = ROOT / "data" / "interim"
OUTPUTS = ROOT / "outputs"
