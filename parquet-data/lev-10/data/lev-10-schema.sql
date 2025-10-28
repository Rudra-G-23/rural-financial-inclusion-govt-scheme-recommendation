-- ================================================
--              Level 10
-- ================================================
CREATE TABLE IF NOT EXISTS "Level 10" (
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
    "Item_Code_12_series" TEXT,
    "OOHP_Quantity_12_series" SMALLINT,
    "OOHP_Value_12_series" SMALLINT,
    "Total_Consumption_Quantity_12_se" SMALLINT,
    "Total_Consumption_Value_12_serie" SMALLINT,
    "Source_12_series" TEXT,
    "Multiplier" INTEGER,
    PRIMARY KEY ("Survey_Name")
);