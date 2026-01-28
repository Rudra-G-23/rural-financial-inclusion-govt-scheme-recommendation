-- Household unique id creation for level 1
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
	) AS "hh_unique_key" 
FROM analytics.level_01_section_1_and_1
LIMIT 3;

-- If we run this it show the 17_255 are matching
-- It means whole dataset is match
SELECT COUNT(*) AS matching_households
FROM (
    SELECT CONCAT_WS('_',
        "FSU_Serial_No","Sector","State","NSS_Region","District",
        "Stratum","Sub_stratum","Panel","Sub_sample","FOD_Sub_Region",
        "Sample_SU_No","Sample_Sub_Division_No",
        "Second_Stage_Stratum_No","Sample_Household_No"
    ) AS hh_key
    FROM analytics.level_01_section_1_and_1
	WHERE "State" = '10'
) l1
INNER JOIN (
    SELECT CONCAT_WS('_',
        "FSU_Serial_No","Sector","State","NSS_Region","District",
        "Stratum","Sub_stratum","Panel","Sub_sample","FOD_Sub_Region",
        "Sample_SU_No","Sample_Sub_Division_No",
        "Second_Stage_Stratum_No","Sample_Household_No"
    ) AS hh_key
    FROM analytics.level_03
	WHERE "State" = '10'
) l2
ON l1.hh_key = l2.hh_key;


-- Create View for Household level datasets (L01, 03, 04, 07, 11)
CREATE OR REPLACE VIEW analytics.level_01_with_key AS
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
FROM analytics.level_01_section_1_and_1
LIMIT 3 ;


-- Merge the level 01 & l02
SELECT 
	*
FROM 
	analytics.level_01_with_key AS l1
LEFT JOIN analytics.level_02_with_key  AS l2
ON l1."hh_unique_key" = l2."hh_unique_key"
LIMIT 3;