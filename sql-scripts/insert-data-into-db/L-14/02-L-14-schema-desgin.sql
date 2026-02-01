/*
Insert Data into Database. 
This is the schema for the level 14.
DATE CREATED - 01-02-2026 | 23:35 IST
*/

CREATE TABLE analytics.level_14 (
        "Survey_Name" TEXT,
        "Year" SMALLINT,

        "FSU_Serial_No" INTEGER,
        "Sector" SMALLINT,
        "State" SMALLINT,
        "NSS_Region" SMALLINT,
        "District" SMALLINT,
        "Stratum" SMALLINT,
        "Sub_stratum" SMALLINT,
        "Panel" SMALLINT,
        "Sub_sample" SMALLINT,
        "FOD_Sub_Region" SMALLINT,

        "Sample_SU_No" INTEGER,
        "Sample_Sub_Division_No" SMALLINT NULL,
        "Second_Stage_Stratum_No" SMALLINT NULL,
        "Sample_Household_No" SMALLINT,

        "Questionnaire_No" TEXT,
        "Level" SMALLINT,
        "SECTION" NUMERIC(14, 1),

        "ITEM_CODE" INTEGER,
        "VALUE_RS" NUMERIC(14, 2),
        "MULTIPLIER" NUMERIC(14, 2),

    ingest_timestamp               TIMESTAMPTZ 
        DEFAULT (now() AT TIME ZONE 'Asia/Kolkata'),

    ingest_date                    DATE 
        DEFAULT (CURRENT_DATE AT TIME ZONE 'Asia/Kolkata')
)