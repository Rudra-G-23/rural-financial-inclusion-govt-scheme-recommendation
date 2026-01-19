/* Create View for Household level datasets (L01, 03, 04, 07, 11) */

-- Level 01
CREATE OR REPLACE VIEW analytics.level_01_with_hh_key AS
SELECT
	CONCAT(
		"FSU_Serial_No",
		"Sector",
		"State",
		"NSS_Region",
		"District",
		"Stratum",
		"Sub_stratum",
		"Panel",
		"Sub_sample",
		"FOD_Sub_Region",
		"Sample_SU_No",
		"Sample_Sub_Division_No",
		"Second_Stage_Stratum_No",
		"Sample_Household_No"
	) AS "hh_unique_key" ,
	*
FROM analytics.level_01_section_1_and_1;

-- Level 03
CREATE OR REPLACE VIEW analytics.level_03_with_hh_key AS
SELECT
	CONCAT(
		"FSU_Serial_No",
		"Sector",
		"State",
		"NSS_Region",
		"District",
		"Stratum",
		"Sub_stratum",
		"Panel",
		"Sub_sample",
		"FOD_Sub_Region",
		"Sample_SU_No",
		"Sample_Sub_Division_No",
		"Second_Stage_Stratum_No",
		"Sample_Household_No"
	) AS "hh_unique_key" ,
	*
FROM analytics.level_03;

-- Level 04
CREATE OR REPLACE VIEW analytics.level_04_with_hh_key AS
SELECT
	CONCAT(
		"FSU_Serial_No",
		"Sector",
		"State",
		"NSS_Region",
		"District",
		"Stratum",
		"Sub_stratum",
		"Panel",
		"Sub_sample",
		"FOD_Sub_Region",
		"Sample_SU_No",
		"Sample_Sub_Division_No",
		"Second_Stage_Stratum_No",
		"Sample_Household_No"
	) AS "hh_unique_key" ,
	*
FROM analytics.level_04_section_4;

-- Level 07
CREATE OR REPLACE VIEW analytics.level_07_with_hh_key AS
SELECT
	CONCAT(
		"FSU_Serial_No",
		"Sector",
		"State",
		"NSS_Region",
		"District",
		"Stratum",
		"Sub_stratum",
		"Panel",
		"Sub_sample",
		"FOD_Sub_Region",
		"Sample_SU_No",
		"Sample_Sub_Division_No",
		"Second_Stage_Stratum_No",
		"Sample_Household_No"
	) AS "hh_unique_key" ,
	*
FROM analytics.level_07_section_4;

-- Level 11
CREATE OR REPLACE VIEW analytics.level_11_with_hh_key AS
SELECT
	CONCAT(
		"FSU_Serial_No",
		"Sector",
		"State",
		"NSS_Region",
		"District",
		"Stratum",
		"Sub_stratum",
		"Panel",
		"Sub_sample",
		"FOD_Sub_Region",
		"Sample_SU_No",
		"Sample_Sub_Division_No",
		"Second_Stage_Stratum_No",
		"Sample_Household_No"
	) AS "hh_unique_key" ,
	*
FROM analytics.level_11_section_4;