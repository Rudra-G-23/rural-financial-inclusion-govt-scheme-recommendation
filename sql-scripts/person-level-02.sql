/* 
==================================================================
--- Person level district comparison analysis on Bihar data---

>>> Goal: Person Level Insights on Bihar District.

>>> Tool:
    - PgAdmin 4
    - Level 02 Data of HCES

>>> Process:
1. Age v/s District
    - Count how many district available
    - Count the age group for bucketing
    - Validate age is negative or hypothetical values

2. Gender v/s District
    - Count the unique gender with label
    - Count the district wise gender

3. Education level v/s District
    - Count the education level with the levels
    - Count the district wise Education level

4. Year of Educations v/s District
    - Count how many unique education year are available
    - Count the district wise Year of Education
    - "Year of Education" level is messy.
    - 01, 1 both is present, both handle correctly in code.
    - Null value also present so Fill with 0.

5. Marital Status v/s District
    - Count how many unique marital status are available
    - Count the district wise Marital Status

---


>>> Finding:
1. Age v/s District
    - Unique District: 38 
    - Age line 0 to 105
    - Age = 0 value exist in 369 rows

2. Gender v/s District
    - Gender: 1-Male, 2-Female, 3-Transgender

3. Education level v/s District
    - 13 Label education level found

4. Year of Educations v/s District
    - "Year of Education" level is messy.
    - In year of education found 0
    - 01, 1 both is present similar other.
    - Null value found 30_160

5. Marital Status v/s District
    - Four label: 
        Never married, currently married(including living together)
        widowed, divorced/separated

---


>>> Messy Data Hint:
    - In age data found the 0. (369 rows) Maybe Wrong Info.
    - In year of education found 0. (118 rows) Maybe NULL value!
============================================================================
*/

-- =========================== Age v/s District ============================

-- How many district available in bihar 
SELECT
	COUNT ( DISTINCT "District")
FROM analytics.level_02_section_3
WHERE "State" = '10';


-- 0-105 Age people are in the bucket
SELECT
	DISTINCT ("Age")
FROM analytics.level_02_section_3
WHERE "State" = '10' 

-- The age = 0 value exist in 369 rows
SELECT
	COUNT (*)
FROM analytics.level_02_section_3
WHERE "State" = '10' AND "Age" = 0

-- =========================== Gender v/s District ============================
-- Gender unique count
SELECT
	DISTINCT "Gender",
	"Gender_label"
FROM analytics.level_02_section_3
WHERE "State" = '10';

-- Gender unique count on district
SELECT 
    "District",
    COUNT(*) FILTER (WHERE "Gender" = 1) AS "Male_count",
    COUNT(*) FILTER (WHERE "Gender" = 2) AS "Female_count",
    COUNT(*) FILTER (WHERE "Gender" = 3) AS "Transgender_count"
FROM analytics.level_02_section_3
WHERE "State" = '10'
GROUP BY "District"
ORDER BY "District";

-- =========================== Education level v/s District ============================
-- Unique Eduction level
SELECT
	DISTINCT "Education_Level",
	"Education_Level_label"
FROM analytics.level_02_section_3
WHERE "State" = '10';

-- Count of the eduction level on district
SELECT 
    "District",
    COUNT(*) FILTER (WHERE "Education_Level" = '01') AS "01",
    COUNT(*) FILTER (WHERE "Education_Level" = '02') AS "02",
    COUNT(*) FILTER (WHERE "Education_Level" = '03') AS "03",
    COUNT(*) FILTER (WHERE "Education_Level" = '04') AS "04",
    COUNT(*) FILTER (WHERE "Education_Level" = '05') AS "05",
    COUNT(*) FILTER (WHERE "Education_Level" = '06') AS "06",
	COUNT(*) FILTER (WHERE "Education_Level" = '07') AS "07",
    COUNT(*) FILTER (WHERE "Education_Level" = '08') AS "08",
    COUNT(*) FILTER (WHERE "Education_Level" = '09') AS "09",
    COUNT(*) FILTER (WHERE "Education_Level" = '10') AS "10",
    COUNT(*) FILTER (WHERE "Education_Level" = '11') AS "11",
    COUNT(*) FILTER (WHERE "Education_Level" = '12') AS "12",
    COUNT(*) FILTER (WHERE "Education_Level" = '13') AS "13"
