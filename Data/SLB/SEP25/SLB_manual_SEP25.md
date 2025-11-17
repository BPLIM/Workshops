---
title: Historical Series of the Portuguese Banking Sector - Data Manual
subtitle: Extraction Date - September 2025
author: BPLIM
date: 12 November 2025
abstract: 'The Historical Series of the Portuguese Banking Sector (SLB) provides comprehensive data on Portuguese credit institutions from 1990 to 2024. The dataset combines eight different data tables covering financial statements (3 tables), credit operations, interest rates, human resources, branch networks, and payment systems. Data is available at both quarterly and yearly frequencies, reported at the banking group level, and updated once a year.'
doi: 10.17900/SLB.Sep2025.V1
pdf-engine: pdflatex
engine: knitr
execute:
  echo: false
  warning: false
format:
  pdf: 
    toc: true
  html:
    toc: true
    footnotes-hover: true
    code-fold: true
    code-copy: true
    theme: default
jupyter: nbstata
---
```{r setup}
#| include: false
library(Statamarkdown)
```

# General Information

> **Dataset Designation in English**: Historical Series of the Portuguese Banking Sector (SLB).

> **Dataset Designation in Portuguese**: Séries Longas do Sector Bancário Português (SLB).

> **Data Type**: longitudinal data.

> **Unit of Analysis**: banking group or stand-alone institution (if not part of a banking group).

> **Frequency**: quarterly and yearly.

> **Start Date**: 1990.

> **Most recent year**: 2024.

> **Reference date**: end of quarter/year.

> **Data Organization**: the data is organized into multiple tables, differentiated by reporting frequency (yearly or quarterly), and information type (QA1-balance sheet statement, QA2-income statement, QA3-solvency, QB1-loans to customers, QB2-interest rates, QC-human resources, QD-branch network, and QE-payment systems). All files are available in Stata format.

> **Version of the Data**: the data made available by BPLIM corresponds to a data freeze at a certain time of the year. Therefore, all files contain information as reported at the extraction date. The most recent update of the data occurred in September 2025.

> **Languages Available**: variables labels are available in Portuguese and in English.^[To view the labels in Stata in either Portuguese (pt) or English (en), use the command `label language pt` or `label language en`, respectively.]

