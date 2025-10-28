-- ================================================
--              Level 13
-- ================================================
CREATE TABLE IF NOT EXISTS "Level 13" (
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
    "Level" TEXT,
    "ITEM_CODE" TEXT,
    "FIRST_PURCHASE_NUMBER" SMALLINT,
    "PURCHASED_ON_HIRE" TEXT,
    "FIRST_PURCHASE_VALUE" INTEGER,
    "REPAIR_COST" INTEGER,
    "SECOND_HAND_NUMBER" SMALLINT,
    "SECOND_HAND_VALUE" INTEGER,
    "TOTAL_EXPENDITURE" INTEGER,
    "MULTIPLIER" INTEGER,
    PRIMARY KEY ("Survey_Name")
);