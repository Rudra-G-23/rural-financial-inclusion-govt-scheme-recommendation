# 📜 SQL Scripts

##### 📂 Bihar Analysis

<details>
<summary>Analysis Scripts</summary>

* [Bihar Data Fetch and Downloaded](../sql-scripts/bihar/analysis/bihar.sql)

  * Download & FSU 27000 value matching
  * **17-01-2026**

* [Person level 02 On Bihar Data](../sql-scripts/bihar/analysis/person-level-02.sql)

  * Overview of Bihar person-level data
  * 5-person data point comparison with district analysis
  * Deep dive at district level
  * **20-01-2026 19:35 IST**

</details>



##### 📂 Bihar Experiment & Merge

<details>
<summary>Experiment & Merge Scripts</summary>

* [Household unique ID creation](../sql-scripts/bihar/experiment-merge/hh-unique-id.sql)

  * Create a unique ID for merging
  * Calculate merged household count
  * **18-01-2026 16:25 IST**

* [HH unique ID for 01, 03, 04, 07, 11 (View)](../sql-scripts/bihar/experiment-merge/hh-01-03-04-07-11-hh-key.sql)

  * Generate household keys for selected rounds

* [Merge all Household datasets](../sql-scripts/bihar/experiment-merge/household_merged_01_03_04_07_11.sql)

  * Create a database view
  * Used later for merging logic
  * **19-01-2026**

* [Merge Level L01, L02 up to level columns](../sql-scripts/bihar/experiment-merge/merge-l01-l02-upto-level-columns.sql)

  * Test whether data is merged
  * Result: no matching keys found
  * **19-01-2026**

* [Experiment with Bihar subset of FSU 27,000](../sql-scripts/bihar/experiment-merge/exp-bihar-27000-hh-1.sql)

  * Experiment to identify best merge strategy
  * **26-01-2026 14:52 IST**

</details>