> **Data Access**: this data set is available to external researchers under the conditions detailed in the *[Guide for Researchers Using Banco de Portugal Microdata Research Laboratory (BPLIM) Data](https://github.com/BPLIM/Manuals/blob/master/Guides/01_Guide_for_Researchers/Guide_for_researchers_v072024.pdf)*.  

> **Digital Object Identifier**: 10.17900/SLB.Sep2025.V1  
   
> **New in this extraction**: Updated data for 2023 and 2024, and all identifier variables are now lower case. The period covered in Table QB2-interest rates was shortened due to data quality issues for new operations between 1997 and 2003. Corrections were made to distinguish between missing values and zeros (more details in the section [“Methodology-Other”](#sec-methodology-other))



# Acronyms and Abbreviations

- BPLIM: Banco de Portugal Laboratório de Investigação em Microdados | Banco de Portugal Microdata Research Laboratory

- COREP/FINREP: Common Reporting / Financial Reporting frameworks (EU)

- IAS/IFRS: International Accounting Standards / International Financial Reporting Standards

- MFI: Monetary Financial Institution

- non-MFI: Non-Monetary Financial Institution

- RGICSF: Regime Geral das Instituições de Crédito e Sociedade Financeiras | Legal Framework of Credit Institutions and Financial Companies



# Geographical Coverage 

The geographic scope of this dataset is Portugal, but the reporting criteria vary: some information includes all institutions with headquarters or branches in the country, while other information is limited only to institutions headquartered in Portugal. 


# Population {#sec-population}

This dataset provides information on credit institutions operating in Portugal that are under the direct supervision of the Banco de Portugal, and governed by the national Legal Framework of Credit Institutions and Financial Companies (known as the RGICSF, "Regime Geral das Instituições de Crédito e Sociedade Financeiras").

In particular, the dataset includes information on *deposit-taking corporations* (a type of monetary financial institution (MFI), usually referred to as banks) and *other financial intermediaries* (a type of non-monetary financial institutions (non-MFI), that excludes insurance corporations and pension funds). The latter are only available from 2008 onward. Figure [-@fig-mfi] provides a simple visual overview of the specific [*MFI*](https://data.ecb.europa.eu/methodology/what-monetary-financial-institution) and [*non-MFI*](https://data.ecb.europa.eu/methodology/what-non-monetary-financial-institution) institutions included in this dataset. 

![Monetary and Non-Monetary Financial Institutions included in SLB](./aux_files/figures/MFI and non_MFI SLB.png){#fig-mfi}

However, be aware that the set of credit institutions included is not common to all tables and type of information. The reporting population is table-specific:

- *QA1-Balance Sheet Statement*, *QA2-Income Statement*, and *QA3-Solvency*: include consolidated financial data for institutions that are part of a banking group (MFI and non-MFI according to Figure [-@fig-mfi]), and individual financial data for institutions that operate alone. The *QA3* table includes fewer institutions than the *QA1* and *QA2* tables because some institutions either are not required to report solvency information.

- *QB1-Loans to Customers*, and *QB2-Interest Rates*: include data on credit activities carried out in Portugal by deposit-taking institutions (MFI) headquartered in Portugal and covered in the Monetary and Financial Institution Statistics ("Estatísticas Monetárias e Financeiras" - EMF). The data is aggregated for institutions that are part of a banking group, and individual for institutions that operate alone. 

- *QC-Human Resources* and *QD-Branch Network*: include activity indicators for deposit-taking institutions (MFI) headquartered in Portugal and that are members of the Portuguese Banking Association ("Associação Portuguesa de Bancos"- APB). The data is aggregated for institutions that are part of a banking group, and individual data for institutions that operate alone.

- *QE-Payment Systems*: includes information on payment systems carried out in the national territory by (some) deposit-taking institutions (MFI). The data is aggregated for institutions that are part of a banking group, and individual data for institutions that operate alone.



# Data periods and frequency

This dataset covers the period 1990 to 2024 and includes both quarterly and yearly information. However, the availability of data is not the same for all type of information. Please refer to the table and figure below for the specific period and frequency of each table.[^freq] 


|  **Table** | **Type of information** | **Frequency** | **Data Period** |
| :---------- | :-------------------- |:-------------- |:------------ |
|QA1|		Balance Sheet |	Yearly | 1990-2024 |
|QA1|		Balance Sheet |	Quarterly | 2001Q1-2024Q4 |
|QA2|		Income Statement |	Yearly | 1990-2024 |
|QA2|		Income Statement |	Quarterly | 2001Q1-2024Q4 |
|QA3|		Solvency |	Yearly | 1994-2024 |
|QA3|		Solvency |	Quarterly | 2009Q1-2024Q4 |
|QB1|		Loans to Customers |	Yearly | 1990-2024 |
|QB1|		Loans to Customers |	Quarterly | 2001Q1-2024Q4 |
|QB2|		Interest Rates |	Yearly | 2003-2024 |
|QB2|		Interest Rates |	Quarterly | 2003Q1-2024Q4 |
|QC|		Human Resources |	Yearly | 1990-2024 |
|QD|		Branch Network |	Yearly | 1990-2024 |
|QE|		Payment Systems |	Yearly | 2000-2024 |


: Data period and frequency by table {#tbl-freq}



![Data period, frequency and main series breaks by table](./aux_files/figures/timetable.png){#fig-timetable}


[^freq]: Figure [-@fig-timetable] available in a large size in the section [“Auxiliary Files”](#sec-auxiliary-files). The yearly data reflects year-end information, except for: (1) interest rates, which are computed as the simple average of the quarterly interest rates; and (2) income statement variables, which are summed up over the period. 

# Methodology {#sec-methodology}

The Banco de Portugal created a working group in late 2017 specifically to assemble the Historical Series of the Portuguese Banking Sector data. Since then, the Bank's Statistical Department (DDE) has managed the updates and applied quality controls to the data. Annually, BPLIM works on this information, analyzing, combining, and documenting it to create a single dataset tailored for the research community. The information provided by BPLIM is fully anonymized to ensure data confidentiality.

This dataset compiles information collected over an extended period. Despite our best harmonization efforts, users should be aware that the data collection methods have varied over time, a factor particularly relevant for older information. Furthermore, as detailed in the section ["Population"](#sec-population), the data linkage between tables is not perfect. **Researchers who use information from multiple tables may need to limit their sample size to ensure consistency across institutions.**^[Table [-@tbl-obsy] and [-@tbl-obsq] present the number of entities reporting in each table in each period.]

While this list is not exhaustive, the following are the most critical factors to consider, alongside an explanation of how the information was harmonized.


## A. Changes in reporting population 

- **A1. Changes in scope:** Full financial data reports (tables *QA*) were implemented for all credit institutions (MFI and non-MFI) beginning in 2008. Prior to this, the dataset was limited to deposit-taking corporations (MFI), which nonetheless represented over 98% of total assets. This change resulted in a significant change in the number of included institutions from 56 in 2007 to 84 in 2008. Recall that, for all the other tables, the coverage is limited to deposit-taking corporations (MFI) and subject to restrictions. 

- **A2. Merger or closure**: When an institution ceases to exist (due to a merger or closure), the timing for the cessation of its reporting varies across different types of information, such as financial reports versus operational details like payment systems and branch data. Thus, differences in tables reported are expected.


## B. Adjustments and breaks on financial data

- **B1. Change in the Chart of Accounts for the Banking System ("Plano de Contas do Setor Bancário" - PCSB):** Before 1998, banks reported provisions as a single, combined figure, with no breakdown among provisions for credit, securities, or credit to other financial institutions. In 1998, they began reporting this detailed information.
  
  Procedure: Detailed information was reconstructed based on the 1998 impairment/asset coverage ratio structure. The remaining values were then allocated in proportion to the corresponding aggregates.

- **B2. Adoption of the International Accounting Standards (IAS):** In March 2005, financial reporting switched from the PCSB standard to IAS. This transition caused two key changes: (1) a substantial share of on-balance-sheet securities had to be valued at market prices instead of the original purchase price; and (2) banks began reporting more granular information on several items, a change reinforced by Banco de Portugal Instruction No. 9/2005. The adoption was phased, leading to a two-year overlap where both PCSB and IAS were used by different institutions.

  Procedure: To mitigate the impact of data breaks caused by the adoption of a new reporting system, an extraordinary report was filed by the 13 main institutions that transitioned in 2005. This report provided 2004 **pro forma** financial statements under the new accounting system. With this information, and for these groups only, the figures from 1990 to 2004 were revised. A correction factor was calculated based on the relative difference between the 2004 figures reported under the old PCSB and the new IAS/AAS **pro forma** figures. For all other institutions, no correction factor was applied, and the breaks in the series were accepted.

- **B3. Adoption of the new Common Reporting Framework (COREP):** In 2014, the EU approved the COREP through the Regulation (EU) No 680/2014. The COREP introduced a new prudential reporting system, with impact in the calculation of own funds.

  Procedure: To ensure the series' continuity, the old definition of base own funds was mapped directly to the COREP standard for Tier 1 capital, thus maintaining the new terminology. Total capital was also kept consistent between both reporting frameworks. However, the database does not include Common Equity Tier 1 (CET1) capital; this concept was recently introduced and could not be back-calculated for years prior to 2014.

- **B4. Adoption of new Financial Reporting Standards (FINREP):** In 2014, the EU approved the FINREP through the Regulation (EU) No 680/2014 (same legislation as COREP). The FINREP integrates the same accounting policies as IAS, but with breakdowns and detail levels that are not fully comparable.

  Procedure: The FINREP was adopted by the end of 2015. To link the two series, correspondence tables were built. These tables aimed for maximum precision by using detailed (granular) information and complying to the definitions of the most recent report (FINREP).^[For more details, check appendices 1 and 2 of the *[Historical Series - Portuguese Banking Sector 1990-2018](https://www.bportugal.pt/sites/default/files/anexos/pdf-boletim/historical_series_portuguese_banking_system.pdf)*.]
  
- **B5. Introduction of the IFRS 9 framework:** In January 2018, credit institutions were required to implement the IFRS 9 framework. Among others, the IFRS 9 sets a  forward-looking "Expected Credit Loss" (ECL) model for recognizing impairment on financial assets, replacing the prior "Incurred Loss" model to ensure that credit losses are provisioned earlier in the credit cycle.

  Procedure: Break in the series was accepted.


## C. Adjustments and breaks on credit data - amounts^[For more details, check the section 3.2 of the *[Historical Series - Portuguese Banking Sector 1990-2018 report](https://www.bportugal.pt/sites/default/files/anexos/pdf-boletim/historical_series_portuguese_banking_system.pdf)*.]


- **C1. Residual for external activity of banking groups:** Credit data reported in the Monetary and Financial Institution Statistics does not include external activity of banking groups, and includes loans and deposits of non-residents in Portugal.

  Procedure: To guarantee that the banking activity in *QB* matches the activity reported on a consolidated basis in *QA1*, a residual variable "other credit" was added to *QB1*.
  
- **C2. Break in Monetary and Financial Institution Statistics:** There was a break in the series from 1996 to 1997.

  Procedure: Values from 1990 to 1996 are estimated by "retropolation".

- **C3. Changes to the data source for sector-detailed credit data on non-financial corporations (NFCs):** Credit data to NFCs by sector sourced from Monetary and Financial Institution Statistics up to December 2001, and Central Credit Register ("Central de Responsabilidade de Crédito" - CRC) from December 2002 onward.

  Procedure: For the transition period between January and November 2002, a linear interpolation was used to estimate the sector weights. After December 2002, the CRC became the source for all credit data by sector. 

- **C4. Changes to the reported overdue loans:** The report of overdued loans in Monetary and Financial Institution Statistics became mandatory in 2014.

  Procedure: Before 2014, overdue loan amounts were reported under the broader category of doubtful loans.

- **C5. Aggregation of data for banking groups:** Credit data is reported in the Monetary and Financial Institution Statistics on an individual basis. 

  Procedure: To ensure the credit data in *QB1* is consistent with the consolidated financial data in *QA1*, the individual data is aggregated and netted for intra-group positions using balance sheet information on loans to financial corporations (main item for intra-group activity). However, since loan data to financial corporations is only available from FINREP (2015 onward), these values had to be estimated ("retropolated" or proxied) for the previous periods.


## D. Adjustments and breaks on credit data - interest rates^[For more details, check the section 3.3 of the *[Historical Series - Portuguese Banking Sector 1990-2018 report](https://www.bportugal.pt/sites/default/files/anexos/pdf-boletim/historical_series_portuguese_banking_system.pdf)*.]

- **D1. Interest rates on new business:** Originally reported monthly and by maturity.

  Procedure: Quarterly figures resulted from monthly data that was initially averaged using the amounts for various contractual maturities, and then weighted by the respective monthly business volume. Yearly data is a simple average of the quarterly figures.

- **D2. Interest rates on outstanding amounts:** Originally reported monthly.

  Procedure: Quarterly figures represent end-of-period positions.

- **D3. Changes in coverage:** Up to the first quarter of 2010, the interest rate data was collected solely from a representative sample that included only certain banking groups.

  Procedure: Break in the series was accepted, resulting on a narrower set of institutions covered in the initial period.


## E. Adjustments and breaks on human resources and branch network data

- **E1. External activity:** There are missing values reported, both for human resources and branch network.

  Procedure: In some cases, when the institution’s internal total human resources (or of an institution belonging to the group) is available, the external total human resources was estimated.

- **E2. Detail data:** For some variables information is not available for all years.^[For more details, check section 3.4 and 3.5 of the *[Historical Series - Portuguese Banking Sector 1990-2018 report](https://www.bportugal.pt/sites/default/files/anexos/pdf-boletim/historical_series_portuguese_banking_system.pdf)*.] 



## F. Adjustments and breaks on payment systems data

- **F1. ATMs and POS terminal data:** Starting in 2000, while the other data starts in 2001.



## G. Other {#sec-methodology-other}

- **Mergers, acquisitions and restructuring:** Institutions frequently undergo M&A events and major restructurings that change their legal form. This dataset follows the principle of core banking group continuity. We track the group's banking activity over time, even if there are substantial legal or structural changes, provided the core business and activities remain the same. This allows for a consistent, long-term view of banking activity. 

- **Missing observation vs missing data vs zeros values:** Because the population criteria for this dataset is dynamic and table-dependent, comparisons across tables can be challenging. To help researchers accurately interpret the data, the dataset distinguishes between three types of missing information.

    - Missing observation: This occurs when an institution does not comply with a table's population criteria for a specific period. The institutionID-dateID combination is not reported in the table, meaning the institution should not be considered part of the table's population for that period.
    
    Example: A MFI stops being a member of the *APB* in 2021; its data is absent in table *QC* from 2021 onward. 
    
    - Missing data: This occurs when an institution does comply with a table's population criteria but data could not be obtained or compiled. The institutionID-dateID combination is reported, but the variables contain missing values for all variables.
    
    Example: A MFI is a member of the *APB* from 2010 to 2020, but data for 2015 could not be obtained; the observation for institutionID-2015 in table *QC* is reported with missing values.
    
    - Zero values: This occurs when an institution complies with a table's population criteria and the reported value for a specific (or all) variable(s) is zero. The institutionID-dateID combination is reported, and the variable values are set to 0. The data is available, and the true measure is numerically zero.


## H. What changed with the new extraction?

- Identifiers have been renamed to lower case;

- The period covered in Table QB2-interest rates was shortened due to data quality issues for new operations between 1997 and 2003;

- The criteria for missing data were revised, and minor corrections were made to previously recorded missing values and zeros. (See the section [“Methodology-Other”](#sec-methodology-other) for details.)


# Description of Variables

Below we provide a general description of the variables included in each data file referred above. For a full account of all variable categories see the section [“Auxiliary Files”](#sec-auxiliary-files).

## Identifiers (common to all tables)

`Anonimized bank identification number` (*bina*) - Anonymized identification number for financial institution that enables tracking the institution over time. BPLIM provides an anonymized version of the financial institution identifier which is denoted by *bina*.

`Date` (*date*)  - Reference quarter/year of the data

`Year` (*year*) - Reference year of the data


## QA1-Balance Sheet Statement Variables

| Variable Name | Variable Description | Unit | Available Period - Yearly Data |  Available Period - Quarterly Data |
| :------ | :------- | :--- | :------: | :------: |
|	QA1_1	|	Cash and cash balances/loans to central banks	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_2	|	Demand deposits in other credit institutions	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_3	|	Loan to other credit institutions - Carrying amount	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_3_1	| > Loan to other credit institutions - Gross carrying amount	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_3_2	|	> Loan to other credit institutions - Impairments and value adjustments	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_4	|	Loan to customers - Carrying amount	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_4_1	|	> Loan to customers - Gross carrying amount	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_4_2	|	> Loan to customers - Impairments and value adjustments	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_5	|	Debt securities - Carrying amount	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_5_1	|	> Debt securities - Gross carrying amount	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_5_1_1	|	> > Debt securities - Gross carrying amount - General government	|	€Millions 	|	1998	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_5_1_2	|	> > Debt securities - Gross carrying amount - Other issuers	|	€Millions 	|	1998	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_5_2	|	> Debt securities - Impairments and value adjustments	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_6	|	Equity instruments	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_7	|	Investments in subsidiaries, joint ventures and associates	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_8	|	Tangible assets	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_9	|	Intangible assets	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_10	|	Other assets	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_10_1	|	> Other assets - Tax assets	|	€Millions 	|	2005	-	2024	|	2005Q1	-	2024Q4	| c                                                                                              
|	QA1_10_1_1	|	> > Other assets - Tax assets - Deferred taxes	|	€Millions 	|	2005	-	2024	|	2005Q1	-	2024Q4	|
|	QA1_10_1_2	|	> > Other assets - Tax assets - Current taxes	|	€Millions 	|	2005	-	2024	|	2005Q1	-	2024Q4	|
|	QA1_10_2	|	> Other assets - Others	|	€Millions 	|	2005	-	2024	|	2005Q1	-	2024Q4	|
|	QA1_11	|	Total assets	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_12	|	Deposits from central banks and other credit institutions	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_12_1	|	> Deposits from central banks and other credit institutions - central banks	|	€Millions 	|	2005	-	2024	|	2005Q1	-	2024Q4	|
|	QA1_12_2	|	> Deposits from central banks and other credit institutions - other credit institutions	|	€Millions 	|	2005	-	2024	|	2005Q1	-	2024Q4	|
|	QA1_13	|	Customer deposits	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_13_1	|	> Customer deposits - Short-term deposits	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_13_2	|	> Customer deposits - Deposits with agreed maturity	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_14	|	Liabilities represented by debt securities	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_15	|	Other liabilities (includes derivatives and short-term liabilities)	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_16	|	Total Liabilities	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_17	|	Equity	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_17_1	|	> Equity - Capital	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_17_2	|	> Equity - Share premium	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_17_3	|	> Equity - Reserves	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_17_3_1	|	> > Equity - Reserves - Retained earnings	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_17_3_2	|	> > Equity - Reserves - Other reserves	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_17_4	|	> Equity - Minority interests	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_17_5	|	> Equity - Consolidated income for the year	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA1_17_6	|	> Equity - Own shares (-)	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|

: Variables of the table *QA1-Balance Sheet Statement* {#tbl-QA1var}
  
  
## QA2-Income Statement Variables

| Variable Name | Variable Description | Unit | Available Period - Yearly Data |  Available Period - Quarterly Data |
| :------ | :------- | :--- | :------: | :------: |
|	QA2_1	|	Interest income	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA2_2	|	Interest expenses	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA2_3	|	Net interest income	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA2_4	|	Capital gains (net)	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA2_5	|	Income from services and commissions (net)	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA2_5_1	|	> Income from services and commissions received	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA2_5_2	|	> Income from services and commissions paid	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA2_6	|	Income from financial operations	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA2_7	|	Other operating results	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA2_8	|	Total operating income	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA2_9	|	Staff expenses	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA2_10	|	Other administrative expenses	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA2_11	|	Depreciation	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA2_12	|	Provisions and impairments (net of reversals)	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA2_12_1	|	> Provisions or reversal of provisions (net)	|	€Millions 	|	2005	-	2024	|	2005Q1	-	2024Q4	|
|	QA2_12_2	|	> Impairment losses and other net value adjustments	|	€Millions 	|	2005	-	2024	|	2005Q1	-	2024Q4	|
|	QA2_12_2_1	|	> > Credit impairment losses	|	€Millions 	|	2005	-	2024	|	2005Q1	-	2024Q4	|
|	QA2_12_2_2	|	> > Other impairment losses and value adjustments	|	€Millions 	|	2005	-	2024	|	2005Q1	-	2024Q4	|
|	QA2_13	|	Other profit or (-) loss	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA2_14	|	Profit or (-) loss before tax	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA2_15	|	Tax expenses or income related to profit or loss	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA2_16	|	Net profit or (-) loss	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA2_17	|	Profit/loss for year attributable to minority interest	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QA2_18	|	Profit/loss for year attributable to owners of parent	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|

: Variables of the table *QA2-Income Statement* {#tbl-QA2var}


## QA3-Solvency Variables

| Variable Name | Variable Description | Unit | Available Period - Yearly Data |  Available Period - Quarterly Data |
| :------ | :------- | :--- | :------: | :------: |
|	QA3_1	|	Tier 1 capital	|	€Millions 	|	1996	-	2024	|	2009Q1	-	2024Q4	|
|	QA3_2	|	Total own funds	|	€Millions 	|	1994	-	2024	|	2009Q1	-	2024Q4	|
|	QA3_3	|	Risk-weighted assets	|	€Millions 	|	1994	-	2024	|	2009Q1	-	2024Q4	|
|	QA3_4	|	Tier 1 capital ratio	|	Percentage	|	1996	-	2024	|	2009Q1	-	2024Q4	|
|	QA3_5	|	Total capital ratio	|	Percentage	|	1994	-	2024	|	2009Q1	-	2024Q4	|

: Variables of the table *QA3-Solvency* {#tbl-QA3var}


## QB1-Loans to Customers Variables

| Variable Name | Variable Description | Unit | Available Period - Yearly Data |  Available Period - Quarterly Data |
| :------ | :------- | :--- | :------: | :------: |
|	QB1_1	|	Gross loans to customers	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QB1_1_1	|	> Gross Loans except to other financial companies	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QB1_1_1_1	|	> > Domestic credit except to other financial companies	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QB1_1_1_1_1	|	> > > Domestic credit to non-financial corporations	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QB1_1_1_1_1_1	|	> > > > Domestic credit to NFCs - Agriculture and fishing	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QB1_1_1_1_1_2	|	> > > > Domestic credit to NFCs – Mining and quarrying and Manufacturing	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QB1_1_1_1_1_3	|	> > > > Domestic credit to NFCs – Construction and public works	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QB1_1_1_1_1_4	|	> > > > Domestic credit to NFCs – Electricity, gas and water	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QB1_1_1_1_1_5	|	> > > > Domestic credit to NFCs – Services	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QB1_1_1_1_1_6	|	> > > > Domestic credit to NFCs – Other	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QB1_1_1_1_2	|	> > > Domestic credit to general government	|	€Millions 	|	1996	-	2024	|	2001Q1	-	2024Q4	|
|	QB1_1_1_1_3	|	> > > Domestic credit to households 	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QB1_1_1_1_3_1	|	> > > > Domestic housing credit	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QB1_1_1_1_3_2	|	> > > > Domestic credit for consumption and other purposes	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QB1_1_1_2	|	> > Other credit	|	€Millions 	|	1990	-	2024	|	2001Q1	-	2024Q4	|
|	QB1_1_2	|	> Domestic credit to other financial companies	|	€Millions 	|	1992	-	2024	|	2001Q1	-	2024Q4	|
|	QB1_2	|	Domestic overdue credit	|	€Millions 	|	1997	-	2024	|	2001Q1	-	2024Q4	|
|	QB1_2_1	|	> Domestic overdue credit to non-financial companies	|	€Millions 	|	1997	-	2024	|	2001Q1	-	2024Q4	|
|	QB1_2_1_1	|	> > Domestic overdue credit to NFCs – Agriculture and fishing	|	€Millions 	|	1997	-	2024	|	2001Q1	-	2024Q4	|
|	QB1_2_1_2	|	> > Domestic overdue credit to NFCs – Mining and quarrying and Manufacturing	|	€Millions 	|	1997	-	2024	|	2001Q1	-	2024Q4	|
|	QB1_2_1_3	|	> > Domestic overdue credit to NFCs – Construction and public works	|	€Millions 	|	1997	-	2024	|	2001Q1	-	2024Q4	|
|	QB1_2_1_4	|	> > Domestic overdue credit to NFCs – Electricity, gas and water	|	€Millions 	|	1997	-	2024	|	2001Q1	-	2024Q4	|
|	QB1_2_1_5	|	> > Domestic overdue credit to NFCs – Services	|	€Millions 	|	1997	-	2024	|	2001Q1	-	2024Q4	|
|	QB1_2_1_6	|	> > Domestic overdue credit to NFCs – Other	|	€Millions 	|	1997	-	2024	|	2001Q1	-	2024Q4	|
|	QB1_2_2	|	> Domestic overdue credit to general government	|	€Millions 	|	1997	-	2024	|	2001Q1	-	2024Q4	|
|	QB1_2_3	|	> Domestic overdue credit to households 	|	€Millions 	|	1997	-	2024	|	2001Q1	-	2024Q4	|
|	QB1_2_3_1	|	> > Domestic overdue housing credit	|	€Millions 	|	1997	-	2024	|	2001Q1	-	2024Q4	|
|	QB1_2_3_2	|	> > Domestic overdue credit for consumption and other purposes	|	€Millions 	|	1997	-	2024	|	2001Q1	-	2024Q4	|

: Variables of the table *QB1-Loans to Customers* {#tbl-QB1var}


## QB2-Interest Rates Variables

| Variable Name | Variable Description | Unit | Available Period - Yearly Data |  Available Period - Quarterly Data |
| :------ | :------- | :--- | :------: | :------: |
|	QB2_1_1	|	Interest rates on outstanding amounts - Loans/Credits	|	Percentage	|	2003	-	2024	|	2003Q1	-	2024Q4	|
|	QB2_1_1_1	|	> Interest rates on outstanding amounts - Credits to non-financial corporations	|	Percentage	|	2003	-	2024	|	2003Q1	-	2024Q4	|
|	QB2_1_1_2	|	> Interest rates on outstanding amounts - Loans to households 	|	Percentage	|	2003	-	2024	|	2003Q1	-	2024Q4	|
|	QB2_1_1_2_1	|	> > Interest rates on outstanding amounts - Housing loans	|	Percentage	|	2003	-	2024	|	2003Q1	-	2024Q4	|
|	QB2_1_1_2_2	|	> > Interest rates on outstanding amounts - Credit for consumption and other purposes	|	Percentage	|	2003	-	2024	|	2003Q1	-	2024Q4	|
|	QB2_1_2	|	Interest rates on outstanding amounts - Deposits	|	Percentage	|	2003	-	2024	|	2003Q1	-	2024Q4	|
|	QB2_1_2_1	|	> Interest rates on outstanding amounts - Demand deposits	|	Percentage	|	2003	-	2024	|	2003Q1	-	2024Q4	|
|	QB2_1_2_1_1	|	> > Interest rates on outstanding amounts - Demand deposits to non-financial corporations	|	Percentage	|	2003	-	2024	|	2003Q1	-	2024Q4	|
|	QB2_1_2_1_2	|	> > Interest rates on outstanding amounts - Demand deposits to households 	|	Percentage	|	2003	-	2024	|	2003Q1	-	2024Q4	|
|	QB2_1_2_2	|	> Interest rates on outstanding amounts - Other deposits	|	Percentage	|	2003	-	2024	|	2003Q1	-	2024Q4	|
|	QB2_1_2_2_1	|	> > Interest rates on outstanding amounts - Other deposits to non-financial corporations	|	Percentage	|	2003	-	2024	|	2003Q1	-	2024Q4	|
|	QB2_1_2_2_2	|	> > Interest rates on outstanding amounts - Other deposits to households 	|	Percentage	|	2003	-	2024	|	2003Q1	-	2024Q4	|
|	QB2_2_1	|	Interest rates on new loans	|	Percentage	|	2003	-	2024	|	2003Q1	-	2024Q4	|
|	QB2_2_1_1	|	> Interest rates on new loans to non-financial corporations	|	Percentage	|	2003	-	2024	|	2003Q1	-	2024Q4	|
|	QB2_2_1_2	|	> Interest rates on new loans to households 	|	Percentage	|	2003	-	2024	|	2003Q1	-	2024Q4	|
|	QB2_2_1_2_1	|	> > Interest rates on new loans to households: Housing loans	|	Percentage	|	2003	-	2024	|	2003Q1	-	2024Q4	|
|	QB2_2_1_2_2	|	> > Interest rates on new loans: Credit for consumption and other purposes	|	Percentage	|	2003	-	2024	|	2003Q1	-	2024Q4	|
|	QB2_2_2	|	Interest rates on deposits: New deposits	|	Percentage	|	2003	-	2024	|	2003Q1	-	2024Q4	|
|	QB2_2_2_1	|	> Interest rates on deposits: New deposits to non-financial corporations	|	Percentage	|	2003	-	2024	|	2003Q1	-	2024Q4	|
|	QB2_2_2_2	|	> Interest rates on deposits: New deposits to households 	|	Percentage	|	2003	-	2024	|	2003Q1	-	2024Q4	|

: Variables of the table *QB2-Interest Rates* {#tbl-QB2var}


## QC-Human Resources Variables

| Variable Name | Variable Description | Unit | Available Period - Yearly Data |
| :------ | :------- | :--- | :------: |
|	QC_1	|	Total	|	Number	|	1992	-	2024	|
|	QC_2	|	International activity	|	Number	|	1992	-	2024	|
|	QC_2_1	|	> Branches and foreign subsidiaries	|	Number	|	1990	-	2024	|
|	QC_2_2	|	> Consolidated foreign bank branches	|	Number	|	1990	-	2024	|
|	QC_3	|	Domestic activity - Banking institutions	|	Number	|	1990	-	2024	|
|	QC_3_1_1	|	> By gender: Male	|	Number	|	2005	-	2024	|
|	QC_3_1_2	|	> By gender: Female	|	Number	|	2005	-	2024	|
|	QC_3_2_1	|	> By age: <30 years old	|	Number	|	1990	-	2024	|
|	QC_3_2_2	|	> By age: 30-44 years old	|	Number	|	1990	-	2024	|
|	QC_3_2_3	|	> By age:> 44 years old	|	Number	|	1990	-	2024	|
|	QC_3_3_1	|	> By seniority: <1 year	|	Number	|	1993	-	2024	|
|	QC_3_3_2	|	> By seniority: 1-5 years	|	Number	|	1990	-	2024	|
|	QC_3_3_3	|	> By seniority: 6-10 years	|	Number	|	1990	-	2024	|
|	QC_3_3_4	|	> By seniority: 11-15 years	|	Number	|	1990	-	2024	|
|	QC_3_3_5	|	> By seniority:> 15 years	|	Number	|	1990	-	2024	|
|	QC_3_4_1	|	> By contract type: Permanent	|	Number	|	2005	-	2024	|
|	QC_3_4_2	|	> By contract type: Fixed-term contract	|	Number	|	2005	-	2024	|
|	QC_3_5_1	|	> By education: Basic	|	Number	|	1993	-	2024	|
|	QC_3_5_2	|	> By education: Secondary	|	Number	|	1993	-	2024	|
|	QC_3_5_3	|	> By education: Higher	|	Number	|	1993	-	2024	|
|	QC_3_6_1	|	> By function: Management	|	Number	|	1995	-	2024	|
|	QC_3_6_2	|	> By functions: Specific	|	Number	|	1995	-	2024	|
|	QC_3_6_3	|	> By function: Administrative	|	Number	|	1995	-	2024	|
|	QC_3_6_4	|	> By function: Support	|	Number	|	1995	-	2024	|
|	QC_3_7_1	|	> By activity: Commercial	|	Number	|	1990	-	2024	|
|	QC_3_7_2	|	> By activity: Other	|	Number	|	1990	-	2024	|

: Variables of the table *QC-Human Resources* {#tbl-QCvar}


## QD-Branch Network Variables

| Variable Name | Variable Description | Unit | Available Period - Yearly Data |
| :------ | :------- | :--- | :------: |
|	QD_1	|	Total	|	Number	|	1992	-	2024	|
|	QD_2	|	Total international activity 	|	Number	|	1992	-	2024	|
|	QD_2_1	|	> Branches and foreign subsidiaries	|	Number	|	1992	-	2024	|
|	QD_2_2	|	> Consolidated foreign bank branches	|	Number	|	1992	-	2024	|
|	QD_3	|	Total domestic activity	|	Number	|	1990	-	2024	|

: Variables of the table *QD-Branch Network* {#tbl-QDvar}



## QE-Payment Systems Variables

| Variable Name | Variable Description | Unit | Available Period - Yearly Data |
| :------ | :------- | :--- | :------: |
|	QE_1	|	Number of ATMs	|	Number	|	2000	-	2024	|
|	QE_2	|	Number of POS terminals	|	Number	|	2000	-	2024	|
|	QE_3	|	Number of payment transactions	|	Number	|	2001	-	2024	|
|	QE_3_1	|	> Cheques	|	Number	|	2001	-	2024	|
|	QE_3_2	|	> Bills of trade and bills of exchange	|	Number	|	2001	-	2024	|
|	QE_3_3	|	> Direct debits	|	Number	|	2001	-	2024	|
|	QE_3_4	|	> Multibanco	|	Number	|	2001	-	2024	|
|	QE_3_4_1	|	> > Home banking payments	|	Number	|	2001	-	2024	|
|	QE_3_4_2	|	> > ATM payments	|	Number	|	2001	-	2024	|
|	QE_3_4_3	|	> > Residual of card payments network	|	Number	|	2001	-	2024	|
|	QE_3_5	|	> Credit transfers	|	Number	|	2001	-	2024	|
|	QE_4	|	Value of payment transactions	|	€Millions 	|	2001	-	2024	|
|	QE_4_1	|	> Cheques	|	€Millions 	|	2001	-	2024	|
|	QE_4_2	|	> Bills of trade and bills of exchange	|	€Millions 	|	2001	-	2024	|
|	QE_4_3	|	> Direct debits	|	€Millions 	|	2001	-	2024	|
|	QE_4_4	|	> Multibanco	|	€Millions 	|	2001	-	2024	|
|	QE_4_4_1	|	> > Home banking payments	|	€Millions 	|	2001	-	2024	|
|	QE_4_4_2	|	> > ATM payments	|	€Millions 	|	2001	-	2024	|
|	QE_4_4_3	|	> > Withdrawals	|	€Millions 	|	2001	-	2024	|
|	QE_4_4_4	|	> > Purchases	|	€Millions 	|	2001	-	2024	|
|	QE_4_4_5	|	> > Residual of card payments network	|	€Millions 	|	2001	-	2024	|
|	QE_4_5	|	> Credit transfers	|	€Millions 	|	2001	-	2024	|

: Variables of the table *QE-Payment Systems* {#tbl-QEvar}



# Basic Descriptive Statistics

We provide basic descriptive statistics based on perturbed data in the [“Auxiliary Files”](#sec-auxiliary-files) section. Since the reporting institutions vary by table and period, we also include Table [-@tbl-obsy] and [-@tbl-obsq], which show the number of institutions reporting for each table-period. According to the missing data criteria outlined in ["Missing observation vs missing data vs zeros values"](#sec-methodology-other), an institution that is expected to report but for which data could not be collected will still appear in the dataset with missing values. These cases are included in the counts shown in Table [-@tbl-obsy] and [-@tbl-obsq]

```{stata}
*| output: false
*| echo: false
*| ExecuteTime: {end_time: '2023-06-20T08:57:52.682458Z', start_time: '2023-06-20T08:57:52.153836Z'}

set linesize 200
global path "U:/DEE-BPLIM/data/products/SLB/2025_09/output/data/final_A"

local filelist "${path}/SLB_A_YBNK_19902024_SEP25_QA1_V01.dta ${path}/SLB_A_YBNK_19902024_SEP25_QA2_V01.dta ${path}/SLB_A_YBNK_19942024_SEP25_QA3_V01.dta ${path}/SLB_A_YBNK_19902024_SEP25_QB1_V01.dta ${path}/SLB_A_YBNK_20032024_SEP25_QB2_V01.dta ${path}/SLB_A_YBNK_19902024_SEP25_QC_V01.dta ${path}/SLB_A_YBNK_19902024_SEP25_QD_V01.dta ${path}/SLB_A_YBNK_20002024_SEP25_QE_V01.dta"

// 2. Initialize a temporary dataset to store the counts
tempfile counts_data
local first_file=1


// 3. Loop through each file, count observations by year, and append to the temporary file 
foreach filename in `filelist' {
    // Check if the file exists before attempting to load
    capture confirm file "`filename'"
    if _rc {
        di as error "File not found: `filename'. Skipping."
        continue
    }
    
    // Load the current file
    qui{
      use year using "`filename'", clear
      gen tmp=1
    
    
    
      collapse (sum) tmp, by(year)
      
      // Add a variable to store the original filename 
      local tmp2 = subinstr("`filename'", "${path}", "", .)
  	local filename_short=substr("`tmp2'",28,3)
      rename tmp `filename_short'
    
	
    	if `first_file' {
            // For the very first file, SAVE the result to the tempfile.
            // This ensures the tempfile is created with variables and data.
            save `counts_data', replace
            local first_file = 0 // Turn off the flag
        }
      else {
          // For all subsequent files, APPEND the result to the tempfile.
          append using `counts_data'
          save `counts_data', replace // Save the updated combined file
      }
    }
}

qui{
  collapse (sum) Q*, by(year)
  rename QC_ QC
  rename QD_ QD
  rename QE_ QE
  order year QA1 QA2 QA3 QB1 QB2 QC QD QE
  sort year
  save `counts_data', replace
  export delimited using "./aux_files/stata/counts_data.csv", replace
  }

```

```{r}
#| label: tbl-obsy
#| tbl-cap: "Number of instituitions in each table -- Yearly Data"
#| echo: false
#| eval: true

library(knitr)
kable(read.csv("./aux_files/stata/counts_data.csv"))
```




```{stata}
*| output: false
*| echo: false
*| ExecuteTime: {end_time: '2023-06-20T08:57:52.682458Z', start_time: '2023-06-20T08:57:52.153836Z'}

set linesize 200
global path "U:/DEE-BPLIM/data/products/SLB/2025_09/output/data/final_A"

local filelist "${path}/SLB_A_QBNK_20012024_SEP25_QA1_V01.dta ${path}/SLB_A_QBNK_20012024_SEP25_QA2_V01.dta ${path}/SLB_A_QBNK_20092024_SEP25_QA3_V01.dta ${path}/SLB_A_QBNK_20012024_SEP25_QB1_V01.dta ${path}/SLB_A_QBNK_20032024_SEP25_QB2_V01.dta"

// 2. Initialize a temporary dataset to store the counts
tempfile counts_dataq
local first_file=1


// 3. Loop through each file, count observations by date, and append to the temporary file 
foreach filename in `filelist' {
    // Check if the file exists before attempting to load
    capture confirm file "`filename'"
    if _rc {
        di as error "File not found: `filename'. Skipping."
        continue
    }
    
    // Load the current file
    qui{
      use date using "`filename'", clear
      gen tmp=1
      
      
      collapse (sum) tmp, by(date)
      
      // Add a variable to store the original filename 
      local tmp2 = subinstr("`filename'", "${path}", "", .)
  	local filename_short=substr("`tmp2'",28,3)
      rename tmp `filename_short'
      
  	
  	if `first_file' {
          // For the very first file, SAVE the result to the tempfile.
          // This ensures the tempfile is created with variables and data.
          save `counts_dataq', replace
          local first_file = 0 // Turn off the flag
      }
      else {
          // For all subsequent files, APPEND the result to the tempfile.
          append using `counts_dataq'
          save `counts_dataq', replace // Save the updated combined file
      }
    }
}

qui{
  collapse (sum) Q*, by(date)
  order date QA1 QA2 QA3 QB1 QB2 
  sort date
  save `counts_dataq', replace
  export delimited using "./aux_files/stata/counts_dataq.csv", replace
}
  

list

```

```{r}
#| label: tbl-obsq
#| tbl-cap: "Number of instituitions in each table -- Quarterly Data"
#| echo: false
#| eval: true

library(knitr)
kable(read.csv("./aux_files/stata/counts_dataq.csv"))
```

# FAQ

**Can I link the SLB data to a credit (CRC-like) dataset provided by BPLIM?**

Yes. However, be aware that the reporting unit level is specific to each dataset, requiring you to ensure you are linking comparable entities. For example, SLB reports consolidated information for banking groups, whereas HCRC reports individual-level information. To guarantee an accurate linkage between the two datasets, you can use the BPLIM's tool [**linkbank**](https://github.com/BPLIM/Tools/tree/master/ados/CRC_FRMBNK/linkbank).


**How are banking groups defined in SLB?**

The consolidated data in SLB is structured according to the prudential scope defined for each banking group. Importantly, the group’s identifier is not derived from its legal name or corporate structure. Instead, it corresponds to the Central Bank’s regulatory reporting ID of the group’s main institution. This approach ensures consistency over time: if a banking group changes its legal name or structure but retains the same main institution with an active reporting ID at Banco de Portugal, the group ID in SLB remains unchanged. As a result, the group’s activity can be tracked consistently across years.


**How to treat missing data and zero values?**

The treatment of missing data and zero values depends on the identification criteria chosen by the researcher. It is important to note that, in SLB, zero values represent actual zeros. There are also two distinct types of incomplete or missing data. For further details, see the subsection ["Missing observation vs missing data vs zeros values"](#sec-methodology-others).


**Are all credit institutions reported in credit datasets provided by BPLIM covered in the SLB?**

No, SLB only covers the institutions defined in the section ["Population"](#sec-population). Moreover, SLB reports information at the banking group level, while credit datasets (all CRC-like datasets) report at the individual level. You should also consider, that reporting frequencies differ: while credit datasets are usually reported monthly, SLB data are provided on a quarterly or yearly basis.


**Can I combine information from multiple SLB tables?**

Yes. However, note that population coverage varies across tables, as each follows different scope criteria. When combining multiple tables, the resulting dataset will include only the overlapping population, leading to a reduced sample size. For further details, see the section ["Population"](#sec-population).

**I’m currently using an older extraction and want to update it with the most recent data. Should I merge the two datasets?**

The BPLIM data extractions are designed to be cumulative and complete. Each new release incorporates the longest available data period while also integrating any necessary quality adjustments/improvements. Therefore, to ensure you are always working with the most accurate and consistent historical record, you should use the most recent extraction of the dataset, as it completely supersedes and replaces all previous versions. You should not combine different extractions.



# References

- Banco de Portugal (2019), **Historical Series - Portuguese Banking Sector 1990-2018**, Banco de Portugal, November 2019. [PT_version](https://www.bportugal.pt/sites/default/files/anexos/pdf-boletim/series_longas_setor_bancario_portugues.pdf) [ENG_version](https://www.bportugal.pt/sites/default/files/anexos/pdf-boletim/historical_series_portuguese_banking_system.pdf)



# Auxiliary Files {#sec-auxiliary-files}

- For the metadata and summary statistics, please check the following auxiliary files: ^[The summary statistics, on perturbed data, are available in BPLIM's servers.]

| File | Description of Variables | Summary Statistics |
|:----|:----:|:----:|
| QA1-Balance Sheet File (yearly)| [meta_Y_QA1](./aux_files/metadata/META_SLB_A_YBNK_19902024_SEP25_QA1_V01.xlsx) | [stat_Y_QA1](./aux_files/descriptive_statistics/METATSS_SLB_A_YBNK_19902024_SEP25_QA1_V01.xlsx) |
| QA1-Balance Sheet File (quarterly)| [meta_Q_QA1](./aux_files/metadata/META_SLB_A_QBNK_20012024_SEP25_QA1_V01.xlsx) | [stat_Q_QA1](./aux_files/descriptive_statistics/METATSS_SLB_A_QBNK_20012024_SEP25_QA1_V01.xlsx)|
| QA2-Income Statement File (yearly) | [meta_Y_QA2](./aux_files/metadata/META_SLB_A_YBNK_19902024_SEP25_QA2_V01.xlsx) | [stat_Y_QA2](./aux_files/descriptive_statistics/METATSS_SLB_A_YBNK_19902024_SEP25_QA2_V01.xlsx) |
| QA2-Income Statement File (quarterly) | [meta_Q_QA2](./aux_files/metadata/META_SLB_A_QBNK_20012024_SEP25_QA2_V01.xlsx) | [stat_Q_QA2](./aux_files/descriptive_statistics/METATSS_SLB_A_QBNK_20012024_SEP25_QA2_V01.xlsx) |
| QA3-Solvency File (yearly) |[meta_Y_QA3](./aux_files/metadata/META_SLB_A_YBNK_19942024_SEP25_QA3_V01.xlsx)  | [stat_Y_QA3](./aux_files/descriptive_statistics/METATSS_SLB_A_YBNK_19942024_SEP25_QA3_V01.xlsx) |
| QA3-Solvency File (quarterly) |[meta_Q_QA3](./aux_files/metadata/META_SLB_A_QBNK_20092024_SEP25_QA3_V01.xlsx)  | [stat_Q_QA3](./aux_files/descriptive_statistics/METATSS_SLB_A_QBNK_20092024_SEP25_QA3_V01.xlsx) |
| QB1-Loans to customers File (yearly) | [meta_Y_QB1](./aux_files/metadata/META_SLB_A_YBNK_19902024_SEP25_QB1_V01.xlsx) | [stat_Y_QB1](./aux_files/descriptive_statistics/METATSS_SLB_A_YBNK_19902024_SEP25_QB1_V01.xlsx) |
| QB1-Loans to customers File (quarterly) | [meta_Q_QB1](./aux_files/metadata/META_SLB_A_QBNK_20012024_SEP25_QB1_V01.xlsx) | [stat_Q_QB1](./aux_files/descriptive_statistics/METATSS_SLB_A_QBNK_20012024_SEP25_QB1_V01.xlsx) |
| QB2-Interest Rates File (yearly) |[meta_Y_QB2](./aux_files/metadata/META_SLB_A_YBNK_20032024_SEP25_QB2_V01.xlsx) |[stat_Y_QB2](./aux_files/descriptive_statistics/METATSS_SLB_A_YBNK_20032024_SEP25_QB2_V01.xlsx) |
| QB2-Interest Rates File (quarterly) |[meta_Q_QB2](./aux_files/metadata/META_SLB_A_QBNK_20032024_SEP25_QB2_V01.xlsx) | [stat_Q_QB2](./aux_files/descriptive_statistics/METATSS_SLB_A_QBNK_20032024_SEP25_QB2_V01.xlsx) |
| QC-Human Resources File |[meta_QC](./aux_files/metadata/META_SLB_A_YBNK_19902024_SEP25_QC_V01.xlsx) | [stat_Y_QC](./aux_files/descriptive_statistics/METATSS_SLB_A_YBNK_19902024_SEP25_QC_V01.xlsx)|
| QD-Branch Network File |[meta_QD](./aux_files/metadata/META_SLB_A_YBNK_19902024_SEP25_QD_V01.xlsx) | [stat_Y_QD](./aux_files/descriptive_statistics/METATSS_SLB_A_YBNK_19902024_SEP25_QD_V01.xlsx)|
| QE-Payment Systems | [meta_QE](./aux_files/metadata/META_SLB_A_YBNK_20002024_SEP25_QE_V01.xlsx)| [stat_Y_QE](./aux_files/descriptive_statistics/METATSS_SLB_A_YBNK_20002024_SEP25_QE_V01.xlsx)|


- Auxiliary file for the [Figure [-@fig-timetable]](./aux_files/Figure_Data period, frequency and main series breaks by table.xlsx): Data period, frequency and main series breaks by table

- Additional auxiliary files available upon request:

  - Report on the coverage by institution-time-table 
  - Auxiliary file required for the BPLIM's tool *linkbank* 


# Useful Links

- Banco de Portugal (2000). [**Historical series about portuguese economy after World War II**.](https://www.bportugal.pt/en/publicacao/historical-series-about-portuguese-economy-after-world-war-ii)
- Banco de Portugal (2017). [**Financial Stability Report: June 2017**.](https://www.bportugal.pt/sites/default/files/anexos/pdf-boletim/ref_06_2017_en.pdf)
- Banco de Portugal (2019). [**Banco de Portugal's Communication**.](https://www.bportugal.pt/comunicado/banco-de-portugal-disponibiliza-informacao-historica-sobre-o-setor-bancario-portugues)


# Useful Ado Files

We provide an ado file, developed by BPLIM staff, designed to assist researchers in integrating datasets containing financial corporation data defined at different levels of analysis. 


## linkbank

This tool is essential for accurately linking individual entity registers from datasets derived from Central Credit Register data (such as CRC and HCRC) to datasets that use a different unit of analysis, like SLB (which represents banking groups or stand-alone institutions). 

For the latest information and updates on the tool, please visit our GitHub page: [**linkbank**](https://github.com/BPLIM/Tools/tree/master/ados/CRC_FRMBNK/linkbank)


# Citation of this Dataset

Banco de Portugal Microdata Research Laboratory (BPLIM) (2025): Historical Series of the Portuguese Banking Sector. Extraction: September 2025. Version: V1. Banco de Portugal - BPLIM. Dataset. https://doi.org/10.17900/SLB.Sep2025.V1

<br>
To cite this data set you can use the package biblatex with the following BibTeX entry: 

```{stata}
*| eval: false
*| echo: true
*| code-fold: false
*| ExecuteTime: {end_time: '2023-06-20T08:57:58.771961Z', start_time: '2023-06-20T08:57:57.953258Z'}
@dataset{SLB.Sep2025.V1,
author = {{Banco de Portugal Microdata Research Laboratory - BPLIM}},
publisher = {Banco de Portugal},
title = {{H}istorical {S}eries of the {P}ortuguese {B}anking {S}ector},
year = {2025},
version = {{ V1, Extraction September 2025}},
doi = {10.17900/SLB.Sep2025.V1},
url = {https://doi.org/10.17900/SLB.Sep2025.V1}
}
```


