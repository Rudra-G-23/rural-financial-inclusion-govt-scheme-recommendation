-- ================================================
--              Level 15
-- ================================================
CREATE TABLE IF NOT EXISTS "Level 15" (
    "Survey_Name" TEXT,
    "Year" TEXT,
    "FSU_Serial_No" TEXT,
    "Sector" TEXT,
    "State" TEXT,
    "NSS_Region" TEXT,
    "District" TEXT,
    "Stratum" TEXT,
    "Sub_stratum" TEXT,
    "Panel" TEXT,
    "Sub_sample" TEXT,
    "FOD_Sub_Region" TEXT,
    "Sample_SU_No" TEXT,
    "Sample_Sub_Division_No" TEXT,
    "Second_Stage_Stratum_No" TEXT,
    "Sample_Household_No" TEXT,
    "Questionnaire_No" TEXT,
    "VISIT" TEXT,
    "LEVEL" TEXT,
    "SECTION" TEXT,
    "TIME_TAKEN" TEXT,
    "MONTHLY_CONSUMPTION_EXP" INTEGER,
    "ONLINE_EXPENDITURE" INTEGER,
    "INFORMANT_CODE" TEXT,
    "RESPONSE_CODE" TEXT,
    "HOUSEHOLD_SIZE" SMALLINT,
    "VISIT_MONTH" INTEGER,
    "MULTIPLIER" INTEGER,
    PRIMARY KEY ("Survey_Name")
);
