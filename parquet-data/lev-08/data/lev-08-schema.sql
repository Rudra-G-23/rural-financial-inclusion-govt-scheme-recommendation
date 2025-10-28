-- ================================================
--              Level 08
-- ================================================
CREATE TABLE IF NOT EXISTS "Level 08" (
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
    "Item_Code_8_1" TEXT,
    "Out_of_home_qty_000" DOUBLE PRECISION,
    "Out_of_home_value_rs" SMALLINT,
    "Total_consumption_qty_000" DOUBLE PRECISION,
    "Total_consumption_value_rs" SMALLINT,
    "Source_8_1" TEXT,
    "Multiplier" INTEGER,
    PRIMARY KEY ("Survey_Name")
);