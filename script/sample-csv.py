"""
Goal:
- Convert all parquet datasets into sample CSV files
- Understand how to merge datasets

Author: Rudra Prasad Bhuyan
Created Time: 16-01-2026 13:20 IST
"""

import os
import polars as pl
from loguru import logger

# Logger setup
logger.remove()
logger.add(
    "sample_csv_log_{time}.log",
    format="{time: YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="INFO",
    rotation="1 day",
)

# Root directory
ROOT_PATH = r"C:\Users\Rudra\Desktop\rural-financial-inclusion-govt-scheme-recommendation\parquet-data"

OUTPUT_DIR = "sample-csv"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Loop from lev-01 to lev-15
for i in range(1, 16):
    level = f"{i:02d}"  # 01, 02, ..., 15

    parquet_path = os.path.join(
        ROOT_PATH,
        f"lev-{level}",
        "data",
        f"lev-{level}_merged.parquet"
    )

    try:
        logger.info(f"Reading {parquet_path}")

        df = pl.read_parquet(parquet_path, n_rows=1000)

        csv_path = os.path.join(OUTPUT_DIR, f"sample-lev-{level}.csv")
        df.write_csv(csv_path)

        logger.success(f"Saved sample CSV: {csv_path}\n\n\n")

    except Exception as e:
        logger.error(f"Failed for lev-{level}: {e}")
