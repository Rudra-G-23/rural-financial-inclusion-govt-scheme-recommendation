# Level 13 Diagram documentation
## Summary

- [Level 13 Diagram documentation](#level-13-diagram-documentation)
	- [Summary](#summary)
	- [Introduction](#introduction)
	- [Database type](#database-type)
	- [Table structure](#table-structure)
		- [Level\_13](#level_13)
	- [Relationships](#relationships)
	- [Database Diagram](#database-diagram)

## Introduction

## Database type

- **Database system:** PostgreSQL
## Table structure

### Level_13

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
| **Level** | TEXT | null |  | |
| **ITEM_CODE** | TEXT | null |  | |
| **FIRST_PURCHASE_NUMBER** | SMALLINT | null |  | |
| **PURCHASED_ON_HIRE** | TEXT | null |  | |
| **FIRST_PURCHASE_VALUE** | INTEGER | null |  | |
| **REPAIR_COST** | INTEGER | null |  | |
| **SECOND_HAND_NUMBER** | SMALLINT | null |  | |
| **SECOND_HAND_VALUE** | INTEGER | null |  | |
| **TOTAL_EXPENDITURE** | INTEGER | null |  | |
| **MULTIPLIER** | INTEGER | null |  | | 


## Relationships


## Database Diagram

```mermaid
erDiagram
	Level_13 {
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
		TEXT Level
		TEXT ITEM_CODE
		SMALLINT FIRST_PURCHASE_NUMBER
		TEXT PURCHASED_ON_HIRE
		INTEGER FIRST_PURCHASE_VALUE
		INTEGER REPAIR_COST
		SMALLINT SECOND_HAND_NUMBER
		INTEGER SECOND_HAND_VALUE
		INTEGER TOTAL_EXPENDITURE
		INTEGER MULTIPLIER
	}
```