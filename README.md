kasi-sentiment-backtest
=======================

Project scaffold for sentiment backtest and data prep.

Structure

- data/
  - raw/        # put NDA raw files here (NOT committed)
  - interim/    # cleaned intermediate outputs
- notebooks/
  - 01_task1_data_prep.ipynb
- src/
  - __init__.py
  - config.py
  - prep.py
- outputs/
  - figures/
  - tables/
- .gitignore
- requirements.txt

Quick start

1. Open this folder in VS Code.
2. Create a virtual environment using Python 3.11+.
3. Install dependencies from `requirements.txt`.
4. Put raw data into `data/raw/` and run the notebook to start cleaning.
