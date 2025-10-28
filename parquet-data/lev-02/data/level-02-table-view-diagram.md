# Level 02 Diagram documentation

## Summary

- [Level 02 Diagram documentation](#level-02-diagram-documentation)
	- [Summary](#summary)
	- [Introduction](#introduction)
	- [Database type](#database-type)
	- [Table structure](#table-structure)
		- [Level 02](#level-02)
	- [Relationships](#relationships)
	- [Database Diagram](#database-diagram)

## Introduction

## Database type

- **Database system:** PostgreSQL
## Table structure

### Level 02

| Name        | Type          | Settings                      | References                    | Note                           |
|-------------|---------------|-------------------------------|-------------------------------|--------------------------------|
| **Survey_Name** | INTEGER | 🔑 PK, not null, unique |  | |
| **Year** | INTEGER | null |  | |
| **FSU_Serial_No** | INTEGER | null |  | |
| **Sector** | INTEGER | null |  | |
| **State** | INTEGER | null |  | |
| **NSS_Region** | INTEGER | null |  | |
| **District** | INTEGER | null |  | |
| **Stratum** | INTEGER | null |  | |
| **Sub_stratum** | INTEGER | null |  | |
| **Panel** | INTEGER | null |  | |
| **Sub_sample** | INTEGER | null |  | |
| **FOD_Sub_Region** | INTEGER | null |  | |
| **Sample_SU_No** | INTEGER | null |  | |
| **Sample_Sub_Division_No** | INTEGER | null |  | |
| **Second_Stage_Stratum_No** | INTEGER | null |  | |
| **Sample_Household_No** | INTEGER | null |  | |
| **Questionnaire_No** | INTEGER | null |  | |
| **Level** | INTEGER | null |  | |
| **Person_Serial_No** | INTEGER | null |  | |
| **Relation_to_Head** | TEXT | null |  | |
| **Gender** | TEXT | null |  | |
| **Age** | INTEGER | null |  | |
| **Marital_Status** | TEXT | null |  | |
| **Education_Level** | TEXT | null |  | |
| **Years_of_Education** | INTEGER | null |  | |
| **Used_Internet_Last_30_Days** | TEXT | null |  | |
| **Days_Away_From_Home_Last_30_Days** | INTEGER | null |  | |
| **Meals_Usually_Taken_Per_Day** | INTEGER | null |  | |
| **Meals_From_School** | INTEGER | null |  | |
| **Meals_From_Employer** | INTEGER | null |  | |
| **Meals_Other** | INTEGER | null |  | |
| **Meals_On_Payment** | INTEGER | null |  | |
| **Meals_At_Home** | INTEGER | null |  | |
| **Revisit_Status** | TEXT | null |  | |
| **FDQ_Original_Member** | TEXT | null |  | |
| **Multiplier** | INTEGER | null |  | | 


## Relationships


## Database Diagram

```mermaid
erDiagram
	Level_02 {
		INTEGER Survey_Name
		INTEGER Year
		INTEGER FSU_Serial_No
		INTEGER Sector
		INTEGER State
		INTEGER NSS_Region
		INTEGER District
		INTEGER Stratum
		INTEGER Sub_stratum
		INTEGER Panel
		INTEGER Sub_sample
		INTEGER FOD_Sub_Region
		INTEGER Sample_SU_No
		INTEGER Sample_Sub_Division_No
		INTEGER Second_Stage_Stratum_No
		INTEGER Sample_Household_No
		INTEGER Questionnaire_No
		INTEGER Level
		INTEGER Person_Serial_No
		TEXT Relation_to_Head
		TEXT Gender
		INTEGER Age
		TEXT Marital_Status
		TEXT Education_Level
		INTEGER Years_of_Education
		TEXT Used_Internet_Last_30_Days
		INTEGER Days_Away_From_Home_Last_30_Days
		INTEGER Meals_Usually_Taken_Per_Day
		INTEGER Meals_From_School
		INTEGER Meals_From_Employer
		INTEGER Meals_Other
		INTEGER Meals_On_Payment
		INTEGER Meals_At_Home
		TEXT Revisit_Status
		TEXT FDQ_Original_Member
		INTEGER Multiplier
	}
```