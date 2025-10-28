# Level 10 Diagram documentation
## Summary

- [Level 10 Diagram documentation](#level-10-diagram-documentation)
	- [Summary](#summary)
	- [Introduction](#introduction)
	- [Database type](#database-type)
	- [Table structure](#table-structure)
		- [Level\_10](#level_10)
	- [Relationships](#relationships)
	- [Database Diagram](#database-diagram)

## Introduction

## Database type

- **Database system:** PostgreSQL
## Table structure

### Level_10

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
| **Item_Code_12_series** | TEXT | null |  | |
| **OOHP_Quantity_12_series** | SMALLINT | null |  | |
| **OOHP_Value_12_series** | SMALLINT | null |  | |
| **Total_Consumption_Quantity_12_se** | SMALLINT | null |  | |
| **Total_Consumption_Value_12_serie** | SMALLINT | null |  | |
| **Source_12_series** | TEXT | null |  | |
| **Multiplier** | INTEGER | null |  | | 


## Relationships


## Database Diagram

```mermaid
erDiagram
	Level_10 {
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
		TEXT Item_Code_12_series
		SMALLINT OOHP_Quantity_12_series
		SMALLINT OOHP_Value_12_series
		SMALLINT Total_Consumption_Quantity_12_se
		SMALLINT Total_Consumption_Value_12_serie
		TEXT Source_12_series
		INTEGER Multiplier
	}
```