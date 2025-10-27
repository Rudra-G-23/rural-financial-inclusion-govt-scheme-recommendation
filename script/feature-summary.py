""" 
Goal: This is the helping script for the features summary.

Author: Rudra Prasad Bhuyan
Data: 27-10-2025 20:11 IST
"""

# ----------------------------------------------------------------
#                          Imports
# ----------------------------------------------------------------
import os
import sys
import polars as pl
from loguru import logger
from datetime import datetime

# ----------------------------------------------------------------
#                          Logging
# ----------------------------------------------------------------
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

logger.add(
    sys.stdout,
    colorize=True,
    format="<blue>{time:YYYY-MM-DD HH:mm:ss}</blue> | "
           "<level>{level: <8}</level> | "
           "<cyan>{message}</cyan>\n",
    level="INFO"
)

logger.add(
    f"parquet-data/lev-02/data/level-02-feature-summary-log_{timestamp}.log",
    encoding="utf-8",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {message}",
    level="INFO",
    rotation="1 day"
)

# ----------------------------------------------------------------
#                          File Path
# ----------------------------------------------------------------
file_path = r"C:\Users\Rudra\Desktop\rural-financial-inclusion-govt-scheme-recommendation\parquet-data\lev-01\data\lev-01_merged.parquet"
file_path = r"parquet-data\lev-02\data\lev-02_merged.parquet"
#file_path = r"parquet-data\lev-03\data\lev-03_merged.parquet"
#file_path = r"parquet-data\lev-04\data\lev-04_merged.parquet"
#file_path = r"parquet-data\lev-05\data\lev-05_merged.parquet"
#file_path = r"parquet-data\lev-06\data\lev-06_merged.parquet"
#file_path = r"parquet-data\lev-07\data\lev-07_merged.parquet"
#file_path = r"parquet-data\lev-08\data\lev-08_merged.parquet"
#file_path = r"parquet-data\lev-09\data\lev-09_merged.parquet"
#file_path = r"parquet-data\lev-10\data\lev-10_merged.parquet"
#file_path = r"parquet-data\lev-11\data\lev-11_merged.parquet"
#file_path = r"parquet-data\lev-12\data\lev-12_merged.parquet"
#file_path = r"parquet-data\lev-13\data\lev-13_merged.parquet"
#file_path = r"parquet-data\lev-14\data\lev-14_merged.parquet"
#file_path = r"parquet-data\lev-15\data\lev-15_merged.parquet"



if not os.path.exists(file_path):
    logger.error(f"----->>> File not found: {os.path.abspath(file_path)}")
else:
    pdf = pl.read_parquet(file_path)
    logger.info(f"Successfully loaded {file_path}")
    #logger.info(f"Column Schema: {pdf.schema}")
    logger.info(f"File size: {pdf.estimated_size(unit='mb')} MB \n\n\n")
    
# ----------------------------------------------------------------
#                          Summary
# ----------------------------------------------------------------
def summary_of_col(col):
    logger.info(f" === {col} Summary === ")
    
    try:       
        desc = pdf[col].describe(percentiles=(0.25, 0.5, 0.75))
        dup_count = pdf[col].is_duplicated().sum()
        missing_count = pdf[col].is_null().sum()
        data_type= pdf[col].dtype
        unique_count = pdf[col].n_unique()
        top_value = pdf[col].mode()[0]

        logger.info(f"Data type: {data_type}")
        logger.info(f"Duplicates: {dup_count}")
        logger.info(f"Missing Values: {missing_count}")
        logger.info(f"unique Values: {unique_count}")
        logger.info(f"Top Value: {top_value}")
        logger.info("\n" + desc.__str__()) # Polar tables to string safely 
        
    except Exception as e:
        logger.error(f"----->>> Error processing {col}: {e}")

for i, col in enumerate(pdf.columns, start=1):
    logger.info(f"\n\n\n{'--'*50}\n")
    logger.info(f"[{i}/{len(pdf.columns)}] Processing {col}")
    summary_of_col(col)

logger.success(f"All Summaries Completed.")

del pdf 