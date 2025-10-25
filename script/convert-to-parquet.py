"""
Goal: 
    - Convert *.sav & *.dta files 
    - Chunk-wise to *.parquet 
    - Store all metadata
    - Better logging.

Author: Rudra Prasad Bhuyan 
Starting Time: 24-10-2025
Final Review Time: 21-10-2025 20:37 IST
"""
    
# ----------------------------------------------------------------
#                          Imports
# ----------------------------------------------------------------
import json
import sys 
import pandas as pd 
import pyreadstat 
from loguru import logger

# ----------------------------------------------------------------
#                           Settings
# ----------------------------------------------------------------
CHUNK_SIZE = 2_00_000

# ----------------------------------------------------------------
#                          Simple Logging
# ----------------------------------------------------------------
logger.remove()

logger.add(
    sys.stdout,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="INFO",
)
logger.add(
    "conversion_parquet_log_{time}.log",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
    level="INFO",
    rotation="1 day"
)

# ----------------------------------------------------------------
#                          Define File Paths
# ----------------------------------------------------------------
lev_paths = {
    1: r"raw-data\LEVEL - 01(Section 1 and 1.1).sav",
    2: r"raw-data\LEVEL - 02 (Section 3).dta",
    3: r"raw-data\LEVEL - 03.sav",
    4: r"raw-data\LEVEL - 04 (Section 4.1).sav",
    5: r"raw-data\LEVEL - 05 ( Sec 5 & 6).dta",
    6: r"raw-data\LEVEL - 06 (Section 7).dta",
    7: r"raw-data\LEVEL - 07 (Section 4.dta",
    8: r"raw-data\LEVEL - 08 (Section 8.dta",
    9: r"raw-data\LEVEL - 09 (Section 9 & 10 & 11).dta",
    10: r"raw-data\LEVEL - 10 (Section 12).dta",
    11: r"raw-data\LEVEL - 11 (Section 4.dta",
    12: r"raw-data\LEVEL - 12 (Section 13).dta",
    13: r"raw-data\Level - 13 (Section 14).dta",
    14: r"raw-data\LEVEL - 14 (Section  A1,B1 & C1).dta",
    15: r"raw-data\LEVEL - 15 (Section 1.dta"
}

# ----------------------------------------------------------------
#                         Function to read files
# ----------------------------------------------------------------
def read_file(path):
    if path.endswith('.sav'):
        return pyreadstat.read_sav(path)
    elif path.endswith('.dta'):
        return pyreadstat.read_dta(path)
    else:
        raise ValueError(f"Unsupported file type: {path}")

# ----------------------------------------------------------------
#                  Functions to save the meta data
# ----------------------------------------------------------------
def save_metadata(meta, level):
    all_meta = {}
    for attr in dir(meta):
        if not attr.startswith('_') and attr not in ['creation_time', 'modification_time']:
            try:
                val = getattr(meta, attr)
                all_meta[attr] = val
            except Exception:
                all_meta[attr] = "Error Reading"

    json_file = f"lev_{level:02d}_metadata.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(all_meta, f, ensure_ascii=False, indent=4)
    logger.info(f"Saved metadata for Level {level} \n\n")
    logger.info("=" * 100)

# ----------------------------------------------------------------
#                          Save parquet data
# ----------------------------------------------------------------
def save_parquet_in_chunks(df, file_name, chunk_size=CHUNK_SIZE):
    
    n_rows = df.shape[0]
    
    for i, start in enumerate(range(0, n_rows, chunk_size)):
        chunk = df.iloc[start: start + chunk_size]
        chunk_file = file_name.replace(".parquet", f"_chunk_{i+1}.parquet")
        chunk.to_parquet(chunk_file, index=False)
        logger.info(f"Save chunk {i+1} of {file_name} with rows {start} to {start + len(chunk)-1}")
    

# ----------------------------------------------------------------
#                          Conversion Loop
# ----------------------------------------------------------------
for i, path in lev_paths.items():
    logger.info(f"Processing Level {i}: {path}")
    
    try:
        df, meta = read_file(path)
        if df is None or df.shape[0] == 0:
            logger.error(f"Level {i} - File loaded but has zero rows: {path}")
            continue

        parquet_file = f"lev_{i:02d}.parquet"
        save_parquet_in_chunks(df, parquet_file)
        save_metadata(meta, i)
        
    except pyreadstat._readstat_parser.ReadstatError as e:
        logger.error(f"Level {i} - Pyreadstat failed: {e}")
    except Exception as e:
        logger.error(f"Level {i} - Unexpected error: {e}")