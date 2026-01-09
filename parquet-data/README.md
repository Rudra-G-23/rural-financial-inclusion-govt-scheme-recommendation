# 👨‍💻 Data & Code Folder

- For each level we have a separate folder for easier to navigate
- Inside each file we got the notebooks and Meta data file.
  - Metadata `*.json` file is created during the file conversion time.
  - All data dictionary `*.md` documents are created by extracting the text form the website.
- Added a All level Folder to store overall data related work.


**Folder Structure**
```bash
parquet-data/
|--all-level/     # Mix level code
|--lev-01/
  |-- Autoviz/    # Raw Dataset autoviz 
  |-- data/       # Raw Dataset & Data dictionary 
  |-- data2/      # Clean dataset 
  |-- notebooks/  # All the notebooks for specific levels
```