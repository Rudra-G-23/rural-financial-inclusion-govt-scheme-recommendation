
# 🔍📋 **Enhanced Data Profiling Checklist**

> **Author**: Rudra Prasad Bhuyan
> **Date**: 26-10-2025 12:17 IST
> **Level:** Advanced Checklist

!!![NOTE] ⚠️ This is a *working draft* — refine it WIP.

---

## 1. **Data Completeness**

* [ ] **Missing Values Detection:** Identify and quantify missing or null values across all columns.

  * Include both `NaN`, empty strings, or placeholders (e.g., “Unknown”, “N/A”).
  * Notes:
* [ ] **Null & Blank Counts:** Compute both null and blank counts per column, and percentage of missing data.

  * Notes:
* [ ] **Row Completeness Check:** Identify rows with a high proportion of missing fields.

  * Notes:
* [ ] **Handling Strategy:** Define how each column’s missing values will be treated (imputation method, removal, domain-specific defaults).

  * Notes:
* [ ] **Data Availability vs Business Rules:** Check whether essential fields (IDs, dates, labels) are ever missing.

  * Notes:

---

## 2. **Data Consistency**

* [ ] **Format Standardization:** Validate consistent data formats (dates, numeric precision, string casing).

  * Notes:
* [ ] **Duplicate Row Check:** Identify exact and near-duplicate records using key and fuzzy matching.

  * Notes:
* [ ] **Categorical Consistency:** Identify inconsistent categorical labels (e.g., “US”, “U.S.”, “United States”).

  * Notes:
* [ ] **Cross-Table Consistency:** Validate data alignment across different datasets (e.g., customer ID exists in both sales and customer tables).

  * Notes:
* [ ] **Value Range Enforcement:** Ensure data values fall within valid or expected limits.

  * Notes:

---

## 3. **Data Distribution**

* [ ] **Descriptive Statistics:** Compute summary stats (mean, median, mode, variance, std, min, max, quartiles).

  * Notes:
* [ ] **Outlier Detection:** Identify and quantify outliers using statistical (IQR, z-score) or domain-based thresholds.

  * Notes:
* [ ] **Skewness & Kurtosis:** Assess data shape and identify columns that may need normalization or transformation.

  * Notes:
* [ ] **Compare with Expected Distribution:** Check whether the data distribution aligns with domain expectations (e.g., age, income).

  * Notes:

---

## 4. **Data Uniqueness**

* [ ] **Primary Key Validation:** Verify that designated unique identifiers truly contain unique values.

  * Notes:
* [ ] **High Cardinality Check:** Identify categorical variables with too many distinct values that may hinder modeling.

  * Notes:
* [ ] **Duplicate Entity Detection:** Check for possible entity duplication using fuzzy matching or composite keys.

  * Notes:

---

## 5. **Data Relationships**

* [ ] **Correlation Analysis:** Evaluate correlations (Pearson, Spearman, Cramér’s V for categorical data).

  * Notes:
* [ ] **Dependency Mapping:** Identify dependent or derived columns (e.g., total_price = quantity × price).

  * Notes:
* [ ] **Multicollinearity Detection:** Detect redundant variables via Variance Inflation Factor (VIF) or PCA.

  * Notes:
* [ ] **Cross-Feature Logic Validation:** Ensure relationships between columns make sense (e.g., start_date < end_date).

  * Notes:

---

## 6. **Categorical Data Analysis**

* [ ] **Category Frequency Distribution:** Analyze top categories and rare ones per column.

  * Notes:
* [ ] **Class Imbalance:** Quantify imbalance ratios for classification targets.

  * Notes:
* [ ] **Encoding Readiness:** Determine appropriate encoding (label, one-hot, frequency, target).

  * Notes:
* [ ] **Rare Label Detection:** Identify categories with very low frequency that may impact model stability.

  * Notes:

---

## 7. **Data Typing**

* [ ] **Data Type Validation:** Confirm each field has the correct logical and technical type.

  * Notes:
* [ ] **Automatic Type Inference Check:** Compare inferred vs. expected types.

  * Notes:
