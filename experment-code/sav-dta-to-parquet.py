# ============================================================================
""" 
Goal: Convert *.sav & *.dta files to *.csv and *.parquet, and store ALL metadata.

Author: Rudra Prasad Bhuyan
Starting Time: 24-102025 08:19 IST
"""
# ============================================================================

# Import 
import pandas as pd
import pyreadstat
import json

# Defile file paths
lev_01_path  = "raw-data\LEVEL - 01(Section 1 and 1.1).sav"
lev_02_path  = "raw-data\LEVEL - 02 (Section 3).sav"
lev_03_path  = "raw-data\LEVEL - 03.sav"
lev_04_path  = "raw-data/LEVEL - 04 (Section 4.1).sav"
lev_05_path  = "raw-data\LEVEL - 05 ( Sec 5 & 6).dta"
lev_06_path  = "raw-data\LEVEL - 06 (Section 7).dta"
lev_07_path  = "raw-data\LEVEL - 07 (Section 4.dta"
lev_08_path  = "raw-data\LEVEL - 08 (Section 8.dta"
lev_09_path  = "raw-data\LEVEL - 09 (Section 9 & 10 & 11).dta"
lev_10_path  = "raw-data\LEVEL - 10 (Section 12).dta"
lev_11_path  = "raw-data\LEVEL - 11 (Section 4.dta"
lev_12_path  = "raw-data\LEVEL - 12 (Section 13).dta"
lev_13_path  = "raw-data\Level - 13 (Section 14).dta"
lev_14_path  = "raw-data\LEVEL - 14 (Section  A1,B1 & C1).dta"
lev_15_path  = "raw-data\LEVEL - 15 (Section 1.dta"

# Dictionary for easier access
lev_paths = {
    1: lev_01_path,
    2: lev_02_path,
    3: lev_03_path,
    4: lev_04_path,
    5: lev_05_path,
    6: lev_06_path,
    7: lev_07_path,
    8: lev_08_path,
    9: lev_09_path,
    10: lev_10_path,
    11: lev_11_path,
    12: lev_12_path,
    13: lev_13_path,
    14: lev_14_path,
    15: lev_15_path
}

# Loop through the file paths
for i in range(1, 16):
    path = lev_paths[i]
    
    try:
        if path.endswith('.sav'):
            df, meta = pyreadstat.read_sav(path)
        elif path.endswith('.dta'):
            df, meta = pyreadstat.read_dta(path)
        else:
            print(f"Unsupported File type: {path}")
            continue
        
        # Save to CSV
        csv_file = f"lev_{i:02d}.csv"
        df.to_csv(csv_file, index=False)
        print(f"Conversion complete! CSV saved: {csv_file}")
        
        # Save to parquet
        parquet_file = f"lev_{i:02d}.parquet"
        df.to_parquet(parquet_file, index=False)
        print(f"Conversion complete! Parquet saved: {parquet_file}")
        
        # Save the meta data
        all_meta = {}
        for attr in dir(meta):
            if not attr.startswith('_') and attr not in ['creation_time', 'modification_time']:
                try:
                    val = getattr(meta, attr)
                    all_meta[attr] = val
                except Exception:
                    all_meta[attr] ="Error Reading"
 
        json_file = f"lev_{i:02d}_metadata.json"
        with open (json_file, 'w', encoding='utf-8') as json_f:
            json.dump(all_meta, json_f, ensure_ascii=False, indent=4)
        print(f"Meta data saved")
        print("=" * 50)
        
    except Exception as e:
        print('=' * 50)
        print(f" ------------> Error processing file for level {i}: {e}") 
        print("=" * 50)