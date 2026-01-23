-- select one section 
SELECT * FROM analytics.level_09_section_9_10_11
WHERE "State" = '10'  AND "FSU_Serial_No" = 27000;

-- find how many rows 
SELECT count(*) FROM analytics.level_05_sec_5_6
WHERE "State" = '10'; 

-- How many hh contains each districts
-- Each districts(38) contains 18 household
-- Item code used in the sample
SELECT 
	DISTINCT "District",
	COUNT (DISTINCT "Sample_Household_No"),
	COUNT (DISTINCT "Item_Code")
FROM analytics.level_05_sec_5_6
WHERE "State" = '10'
GROUP BY "District";