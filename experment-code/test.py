""" 
Goal: Create the pandas profilling for each level.

Author: Rudra Prasad Profiling
Time: 25-10-2025 18:20 IST
"""

import os
import pandas as pd
from loguru import logger
from ydata_profiling import ProfileReport

root_dir = r"C:\Users\Rudra\Desktop\rural-financial-inclusion-govt-scheme-recommendation\parquet-data"

for i in range(1, 16):
    try:
        level_dir = os.path.join(root_dir, f"lev-{i:02d}")
        logger.info(f"Fetch the {level_dir}")
        
        csv_path = os.path.join(level_dir, f"lev-{i:02d}_merged.csv")
        df = pd.read_csv(csv_path) 
        logger.info(f"Data is ready.")
        
        profile = ProfileReport(df, minimal=True, title=f"lev-{i:02d}-data-profile")
        logger.info(f"Generating report ....")
        
        profile.to_file(f"lev-{i:02d}-report.html")
        logger.success(f"\n\n\n ======================= lev-{i:02d} Report Created! ======================= \n\n\n")

    except Exception as e:
        logger.error(f"Eror at lev-{i:02d}: {e} \n")