---
title: Historical Series of the Portuguese Banking Sector - Data Manual
subtitle: Extraction Date - October 2023
author: BPLIM
date: December 2023
abstract: 'The Historical Series of the Portuguese Banking Sector Database (SLB) reports, on a consolidated basis, a wide range of series on bank''s financial statements (i.e., balance sheet, income statement, and solvency), loans to customers, interest rates, human resources, branch network, and payment systems. The dataset is updated annually.'
doi: 10.17900/SLB.Oct2023.V1
pdf-engine: pdflatex
execute:
  echo: false
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

# General Information

> **Dataset Designation in English**: Historical Series of Portuguese Banking Sector (SLB)

> **Dataset Designation in Portuguese**: Séries Longas do Sector Bancário Português (SLB)

> **Data Type**: longitudinal data

> **Unit of Analysis**: banking group/stand-alone institution

> **Frequency**: yearly and quarterly.[^1]

> **Start Date**: 1990

> **Most recent year**: 2022

> **Reference date**: month-end

> **Data Organization**: data is organized by frequency, i.e., yearly and quarterly, and information type, i.e., balance sheet statement (QA1),  income statement (QA2), solvency (QA3), loans to customers (QB1), interest rates (QB2), human resources (QC), branch network (QD), and payment systems (QE). All data files are available in Stata format.

> **Version of the Data**: the data made available by BPLIM corresponds to a data freeze at a certain time of the year. Therefore, all files contain information as reported at the extraction date. The most recent update of the data occurred in October 2023.

> **Languages Available**: variables labels are available in Portuguese and in English.[^2]

> **Data Access**: data made available to external researchers under certain conditions and has to be aggregated at the firm level with the external researchers proposing the aggregation method.[^3]

[^1]: The yearly date reflects year-end information, except for interest rates which are computed as the average of the quarterly interest rates and income statement variables which are summed up over the period.

[^2]: To see the labels in English type the following command line in Stata: 'label language en'.