FROM analytics.level_02_section_3
WHERE "State" = '10'
GROUP BY "District"
ORDER BY "District";

-- =========================== Year of Educations v/s District ============================
-- Unique "Year of education"
SELECT
	DISTINCT "Years_of_Education"
FROM analytics.level_02_section_3
WHERE "State" = '10'
ORDER BY "Years_of_Education" ASC;

-- District count of "Year of education level"
SELECT 
    "District",
    COALESCE(COUNT(*) FILTER (WHERE "Years_of_Education" IN ('0', '00')), 0) AS "0",
    COALESCE(COUNT(*) FILTER (WHERE "Years_of_Education" IN ('1', '01')), 0) AS "01",
    COALESCE(COUNT(*) FILTER (WHERE "Years_of_Education" IN ('2', '02')), 0) AS "02",
    COALESCE(COUNT(*) FILTER (WHERE "Years_of_Education" IN ('3', '03')), 0) AS "03",
    COALESCE(COUNT(*) FILTER (WHERE "Years_of_Education" IN ('4', '04')), 0) AS "04",
    COALESCE(COUNT(*) FILTER (WHERE "Years_of_Education" IN ('5', '05')), 0) AS "05",
    COALESCE(COUNT(*) FILTER (WHERE "Years_of_Education" IN ('6', '06')), 0) AS "06",
    COALESCE(COUNT(*) FILTER (WHERE "Years_of_Education" IN ('7', '07')), 0) AS "07",
    COALESCE(COUNT(*) FILTER (WHERE "Years_of_Education" IN ('8', '08')), 0) AS "08",
    COALESCE(COUNT(*) FILTER (WHERE "Years_of_Education" IN ('9', '09')), 0) AS "09",
    COALESCE(COUNT(*) FILTER (WHERE "Education_Level" = '10'), 0) AS "10",
    COALESCE(COUNT(*) FILTER (WHERE "Education_Level" = '11'), 0) AS "11",
    COALESCE(COUNT(*) FILTER (WHERE "Education_Level" = '12'), 0) AS "12",
    COALESCE(COUNT(*) FILTER (WHERE "Education_Level" = '13'), 0) AS "13",
    COALESCE(COUNT(*) FILTER (WHERE "Education_Level" = '14'), 0) AS "14",
    COALESCE(COUNT(*) FILTER (WHERE "Education_Level" = '15'), 0) AS "15",
    COALESCE(COUNT(*) FILTER (WHERE "Education_Level" = '16'), 0) AS "16",
    COALESCE(COUNT(*) FILTER (WHERE "Education_Level" = '17'), 0) AS "17",
    COALESCE(COUNT(*) FILTER (WHERE "Education_Level" = '18'), 0) AS "18",
    COALESCE(COUNT(*) FILTER (WHERE "Education_Level" = '19'), 0) AS "19",
    COALESCE(COUNT(*) FILTER (WHERE "Education_Level" = '20'), 0) AS "20"
FROM analytics.level_02_section_3
WHERE "State" = '10'
GROUP BY "District"
ORDER BY "District";

-- Year of education level is 0.
SELECT
	COUNT (*) 
FROM analytics.level_02_section_3
WHERE "State" = '10' AND "Years_of_Education" = '0';

-- Null value count
SELECT
	COUNT (*) 
FROM analytics.level_02_section_3
WHERE "State" = '10'AND "Years_of_Education" IS NULL ;


-- =========================== Marital Status v/s District ============================

-- Marital Status unique with the label
SELECT
	DISTINCT ("Marital_Status"),
	"Marital_Status_label"
FROM analytics.level_02_section_3
WHERE "State" = '10';

-- District wise count the marital status
SELECT 
    "District",
    COUNT(*) FILTER (WHERE "Marital_Status" = 1) AS "never_married_count",
    COUNT(*) FILTER (WHERE "Marital_Status" = 2) AS "married_living_together_count",
    COUNT(*) FILTER (WHERE "Marital_Status" = 3) AS "widowed_count",
	COUNT(*) FILTER (WHERE "Marital_Status" = 4) AS "divorced/separated_count"
FROM analytics.level_02_section_3
WHERE "State" = '10'
GROUP BY "District"
ORDER BY "District";