* [ ] **Precision & Scale Validation (Numerics):** Ensure decimals are within acceptable tolerance.

  * Notes:
* [ ] **Type Conversion Plan:** Define any conversions required for downstream processing.

  * Notes:

---

## 8. **Date/Time Integrity**

* [ ] **Date Range Validation:** Ensure date values fall within valid business or system periods.

  * Notes:
* [ ] **Chronological Consistency:** Validate time sequence logic (e.g., delivery_date > order_date).

  * Notes:
* [ ] **Timezone Handling:** Ensure timezones are consistent or converted appropriately.

  * Notes:
* [ ] **Frequency Check (Time Series):** Check for gaps or irregular intervals in temporal data.

  * Notes:

---

## 9. **Data Integrity**

* [ ] **Referential Integrity:** Ensure foreign keys exist and link properly across tables.

  * Notes:
* [ ] **Business Rule Consistency:** Validate logical constraints (e.g., no negative prices, realistic ages).

  * Notes:
* [ ] **Record Versioning Check:** Confirm latest records are appropriately flagged or timestamped.

  * Notes:
* [ ] **Audit Trail Validation:** Check for system-generated metadata (created_by, updated_at).

  * Notes:

---

## 10. **Text Data Quality**

* [ ] **Length Distribution:** Check for abnormal lengths (too short/long) and truncation.

  * Notes:
* [ ] **Whitespace & Special Characters:** Detect and handle irregular spacing or non-printable characters.

  * Notes:
* [ ] **Language Consistency:** Confirm that text fields match expected language or script.

  * Notes:
* [ ] **Spelling & Grammar Review:** Run automated text quality checks (e.g., typos, slang, abbreviations).

  * Notes:
* [ ] **Semantic Consistency:** Assess if free text fields align semantically with related structured data.

  * Notes:

---

## 11. **Data Source Validity**

* [ ] **Source Documentation:** Confirm data source lineage and metadata availability.

  * Notes:
* [ ] **Source Reliability:** Evaluate trustworthiness and stability of the data provider.

  * Notes:
* [ ] **Version Control:** Check dataset version, update frequency, and refresh schedules.

  * Notes:
* [ ] **Data Extraction Validation:** Ensure no data loss during ingestion or transformation.

  * Notes:

---

## 12. **Handling Special Cases**

* [ ] **Imputation Methods:** Document chosen imputation methods (mean/median/mode/KNN/ML-based).

  * Notes:
* [ ] **Outlier Treatment:** Decide whether to remove, cap, or transform outliers.

  * Notes:
* [ ] **Encoding Schemes:** Specify encoding strategy for categorical and ordinal data.

  * Notes:
* [ ] **Scaling & Normalization:** Determine scaling techniques for numeric data.

  * Notes:
* [ ] **Error Logging:** Establish error-handling mechanisms for exceptional cases.

  * Notes:

---

## 13. **Visualization**

* [ ] **Numeric Distributions:** Plot histograms, boxplots, and density curves.

  * Notes:
* [ ] **Categorical Distributions:** Plot bar charts, pie charts, and count plots.

  * Notes:
* [ ] **Correlation Heatmaps:** Visualize numeric and categorical correlations.

  * Notes:
* [ ] **Time Series Trends:** Visualize temporal patterns and anomalies.

  * Notes:
* [ ] **Missing Value Maps:** Use heatmaps to visualize data completeness.

  * Notes:

---

## 14. **Documentation & Audit Trail**

* [ ] **Assumptions Log:** Record any assumptions made during profiling.

  * Notes:
* [ ] **Data Quality Findings:** Document key data quality issues identified.

  * Notes:
* [ ] **Decisions and Actions:** Capture all cleaning and transformation decisions.

  * Notes:
* [ ] **Reproducibility Notes:** Save profiling scripts, parameters, and environment details.

  * Notes:

---

## ✅ **Final Review & Reporting**

* [ ] Summarize major issues and recommended resolutions.
* [ ] Create a structured data profiling report (HTML, PDF, or notebook).
* [ ] Assign ownership for data remediation tasks.
* [ ] Establish a revalidation plan post-cleaning.