[^3]: Conditions for data access for external researchers are detailed in the *[Guide for Researchers Using Banco de Portugal Microdata Research Laboratory (BPLIM) Data](https://msites-dee-bplim-prd.azurewebsites.net/sites/default/files/guide_for_researchers_v2021_v2.pdf)*.

> **Digital Object Identifier**: 10.17900/SLB.Oct2023.V1



# Population

The information provided refers to banking groups and stand-alone institutions resident in Portugal for the period between 1990 and 2022. For tables *Balance Sheet Statement (QA1)*, *Income Statement (QA2)*, and *Solvency (QA3)*, the data was compiled on a consolidated basis, whereas the remaining tables aggregate the information of the resident Other Monetary Financial Institutions (except Central Bank) belonging to a banking group.

The coverage of financial institutions varies depending on the data table. \

The *Balance Sheet Statement (QA1)*,  *Income Statement (QA2)*, and *Solvency (QA3)* tables include the institutions that are subject to Banco de Portugal's supervision, namely the Other Monetary Financial Institutions (OMFIs) since 1990 and institutions that have been part of the banking system since 2008. These institutions are contemplated in the Legal Framework of Credit Institutions and Financial Companies ("Regime Geral das Instituições de Crédito e Sociedade Financeiras - RGICSF"). The number of institutions that are part of the banking system has varied over the past decades.

The tables of *Loans to Customers (QB1)* and *Interest Rates (QB2)* include resident institutions (except for the central bank) that are covered by the Monetary and Financial Institution Statistics ("Estatísticas Monetárias e Financeiras - EMF"). The aggregated data is obtained by aggregating individual institution's information on their activities carried out in the national territory.

The table of *Human Resources (QC)* contains a total of 69 entities, considered to be banking groups on a consolidated basis.

The table of *Branch Network (QD)* covers a similar group of institutions as the *Human Resources (QC)* table, corresponding to an average of 28 institutions per year, with a
maximum of 35 (in 1999) and a minimum of around 20 institutions from 2012 onwards.

The institutions covered by *Human Resources (QC)* and *Branch Network (QD)* are members of the Portuguese Banking Association ("Associação Portuguesa de Bancos- APB"). The aggregated data is obtained by aggregating information of the individual institutions that make up the banking group.

The table of *Payment Systems (QE)* is constructed based on information on payment systems and instruments reported to the Banco de Portugal’s Payment Systems Department, under the Interbank Clearing System (SICOI).

# Methodology

The Historical Series of the Portuguese Banking Sector data is collected and assembled by a working group at Banco de Portugal which was established at the end of 2017 with the objective of constructing historical series on the Portuguese banking sector. The SLB database covers the period from 1990 to 2022 and the data is available at yearly frequency. For some tables (i.e., i.e., balance sheet, income statement, solvency, loans to customers, and interest rates), the data is also available at quarterly frequency. However, it should be noted that the data period and the availability of the data frequency differ according to the data table, the variable and the institution under consideration, which leads to some breaks in the series.[^4]
For example, interest rates between 2003 and 2010 are collected based on a sample, which explains the missing observations during this period of time.

**Table 1**  - Tables and Data Period

|  **Table** | **Type of information** | **Frequency**[^5]  | **Data Period** |
| :---------- | :-------------------- |:-------------- |:------------ |
|QA1|		Balance Sheet |	Yearly | 1990-2022 |
|QA1|		Balance Sheet |	Quarterly | 2001Q1-2022Q4 |
|QA2|		Income Statement |	Yearly | 1990-2022 |
|QA2|		Income Statement |	Quarterly | 2001Q1-2022Q4 |
|QA3|		Solvency |	Yearly | 1994-2022 |
|QA3|		Solvency |	Quarterly | 2009Q1-2022Q4 |
|QB1|		Loans to Customers |	Yearly | 1990-2022 |
|QB1|		Loans to Customers |	Quarterly | 2001Q1-2022Q4 |
|QB2|		Interest Rates |	Yearly | 1997-2022 |
|QB2|		Interest Rates |	Quarterly | 1997Q4-2022Q4 |
|QC|		Human Resources |	Yearly | 1990-2022 |
|QD|		Branch Network |	Yearly | 1990-2022 |
|QE|		Payment Systems |	Yearly | 2000-2022 |


Despite the  efforts of maintaining the greatest possible coherence over time, we shall still note some series breaks in the data caused by changes to supervisory information reports, to accounting practices and/or to the perimeter of banking
groups, i.e. mergers/acquisitions between banking institutions.[^6]

Some important changes in accounting procedures that have caused series breaks are the following:

- the introduction of the International Accounting Standards (IAS) in March 2005 requires financial institutions to value a substantial share of on-balance-sheet assets in securities at market prices, in contrast to the former valuation at the purchase
price;;
- the standardization of prudential reporting at European level (COREP) from 2014 onward has led to significant alterations in the definitions underlying the main solvency ratios;
- the introduction of IFRS 9 in January 2018, in addition to other changes, results in a major change in the impairment calculation method from an incurred loss model towards an expected loss model.

In order to be able to build retrospective series, the data is constructed based on the more recent financial reporting standards (FINREP). This decision was also made to facilitate future updates of the data and to ensure compatibility with the most recent analysis of the banking sector.

Solvency indicators were chosen with the objective of maintaining the highest consistency across the entire period. In particular, the implementation of the new prudential reporting system at the beginning of 2014 through Commission Implementing Regulation (EU) No 680/2014, known as COREP, resulted in a set of methodological changes in the calculation of own funds.
The continuity of the series was guaranteed, by matching the concept of base own funds according to the previous reporting system to Tier 1 capital in COREP, thus keeping the latest terminology, and total capital in line with both reporting systems. Given the recent introduction in the regulatory framework, an option was made not to include in the database the concept of Common Equity Tier 1 capital (CET1), which could not be retropolated for earlier periods (prior to 2014).

The detailed solutions adopted to ensure a single format over the entire period are documented in [**Historical Series - Portuguese Banking Sector 1990-2018**](https://www.bportugal.pt/sites/default/files/anexos/pdf-boletim/historical_series_portuguese_banking_system.pdf)


[^4]: Please refer to the section [Description of Variables](#description-of-variables) for more details.
[^5]: The yearly date reflects year-end information, except for interest rates which are computed as the average of the quarterly interest rates.
[^6]: Please refer to the ["Historical Series - Portuguese Banking Sector 1990-2018" report](https://www.bportugal.pt/sites/default/files/anexos/pdf-boletim/historical_series_portuguese_banking_system.pdf) for more details.

## A. What can change with a new extraction?

The distinction between zeros and nulls was introduced for combinations (of active banks and reported series) without values in the Financial Monetary Statistics:

- For QB1 (Loans to Customers), as they involve amounts, there are no entries as null – amounts for which there are no loans are filled with zero.

- In QB2 for the interest rates, this distinction is made based on the associated amount – rates for which there is no associated amount are filled with null, while when there is an associated amount the rate value is filled with zero.

Comparing with the data from the last year, we have some observations that have been removed to align the universe of active entities in each year with the Financial Stability Department universe.


# Description of Variables

Below we provide a general description of the variables included in each data file referred above. For a full account of all variable categories and changes over time see [“Auxiliary Files” section](#auxiliary-files).

## A.	Balance Sheet File

### A1. Identifiers

`Bank identifier` (*bina*) - Anonymized identification number for financial institution that enables tracking the institution over time. BPLIM provides an anonymized version of the financial institution identifier which is denoted by *bina*.

`Reference quarter of the data` (*Date*)  - Reference quarter of the data

`Reference Year of the data` (*Year*) - Reference year of the data

### A2. Balance Sheet Variables

**Table 3**  - Balance Sheet Variables

| Variable Name | Variable Description | Unit | Available Period - Yearly Data |  Available Period - Quarterly Data |
| :------ | :------- | :--- | :------: | :------: |
|	QA1_1	|	Cash and cash balances/loans to central banks	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_2	|	Demand deposits in other credit institutions	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_3	|	Loan to other credit institutions - Carrying amount	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_3_1	| > Loan to other credit institutions - Gross carrying amount	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_3_2	|	> Loan to other credit institutions - Impairments and value adjustments	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_4	|	Loan to customers - Carrying amount	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_4_1	|	> Loan to customers - Gross carrying amount	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_4_2	|	> Loan to customers - Impairments and value adjustments	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_5	|	Debt securities - Carrying amount	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_5_1	|	> Debt securities - Gross carrying amount	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_5_1_1	|	> > Debt securities - Gross carrying amount - General government	|	€Millions 	|	1998	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_5_1_2	|	> > Debt securities - Gross carrying amount - Other issuers	|	€Millions 	|	1998	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_5_2	|	> Debt securities - Impairments and value adjustments	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_6	|	Equity instruments	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_7	|	Investments in subsidiaries, joint ventures and associates	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_8	|	Tangible assets	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_9	|	Intangible assets	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_10	|	Other assets	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_10_1	|	> Other assets - Tax assets	|	€Millions 	|	2005	-	2022	|	2005Q1	-	2022Q4	|
|	QA1_10_1_1	|	> > Other assets - Tax assets - Deferred taxes	|	€Millions 	|	2005	-	2022	|	2005Q1	-	2022Q4	|
|	QA1_10_1_2	|	> > Other assets - Tax assets - Current taxes	|	€Millions 	|	2005	-	2022	|	2005Q1	-	2022Q4	|
|	QA1_10_2	|	> Other assets - Others	|	€Millions 	|	2005	-	2022	|	2005Q1	-	2022Q4	|
|	QA1_11	|	Total assets	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_12	|	Deposits from central banks and other credit institutions	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_12_1	|	> Deposits from central banks and other credit institutions - central banks	|	€Millions 	|	2005	-	2022	|	2005Q1	-	2022Q4	|
|	QA1_12_2	|	> Deposits from central banks and other credit institutions - other credit institutions	|	€Millions 	|	2005	-	2022	|	2005Q1	-	2022Q4	|
|	QA1_13	|	Customer deposits	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_13_1	|	> Customer deposits - Short-term deposits	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_13_2	|	> Customer deposits - Deposits with agreed maturity	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_14	|	Liabilities represented by debt securities	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_15	|	Other liabilities (includes derivatives and short-term liabilities)	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_16	|	Total Liabilities	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_17	|	Equity	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_17_1	|	> Equity - Capital	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_17_2	|	> Equity - Share premium	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_17_3	|	> Equity - Reserves	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_17_3_1	|	> > Equity - Reserves - Retained earnings	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_17_3_2	|	> > Equity - Reserves - Other reserves	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_17_4	|	> Equity - Minority interests	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_17_5	|	> Equity - Consolidated income for the year	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA1_17_6	|	> Equity - Own shares (-)	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|

## B.	Income Statement File

### B1. Identifiers

`Bank identifier` (*bina*) - Anonymized identification number for financial institution that enables tracking the institution over time. BPLIM provides an anonymized version of the financial institution identifier which is denoted by *bina*.

`Reference quarter of the data` (*Date*)  - Reference quarter of the data

`Reference Year of the data` (*Year*) - Reference year of the data

### B2. Income Statement Variables

**Table 4** - Income Statement Variables

| Variable Name | Variable Description | Unit | Available Period - Yearly Data |  Available Period - Quarterly Data |
| :------ | :------- | :--- | :------: | :------: |
|	QA2_1	|	Interest income	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA2_2	|	Interest expenses	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA2_3	|	Net interest income	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA2_4	|	Capital gains (net)	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA2_5	|	Income from services and commissions (net)	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA2_5_1	|	> Income from services and commissions received	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA2_5_2	|	> Income from services and commissions paid	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA2_6	|	Income from financial operations	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA2_7	|	Other operating results	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA2_8	|	Total operating income	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA2_9	|	Staff expenses	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA2_10	|	Other administrative expenses	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA2_11	|	Depreciation	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA2_12	|	Provisions and impairments (net of reversals)	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA2_12_1	|	> Provisions or reversal of provisions (net)	|	€Millions 	|	2005	-	2022	|	2005Q1	-	2022Q4	|
|	QA2_12_2	|	> Impairment losses and other net value adjustments	|	€Millions 	|	2005	-	2022	|	2005Q1	-	2022Q4	|
|	QA2_12_2_1	|	> > Credit impairment losses	|	€Millions 	|	2005	-	2022	|	2005Q1	-	2022Q4	|
|	QA2_12_2_2	|	> > Other impairment losses and value adjustments	|	€Millions 	|	2005	-	2022	|	2005Q1	-	2022Q4	|
|	QA2_13	|	Other profit or (-) loss	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA2_14	|	Profit or (-) loss before tax	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA2_15	|	Tax expenses or income related to profit or loss	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA2_16	|	Net profit or (-) loss	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA2_17	|	Profit/loss for year attributable to minority interest	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QA2_18	|	Profit/loss for year attributable to owners of parent	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|

## C.	Solvency File

### C1. Identifiers

`Bank identifier` (*bina*) - Anonymized identification number for financial institution that enables tracking the institution over time. BPLIM provides an anonymized version of the financial institution identifier which is denoted by *bina*.

`Reference quarter of the data` (*Date*)  - Reference quarter of the data

`Reference Year of the data` (*Year*) - Reference year of the data

### C2. Instrument Characteristics

**Table 5** - Solvency

| Variable Name | Variable Description | Unit | Available Period - Yearly Data |  Available Period - Quarterly Data |
| :------ | :------- | :--- | :------: | :------: |
|	QA3_1	|	Tier 1 capital	|	€Millions 	|	1996	-	2022	|	2009Q1	-	2022Q4	|
|	QA3_2	|	Total own funds	|	€Millions 	|	1994	-	2022	|	2009Q1	-	2022Q4	|
|	QA3_3	|	Risk-weighted assets	|	€Millions 	|	1994	-	2022	|	2009Q1	-	2022Q4	|
|	QA3_4	|	Tier 1 capital ratio	|	Percentage	|	1996	-	2022	|	2009Q1	-	2022Q4	|
|	QA3_5	|	Total capital ratio	|	Percentage	|	1994	-	2022	|	2009Q1	-	2022Q4	|

## D.	Loans to Customers File

### D1. Identifiers

`Bank identifier` (*bina*) - Anonymized identification number for financial institution that enables tracking the institution over time. BPLIM provides an anonymized version of the financial institution identifier which is denoted by *bina*.

`Reference quarter of the data` (*Date*)  - Reference quarter of the data

`Reference Year of the data` (*Year*) - Reference year of the data

### D2. Loans to Customers Variables

**Table 6** - Loans to Customers Variables

| Variable Name | Variable Description | Unit | Available Period - Yearly Data |  Available Period - Quarterly Data |
| :------ | :------- | :--- | :------: | :------: |
|	QB1_1	|	Gross loans to customers	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QB1_1_1	|	> Gross Loans except to other financial companies	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QB1_1_1_1	|	> > Domestic credit except to other financial companies	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QB1_1_1_1_1	|	> > > Domestic credit to non-financial corporations	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QB1_1_1_1_1_1	|	> > > > Domestic credit to NFCs - Agriculture and fishing	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QB1_1_1_1_1_2	|	> > > > Domestic credit to NFCs – Mining and quarrying and Manufacturing	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QB1_1_1_1_1_3	|	> > > > Domestic credit to NFCs – Construction and public works	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QB1_1_1_1_1_4	|	> > > > Domestic credit to NFCs – Electricity, gas and water	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QB1_1_1_1_1_5	|	> > > > Domestic credit to NFCs – Services	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QB1_1_1_1_1_6	|	> > > > Domestic credit to NFCs – Other	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QB1_1_1_1_2	|	> > > Domestic credit to general government	|	€Millions 	|	1996	-	2022	|	2001Q1	-	2022Q4	|
|	QB1_1_1_1_3	|	> > > Domestic credit to households 	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QB1_1_1_1_3_1	|	> > > > Domestic housing credit	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QB1_1_1_1_3_2	|	> > > > Domestic credit for consumption and other purposes	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QB1_1_1_2	|	> > Other credit	|	€Millions 	|	1990	-	2022	|	2001Q1	-	2022Q4	|
|	QB1_1_2	|	> Domestic credit to other financial companies	|	€Millions 	|	1992	-	2022	|	2001Q1	-	2022Q4	|
|	QB1_2	|	Domestic overdue credit	|	€Millions 	|	1997	-	2022	|	2001Q1	-	2022Q4	|
|	QB1_2_1	|	> Domestic overdue credit to non-financial companies	|	€Millions 	|	1997	-	2022	|	2001Q1	-	2022Q4	|
|	QB1_2_1_1	|	> > Domestic overdue credit to NFCs – Agriculture and fishing	|	€Millions 	|	1997	-	2022	|	2001Q1	-	2022Q4	|
|	QB1_2_1_2	|	> > Domestic overdue credit to NFCs – Mining and quarrying and Manufacturing	|	€Millions 	|	1997	-	2022	|	2001Q1	-	2022Q4	|
|	QB1_2_1_3	|	> > Domestic overdue credit to NFCs – Construction and public works	|	€Millions 	|	1997	-	2022	|	2001Q1	-	2022Q4	|
|	QB1_2_1_4	|	> > Domestic overdue credit to NFCs – Electricity, gas and water	|	€Millions 	|	1997	-	2022	|	2001Q1	-	2022Q4	|
|	QB1_2_1_5	|	> > Domestic overdue credit to NFCs – Services	|	€Millions 	|	1997	-	2022	|	2001Q1	-	2022Q4	|
|	QB1_2_1_6	|	> > Domestic overdue credit to NFCs – Other	|	€Millions 	|	1997	-	2022	|	2001Q1	-	2022Q4	|
|	QB1_2_2	|	> Domestic overdue credit to general government	|	€Millions 	|	1997	-	2022	|	2001Q1	-	2022Q4	|
|	QB1_2_3	|	> Domestic overdue credit to households 	|	€Millions 	|	1997	-	2022	|	2001Q1	-	2022Q4	|
|	QB1_2_3_1	|	> > Domestic overdue housing credit	|	€Millions 	|	1997	-	2022	|	2001Q1	-	2022Q4	|
|	QB1_2_3_2	|	> > Domestic overdue credit for consumption and other purposes	|	€Millions 	|	1997	-	2022	|	2001Q1	-	2022Q4	|

## E.	Interest Rates File

### E1. Identifiers
`Bank identifier` (*bina*) - Anonymized identification number for financial institution that enables tracking the institution over time. BPLIM provides an anonymized version of the financial institution identifier which is denoted by *bina*.

`Reference quarter of the data` (*Date*)  - Reference quarter of the data

`Reference Year of the data` (*Year*) - Reference year of the data

### E2. Interest Rates Variables

**Table 7** - Interest Rates Variables

| Variable Name | Variable Description | Unit | Available Period - Yearly Data |  Available Period - Quarterly Data |
| :------ | :------- | :--- | :------: | :------: |
|	QB2_1_1	|	Interest rates on outstanding amounts - Loans/Credits	|	Percentage	|	2003	-	2022	|	2003Q1	-	2022Q4	|
|	QB2_1_1_1	|	> Interest rates on outstanding amounts - Credits to non-financial corporations	|	Percentage	|	2003	-	2022	|	2003Q1	-	2022Q4	|
|	QB2_1_1_2	|	> Interest rates on outstanding amounts - Loans to households 	|	Percentage	|	2003	-	2022	|	2003Q1	-	2022Q4	|
|	QB2_1_1_2_1	|	> > Interest rates on outstanding amounts - Housing loans	|	Percentage	|	2003	-	2022	|	2003Q1	-	2022Q4	|
|	QB2_1_1_2_2	|	> > Interest rates on outstanding amounts - Credit for consumption and other purposes	|	Percentage	|	2003	-	2022	|	2003Q1	-	2022Q4	|
|	QB2_1_2	|	Interest rates on outstanding amounts - Deposits	|	Percentage	|	2003	-	2022	|	2003Q1	-	2022Q4	|
|	QB2_1_2_1	|	> Interest rates on outstanding amounts - Demand deposits	|	Percentage	|	2003	-	2022	|	2003Q1	-	2022Q4	|
|	QB2_1_2_1_1	|	> > Interest rates on outstanding amounts - Demand deposits to non-financial corporations	|	Percentage	|	2003	-	2022	|	2003Q1	-	2022Q4	|
|	QB2_1_2_1_2	|	> > Interest rates on outstanding amounts - Demand deposits to households 	|	Percentage	|	2003	-	2022	|	2003Q1	-	2022Q4	|
|	QB2_1_2_2	|	> Interest rates on outstanding amounts - Other deposits	|	Percentage	|	2003	-	2022	|	2003Q1	-	2022Q4	|
|	QB2_1_2_2_1	|	> > Interest rates on outstanding amounts - Other deposits to non-financial corporations	|	Percentage	|	2003	-	2022	|	2003Q1	-	2022Q4	|
|	QB2_1_2_2_2	|	> > Interest rates on outstanding amounts - Other deposits to households 	|	Percentage	|	2003	-	2022	|	2003Q1	-	2022Q4	|
|	QB2_2_1	|	Interest rates on new loans	|	Percentage	|	1997	-	2022	|	1997Q4	-	2022Q4	|
|	QB2_2_1_1	|	> Interest rates on new loans to non-financial corporations	|	Percentage	|	1997	-	2022	|	1997Q4	-	2022Q4	|
|	QB2_2_1_2	|	> Interest rates on new loans to households 	|	Percentage	|	1997	-	2022	|	1997Q4	-	2022Q4	|
|	QB2_2_1_2_1	|	> > Interest rates on new loans to households: Housing loans	|	Percentage	|	1997	-	2022	|	1997Q4	-	2022Q4	|
|	QB2_2_1_2_2	|	> > Interest rates on new loans: Credit for consumption and other purposes	|	Percentage	|	1997	-	2022	|	1997Q4	-	2022Q4	|
|	QB2_2_2	|	Interest rates on deposits: New deposits	|	Percentage	|	1997	-	2022	|	1997Q4	-	2022Q4	|
|	QB2_2_2_1	|	> Interest rates on deposits: New deposits to non-financial corporations	|	Percentage	|	1997	-	2022	|	1997Q4	-	2022Q4	|
|	QB2_2_2_2	|	> Interest rates on deposits: New deposits to households 	|	Percentage	|	1997	-	2022	|	1997Q4	-	2022Q4	|

## F.	Human Resources File

### F1. Identifiers

`Bank identifier` (*bina*) - Anonymized identification number for financial institution that enables tracking the institution over time. BPLIM provides an anonymized version of the financial institution identifier which is denoted by *bina*.

`Reference Year of the data` (*Year*) - Reference year of the data


### F2. Human Resources Variables

**Table 8** - Human Resources Variables

| Variable Name | Variable Description | Unit | Available Period - Yearly Data |
| :------ | :------- | :--- | :------: |
|	QC_1	|	Total	|	Number	|	1992	-	2022	|
|	QC_2	|	International activity	|	Number	|	1992	-	2022	|
|	QC_2_1	|	> Branches and foreign subsidiaries	|	Number	|	1990	-	2022	|
|	QC_2_2	|	> Consolidated foreign bank branches	|	Number	|	1990	-	2022	|
|	QC_3	|	Domestic activity - Banking institutions	|	Number	|	1990	-	2022	|
|	QC_3_1_1	|	> By gender: Male	|	Number	|	2005	-	2022	|
|	QC_3_1_2	|	> By gender: Female	|	Number	|	2005	-	2022	|
|	QC_3_2_1	|	> By age: <30 years old	|	Number	|	1990	-	2022	|
|	QC_3_2_2	|	> By age: 30-44 years old	|	Number	|	1990	-	2022	|
|	QC_3_2_3	|	> By age:> 44 years old	|	Number	|	1990	-	2022	|
|	QC_3_3_1	|	> By seniority: <1 year	|	Number	|	1993	-	2022	|
|	QC_3_3_2	|	> By seniority: 1-5 years	|	Number	|	1990	-	2022	|
|	QC_3_3_3	|	> By seniority: 6-10 years	|	Number	|	1990	-	2022	|
|	QC_3_3_4	|	> By seniority: 11-15 years	|	Number	|	1990	-	2022	|
|	QC_3_3_5	|	> By seniority:> 15 years	|	Number	|	1990	-	2022	|
|	QC_3_4_1	|	> By contract type: Permanent	|	Number	|	2005	-	2022	|
|	QC_3_4_2	|	> By contract type: Fixed-term contract	|	Number	|	2005	-	2022	|
|	QC_3_5_1	|	> By education: Basic	|	Number	|	1993	-	2022	|
|	QC_3_5_2	|	> By education: Secondary	|	Number	|	1993	-	2022	|
|	QC_3_5_3	|	> By education: Higher	|	Number	|	1993	-	2022	|
|	QC_3_6_1	|	> By function: Management	|	Number	|	1995	-	2022	|
|	QC_3_6_2	|	> By functions: Specific	|	Number	|	1995	-	2022	|
|	QC_3_6_3	|	> By function: Administrative	|	Number	|	1995	-	2022	|
|	QC_3_6_4	|	> By function: Support	|	Number	|	1995	-	2022	|
|	QC_3_7_1	|	> By activity: Commercial	|	Number	|	1990	-	2022	|
|	QC_3_7_2	|	> By activity: Other	|	Number	|	1990	-	2022	|

## G.	Branch Network File

### G1. Identifiers

`Bank identifier` (*bina*) - Anonymized identification number for financial institution that enables tracking the institution over time. BPLIM provides an anonymized version of the financial institution identifier which is denoted by *bina*.

`Reference Year of the data` (*Year*) - Reference year of the data


### G2. Bank Branch Network Variables

**Table 9** - Bank Branch Network Variables

| Variable Name | Variable Description | Unit | Available Period - Yearly Data |
| :------ | :------- | :--- | :------: |
|	QD_1	|	Total	|	Number	|	1992	-	2022	|
|	QD_2	|	Total international activity 	|	Number	|	1992	-	2022	|
|	QD_2_1	|	> Branches and foreign subsidiaries	|	Number	|	1992	-	2022	|
|	QD_2_2	|	> Consolidated foreign bank branches	|	Number	|	1992	-	2022	|
|	QD_3	|	Total domestic activity	|	Number	|	1990	-	2022	|

## H.	Payment Systems File

### H1. Identifiers

`Bank identifier` (*bina*) - Anonymized identification number for financial institution that enables tracking the institution over time. BPLIM provides an anonymized version of the financial institution identifier which is denoted by *bina*.

`Reference Year of the data` (*Year*) - Reference year of the data


### H2. Payment Systems Variables

**Table 10** - Payment Systems Variables

| Variable Name | Variable Description | Unit | Available Period - Yearly Data |
| :------ | :------- | :--- | :------: |
|	QE_1	|	Number of ATMs	|	Quantity	|	2000	-	2022	|
|	QE_2	|	Number of POS terminals	|	Quantity	|	2000	-	2022	|
|	QE_3	|	Number of payment transactions	|	Quantity	|	2001	-	2022	|
|	QE_3_1	|	> Cheques	|	Quantity	|	2001	-	2022	|
|	QE_3_2	|	> Bills of trade and bills of exchange	|	Quantity	|	2001	-	2022	|
|	QE_3_3	|	> Direct debits	|	Quantity	|	2001	-	2022	|
|	QE_3_4	|	> Multibanco	|	Quantity	|	2001	-	2022	|
|	QE_3_4_1	|	> > Home banking payments	|	Quantity	|	2001	-	2022	|
|	QE_3_4_2	|	> > ATM payments	|	Quantity	|	2001	-	2022	|
|	QE_3_4_3	|	> > Residual of card payments network	|	Quantity	|	2001	-	2022	|
|	QE_3_5	|	> Credit transfers	|	Quantity	|	2001	-	2022	|
|	QE_4	|	Value of payment transactions	|	€Millions 	|	2001	-	2022	|
|	QE_4_1	|	> Cheques	|	€Millions 	|	2001	-	2022	|
|	QE_4_2	|	> Bills of trade and bills of exchange	|	€Millions 	|	2001	-	2022	|
|	QE_4_3	|	> Direct debits	|	€Millions 	|	2001	-	2022	|
|	QE_4_4	|	> Multibanco	|	€Millions 	|	2001	-	2022	|
|	QE_4_4_1	|	> > Home banking payments	|	€Millions 	|	2001	-	2022	|
|	QE_4_4_2	|	> > ATM payments	|	€Millions 	|	2001	-	2022	|
|	QE_4_4_3	|	> > Withdrawals	|	€Millions 	|	2001	-	2022	|
|	QE_4_4_4	|	> > Purchases	|	€Millions 	|	2001	-	2022	|
|	QE_4_4_5	|	> > Residual of card payments network	|	€Millions 	|	2001	-	2022	|
|	QE_4_5	|	> Credit transfers	|	€Millions 	|	2001	-	2022	|

# Basic Descriptive Statistics


**Table 11** - Number of observations over the data period (as of December) -- Panel A: Yearly Data

```{stata}
*| output: true
*| echo: false
*| ExecuteTime: {end_time: '2023-06-20T08:57:52.682458Z', start_time: '2023-06-20T08:57:52.153836Z'}

set linesize 200

global path "Z:/data/Products/SLB/2023_10/Output/Data/"
quietly use "${path}/SLB_A_YBNK_19902022_OCT23_QA1_V01.dta", clear
quietly append using "${path}/SLB_A_YBNK_19902022_OCT23_QA2_V01.dta"
quietly append using "${path}/SLB_A_YBNK_19942022_OCT23_QA3_V01.dta"
quietly append using "${path}/SLB_A_YBNK_19902022_OCT23_QB1_V01.dta"
quietly append using "${path}/SLB_A_YBNK_19972022_OCT23_QB2_V01.dta"
quietly append using "${path}/SLB_A_YBNK_19902022_OCT23_QC_V01.dta"
quietly append using "${path}/SLB_A_YBNK_19902022_OCT23_QD_V01.dta"
quietly append using "${path}/SLB_A_YBNK_20002022_OCT23_QE_V01.dta"

quietly label language en
version 16: table year, contents(freq) center
```

**Table 11** - Number of observations over the data period (as of December) -- Panel B: Quarterly Data

```{stata}
*| output: true
*| echo: false
*| ExecuteTime: {end_time: '2023-06-20T08:57:52.682458Z', start_time: '2023-06-20T08:57:52.153836Z'}

set linesize 200

global path "Z:/data/Products/SLB/2023_10/Output/Data/"
quietly use "${path}/SLB_A_QBNK_20012022_OCT23_QA1_V01.dta", clear
quietly append using "${path}/SLB_A_QBNK_20012022_OCT23_QA2_V01.dta"
quietly append using "${path}/SLB_A_QBNK_20092022_OCT23_QA3_V01.dta"
quietly append using "${path}/SLB_A_QBNK_20012022_OCT23_QB1_V01.dta"
quietly append using "${path}/SLB_A_QBNK_19972022_OCT23_QB2_V01.dta"

quietly label language en
version 16: table date, contents(freq) center
```

# References

Below is a list of main references:

1.    [**Series Longas - Setor Bancario Portugues 1990-2018**](https://www.bportugal.pt/sites/default/files/anexos/pdf-boletim/series_longas_setor_bancario_portugues.pdf)

2.    [**Historical Series - Portuguese Banking Sector 1990-2018**](https://www.bportugal.pt/sites/default/files/anexos/pdf-boletim/historical_series_portuguese_banking_system.pdf)

3.    Banco de Portugal (2017), [**Financial Stability Report**](https://www.bportugal.pt/sites/default/files/anexos/pdf-boletim/ref_06_2017_en.pdf), Banco de Portugal, June 2017, 84-91.



# Auxiliary Files

For a description of each variable in each dataset (name, unit of measurement, data and storage type, format, year of first and last observation), an account of the changes occurred over time, summary statistics[^8] for each dataset and a codebook for each dataset, please check the following auxiliary files:

| File | Description of Variables | Summary Statistics | Codebook | Dataset description |
| :---- | :----: | :----: | :----: |  :----: |
| Summary of all variables (Portuguese and English labels) | [variables_pt_en](./aux_files/variables_description/variables_pt_en.html) |
| Balance Sheet File |   | [SLB_stat_bal](./aux_files/descriptive_statistics/SLB_stat_bal.html) | [SLB_cdbk_bal](./aux_files/codebook/SLB_cdbk_bal.html) | [SLB_dscr_bal](./aux_files/describe_dataset/SLB_dscr_bal.html) |
| Income Statement File |	 | [SLB_stat_lp](./aux_files/descriptive_statistics/SLB_stat_lp.html) | 	[SLB_cdbk_lp](./aux_files/codebook/SLB_cdbk_lp.html) | [SLB_dscr_lp](./aux_files/describe_dataset/SLB_scr_lp.html) |
| Solvency File |	 | [SLB_stat_fi](./aux_files/descriptive_statistics/SLB_stat_fi.html) | 	[SLB_cdbk_fi](./aux_files/codebook/SLB_cdbk_fi.html) | [SLB_dscr_fi](./aux_files/describe_dataset/SLB_dscr_fi.html) |
| Loans to customers File |	 | [SLB_stat_credit](./aux_files/descriptive_statistics/SLB_stat_credit.html) | 	[SLB_cdbk_credit](./aux_files/codebook/SLB_cdbk_credit.html) | [SLB_dscr_credit](./aux_files/describe_dataset/SLB_dscr_credit.html) |
| Interest Rates File |	  | [SLB_stat_interest](./aux_files/descriptive_statistics/SLB_stat_interest.html) | 	[SLB_cdbk_interest](./aux_files/codebook/SLB_cdbk_interest.html) | [SLB_dscr_interest](./aux_files/describe_dataset/SLB_dscr_interest.html) |
| Human Resources File |	 | [SLB_stat_employee](./aux_files/descriptive_statistics/SLB_stat_employee.html) | 	[SLB_cdbk_employee](./aux_files/codebook/SLB_cdbk_employee.html) | [SLB_dscr_employee](./aux_files/describe_dataset/SLB_dscr_employee.html) |
| Branch Network File |	  | [SLB_stat_branch](./aux_files/descriptive_statistics/SLB_stat_branch.html) | 	[SLB_cdbk_branch](./aux_files/codebook/SLB_cdbk_branch.html) | [SLB_dscr_branch](./aux_files/describe_dataset/SLB_dscr_branch.html) |
| Payment Systems |	  | [SLB_stat_payment](./aux_files/descriptive_statistics/stat_payment.html) | 	[SLB_cdbk_payment](./aux_files/codebook/SLB_cdbk_payment.html) | [SLB_dscr_payment](./aux_files/describe_dataset/SLB_dscr_payment.html) |




The Summary Statistics, Codebook and Dataset Description files are available on BPLIM's servers.

[^8]: Please note that the summary statistics are run based on the perturbed data.

# Useful Links

[**Historical series about portuguese economy after World War II**](https://www.bportugal.pt/en/publicacao/historical-series-about-portuguese-economy-after-world-war-ii)

[**Banco de Portugal's Communication**](https://www.bportugal.pt/comunicado/banco-de-portugal-disponibiliza-informacao-historica-sobre-o-setor-bancario-portugues)

# Useful Ado Files

We provide an ado file written by BPLIM staff for researchers to implement the
matching of the Historical Series of the Portuguese Banking Sector (SLB) which
reports consolidated information with the Central Credit Responsibility (CRC)
database which reports individual-level information.


## [**mergecrcslb**](https://github.com/BPLIM/Tools/tree/master/ados/CRC_FRMBNK/mergecrcslb)

`Description`

`mergecrcslb ` is a Stata user-written command to help Create linking ids for
financial institutions in the Central Credit Responsibility (CRC) database for
the purpose of merging with Historical Series of the Portuguese Banking Sector (SLB).
By default, the ado should only be applied to the original CRC datasets
(bank-firm level or exposure level) prepared by BPLIM.


`Syntax`

```
mergecrcslb bankvar timevar

```

where `panelvar` is BPLIM's anonymized bank identifier and `timevar` identifies the time variable (monthly).


# Appendix

1.    [List of Included Institutions by Variable](./attachments/QF_Lista Instituições por variáveis_2022.xlsx)[^9]

2.    [The Evolution of Banking Groups Over Time](./attachments/QG_Perímetros por Grupo Bancário_2022.xlsx)[^10]

[^9]: 24 institutions were eliminated in the current update, given the entry into force of the [Investment Companies Regulation](https://www.cmvm.pt/pt/Legislacao/Legislacaonacional/Circulares/Documents/Circular%20relativa%20%C3%A0%20entrada%20em%20vigor%20do%20Regime%20de%20Empresas%20de%20Investimento.pdf). The weight of these institutions in the financial system is however residual.

[^10]: Information on the over-time evolution of banking groups is only available upon request to internal researchers.

# Citation of this Dataset

Banco de Portugal Microdata Research Laboratory (BPLIM) (2023): Historical Series of the Portuguese Banking Sector. Extraction: October 2023. Version: V1. Banco de Portugal - BPLIM. Dataset. https://doi.org/10.17900/SLB.Oct2023.V1

<br>
To cite this data set you can use the package biblatex with the following BibTeX entry: 

```{stata}
*| eval: false
*| echo: true
*| code-fold: false
*| ExecuteTime: {end_time: '2023-06-20T08:57:58.771961Z', start_time: '2023-06-20T08:57:57.953258Z'}
@dataset{SLB.Oct2023.V1,
author = {{Banco de Portugal Microdata Research Laboratory - BPLIM}},
publisher = {Banco de Portugal},
title = {{H}istorical {S}eries of the {P}ortuguese {B}anking {S}ector},
year = {2023},
version = {{ V1, Extraction October 2023}},
doi = {10.17900/SLB.Oct2023.V1},
url = {https://doi.org/10.17900/SLB.Oct2023.V1}
}
```


