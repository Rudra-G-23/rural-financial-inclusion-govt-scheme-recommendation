# 🧾 HCES 2023–24 — LEVEL  03 Data Dictionary

Link: https://microdata.gov.in/NADA/index.php/catalog/237/data-dictionary/F3?file_name=LEVEL%20-%2003

| **Column Name**                      | **Simple Description (For Non-Technical Audience)**                                                                                 |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Survey_Name**                      | Name of the survey conducted.                                                                                                       |
| **Year**                             | Year when the data was collected.                                                                                                   |
| **FSU_Serial_No**                    | Serial number of the First Stage Unit (FSU), i.e., the area or block selected for survey.                                           |
| **Sector**                           | Type of area: Rural or Urban.                                                                                                       |
| **State**                            | Name of the state where the household is located.                                                                                   |
| **NSS_Region**                       | Statistical region code as defined by NSS (used for grouping areas).                                                                |
| **District**                         | Name of the district.                                                                                                               |
| **Stratum**                          | Sampling layer used to group households with similar features for fair representation.                                              |
| **Sub_stratum**                      | Sub-layer within a stratum for more detailed classification.                                                                        |
| **Panel**                            | Indicates if the data belongs to a repeated survey panel.                                                                           |
| **Sub_sample**                       | Identifies smaller sample sets within the main survey.                                                                              |
| **FOD_Sub_Region**                   | Sub-region under the Field Operations Division (responsible for data collection).                                                   |
| **Sample_SU_No**                     | Number assigned to the selected survey unit (SU).                                                                                   |
| **Sample_Sub_Division_No**           | Sub-division number of the sample unit.                                                                                             |
| **Second_Stage_Stratum_No**          | Stratum number for the second stage of sampling (households).                                                                       |
| **Sample_Household_No**              | Unique number for each household included in the sample.                                                                            |
| **Questionnaire_No**                 | Identification number of the questionnaire used.                                                                                    |
| **Level**                            | Indicates the section/level of the dataset.                                                                                         |
| **HH_Size_FDQ**                      | Total number of household members recorded in the First Data Questionnaire (FDQ).                                                   |
| **Engaged_in_Economic_Activity_Las** | Whether any household member was engaged in economic activities (excluding domestic workers or paying guests) in the past 365 days.{1:Y, 2:N} |
| **NCO_2015_Code**                    | Code based on National Classification of Occupations 2015 (3-digit occupation code).                                                |
| **NIC_2008_Code**                    | Code based on National Industrial Classification 2008 (5-digit industry code).                                                      |
| **Max_Income_Activity**              | Broad type of activity that provided the household with maximum income in the past year.   {1:Self-employment, 2:Regular wage/salary earning, 3:Casual Labour}                                |
| **Self_Employment_Source_Sector**    | Whether self-employment income was mainly from agriculture(1) or non-agriculture(2).                                                      |
| **Regular_Wage_Source_Sector**       | Whether regular wage/salary income was mainly from agriculture(3) or non-agriculture.(4)                                                  |
| **Casual_Labour_Source_Sector**      | Whether casual labour income was mainly from agriculture(5) or non-agriculture.(6)                                                        |
| **Household_Type**                   | Type of household based on main source of income or livelihood.                                                                     |
| **Religion_of_HH_Head**              | Religion of the head of the household. (*See below)                                                                                             |
| **Social_Group_of_HH_Head**          | Social group/caste category of the household head.    (*See Below)                                                                              |
| **Land_Ownership**                   | Indicates whether the household owns any land (either possessed or leased out).     {1:Y, 2:N}                                                |
| **Type_of_Land_Owned**               | Type of land owned (e.g., agricultural, non-agricultural). {1:Homestead only, 2:Homestead and other land, 3:Other land only}                                                                         |
| **Total_Area_Land_Owned_Acres**      | Total area of land owned by the household (in acres, up to 2 decimal places).                                                       |
| **Dwelling_Unit_Exists**             | Whether the household has its own dwelling unit at the place of survey. {1:Y, 2:0}                                                            |
| **Type_of_Dwelling_Unit**            | Type of housing unit (e.g., kutcha, pucca, rented, owned). {1:Owned, 2:Hired, 3:Others}                                                                          |
| **Energy_Source_Cooking**            | Main source of energy used for cooking (e.g., LPG, wood, electricity). (*See Below)                                                             |
| **Energy_Source_Lighting**           | Main source of energy used for lighting (e.g., electricity, kerosene, solar).                (*See Below)                                       |
| **Ration_Card_Type**                 | Type of ration card held by the household (e.g., APL, BPL, Antyodaya).         (*See Below)                                                     |
| **Rent_Rate_Available_Rural**        | Whether local rent rate data is available (only applicable to rural areas).    {1:Y, 2:N}                                                     |
| **Benefitted_From_PMGKY**            | Whether the household benefited from the **Pradhan Mantri Garib Kalyan Yojana (PMGKY)** {1:Y, 2:N}.                                            |
| **Multiplier**                       | Weight assigned to the household for statistical representation of the total population.                                            |

---

#### Region_of_HH_Head

|Value | Category |
|-----------|-----------------|
|01  |Not Reported |
|02  |Hinduism |
|30  |Islam |
|04  |Christianity |
|05  |Sikhism |
|06  |Jainism |
|07  |Buddhism |
|08  |Zoroastrianism |
|09  |Others |


#### Social_Group_of_HH_Head
|Value|	Category|		
|----------|-----------|
|0    |	Not reported        |
|1    |	scheduled tribe|
|2    |	scheduled Caste|
|3    |	other backward class|
|9    |	others|

#### Energy_Source_Cooking
| Value | Category                                                      |
| ----- | ------------------------------------------------------------- |
| 01    | firewood, chips & crop residue                                |
| 02    | LPG                                                           |
| 03    | other natural gas                                             |
| 04    | dung cake                                                     |
| 05    | kerosene                                                      |
| 06    | coke, coal                                                    |
| 07    | gobar gas                                                     |
| 08    | other biogas                                                  |
| 09    | others                                                        |
| 10    | charcoal                                                      |
| 11    | electricity (incl. generated by solar /wind power generators) |
| 12    | no cooking arrangement                                        |

#### Energy_Source_Lighting
| Value | Category                                                      |
| ----- | ------------------------------------------------------------- |
| 1     | electricity (incl. generated by solar /wind power generators) |
| 2     | kerosene                                                      |
| 3     | other oil                                                     |
| 4     | gas                                                           |
| 5     | candle                                                        |
| 6     | no lighting arrangement                                       |
| 9     | others                                                        |


#### Ration_Card_Type
| Value | Category                          |
| ----- | --------------------------------- |
| 0     | No ration card                    |
| 1     | Antyodaya Anna Yojana (AAY)       |
| 2     | Below Poverty Line (BPL)          |
| 3     | Above Poverty Line (APL)          |
| 4     | Priority House Holds (PHH)        |
| 5     | State Food Security Scheme (SFSS) |
| 9     | Others                            |
