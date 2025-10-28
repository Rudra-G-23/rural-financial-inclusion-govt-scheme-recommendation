# Level 15 Diagram documentation
## Summary

- [Level 15 Diagram documentation](#level-15-diagram-documentation)
	- [Summary](#summary)
	- [Introduction](#introduction)
	- [Database type](#database-type)
	- [Table structure](#table-structure)
		- [Level\_15](#level_15)
	- [Relationships](#relationships)
	- [Database Diagram](#database-diagram)

## Introduction

## Database type

- **Database system:** PostgreSQL
## Table structure

### Level_15

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **Survey_Name** | TEXT | 🔑 PK, null |  | |
| **Year** | TEXT | null |  | |
| **FSU_Serial_No** | TEXT | null |  | |
| **Sector** | TEXT | null |  | |
| **State** | TEXT | null |  | |
| **NSS_Region** | TEXT | null |  | |
| **District** | TEXT | null |  | |
| **Stratum** | TEXT | null |  | |
| **Sub_stratum** | TEXT | null |  | |
| **Panel** | TEXT | null |  | |
| **Sub_sample** | TEXT | null |  | |
| **FOD_Sub_Region** | TEXT | null |  | |
| **Sample_SU_No** | TEXT | null |  | |
| **Sample_Sub_Division_No** | TEXT | null |  | |
| **Second_Stage_Stratum_No** | TEXT | null |  | |
| **Sample_Household_No** | TEXT | null |  | |
| **Questionnaire_No** | TEXT | null |  | |
| **VISIT** | TEXT | null |  | |
| **LEVEL** | TEXT | null |  | |
| **SECTION** | TEXT | null |  | |
| **TIME_TAKEN** | TEXT | null |  | |
| **MONTHLY_CONSUMPTION_EXP** | INTEGER | null |  | |
| **ONLINE_EXPENDITURE** | INTEGER | null |  | |
| **INFORMANT_CODE** | TEXT | null |  | |
| **RESPONSE_CODE** | TEXT | null |  | |
| **HOUSEHOLD_SIZE** | SMALLINT | null |  | |
| **VISIT_MONTH** | INTEGER | null |  | |
| **MULTIPLIER** | INTEGER | null |  | | 


## Relationships


## Database Diagram

```mermaid
erDiagram
	Level_15 {
		TEXT Survey_Name
		TEXT Year
		TEXT FSU_Serial_No
		TEXT Sector
		TEXT State
		TEXT NSS_Region
		TEXT District
		TEXT Stratum
		TEXT Sub_stratum
		TEXT Panel
		TEXT Sub_sample
		TEXT FOD_Sub_Region
		TEXT Sample_SU_No
		TEXT Sample_Sub_Division_No
		TEXT Second_Stage_Stratum_No
		TEXT Sample_Household_No
		TEXT Questionnaire_No
		TEXT VISIT
		TEXT LEVEL
		TEXT SECTION
		TEXT TIME_TAKEN
		INTEGER MONTHLY_CONSUMPTION_EXP
		INTEGER ONLINE_EXPENDITURE
		TEXT INFORMANT_CODE
		TEXT RESPONSE_CODE
		SMALLINT HOUSEHOLD_SIZE
		INTEGER VISIT_MONTH
		INTEGER MULTIPLIER
	}
```