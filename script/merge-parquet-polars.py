""" 
Goal: Merge all single file for each level and make one parquet dataset.

Author: Rudra Prasad Bhuyan
Starting Time: 25-10-2025
"""

# ----------------------------------------------------------------
#                          Imports
# ----------------------------------------------------------------
import os
import pandas as pd
import pyarrow.parquet as pq
from loguru import logger

# ----------------------------------------------------------------
#                          Simple Logging
# ----------------------------------------------------------------
logger.remove()

logger.add(
    "merge_parquet_log_{time}.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="INFO",
    rotation="1 day"
)

# ----------------------------------------------------------------
#                      Each Level Scanning
# ----------------------------------------------------------------
def merge_parquet_files(lev_dir: str, output_file: str):
    """Merge all the parqet files present in each level directory.
    
    Args:
        lev_dir (str): Each Level directory
        output_file (str): Concatenate Outout files.
    """
    
    try:
        # Search the parquet fiels
        parquet_files = [f for f in os.listdir(lev_dir) if f.endswith('.parquet')]
        
        if not parquet_files:
            logger.warning(f"No parquet files found in {lev_dir}")
            return
        
        logger.info(f"Found {len(parquet_files)} parquet_files chunk files in {lev_dir}")
        
        dfs = []
        
        # Check the chunks files
        for file in parquet_files:
            file_path = os.path.join(lev_dir, file)
            logger.info(f"Reading file {file_path}")
            
            df = pd.read_parquet(file_path)
            dfs.append(df)
            logger.info(f"This chunks {file} appended in {lev_dir}")
        
        # Append in the dfs and merge (for parquet output)
        final_df = pd.concat(dfs, ignore_index=True)
        final_df.to_parquet(output_file, index=False)
        logger.info(f"\n Parquet Merged files from {lev_dir} into {output_file}")
        
    except Exception as e:
        logger.error(f"-----> Error mergining parquet files fomr {lev_dir}: {e} \n")

# ----------------------------------------------------------------
#                       Root Level Scanning
# ----------------------------------------------------------------
def merge_all_parquet_files(root_dir: str):
    """Merge all the parquet files inside each level directories.

    Args:
        root_dir (str): File path of root file where each level present.
    """
    
    try:
        # Check the each level folder
        lev_dirs = []
        for folder in os.listdir(root_dir):
            folder_path = os.path.join(root_dir, folder)
            if os.path.isdir(folder_path) and folder.startswith('lev-'):
                lev_dirs.append(folder_path)
                logger.info(f"{folder_path} is append in {lev_dirs}")
        logger.success(f"\n\n\n  {'='*25} All level fetch successfully.{'='*25} \n\n\n")
                
        if not lev_dirs:
            logger.warning(f"\n -----> No 'lev-*' directories found in {root_dir} <----- \n")
            return

        logger.info(f"Found {len(lev_dirs)} level directories: {lev_dirs}")
        
        # Merge all praquet files for each level
        for lev_dir in lev_dirs:
            level = os.path.basename(lev_dir)        
            parquet_output_file = os.path.join(lev_dir, f"{level}_merged.parquet")
            merge_parquet_files(lev_dir, parquet_output_file)
            
            logger.success(f" \n\n\n  {'='*25} {level} Merged Completed. {'='*25} \n\n\n ")
        
        logger.success(f"All levels have been processed.")
            
    except Exception as e:
        logger.error(f"-----> Error merginig parquet files from root directory {root_dir}: {e}")
        

if __name__ ==  "__main__":
    # Root directory where lev-01, lev-02, ... folders are located
    root_dir = r"C:\Users\Rudra\Desktop\rural-financial-inclusion-govt-scheme-recommendation\parquet-data"
    
    merge_all_parquet_files(root_dir)