/* 
==================================================================
--- Merge Level 01 and 02 Datasets ---
Process:
- Create two temporary view
- Perform merging
- Notice the Data with time

Finding:
1. Level 01 total rows: 2_61_953
2. Level 02 total rows: 11_07_221 
3. During Join time Rows found:
	- l1 LEFT join with l2: 2_61_953  | Time: 00:01:21.206
	- l2 LEFT join with l1: 11_07_221 | Time: 00:04:42.977
	- l2 INNER join with l2: 0		  | Time: 00:00:09.867

4. No Common key is found.
5. Found only lot of Null values.
6. Duplicated Data.
*/
============================================================================

-- Level 01
DROP VIEW IF EXISTS temp_01;
CREATE TEMP VIEW temp_01 AS 
SELECT
	CONCAT_WS(
	    '_',
	    "Survey_Name", "Year", "FSU_Serial_No", "Sector", "State", 
		"NSS_Region", "District", "Stratum", "Sub_stratum", "Panel",
	    "Sub_sample", "FOD_Sub_Region", "Sample_SU_No",
	    "Sample_Sub_Division_No", "Second_Stage_Stratum_No",
	    "Sample_Household_No", "Sample_Household_No", "Level"
	) AS k1,
	*
FROM analytics.level_01_section_1_and_1 AS l01;

-- Level 02
DROP VIEW IF EXISTS temp_02;
CREATE TEMP VIEW temp_02 AS 
SELECT
	CONCAT_WS(
	    '_',
	    "Survey_Name", "Year", "FSU_Serial_No", "Sector", "State", 
		"NSS_Region", "District", "Stratum", "Sub_stratum", "Panel",
	    "Sub_sample", "FOD_Sub_Region", "Sample_SU_No",
	    "Sample_Sub_Division_No", "Second_Stage_Stratum_No",
	    "Sample_Household_No", "Sample_Household_No", "Level"
	) AS k2,
	*
FROM analytics.level_02_section_3 AS l02;

------------------------- Left joint (L01 -> L02) -------------------------
SELECT
    l01.*,
    l02.*
FROM temp_01 l01
LEFT JOIN temp_02 l02 
    ON l01.k1 = l02.k2;

------------------------- Left joint (L02 -> L01) -------------------------
SELECT
    l01.*,
    l02.*
FROM temp_02 l02
LEFT JOIN temp_01 l01
    ON l02.k2 = l01.k1;

------------------------- Inner joint  -------------------------
SELECT
	COUNT(*)
FROM temp_01 l01
INNER JOIN temp_02 l02
    ON l02.k2 = l01.k1;