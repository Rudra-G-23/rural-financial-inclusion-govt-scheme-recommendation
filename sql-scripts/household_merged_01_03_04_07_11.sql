CREATE OR REPLACE VIEW analytics.household_merged_01_03_04_07_11 AS
SELECT
    /* ---- Level 01 household Identifiers ---- */
    l01.hh_unique_key,
	l01."Survey_Name",
	l01."Year",
    l01."FSU_Serial_No",
    l01."Sector",
    l01."State",
    l01."NSS_Region",
    l01."District",
    l01."Stratum",
    l01."Sub_stratum",
    l01."Panel",
    l01."Sub_sample",
    l01."FOD_Sub_Region",
    l01."Sample_SU_No",
    l01."Sample_Sub_Division_No",
    l01."Second_Stage_Stratum_No",
    l01."Sample_Household_No",
	l01."Questionnaire_No",
	l01."Level",
	l01."Survey_Code",
	l01."Reason_for_Substitution_Code",
	
    /* ---- Level 03 columns ---- */
    l03."HH_Size_FDQ",
	l03."Engaged_in_Economic_Activity_Las",

    /* ---- Level 04 columns ---- */
    l04."Ration_Any_Item_Last_30_Days",
	l04."Ration_Rice",
	l04."Ration_Wheat",

    /* ---- Level 07 columns ---- */
    l07."Kerosene_ration_card",
	l07."LPG_subsidy_received",

    /* ---- Level 11 columns ---- */
    l11."Online_Clothing",
	l11."Online_Footwear"
	
FROM analytics.level_01_with_hh_key l01

LEFT JOIN analytics.level_03_with_hh_key l03
    ON l01.hh_unique_key = l03.hh_unique_key

LEFT JOIN analytics.level_04_with_hh_key l04
    ON l01.hh_unique_key = l04.hh_unique_key

LEFT JOIN analytics.level_07_with_hh_key l07
    ON l01.hh_unique_key = l07.hh_unique_key

LEFT JOIN analytics.level_11_with_hh_key l11
    ON l01.hh_unique_key = l11.hh_unique_key;
