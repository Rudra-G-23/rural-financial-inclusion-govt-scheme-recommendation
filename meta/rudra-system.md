# About My Device (Chocolate)

- Device name:	LAPTOP-E03IAI0P
- Processor:	AMD Ryzen 5 5500U with Radeon Graphics          (2.10 GHz)
- RAM:	16.0 GB (15.3 GB usable)
- System type:	64-bit operating system, x64-based processor
- Pen and touch	No pen or touch input is available for this display

---

# Project essentials 

**IDE / Coding**

* VS Code — main editor (extensions: Python, Pylance, Jupyter, GitLens, Docker, Drawio)

**Storing & sharing**

* Git + GitHub (use feature branches, PRs, CODEOWNERS)


**Languages & Version**

* Python 3.10+

**File formats I'll use**

* Notebooks: `.ipynb`
* Scripts: `.py`
* Metadata & notes: `.md`, `.txt`
* Tabular data: Parquet (`.parquet`), CSV (`.csv`)
* Models & artifacts: Pickle / joblib 
* Config: `.yaml`, `.json`
* Geospatial: GeoJSON / Shapefiles (if mapping states)

**Core data & ML libraries**

* pandas — data manipulation (easy & familiar)
* polars — for fast, low-memory data processing on larger tables
* numpy — numeric ops
* scipy — stats & utilities
* scikit-learn — baseline models, preprocessing, pipelines

**Advanced models**

* XGBoost
* LightGBM
* CatBoost

**Feature engineering**

* category_encoders — targeted categorical encoders
* featuretools — automated feature engineering (optional)
* imbalanced-learn — resampling for class imbalance

**Model search & optimization**

* Optuna — hyperparameter tuning and experiments

**Model tracking & reproducibility**

* MLflow — tracking experiments, models, metrics
* DVC (Data Version Control) — version data + models 

**Explainability & diagnostics**

* SHAP — feature importance & local explanations
* LIME — local explanations

**Visualization & mapping**

* matplotlib — base plotting
* plotly — interactive charts for dashboards
* folium — maps for state-level visualization
* geopandas — geospatial joins / plotting for states

**Deployment & APIs**

* FastAPI — serve models as APIs
* Docker — containerize services

**Dashboards / front-end**

* Streamlit — quick dashboards
* Plotly — production dashboards

**Utilities & helpers**

* joblib — save/load models & parallel jobs
* tqdm — progress bars
* loguru — logging
* rich — pretty-print in CLI