import os
import pandas as pd
import pyarrow.parquet as pq
from loguru import logger

# Set up the logger
logger.add("merge_parquet.log", rotation="1 day", level="INFO", format="{time} {level} {message}")

def merge_parquet_files(lev_dir: str, output_file: str):
    try:
        # Find all parquet chunks in the given level directory
        parquet_files = [f for f in os.listdir(lev_dir) if f.endswith('.parquet')]
        
        if not parquet_files:
            logger.warning(f"No parquet files found in {lev_dir}")
            return

        logger.info(f"Found {len(parquet_files)} parquet chunk files in {lev_dir}")
        
        # Initialize an empty list to collect dataframes
        dfs = []
        
        for file in parquet_files:
            file_path = os.path.join(lev_dir, file)
            logger.info(f"Reading file {file_path}")
            
            # Read parquet file into dataframe
            df = pd.read_parquet(file_path)
            dfs.append(df)
        
        # Concatenate all dataframes into one
        final_df = pd.concat(dfs, ignore_index=True)
        
        # Write the merged dataframe into a single parquet file
        final_df.to_parquet(output_file, index=False)
        logger.info(f"Merged files from {lev_dir} into {output_file}")
    
    except Exception as e:
        logger.error(f"Error merging parquet files from {lev_dir}: {e}")

def merge_all_parquet_files(root_dir: str):
    try:
        # Loop through all the 'lev-xx' directories
        lev_dirs = [os.path.join(root_dir, d) for d in os.listdir(root_dir) if os.path.isdir(os.path.join(root_dir, d)) and d.startswith('lev-')]

        if not lev_dirs:
            logger.warning(f"No 'lev-*' directories found in {root_dir}")
            return
        
        logger.info(f"Found {len(lev_dirs)} level directories: {lev_dirs}")
        
        # Merge parquet files for each level
        for lev_dir in lev_dirs:
            level = os.path.basename(lev_dir)  # e.g., 'lev-01'
            output_file = os.path.join(lev_dir, f"{level}_merged.parquet")
            
            logger.info(f"Starting to merge parquet files in {lev_dir}")
            merge_parquet_files(lev_dir, output_file)
        
        logger.info("All levels have been processed.")
    
    except Exception as e:
        logger.error(f"Error merging parquet files from root directory {root_dir}: {e}")

if __name__ == "__main__":
    # Root directory where lev-01, lev-02, ... folders are located
    root_dir = r"C:\Users\Rudra\Desktop\rural-financial-inclusion-govt-scheme-recommendation\parquet-data"
    
    # Start the merging process
    merge_all_parquet_files(root_dir)
