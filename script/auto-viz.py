"""
Goal: Create AutoViz report for each level (memory-efficient).

Author: Rudra Prasad Bhuyan
Time: 25-10-2025 18:40 IST
"""

# ----------------------------------------------------------------
#                          Imports
# ----------------------------------------------------------------
import os
import pandas as pd
from loguru import logger
from autoviz.AutoViz_Class import AutoViz_Class

# ----------------------------------------------------------------
#                          Logging
# ----------------------------------------------------------------
logger.remove()
logger.add("autoviz_log_{time}.log", level="INFO", rotation="1 day")
logger.add(lambda msg: print(msg, end=""))  

# ----------------------------------------------------------------
#                          Paths
# ----------------------------------------------------------------
root_dir = r"C:\Users\Rudra\Desktop\rural-financial-inclusion-govt-scheme-recommendation\parquet-data"

# Initialize 
AV = AutoViz_Class()
ROW_SIZE = 1_00_000
COLUMN_SIZE = 50

# ----------------------------------------------------------------
#                          Data Profiling
# ----------------------------------------------------------------
for i in range(1, 16):
    try:
        level_dir = os.path.join(root_dir, f"lev-{i:02d}")
        csv_path = os.path.join(level_dir, f"lev-{i:02d}_merged.csv")
        report_path = os.path.join(level_dir, f"lev-{i:02d}_autoviz.html")

        logger.info(f"Fetching data from {csv_path}")

        if not os.path.exists(csv_path):
            logger.warning(f"CSV not found for lev-{i:02d}")
            continue

        df = pd.read_csv(csv_path)

        # Generate AutoViz report
        dft = AV.AutoViz(
            filename="",         
            dfte=df,
            depVar="",
            chart_format="html",
            save_plot_dir=level_dir,
            max_rows_analyzed=ROW_SIZE,
            max_cols_analyzed=COLUMN_SIZE
        )

        logger.success(f"\n\n\n =========================== lev-{i:02d} AutoViz Report Created. =========================== \n\n\n")

        # Free memory explicitly
        del df, dft

    except Exception as e:
        logger.error(f"----->>> Error at lev-{i:02d}: {e}\n")