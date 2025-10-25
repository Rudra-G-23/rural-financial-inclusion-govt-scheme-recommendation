"""
Goal: Create the pandas profiling report for each level (memory-efficient).

Author: Rudra Prasad Bhuyan
Time: 25-10-2025 18:20 IST
"""

# ----------------------------------------------------------------
#                          Imports
# ----------------------------------------------------------------
import os
import pandas as pd
from loguru import logger
from ydata_profiling import ProfileReport

# ----------------------------------------------------------------
#                          Logging
# ----------------------------------------------------------------
logger.remove()
logger.add("profiling_log_{time}.log", level="INFO", rotation="1 day")
logger.add(lambda msg: print(msg, end=""))  

root_dir = r"C:\Users\Rudra\Desktop\rural-financial-inclusion-govt-scheme-recommendation\parquet-data"

# ----------------------------------------------------------------
#                          Data Profiling
# ----------------------------------------------------------------
for i in range(1, 16):
    try:
        level_dir = os.path.join(root_dir, f"lev-{i:02d}")
        csv_path = os.path.join(level_dir, f"lev-{i:02d}_merged.csv")
        report_path = os.path.join(level_dir, f"lev-{i:02d}_report.html")

        logger.info(f"Fetching data from {csv_path}")

        if not os.path.exists(csv_path):
            logger.warning(f"CSV not found for lev-{i:02d}")
            continue

        # Read only a sample if the file is huge
        file_size = os.path.getsize(csv_path) / (1024 * 1024)  # MB
        if file_size > 500:  # for large files > 500 MB
            logger.info(f"Large file ({file_size:.1f} MB). Sampling 250,000 rows for profiling.")
            df = pd.read_csv(csv_path, nrows= 2_000_000)
        else:
            df = pd.read_csv(csv_path)

        logger.info(f"Data loaded. Shape: {df.shape}")

        # Generate minimal profile
        profile = ProfileReport(
            df,
            title=f"lev-{i:02d} Data Profile",
            minimal=True,
            explorative=False,
            progress_bar=True,
        )

        profile.to_file(report_path)
        logger.success(f"\n\n\n =========================== lev-{i:02d} Report Created. =========================== \n\n\n")

        # Free memory explicitly
        del df, profile

    except Exception as e:
        logger.error(f"----->>> Error at lev-{i:02d}: {e}\n")
