# Level 08 Diagram documentation

## Summary

- [Level 08 Diagram documentation](#level-08-diagram-documentation)
	- [Summary](#summary)
	- [Introduction](#introduction)
	- [Database type](#database-type)
	- [Table structure](#table-structure)
		- [Level 08](#level-08)
	- [Relationships](#relationships)
	- [Database Diagram](#database-diagram)

## Introduction

## Database type

- **Database system:** PostgreSQL
## Table structure

### Level 08

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
| **Item_Code_8_1** | TEXT | null |  | |
| **Out_of_home_qty_000** | DOUBLE PRECISION | null |  | |
| **Out_of_home_value_rs** | SMALLINT | null |  | |
| **Total_consumption_qty_000** | DOUBLE PRECISION | null |  | |
| **Total_consumption_value_rs** | SMALLINT | null |  | |
| **Source_8_1** | TEXT | null |  | |
| **Multiplier** | INTEGER | null |  | | 


## Relationships


## Database Diagram

```mermaid
erDiagram
	Level_08 {
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
		TEXT Item_Code_8_1
		DOUBLE PRECISION Out_of_home_qty_000
		SMALLINT Out_of_home_value_rs
		DOUBLE PRECISION Total_consumption_qty_000
		SMALLINT Total_consumption_value_rs
		TEXT Source_8_1
		INTEGER Multiplier
	}
```