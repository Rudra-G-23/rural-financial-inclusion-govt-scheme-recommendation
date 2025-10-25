"""
Goal: Convert all parquet dataset into CSV file format.

Author: Rudra Prasad Bhuyan
Start Time: 25-10-2025 17:43 IST
"""
# ----------------------------------------------------------------
#                          Imports
# ----------------------------------------------------------------
import os
import sys
import pandas as pd
from loguru import logger

# ----------------------------------------------------------------
#                          Logging
# ----------------------------------------------------------------
logger.remove()

logger.add(
    sys.stdout,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="INFO",
)
logger.add(
    "conversion-csv-log-{time}.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="INFO",
    rotation="1 day"
)

root_dir = r"C:\Users\Rudra\Desktop\rural-financial-inclusion-govt-scheme-recommendation\parquet-data"

# ----------------------------------------------------------------
#                          Conversion
# ----------------------------------------------------------------
for i in range(1, 16):
    try:
        level_dir = os.path.join(root_dir, f"lev-{i:02d}")
        logger.info(f"Fetch the {level_dir}")
        
        parquet_path = os.path.join(level_dir, f"lev-{i:02d}_merged.parquet")
        logger.info(f"Find the merged parquet file successfully.")
        
        csv_path = os.path.join(level_dir, f"lev-{i:02d}_merged.csv")
        df = pd.read_parquet(parquet_path)
        df.to_csv(csv_path, index=False)
        
        logger.success(f"\n\n\n ======================= lev-{i:02d} parquet convert to CSV file. ======================= \n\n\n")

    except Exception as e:
        logger.error(f"----->>> Error at lev-{i:02d}: {e}\n")