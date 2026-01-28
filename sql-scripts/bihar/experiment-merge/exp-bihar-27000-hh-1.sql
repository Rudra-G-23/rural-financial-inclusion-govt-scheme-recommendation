/* 
============================| Experiment on Merging |====================================
>>> Thought Process
1. Narrow down the datasets [Data -> Bihar -> FSU 27_000 -> HH 1] for all the datasets.
2. Create the household key

==========================================================================================
*/

-- Bihar 01
CREATE VIEW analytics.bl_01 AS
SELECT	*
FROM analytics.level_01_section_1_and_1
WHERE "State" = '10' AND "Sample_Household_No" = '01' AND "FSU_Serial_No" = '27000';

-- Bihar 02
CREATE VIEW analytics.bl_02 AS
SELECT	*
FROM analytics.level_02_section_3
WHERE "State" = '10' AND "Sample_Household_No" = '01' AND "FSU_Serial_No" = '27000';


-- Bihar 03
CREATE VIEW analytics.bl_03 AS
SELECT	*
FROM analytics.level_03
WHERE "State" = '10' AND "Sample_Household_No" = '01' AND "FSU_Serial_No" = '27000';

-- Bihar 04
CREATE VIEW analytics.bl_04 AS
SELECT	*
FROM analytics.level_04_section_4
WHERE "State" = '10' AND "Sample_Household_No" = '01' AND "FSU_Serial_No" = '27000';

-- Bihar 05
CREATE VIEW analytics.bl_05 AS
SELECT	*
FROM analytics.level_05_sec_5_6
WHERE "State" = '10' AND "Sample_Household_No" = '01' AND "FSU_Serial_No" = '27000';

-- Bihar 06
CREATE VIEW analytics.bl_06 AS
SELECT	*
FROM analytics.level_06_section_7
WHERE "State" = '10' AND "Sample_Household_No" = '01' AND "FSU_Serial_No" = '27000';

-- Bihar 07
CREATE VIEW analytics.bl_07 AS
SELECT	*
FROM analytics.level_07_section_4
WHERE "State" = '10' AND "Sample_Household_No" = '01' AND "FSU_Serial_No" = '27000';

-- Bihar 08
CREATE VIEW analytics.bl_08 AS
SELECT	*
FROM analytics.level_08_section_8
WHERE "State" = '10' AND "Sample_Household_No" = '01' AND "FSU_Serial_No" = '27000';

-- Bihar 09
CREATE VIEW analytics.bl_09 AS
SELECT	*
FROM analytics.level_09_section_9_10_11
WHERE "State" = '10' AND "Sample_Household_No" = '01' AND "FSU_Serial_No" = '27000';

-- Bihar 10
CREATE VIEW analytics.bl_10 AS
SELECT	*
FROM analytics.level_10_section_12
WHERE "State" = '10' AND "Sample_Household_No" = '01' AND "FSU_Serial_No" = '27000';

-- Bihar 11
CREATE VIEW analytics.bl_11 AS
SELECT	*
FROM analytics.level_11_section_4
WHERE "State" = '10' AND "Sample_Household_No" = '01' AND "FSU_Serial_No" = '27000';

-- Bihar 12
CREATE VIEW analytics.bl_12 AS
SELECT	*
FROM analytics.level_12_section_13
WHERE "State" = '10' AND "Sample_Household_No" = '01' AND "FSU_Serial_No" = '27000';

-- Bihar 13
CREATE VIEW analytics.bl_13 AS
SELECT	*
FROM analytics.level_13_section_14
WHERE "State" = '10' AND "Sample_Household_No" = '01' AND "FSU_Serial_No" = '27000';

-- Bihar 14 dataset is missing in analytics schema 

-- Bihar 15
CREATE VIEW analytics.bl_15 AS
SELECT	*
FROM analytics.level_15_section_1
WHERE "State" = '10' AND "Sample_Household_No" = '01' AND "FSU_Serial_No" = '27000';


-- Household key on bihar 01
CREATE VIEW analytics.bl_01_key AS
SELECT
	CONCAT_WS('_', "Survey_Name", "Year",
	"FSU_Serial_No","Sector","State","NSS_Region","District",
	"Stratum","Sub_stratum","Panel","Sub_sample","FOD_Sub_Region",
	"Sample_SU_No","Sample_Sub_Division_No",
	"Second_Stage_Stratum_No","Sample_Household_No"
	) AS hh_key,
	*	
FROM analytics.bl_01

-- Household key on bihar 02 
CREATE VIEW analytics.bl_02_key AS
SELECT
	CONCAT_WS('_', "Survey_Name", "Year",
	"FSU_Serial_No","Sector","State","NSS_Region","District",
	"Stratum","Sub_stratum","Panel","Sub_sample","FOD_Sub_Region",
	"Sample_SU_No","Sample_Sub_Division_No",
	"Second_Stage_Stratum_No","Sample_Household_No"
	) AS hh_key,
	*	
FROM analytics.bl_02

-- Solution of Joining with one sample house hold method
-- Without deleting any data point  
CREATE TEMP VIEW temp_bl_02 AS
SELECT
	"hh_key",
	COUNT ("Relation_to_Head"),
	AVG ("Age")
FROM analytics.bl_02_key
GROUP BY "hh_key";


SELECT 
	l1."Sample_Household_No",
	l2.*
FROM  analytics.bl_01_key AS l1
LEFT JOIN temp_bl_02 AS l2
on l1.hh_key = l2.hh_key