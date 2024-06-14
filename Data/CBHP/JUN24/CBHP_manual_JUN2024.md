---
title: Central Balance Sheet Harmonized Panel Data - Data Manual
subtitle: Extraction Date - June 2024
author: BPLIM
date: 14 June 2024
abstract: 'In 2010, the national accounting standards underwent some changes, and *Plano Oficial de Contabilidade* (POC, Official Chart of Accounts) was replaced by *Sistema de Normalização Contabilística* (SNC, Accounting Standards System). This had an impact on the base information in the Central Balance Sheet Database (CB). This manual describes the panel data of Central Balance Sheet Database with harmonized variables over time available at BPLIM.'
doi: 10.17900/CB.CBHP.Jun2024.V1
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
jupyter:
  kernelspec:
    display_name: Stata (nbstata)
    language: stata
    name: nbstata
---

# General Information

> **Dataset Designation in English**: Central Balance Sheet Harmonized Panel Data (CBHP)

> **Dataset Designation in Portuguese**: *Painel Harmonizado da Central de Balanços* (CBHP)

> **Data Type**: Longitudinal Data

> **Unit of Analysis**: Firms

> **Frequency**: Annual

> **Start Date**: 2006

> **Most recent year**: 2022

> **Reference date**: The data reports to the fiscal period declared by the firm. For most cases, the fiscal period coincides with the civil year. For those firms with fiscal period different than the civil year, the reference year is the one covering most of the days of the fiscal period.

> **Data Organization**: Data is organized in five files:

  - General Information on the firm (Cover Sheet),
  - Economic and Financial Information (Balance Sheet and Profit and Loss Statements),
  - Employment Information,
  - Trade Information per Market,
  - Corporate Actions.

  In all files each row corresponds to one firm in a given year. [^1] All files are available in Stata format, version 18.

> **Version of the Data**: The data made available by BPLIM corresponds to a data freeze at a certain time of the year.[^2] Therefore, all files contain the information as reported in the extraction date. The most recent update of the data occurred in June 2024.

[^1]: For \'Corporate Actions\' data file, there may be multiple firm entries per year since the firm may be involved in more than one event for the same reference year.

[^2]: For more information, see the manual on the Annual Data of Central Balance Sheet Database.

> **Languages Available**: Variable labels and value labels are available in Portuguese and for most of the variables also in English. [^3]

[^3]: To see the labels in English type the following command line in Stata: 'label language en'.


> **Related Datasets**: This product is built based on the information from Central Balance Sheet Database (CB).


> **Digital Object Identifier**: 10.17900/CB.CBHP.Jun2024.V1

> **New in this extraction**: variable *concelho* (Municipality) is now available.

# Geographical Coverage

The data refers to firms located in the Mainland Portugal and Autonomous Regions – Azores and Madeira.

# Population

The population of the CBHP is the same as in the annual data, i.e. the population of all Portuguese non-financial corporations. For more information, please see the manual on [*Central Balance Sheet Database (CB) - Annual Data*](../../CB/Jun2024/Pack_CB_Empresas_Jun24/CB_manual_Jun2024.html).

# Methodology

Central Balance Sheet Database (CB) provides economic and financial information on Portuguese non-financial corporations. The data is collected through *Informação Empresarial Simplicada* (IES) since 2006. In 2010, the national accounting standards underwent some changes, and *Plano Oficial de Contabilidade* (POC, Official Chart of Accounts) was replaced by *Sistema de Normalização Contabilística* (SNC, Accounting Standards System), which is closer to the International Accounting Standards (IAS) and International Financial Reporting Standards (IFRS). This had an impact on the base information in CB (Banco de Portugal, 2014; Banco de Portugal, 2019).

![](./attachments/accounting_years.PNG)

With the introduction of SNC, several changes were introduced. For example:

- some accounting items were simply redenominated;

- some accounting items were aggregated or disaggregated;

- there are new variables being reported. The Interest Income (VF16150) and Net Non-current Assets Held for Sale (VF16035) are some examples of variables that are not reported in the financial statements written according to POC;

- the asset items in POC accounting system were reported in gross terms and the amortizations and adjustments were reported separately for each item of the Balance Sheet. The financial statement written according to SNC does not have a separate item for depreciations as POC did and all variables are being reported in net terms.

- SNC introduced different reporting standards for firms with different sizes. After 2010, Micro-Entities and Small-sized Entities [^4] were required to report a lower number of variables.

Therefore, some accounting items in the old accounting system have an approximate correspondence and others have no correspondence at all in SNC.
Some variables had to be aggregated to guarantee the comparability before and after 2010. Besides, the harmonized variables can only be calculated if their components are reported for all entities according to the reporting standards adopted by the firm. Therefore, CBHP contains a lower number of variables than those included in CB.
Currently we make available approximately 60 harmonized variables on the Balance Sheet and Profit and Loss Statement. In the Employment Information file, we make available 20 variables and in the Trade Information per market file, 14 variables are available. All variables in the Cover Sheet File and the Corporate Actions File are available given that this type of information was not affected by the accounting standards.

Table 1 – Number of Harmonized Variables by type of information

| Type of Information	| Number of Harmonized Variables |	Time Period |
| :----------- | :-----------: | :------: |
| General Information (Cover Sheet) File	| 27 | 2006-2022 |
| Economic and Financial Information File | 62 | 2006-2022 |
| Employment Information File | 20 | 2006-2022 |
| Trade Information per Market File | 14 | 2006-2022 |
| Corporate Actions | 10 | 2006-2022 |

In this section, we describe the procedure to compute the harmonized variables available in CBHP. For a complete account on how each variable made available in the panel was computed, check the [Description of Variables](#description-of-variables).
All the calculations are done based on the annual files of CB. Therefore, the number of firms and the time period available are the same as in the annual files. The panel dataset is updated once per year around the month of June, at the same time as the annual data of CB. The most recent extraction occurred in June 2024 and includes data from 2006 to 2022.

The harmonization procedure is different for each file described in Table 1. While the information in the Cover sheet did not suffer any significant change with the introduction of SNC, the harmonization of the Economic and Financial Information is not a straightforward task. Therefore, we classified the harmonization methodology in three different categories:

- **Type 1**: covers the information unaffected by the change in the accounting system, which includes the Cover Sheet and the Corporate Actions Files. In these cases, we simply append the annual datasets. The name of the variables remain the same since no change on the original data was undertaken.

- **Type 2**: covers the information that was directly affected by the change in the accounting system, i.e., the Economic and Financial Information and Trade Information per Market. It also includes the Employment Information because the variables are collected through different tables in IES and have different denominations under POC and SNC accounting systems.
For this type of files, we rely on the definition of the variables under the current accounting system (SNC) and compute a formula using the POC items needed to ensure the comparability over time.
For example, the procedure to compute the item Turnover (D001) is illustrated below for a fictional firm:

| | | | | | | | |
| :---: | :-------: | :---: | :------: | :------: | :------: | :------: | :------: |
| **ano** |	**tina** | planocont | VF03045	| VF03046	| VF03047	| VF16132	| **D001** |
| **2006** | **500000000** | POC | . | . | . | . | **0** |
| **2007** | **500000000** | POC | 100 | 100 | 100 | . | **300** |
| **2008** | **500000000** | POC | 100 | 100 | . | . | **200** |
| **2009** | **500000000** | POC | 100 | 100 | 100 | . | **300** |
| **2010** | **500000000** | SNC | . | . | . | 100 | **100** |
| **2011** | **500000000** | SNC | . | . | . | 100 | **100** |
| **2012** | **500000000** | SNC | . | . | . | 100 | **100** |
| **2013** | **500000000** | SNC | . | . | . | 100 | **100** |
| **2014** | **500000000** | SNC | . | . | . | 100 | **100** |
| **2015** | **500000000** | SNC | . | . | . | 100 | **100** |
| **2016** | **500000000** | SNC | . | . | . | 100 | **100** |
| **2017** | **500000000** | SNC | . | . | . | 100 | **100** |
| **2018** | **500000000** | SNC | . | . | . | 100 | **100** |
| **2019** | **500000000** | SNC | . | . | . | 100 | **100** |

The SNC variable - VF16132 (Turnover) - corresponds to the sum of the variables VF03045 (Sales of goods), VF03046 (Sales of products) and VF03047 (Provision of services) in the POC accounting system. Therefore, a new harmonized variable is computed - D001 - using these auxiliary variables. After calculating the harmonized variable, the auxiliary variables are dropped and only the variables in bold are kept in the dataset.
All missing values in the auxiliary variables are treated as zeros. The report of IES is mandatory for all firms that are required to send the financial statements to the Ministry of Finance. Therefore, all items have to be completed in a consistent manner so that the firm is able to submit the declaration and the real value of a specific variable is assumed to be zero if it is not reported.
The naming convention for Balance Sheet variables in the panel data is Bxxx or BLxxx, for Profit and Loss Statement is Dxxx or DLxxx, for Employment Information is Exxx and for Trade Information per Market is MGxxx.


After identifying all variables that can be potentially included in the panel dataset, we produced and analyzed technical reports on each variable. Namely, we did the following checks to ensure the compatibility of the panel variables over time:

1. analyze the evolution of the mean and median values of the relative changes over time. [^5] We try to identify whether there is any discontinuity in 2010, the first year in which most of the firms reported under *Sistema de Normalização Contabilística*.[^6]
2. check whether abnormal relative changes (relative changes above 100%) are found more often in the transition to the new accounting system.
3. decomposition of the yearly variation of the total value of each variable due to the expansion and contraction of incumbents and the entry and exit of firms.
4. regression of each variable on time dummies to detect any structural change in the variable after 2010.

The link to the report on each variable is available in the section [Description of Variables](#description-of-variables).[^38]
The harmonization procedure tries to ensure the compatibility of the variables over time as much as possible. However, there may be more than one harmonization methodology and the transition between the old and the new accounting rules and concepts may take some time. For these reasons, some harmonized variables may show a clear discontinuity in 2010.

We also produce reports for the Economic and Financial Information File, Employment Information File and Trade Information per Market File checking whether the sum of disaggregated variables corresponds to the aggregated variables. These reports are available in the [Auxiliary Files Section](#auxiliary-files).


- **Type 3**: covers the Economic and Financial Indicators files containing information affected by the change in the accounting system. The information on this file is calculated using the variables available in the Economic and Financial Information File. We provide a Stata ado file and an R script to compute all the economic and financial indicators that are possible to harmonize over time given the information available in the panel dataset. By adopting this procedure, the size of the dataset is minimized. All indicators variables calculated by these scripts are denominated Rxxx.

[^4]: A Micro-Entity is defined as a firm that falls below in at least two of the following criteria at the balance sheet date of the previous fiscal period: i) total assets equal to 500.000 euros; ii) net turnover equal to 500.000 euros; or iii) average number of employees equal to 5. Small-sized Entities are firms satisfying at least two of the following conditions: i) total assets below 1.500.000 euros; ii) Total net sales and other income lower than 3.000.000 euros or; iii) average number of employees less than 50. For more details please check the manual on [*Central Balance Sheet Database (CB) - Annual Data*](../../CB/Jun2024/Pack_CB_Empresas_Jun24/CB_manual_JUN2024.html).

[^5]: The relative changes are defined as the difference between the value of the variable observed in year t minus the value observed in the previous year. Relative changes are computed with respect to the average of year t and t-1 and are measured in percentage.

[^6]: In 2010 some declarations were reported according to *Plano Oficial de Contas*. This situation occurs mostly for declarations sent in the cessation period and before or after the firms adopts a special fiscal period - a fiscal period different from the calendar year.

[^38]: All reports are available on BPLIM's servers.

# Description of Files

Similarly to the annual data files, CBHP is organized in five files. Each file provides a different type of information, namely:

| Type of Information | File Name |
| :------ | :----------- |
| **A.	General Information (Cover sheet)** | CBHP_A_YFRM_yyyyYYYY_eeee_ROSTO_V01.dta |
| **B.	Economic and Financial Information** | CBHP_A_YFRM_yyyyYYYY_eeee_CONTAS_V01.dta |
| **C.	Employment Information** | CBHP_A_YFRM_yyyyYYYY_eeee_PESSOAL_V01.dta |
| **D.	Trade Information per Market** | CBHP_A_YFRM_yyyyYYYY_eeee_MG_V01.dta |
| **E.	Corporate Actions** | CBHP_A_YFRM_yyyyYYYY_eeee_AMARC_V01.dta |

Where *A* stands for anonymized and *yyyy* corresponds to the first year available and *YYYY* corresponds to most recent year available. *eeee* reports the extraction date.

All files contain a unique firm identifier (*tina*) and a reference year (*ano*) allowing the matching of the different types of information by firm. Whenever possible, labels and value labels were attributed to all categorical variables. All data sets are anonymized.

# Description of Variables

Below we provide a general description of the variables included in the data. The metadata files are available in the [“Auxiliary Files” section](#auxiliary-files).

## A.	General Information File (Cover Sheet)

The information reported in this file was not affected by the change in the accounting system. Therefore, the panel dataset includes all the variables available in the annual data files. The variables reporting the accounting system (*planocont*) and the accounting standards (*regime*) under which the firm is reporting information are kept in the panel dataset. These variables do not have any interpretation given that all the economic and financial variables included in the panel dataset are harmonized over time. They are kept in the dataset because they may be useful in case one wants to calculate additional variables not provided by BPLIM using the CB annual data.

The information contained in this file has three different sources: variables reported by the firm through IES, variables computed by the Statistics Department of *Banco de Portugal* using the information reported in IES and variables collected by the Ministry of Justice through the Central Registry of Companies.[^23]

### A1. Identifiers

`Firm identifier` (*tina*) – Unique identifier that enables tracking the legal entity over time. *tina* is the anonymized tax identification number.

`Reference year of the data` (*ano*) – Reference year of the data.

### A2. Variables reported by the firm through IES
`Fiscal Period` (*datainitrib*, *datafimtrib* and *numdias*):

*datainitrib* - fiscal year start date;

*datafimtrib* - fiscal year end date;

*numdias* - total number of days of the fiscal year.


`Reporting Type` (*planocont*) – indicates the accounting system according to which the firm reports the information, i.e., POC or SNC.

| Code | Designation |
| :------: | :----------- |
| 0 | POC | Official Chart of Accounts |
| 1 | SNC | Accounting Standards System |


`Reporting Standards` (*regime*) – with the introduction of SNC firms must select their reporting standards. Therefore this variable is only available after 2009.

| Code | Designation |
| :------: | :----------- |
| -1 | Not specified |
| 1 | International Accounting Standards (NIC's) |
| 2 | Accounting and Financial Reporting Standards (NCRF's) |
| 3 | Accounting and Financial Reporting Standards for Small-Sized Entities (NCRF-PE) |
| 4 | Accounting and Financial Reporting Standards for Micro-Entities (NC-ME) |


`Declaration Motive` (*motivodec*) – indicates the reason to submit the declaration.

| Code | Designation |
| :------: | :----------- |
| 0 | Normal |
| 1 | Consolidation |
| 2 | Ceasing Period |
| 3 | Special fiscal period - before the change |
| 4 | Special fiscal period - after the change |
| 5 | First fiscal period |

`Number of Establishments` – firms report the total number of national and foreign establishments (*numestabnac* and *numestabest*, respectively).[^24] *numestab* provides information on the total number of establishments.[^25] According to the filling instructions, the Headquarter should be considered an establishment.

`Firm’s Situation` (*sitempresa*) – indicates the firm situation at the end of the fiscal period.

| Code |     Designation |
| :------: | :----------- |
| 1 | In business |
| 2 | End of business |
| 3 | Dissolved |
| 4 | Liquidated |

`Reference date of firm’s situation` (*datasitempresa*) – reports the reference date of the firm’s situation. This information is required in case the firm reports codes 2, 3 and 4 in *sitempresa* variable.

`Firm in liquidation` (*liquidacao*) - identifies firms in liquidation. According to the [Article 146 of the Portuguese Code of Commercial Companies](https://dre.pt/web/guest/legislacao-consolidada/-/lc/116042191/201906302305/73599989/diploma/indice), dissolved firms are required to add the expression "Em liquidação" to their name while they are in the liquidation process. This variable is created by BPLIM using the information contained in the company's name as reported by the firm in IES forms. It takes value one if the expression "em liquida" is found in the company's name.

`Share of turnover of the main economic activity` (*pervvn*) – indicates the proportion of turnover that the main economic activity represents among all the activities carried on by the firm.

`Branch` (*sucursal*) - dummy variable that takes value one for branches of foreign firms located in Portugal. Branch offices are identified using the information contained in the name as reported by the firm in IES and the tax identification number of the company. Notably, the legislation states that the name of these companies includes expressions such as "Sucursal" or "Representação Permanente" (see, for example, [Article 21 of Ordinance n. 1416-A/2006](https://dre.pt/pesquisa/-/search/235919/details/maximized) or [Article 5 of Decree-Law n. 73/2008](https://dre.pt/pesquisa/-/search/249803/details/maximized)) and the firms are assigned with tax identification numbers started by "98".

`Exporting Firm` (*exporta*) - categorical variable created by BPLIM to identify firms exporting to the European Union or Extra-European Union Markets. This variable is constructed based on the information reported in the Trade Information per Market files, according to the formulas below:

| Code | Designation | Formula using POC variables | Formula using SNC variables |
| ---- | ------------ | --------- | ----------- |
| 0 | Does not Export [^34] | VF03953 = 0 ***and*** VF03954 = 0 ***and*** VF03957 = 0 ***and*** VF03958 = 0 | VF15620 = 0 ***and*** VF15624 = 0 ***and*** VF15621 = 0  ***and*** VF15625 = 0 |
| 1 | Exports to EU Market | VF03953 (EU Market - Total sales) $>$ 0 ***or*** VF03954 (EU Market - Total services) $>$ 0 | VF15620 (EU Market - Total sales) $>$ 0 ***or*** VF15624 (EU Market - Total services) $>$ 0|
| 2 | Exports to Extra-EU Market | VF03957 (Extra-EU Market - Total sales) $>$ 0 ***or*** VF03958 (Extra-EU Market - Total services) $>$ 0 |  VF15621 (Extra-EU Market - Total sales) $>$ 0 ***or*** VF15625 (Extra-EU Market - Total services) $>$ 0 |
| 3 | Exports to EU and Extra-EU Market | (VF03953 ***or*** VF03954) $>$ 0 ***and*** (VF03957 ***or*** VF03958) $>$ 0 | (VF15620 ***or*** VF15624) $>$ 0 ***and*** (VF15621 ***or*** VF15625) $>$ 0 |

[^34]: Missing values in the referred variables are treated as zeros.


`Single Holder Private Limited Company` (*unipessoal*) - dummy variable that takes value one for companies under the legal form "Single Holder Private Limited Company" (*Sociedade Unipessoal por Quotas*) and zero otherwise. This information is identified using the name reported by the firm in *IES*, given the obligation for this type of firms to include the word "UNIPESSOAL" in their name ([Decree-Law no 257/96, December 31](https://www.pgdlisboa.pt/leis/lei_mostra_articulado.php?artigo_id=462A0004&nid=462&tabela=leis&pagina=1&ficha=1&nversao=)). [^37]

[^37]: Some variants of the word "UNIPESSOAL" are also considered to include misspelled words and branches of foreign companies (eg. "UNIPESSSOAL", "UNIPESOAL", "UNIPERSONAL", "UNIPERSONNELLE", etc.).

### A3. Variables created by the Statistics Department of *Banco de Portugal*

`Institutional Sector` (*sectorinstfinal*) - reports the institutional sector to which the firm belongs to. As explained in the Sections “Population” and “Methodology”, CB only includes non-financial corporations. Therefore, this variable identifies the type of non-financial corporation, such as public, private or holding company. The algorithm to allocate firms according to the institutional sector is based on the classification of economic activity, the name of the firm and other variables available at *Banco de Portugal*. Therefore, in some cases the institutional sector may not be in line with the sector of economic activity.

| Code | Designation |
| :----: | :----------- |
| 002 | Non-financial corporations |
| 003 | Public non-financial corporations |
| 004 | Private non-financial corporations |
| 005 | Foreign controlled non-financial corporations |
| 006 | Non-financial corporations of central government - Enterprises |
| 007 | Non-financial corporations of central government - Other entities |
| 008 | Non-financial corporations of the regional government of Madeira - Enterprises |
| 009 | Non-financial corporations of the regional government of Madeira - Other entities |
| 010 | Non-financial corporations of the regional government of Azores - Enterprises |
| 011 | Non-financial corporations of the regional government of Azores - Other entities |
| 012 | Non-financial corporations of the local government of Mainland Portugal - Enterprises |
| 013 | Non-financial corporations of the local government of Mainland Portugal - Other entities |
| 014 | Non-financial corporations of the local government of Azores - Enterprises |
| 015 | Non-financial corporations of the local government of Azores - Other entities |
| 016 | Non-financial corporations of the local government of Madeira - Enterprises |
| 017 | Non-financial corporations of the local government of Madeira - Other entities |
| 302 | Public non-financial holding companies |
| 308 | Private non-financial holding companies |
| 314 | Foreign controlled non-financial holding companies |



`Indicator of Economic Activity` (*indactiecon*) – this variable reports the firm situation revised by the Statistics Department of *Banco de Portugal*. It is constructed using the information reported by the firm in IES (*sitempresa*) and complemented with other sources. Notably, it takes into account whether the firm contracts new loans, maintains commercial transactions with firms abroad or pays and settles the Value Added Tax, among others.


| Code | Designation |
| :------: | :----------- |
| 0  | Unknown |
| 10 | Awaiting business start |
| 20 | In business |
| 30 | Suspended activity |
| 40 | Ceased activity |
| 97 | Invalid |
| 98 | Not specified|


`Dimension Category` (*dimcomissao*) - this variable classifies firms according to four dimension categories following the [Commission Recommendation 2003/361/CE](./aux_files/legislation/CR_2003_361_ec.pdf)[^33]:

| Code | Designation |
| :------: | :----------- |
| 1 | Microenterprises |
| 2 | Small enterprises |
| 3 | Medium-sized enterprises |
| 4 | Large enterprises |


 This classification is based on the number of employees and either total turnover or assets:

| Company category | Staff headcount | and |  (Turnover | or | Balance sheet total) |
| ------ | ----------- | --- | -------- | --- | ----------- |
| Medium-sized | <250 | and | ($\leq$ €50 m | or | $\leq$ €43 m) |
| Small | <50 | and | ($\leq$ €10 m | or | $\leq$ €10 m) |
| Micro | <10 | and | ($\leq$ €2 m | or | $\leq$ €2 m)  |
Source: [European Commission](http://ec.europa.eu/growth/smes/business-friendly-environment/sme-definition_en)

[^33]: Note that the firms belonging to a business group are not being excluded from the definition of microenterprises in the variable *dimcomissao*.

`Founding year` (*ancon*) – corresponds to the year of business start according to the Indicator of Economic Activity (*indactiecon*). This information is complemented with the founding date reported in the Central Registry of Companies.

### A4. Variables extracted from Central Registry of Companies (Ministry of Justice)

`Legal form` (*natju*) – this variable reports firm’s legal form. For a complete list of codes see the metadata file [CBHP_meta_YFRM_JUN24_ROSTO_V01](./aux_files/metafiles/CBHP_meta_YFRM_JUN24_ROSTO_V01.xlsx).

`Sector of Activity` (*cae21*, *cae3*, *caekotu*):

`Main Sector of Activity` (*cae21* and *cae3*) - reports firm's main sector of activity. The criteria to define the main sector of activity is the gross value added at factor cost. When it is not possible to use this information to define the main sector of activity, firms are requested to use turnover or the number of people permanently employed by the firm. From 2006 to 2008, firms reported the code of “The Portuguese Classification of Economic Activities - Revision 2.1” (CAE Rev. 2.1) at the highest level of disaggregation. Since 2008, firms report their main activity according to the “The Portuguese Classification of Economic Activities - Revision 3” (CAE Rev. 3). The Statistics Department of *Banco de Portugal* provides the information on the main sector of activity according to both classifications CAE Rev. 2.1 and CAE Rev. 3 whenever possible. The source of this information is the CAE registered in the “Central Registry of Companies” for each company. Whenever the correspondence is not unique, the match between codes according to CAE Rev. 2.1 and CAE Rev. 3 is implemented based on the highest frequency of the matches.[^26] For a complete list of codes see the metadata file [CBHP_meta_YFRM_JUN24_ROSTO_V01](./aux_files/metafiles/CBHP_meta_YFRM_JUN24_ROSTO_V01.xlsx).

The main sector of activity is reported at the highest disaggregation level (5 digit) and can be aggregated using the Stata package [`validarcae`](https://github.com/BPLIM/Tools/tree/master/ados/General/validarcae) available in the SSC.


`CAE sections K, O, T or U` (*caekotu*) - this variable was created by BPLIM using the information in *cae3* (Classification of Economic Activity Rev. 3). It takes value one if the main economic activity of the firm is within one of the following sections of economic activity:

- K- Financial and insurance activities,
- O-Public administration and defence; compulsory social security,
- T-Activities of households as employers; undifferentiated goods- and services-producing activities of households for own use,
- U-Activities of extraterritorial organizations and bodies.

This variable allows for the identification of the cases in which the information on the sector of economic activity reported by the firm is not in line with the institutional sector to which the firm is allocated by the Statistics Department of *Banco de Portugal*. This may happen because *Banco de Portugal* uses complementary sources of information besides the classification of economic activities to classify firms as non-financial corporations.

`Municipality` (*concelho*) – provides information on the municipality in which the firm is located. The classification of this variable is according to *DICOFRE* and differs from the [Code of the administrative division](http://smi.ine.pt/Versao/Detalhes/17) for Autonomous Regions. For a complete list of codes see the metadata file [CBHP_meta_YFRM_JUN24_ROSTO_V01](./aux_files/metafiles/CBHP_meta_YFRM_JUN24_ROSTO_V01.xlsx).

The Stata package `validarloc` available in [BPLIM's Github repository](https://github.com/BPLIM/Tools/tree/master/ados/General/validarloc) allows to validate and aggregate the Portuguese administrative division codes. To convert the Portuguese municipality classification to the Nomenclature of Territorial Units for Statistics (NUTS), the Stata package `coconuts` is also available in [BPLIM's Github repository](https://github.com/BPLIM/Tools/tree/master/ados/General/coconuts).


[^23]: *Ficheiro Central de Pessoas Colectivas*.

[^24]: All establishments, including those in which no productive activity is carried on are included.

[^25]: Establishment is defined as an enterprise or part of an enterprise that carries on economic activities in a geographically identified place, with one or more workers.

[^26]: For more information on firm’s sector of activity please see [SICAE Website](http://www.sicae.pt/Default.aspx).

## B.	Economic and Financial Information File

This file provides a set of balance sheet and profit and loss statement variables harmonized over time. For a full account of the SNC items included in the definition of the harmonized variable see the auxiliary file [contas_snc_items.html](./aux_files/variables_description/contas_snc_items.html).

### B1. Identifiers

`Firm identifier` (*tina*) – Unique identifier that enables tracking the legal entity over time. *tina* is the anonymized tax identification number.

`Reference year of the data` (*ano*) – Reference year of the data.

### B2. Balance Sheet Variables

### Assets

| Variable | Variable description | Definition | SNC Variable | Formula in POC | Variable Report |
| :----: | :-------------- | :----------- | :-----: | :---------: | :----------: |
| B001 | **Total Assets** | Total non-current assets; Total current assets | VF15991 | [Formula in POC](#b001---formula-in-poc) | [Report - B001](./aux_files/technical_reports/variable_report/Contas/B001_tmd.html) |
| B004 | > Total non-current assets | Fixed tangible assets and intangible assets; Financial investments; Remaining non-current assets | VF15994 | [Formula in POC](#b004---formula-in-poc) | [Report - B004](./aux_files/technical_reports/variable_report/Contas/B004_tmd.html) |
| B005 | > > Fixed tangible assets and intangible assets | Intangible assets (including Goodwill); Land and buildings; Basic equipment; Other fixed assets; Payments on account of fixed assets | VF15995 | [Formula in POC](#b005---formula-in-poc) | [Report - B005](./aux_files/technical_reports/variable_report/Contas/B005_tmd.html) |
| B012 | > > > Fixed tangible assets | Land and buildings; Basic equipment; Other fixed assets; Payments on account of fixed assets [^7] | VF16002 | [Formula in POC](#b012---formula-in-poc) | [Report - B012](./aux_files/technical_reports/variable_report/Contas/B012_tmd.html) |
| B025 | > > Financial investments | Investments in subsidiary and associated companies; Financial investments (excepting investments in subsidiary and associated companies | VF16015 | [Formula in POC](#b025---formula-in-poc) | [Report - B025](./aux_files/technical_reports/variable_report/Contas/B025_tmd.html) |
| B158 | > > Non-current assets - Remaining non-current assets | Shareholders / partners; Deferred tax assets | VF18510 | [Formula in POC](#b158---formula-in-poc) | [Report - B158](./aux_files/technical_reports/variable_report/Contas/B158_tmd.html) |
| B029 | > Total Current assets | Inventories and biological assets; Customers; Remaining current assets; Cash and bank deposits; Non-current assets held for sale [^8] | VF16019 | [Formula in POC](#b029---formula-in-poc) | [Report - B029](./aux_files/technical_reports/variable_report/Contas/B029_tmd.html) |
| B032 | > > Current assets - Inventories and biological assets | Raw and subsidiary materials and consumables; Advances from customers; Inventories (excepting Raw and subsidiary materials and consumables) | VF16022 | [Formula in POC](#b032---formula-in-poc) | [Report - B032](./aux_files/technical_reports/variable_report/Contas/B032_tmd.html) |
| B041 | > > Current assets - Customers | | VF16031 | [Formula in POC](#b041---formula-in-poc) | [Report - B041](./aux_files/technical_reports/variable_report/Contas/B041_tmd.html) |
| B049 | > > Current assets - Cash and bank deposits | | VF16039 | [Formula in POC](#b049---formula-in-poc) | [Report - B049](./aux_files/technical_reports/variable_report/Contas/B049_tmd.html) |
| B159 | > > Current assets - Remaining current assets | Current assets - State and other public entities; Other current assets; Shareholders; Deferred expense | VF18511 | [Formula in POC](#b159---formula-in-poc) | [Report - B159](./aux_files/technical_reports/variable_report/Contas/B159_tmd.html) |
| B042 | > > Current assets - State and other public entities | | VF16032 | [Formula in POC](#b042---formula-in-poc) | [Report - B042](./aux_files/technical_reports/variable_report/Contas/B042_tmd.html) |


[^7]: With the introduction of SNC some components that were previously classified as fixed tangible assets were reallocated to intangible assets to accommodate international standards. An example is highway concessions which were considered as tangible assets in POC and were reclassified as intangible assets in SNC.
[^8]: This variable has no match in *Plano Oficial de Contas*.

### Equity

| Variable | Variable description | Definition | SNC Variable | Formula in POC | Variable Report |
| :----: | :-------------- | :----------- | :-----: | :---------: |  :----------: |
| B060 | **Equity and Liabilities** | Equity; Liabilities | VF16050 | [Formula in POC](#b060---formula-in-poc) | [Report - B060](./aux_files/technical_reports/variable_report/Contas/B060_tmd.html) |
| B061 | > **Equity** | Paid-up capital;	Other equity instruments; Reserves and retained earnings; Other items of equity; Net income; Interim dividends | VF16051 | [Formula in POC](#b061---formula-in-poc) | [Report - B061](./aux_files/technical_reports/variable_report/Contas/B061_tmd.html) |
| BL005 |	> > Legal reserves | | VF13024 | [Formula in POC](#bl005---formula-in-poc) | [Report - BL005](./aux_files/technical_reports/variable_report/Contas/BL005_tmd.html) |
| BL007 | > > Retained earnings | | VF13026 | [Formula in POC](#bl007---formula-in-poc) | [Report - BL007](./aux_files/technical_reports/variable_report/Contas/BL007_tmd.html) |
| B074 | > > Interim dividends | | VF16064 | [Formula in POC](#b074---formula-in-poc) | [Report - B074](./aux_files/technical_reports/variable_report/Contas/B074_tmd.html) |
| B143 | > > Subscribed capital | |VF16425 | [Formula in POC](#b143---formula-in-poc) | [Report - B143](./aux_files/technical_reports/variable_report/Contas/B143_tmd.html) |


### Liabilities

| Variable | Variable description | Definition | SNC Variable | Formula in POC | Variable Report |
| :----: | :-------------- | :----------- | :-----: | :---------: |  :----------: |
| B080 | > **Liabilities** | Non-current liabilities; Current liabilities | VF16070 | [Formula in POC](#b080---formula-in-poc) | [Report - B080](./aux_files/technical_reports/variable_report/Contas/B080_tmd.html) |
| B081 | > > Non-current liabilities | Obtained funding; Post-employment benefits; Remaining non-current liabilities | VF16071 | [Formula in POC](#b081---formula-in-poc) | [Report - B081](./aux_files/technical_reports/variable_report/Contas/B081_tmd.html) |
| B085 | > > > Non-current liabilities - Obtained funding | | VF16075 | [Formula in POC](#b085---formula-in-poc) | [Report - B085](./aux_files/technical_reports/variable_report/Contas/B085_tmd.html) |
| B160 | > > > Non-current liabilities - Remaining non-current liabilities | Provisions; Other accounts payable; Deferred tax liabilities | VF18512 | [Formula in POC](#b160---formula-in-poc) | [Report - B160](./aux_files/technical_reports/variable_report/Contas/B160_tmd.html) |
| B089 | > > Current liabilities | Suppliers; Obtained funding; Remaining current liabilities | VF16079 | [Formula in POC](#b089---formula-in-poc) | [Report - B089](./aux_files/technical_reports/variable_report/Contas/B089_tmd.html) |
| B093 | > > > Current liabilities - Suppliers | | VF16083 | [Formula in POC](#b093---formula-in-poc) | [Report - B093](./aux_files/technical_reports/variable_report/Contas/B093_tmd.html) |
| B096 | > > > Current liabilities - Obtained Funding | | VF16086 | [Formula in POC](#b096---formula-in-poc) | [Report - B096](./aux_files/technical_reports/variable_report/Contas/B096_tmd.html) |
| B161 | > > > Current liabilities - Remaining current liabilities | State and other public sector institutions; Other current liabilities; Deferred income | VF18513 | [Formula in POC](#b161---formula-in-poc) | [Report - B161](./aux_files/technical_reports/variable_report/Contas/B161_tmd.html) |
| B094 | > > > > Current liabilities - State and other public entities | | VF16084 | [Formula in POC](#b094---formula-in-poc) | [Report - B094](./aux_files/technical_reports/variable_report/Contas/B094_tmd.html) |

### B3. Profit and Loss Statement Variables

| Variable | Variable description | Definition | SNC Variable | Formula in POC | Variable Report |
| :----: | :-------------- | :----------- | :-----: | :---------: |  :----------: |
| D021 | **Total income** | Turnover; Remaining income | VF16152 | [Formula in POC](#d021---formula-in-poc) | [Report - D021](./aux_files/technical_reports/variable_report/Contas/D021_tmd.html) |
| D001 | > Turnover | Sales; Services | VF16132 | [Formula in POC](#d001---formula-in-poc) | [Report - D001](./aux_files/technical_reports/variable_report/Contas/D001_tmd.html) |
| D002 | > > Sales | Sales of good and products | VF16133 | [Formula in POC](#d002---formula-in-poc) | [Report - D002](./aux_files/technical_reports/variable_report/Contas/D002_tmd.html) |
| DL017 | > > Services | | VF15599 | [Formula in POC](#dl017---formula-in-poc) | [Report - DL017](./aux_files/technical_reports/variable_report/Contas/DL017_tmd.html) |
| D111 | > Remaining Income | Operating subsidies; Variation in production; Capitalized production; Other incomes; Obtained interest and similar income[^10] | VF18514 | [Formula in POC](#d111---formula-in-poc) | [Report - D111](./aux_files/technical_reports/variable_report/Contas/D111_tmd.html) |
| D005 | > > Operating subsidies | | VF16136 | [Formula in POC](#d005---formula-in-poc) | [Report - D005](./aux_files/technical_reports/variable_report/Contas/D005_tmd.html) |
| D006 | > > Variation in production | | VF16137 | [Formula in POC](#d006---formula-in-poc) | [Report - D006](./aux_files/technical_reports/variable_report/Contas/D006_tmd.html) |
| D007 | > > Capitalized production | | VF16138 | [Formula in POC](#d007---formula-in-poc) | [Report - D007](./aux_files/technical_reports/variable_report/Contas/D007_tmd.html) |
| DL043 |	Supplementary income | | VF15650 | [Formula in POC](#dl043---formula-in-poc) | [Report - DL043](./aux_files/technical_reports/variable_report/Contas/DL043_tmd.html) |
| D013 | Other incomes - Income from financial assets | | VF16144 | [Formula in POC](#d013---formula-in-poc) | [Report - D013](./aux_files/technical_reports/variable_report/Contas/D013_tmd.html) |
| D062 | **Total Expenses** | Costs of goods sold and material consumed; Supplies and external services; Employee expenses; Remaining expenses; Expenses/reversals of depreciations and amortizations; Interest expenses; Income tax | VF16193 | [Formula in POC](#d062---formula-in-poc) | [Report - D062](./aux_files/technical_reports/variable_report/Contas/D062_tmd.html) |
| D025 | > Costs of goods sold and material consumed | |VF16156 | [Formula in POC](#d025---formula-in-poc) | [Report - D025](./aux_files/technical_reports/variable_report/Contas/D025_tmd.html) |
| D026 | > Supplies and external services | | VF16157 | [Formula in POC](#d026---formula-in-poc) | [Report - D026](./aux_files/technical_reports/variable_report/Contas/D026_tmd.html) |
| D029 | > Employee expenses | Salaries; Social security expenses; Other employee expenses | VF16160 | [Formula in POC](#d029---formula-in-poc) | [Report - D029](./aux_files/technical_reports/variable_report/Contas/D029_tmd.html) |
| D030 | > > Salaries | Salaries of Corporate Bodies; Salaries of employees | VF16161 | [Formula in POC](#d030---formula-in-poc) | [Report - D030](./aux_files/technical_reports/variable_report/Contas/D030_tmd.html) |
| DL011 | > > > Salaries of corporate bodies | | VF15555 | [Formula in POC](#dl011---formula-in-poc) | [Report - DL011](./aux_files/technical_reports/variable_report/Contas/DL011_tmd.html) |
| DL012 | > > > Salaries of employees | | VF15557 | [Formula in POC](#dl012---formula-in-poc) | [Report - DL012](./aux_files/technical_reports/variable_report/Contas/DL012_tmd.html) |
| DL045 | > > Employee expenses - Other, except salaries | Social security expenses; Insurance schemes for accidents at work and occupational diseases; Expenses with social actions; Post-employment benefits; Indemnities; Other employee expenses | VF15554 - VF16161 | [Formula in POC](#dl045---formula-in-poc) | [Report - DL045](./aux_files/technical_reports/variable_report/Contas/DL045_tmd.html) |
| DL013 | > > > Social security expenses | | VF15565 | [Formula in POC](#dl013---formula-in-poc) | [Report - DL013](./aux_files/technical_reports/variable_report/Contas/DL013_tmd.html) |
| DL014	| > > > Insurance schemes for accidents at work and occupational diseases | | VF15566 | [Formula in POC](#dl014---formula-in-poc) | [Report - DL014](./aux_files/technical_reports/variable_report/Contas/DL014_tmd.html) |
| D108 | > Remaining expenses | Impairment (losses/reversals) and changes (gains/losses) in fair value; Provisions (increases/decreases); Other expenses | VF16572 | [Formula in POC](#d108---formula-in-poc) | [Report - D108](./aux_files/technical_reports/variable_report/Contas/D108_tmd.html) |
| D041 | > Expenses/reversals of depreciations and amortizations | | VF16172 | [Formula in POC](#d041---formula-in-poc) | [Report - D041](./aux_files/technical_reports/variable_report/Contas/D041_tmd.html) |
| D053 | > Interest expenses | | VF16184 | [Formula in POC](#d053---formula-in-poc) | [Report - D053](./aux_files/technical_reports/variable_report/Contas/D053_tmd.html) |
| D060 | > Income tax | | VF16191 | [Formula in POC](#d060---formula-in-poc) | [Report - D060](./aux_files/technical_reports/variable_report/Contas/D060_tmd.html) |
| D112 | Impairment losses, changes in fair value and other expenses and losses in fin. invest. and fin. instrum. | Impairment (losses/reversals) and changes (gains/losses) in fair value in financial instruments and investments; Other expenses - expenses in financial investments and other financing expenses | VF18515 | [Formula in POC](#d112---formula-in-poc) | [Report - D112](./aux_files/technical_reports/variable_report/Contas/D112_tmd.html) |
| D082 | **Operating net income** | (Turnover; Remaining income (excepting Obtained interest and similar income) [^9]; Impairment losses, changes in fair value and other expenses and losses in fin. invest. and fin. instrum.) - (Income from financial assets; Costs of goods sold and material consumed, Supplies and external services, Employee expenses and Remaining expenses) | VF16213 | [Formula in POC](#d082---formula-in-poc) | [Report - D082](./aux_files/technical_reports/variable_report/Contas/D082_tmd.html) |
| D084 | **Earnings before Interest, Taxes, Depreciation and Amortization - EBITDA** | (Turnover; Remaining income (excepting Obtained interest and similar income) [^10]) - (Costs of goods sold and material consumed; Supplies and external services; Employee expenses; Remaining expenses) | VF16215 |  [Formula in POC](#d084---formula-in-poc) | [Report - D084](./aux_files/technical_reports/variable_report/Contas/D084_tmd.html) |
| D085 | **Earning before Interest and Tax - EBIT** | (Turnover; Remaining income (excepting Obtained interest and similar income) [^10]) - (Costs of goods sold and material consumed; Supplies and external services; Employee expenses; Remaining expenses; Expenses/reversals of depreciations and amortizations) | VF16216 | [Formula in POC](#d085---formula-in-poc) | [Report - D085](./aux_files/technical_reports/variable_report/Contas/D085_tmd.html) |
| D086 | **Earnings before Tax - EBT** | (Turnover; Operating subsidies; Variation in production; Capitalized production; Other income; Interest, dividends and other similar income) - (Costs of goods sold and material consumed; Supplies and external services; Employee expenses; Impairment, provisions, Losses/reversals of depreciations and amortizations; Other expenses; Financial expenses and losses)[^11] | VF16217 | [Formula in POC](#d086---formula-in-poc) | [Report - D086](./aux_files/technical_reports/variable_report/Contas/D086_tmd.html) |
| D087 | **Net income** | Total Income - Total Expenses [^12] | VF16218 | [Formula in POC](#d087---formula-in-poc) | [Report - D087](./aux_files/technical_reports/variable_report/Contas/D087_tmd.html) |
| DL002 | Other expenses - Cash discounts granted | | VF15843 | [Formula in POC](#dl002---formula-in-poc) | [Report - DL002](./aux_files/technical_reports/variable_report/Contas/DL002_tmd.html) |
| DL005 | Other expenses - Other - Donations | | VF15859 | [Formula in POC](#dl005---formula-in-poc) | [Report - DL005](./aux_files/technical_reports/variable_report/Contas/DL005_tmd.html) |
| DL047 | Indirect taxes | Indirect Taxes; Fees [^13] | VF15841 + VF15842 | [Formula in POC](#dl047---formula-in-poc) | [Report - DL047](./aux_files/technical_reports/variable_report/Contas/DL047_tmd.html) |


[^9]: The item "Obtained interest and similar income" has no correspondence in the POC accounting system.

[^10]: Obtained interest and similar income has to be subtracted to Remaining Income to make it compatible with the POC formula.

[^11]: In SNC, some components of EBT are different from the ones used to compute EBIT.

[^12]: This variable is not computed using the total income and total expenses as given by D021 and D062, respectively. This formula corresponds to the difference between D020 - Total income and D061 - Total expenses.

[^13]: Indirect taxes (account 6812) and fees (account 6813) are reported separately in the *Sistema de Normalização Contabilística* (SNC, Accounting Standards System).

## C. Employment Information File

This file contains information on the number of employees and number of hours worked. Although the change in the accounting system did not have a direct impact on the report of this information, the denomination of the variables is different under both accounting regimes. Also, some variables are no longer required after 2010, such as the number of paid apprentices and home workers. The number of employees by gender only started being reported after 2010.
These variables are reported on Tables Q05-0507-Nota7 in the forms written according to POC and Q05A-05291-A in the forms written according to SNC.

### C1. Identifiers

`Firm identifier` (*tina*) – Unique identifier that enables tracking the legal entity over time. *tina* is the anonymized tax identification number.

`Reference year of the data` (*ano*) – Reference year of the data.

### C2. Number of employees

| Variable | Variable description | SNC Variable | Formula in POC | Variable Report |
| :----: | :-------------- | :-----: | :---------: |  :----------: |
| E001 | Number of (paid and unpaid) employees | VF15532	| VF03319 | [Report - E001](./aux_files/technical_reports/variable_report/Pessoal/E001_tmd.html)
| E002 | Number of paid employees | VF15534 | VF03321 | [Report - E002](./aux_files/technical_reports/variable_report/Pessoal/E002_tmd.html)
| E003 | Number of unpaid employees | VF15536 | VF04902 | [Report - E003](./aux_files/technical_reports/variable_report/Pessoal/E003_tmd.html)
| E004 | Number of (paid and unpaid) full-time employees| VF15538 | VF03320 | [Report - E004](./aux_files/technical_reports/variable_report/Pessoal/E004_tmd.html)
| E005 | Number of paid full-time employees | VF15540 | VF04903 | [Report - E005](./aux_files/technical_reports/variable_report/Pessoal/E005_tmd.html)
| E006 | Number of (paid and unpaid) part-time employees | VF15542 | VF04904 | [Report - E006](./aux_files/technical_reports/variable_report/Pessoal/E006_tmd.html)
| E007 | Number of paid part-time employees | VF15544 |	VF03324 | [Report - E007](./aux_files/technical_reports/variable_report/Pessoal/E007_tmd.html)
| E008 | Number of employees allocated to research and development | VF15550	| VF03326 | [Report - E008](./aux_files/technical_reports/variable_report/Pessoal/E008_tmd.html)
| E009 | Service providers | VF15551 | VF03325 | [Report - E009](./aux_files/technical_reports/variable_report/Pessoal/E009_tmd.html)
| E010 | Temporary Agency Employment | VF15553 | VF03327 | [Report - E010](./aux_files/technical_reports/variable_report/Pessoal/E010_tmd.html)

### C3. Number of hours of work

| Variable | Variable description | SNC Variable | Formula in POC | Variable Report |
| :----: | :-------------- | :-----: | :---------: |  :----------: |
| E011 | Number of hours worked by paid and unpaid employees | VF15533 | VF03328 | [Report - E011](./aux_files/technical_reports/variable_report/Pessoal/E011_tmd.html)
| E012 | Number of hours worked by paid employees | VF15535	| VF03330 | [Report - E012](./aux_files/technical_reports/variable_report/Pessoal/E012_tmd.html)
| E013 | Number of hours worked by unpaid employees | VF15537 | VF04905 | [Report - E013](./aux_files/technical_reports/variable_report/Pessoal/E013_tmd.html)
| E014 | Number of hours worked by paid and unpaid full-time employees | VF15539 | VF03329 | [Report - E014](./aux_files/technical_reports/variable_report/Pessoal/E014_tmd.html)
| E015 | Number of hours worked by paid full-time employees | VF15541 | VF04906 | [Report - E015](./aux_files/technical_reports/variable_report/Pessoal/E015_tmd.html)
| E016 | Number of hours worked by paid and unpaid part-time employees | VF15543 | VF04907 | [Report - E016](./aux_files/technical_reports/variable_report/Pessoal/E016_tmd.html)
| E017 | Number of hours worked by paid part-time employees | VF15545 | VF03331 | [Report - E017](./aux_files/technical_reports/variable_report/Pessoal/E017_tmd.html)
| E018 | Number of hours worked by service providers | VF15552 | VF03332 | [Report - E018](./aux_files/technical_reports/variable_report/Pessoal/E018_tmd.html)

## D. Trade information per market file

According to the forms written according to POC and respective filling instructions (Q0544-Nota44), some variables are reported in net terms. These variables were reported in a different table and have new denominations in the new accounting system (Q05-A-05302-A). However, there is a direct correspondence between the POC and SNC variables.

### D1. Identifiers

`Firm identifier` (*tina*) – Unique identifier that enables tracking the legal entity over time. *tina* is the anonymized tax identification number.

`Reference year of the data` (*ano*) – Reference year of the data.

### D2. Variables available

| Variable | Variable description | SNC Variable | Formula in POC | Variable Report |
| :----: | :-------------- | :-----: | :---------: |  :----------: |
| MG001 | Total Sales - Internal Market	| VF15619 | VF03949 | [Report - MG001](./aux_files/technical_reports/variable_report/MG/MG001_tmd.html) |
| MG002	| Total Services - Internal Market | VF15623 | VF03950 | [Report - MG002](./aux_files/technical_reports/variable_report/MG/MG002_tmd.html) |
| MG003	| Total Purchases - Internal Market	| VF15627 |	VF03951 | [Report - MG003](./aux_files/technical_reports/variable_report/MG/MG003_tmd.html) |
| MG004	| Total Sales - EU-Market | VF15620 | VF03953 | [Report - MG004](./aux_files/technical_reports/variable_report/MG/MG004_tmd.html) |
| MG005	| Total Services - EU-Market | VF15624 | VF03954 | [Report - MG005](./aux_files/technical_reports/variable_report/MG/MG005_tmd.html) |
| MG006	| Total Purchases - EU-Market | VF15628 | VF03955 | [Report - MG006](./aux_files/technical_reports/variable_report/MG/MG006_tmd.html) |
| MG007	| Total Sales - Extra EU-Market | VF15621 |	VF03957 | [Report - MG007](./aux_files/technical_reports/variable_report/MG/MG007_tmd.html) |
| MG008	| Total Services - Extra EU-Market | VF15625 | VF03958 | [Report - MG008](./aux_files/technical_reports/variable_report/MG/MG008_tmd.html) |
| MG009 | Total Purchases - Extra EU-Market | VF15629 | VF03959 | [Report - MG009](./aux_files/technical_reports/variable_report/MG/MG009_tmd.html) |
| MG010	| Total Sales | VF15622 | VF03961 | [Report - MG010](./aux_files/technical_reports/variable_report/MG/MG010_tmd.html) |
| MG011	| Total Services | VF15626 | VF05195 | [Report - MG011](./aux_files/technical_reports/variable_report/MG/MG011_tmd.html) |
| MG012	| Total Purchases | VF15630 | VF03962 | [Report - MG012](./aux_files/technical_reports/variable_report/MG/MG012_tmd.html) |

## E. Corporate Actions File

This file contains information on firm actions that occurred during the fiscal period altering the structure of the firm and affecting the comparability of the economic and financial information over time. The variables below are computed by the Statistics Department of *Banco de Portugal* and, therefore, are not affected by the change in the accounting system. The data has a significant but not exhaustive coverage of the corporate actions that have an impact on the structure of the non-financial corporations included in CBHP.

### E1. Identifiers

`Firm identifier` (*tina_origem*, *tina_destino*) – firm identification codes that enable identifying the firm of origin and the firm of destination of the corporate action.

*tina_origem* - firm of origin's anonymized tax identification number,

*tina_destino* - firm of destination's anonymized tax identification number.

`Reference year of the data` (*ano*) – Reference year of the data.

`Number of order of the corporate action` (*numordem*): Corporate action's number of order.

### E2. Information on the Corporate Action

`Type of corporate action` (*tipoacont*) - this variable reports the type of corporate action:

| Code | Designation |
| :----: | :----------- |
| 10 | Merge |
| 20 | Split |
| 30 | Activity Interruption by non-seasonal companies (>3 months, consecutive or not) |
| 62 | Dissolution of a significant part of productive assets without split |
| 67 | Other corporate actions |
| 70 | Disposal of a significant part of productive assets |
| 71 | Acquisition of a significant part of productive assets |
| 72 | Transfer of a significant part of productive assets |
| 78 | Change of economic activity with the creation of a new firm |
| 79 | Change of economic activity without the creation of a new firm |

Some relevant definitions are available in subsection [E3. Relevant Definitions](#e3.-relevant-definitions)

`Number of months of activity interruption` (*mesesparagem*) - number of months the firm interrupted its activity. This variable is only filled in when the type of corporate action corresponds to an activity interruption (*tipoacont*=30).



`Effect on data comparability` (*efeitopessoal*, *efeitobalanco*, *efeitodemresult*, *efeitocontas*) - set of dummy variables stating whether the corporate action has an effect on data comparability. By default, it is considered that the corporate action has an effect on data comparability if the relative annual change of the relevant variable (Number of Paid and Unpaid Employees, Total Assets or Turnover) exceeds 10%. After the quality control takes place, however, the action may be considered to have or not an effect on data comparability according to the analysis of the firm's information.

*efeitopessoal* - dummy variable taking value one ("Yes") if the corporate action has an impact on the Number of Paid and Unpaid Employees.[^14]

*efeitobalanco* - dummy variable taking value one ("Yes") if the corporate action has an impact on Total Assets.

*efeitodemresult* - dummy variable taking value one ("Yes") if the corporate action has an impact on Turnover.

*efeitocontas* - dummy variable taking value one ("Yes") if the corporate action has an impact on the overall economic and financial statements.


[^14]: Please note that the variable Number of Paid and Unpaid Employees is only reported in IES from 2006 onwards. Therefore, it is not possible to assess the effects of the corporate actions reported in 2006 on employment information (*efeitopessoal*). For this reason, the variable *efeitocontas* may also be understated in 2006.

### E3. Relevant definitions

**Merge**- This corporate action occurs if two or more companies combine into a newly created company or an existing one. In this last case, the firm is simultaneously the Firm of Origin and the Firm of Destination.

**Split** – This corporate action occurs when a company divides its activity into two or more existing and/or newly created companies. If the firm splitting its activity stay in business then this firm is simultaneously the Firm of Origin and the Firm of Destination.

**Change of Economic Activity (with/without the creation of a new firm)** - structural change on the firm affecting the comparability of the information over time. For example, a firm being assigned a new Tax Identification Number due to changes in firm's legal form, sector of activity or institutional sector.

**Dissolution of a significant part of productive assets without split** - significant diminution in the economic activity of the firm that is not explained by the transfer of productive assets to an existing or newly created firm.

## F. Economic and Financial indicators

The Economic and Financial Indicators are calculated based on the information available in the Economic and Financial Information file. For an overview of the formulas used to compute these variables check the auxiliary file [indicadores_formula.html](./aux_files/variables_description/indicadores_formula.html).
A Stata ado file ([cbhp_addindic.ado](https://github.com/BPLIM/Tools/tree/master/ados/CBHP/cbhp_addindic)) and an R script ([cbhp_addindic.R](https://github.com/BPLIM/Tools/tree/master/Rscripts/CBHP/cbhp_addindic)) are provided by BPLIM upon request to create the variables listed below. These variables follow the naming convention Rxxx.


| Variable Name | Variable Description |
| ------ | ------- |
| R001 | Current ratio |
| R002 | Quick ratio |
| R003 | Capital ratio |
| R006 | Assets to equity ratio |
| R007 | Solvency ratio |
| R009 |	Non-current assets coverage ratio |
| R023 |	Financial Cost Effect |
| R034 |	Return on sales |
| R036 |	Return on assets |
| R040 | EBITDA over Turnover |
| R041 | Degree of combined leverage |
| R050 | Asset turnover (times) |
| R056 | Coefficient Fixed non-financial assets over employee expenses |
| R150 | Asset turnover ratio |
| R152 | Profit or loss of the year before taxes (EBT) / Equity |
| R155 | Profit or loss of the year before taxes (EBT) / Net turnover |
| R156 | Equity / Total assets |
| R157 | Trade payables / Total assets |
| R158 | Total income / Net turnover |
| R159 | Total expenses / Net turnover |
| R160 | Financial fixed assets / Total assets |
| R161 | Trade receivables / Total assets |

# Basic Descriptive Statistics

Table 2- Firm flows (as of June 2024 extraction)

```{stata}
*| output: false
*| echo: false
set linesize 200
local extraction="JUN24"
local ref="2024_06"
local startyr="2006"
local finyear="2022"
local version="V01"
local file1="YFRM"
```

```{stata}
*| output: true
*| echo: false
quietly use "../../Output/Data/Firms/CBHP_I_`file1'_`startyr'`finyear'_`extraction'_ROSTO_`version'.dta", clear
panelstat nipc ano, gaps pattern demog
```

# Auxiliary Files

For summary statistics, a codebook and description of each dataset please check the following auxiliary files [^32]:

| File | Metafiles | Summary Statistics | Report |
| :--- | :---: | :---: | :---: |
| General Information | [meta_ROSTO](./aux_files/metafiles/CBHP_meta_YFRM_JUN24_ROSTO_V01.xlsx) | [stat_ROSTO](./aux_files/descriptive_statistics/ROSTO/CBHP_metastats_YFRM_JUN24_ROSTO_V01.xlsx) |
| Economic and Financial Information | [meta_CONTAS](./aux_files/metafiles/CBHP_meta_YFRM_JUN24_CONTAS_V01.xlsx) | [stat_CONTAS](./aux_files/descriptive_statistics/CONTAS/CBHP_metastats_YFRM_JUN24_CONTAS_V01.xlsx) | [rprt_CONTAS](./aux_files/technical_reports/report_JUN24_CONTAS20062022.html) |
| Employment Information | [meta_PESSOAL](./aux_files/metafiles/CBHP_meta_YFRM_JUN24_PESSOAL_V01.xlsx) | [stat_PESSOAL](./aux_files/descriptive_statistics/PESSOAL/CBHP_metastats_YFRM_JUN24_PESSOAL_V01.xlsx) | [rprt_PESSOAL](./aux_files/technical_reports/report_JUN24_PESSOAL20062022_VS_CONTAS20062022.html) |
| Trade Information per Market | [meta_MG](./aux_files/metafiles/CBHP_meta_YFRM_JUN24_MG_V01.xlsx) | [stat_MG](./aux_files/descriptive_statistics/MG/CBHP_metastats_YFRM_JUN24_MG_V01.xlsx) | [rprt_MG](./aux_files/technical_reports/report_JUN24_MG20062022_VS_CONTAS20062022.html) |
| Corporate Actions | [meta_AMARC](./aux_files/metafiles/CBHP_meta_YFRM_JUN24_AMARC_V01.xlsx) | [stat_AMARC](./aux_files/descriptive_statistics/AMARC/CBHP_metastats_YFRM_JUN24_AMARC_V01.xlsx) | |

[^32]: The summary statistics are available on BPLIM's servers.

# Frequently Asked Questions

The most frequently asked questions can be found [here](./aux_files/faq/CBHP_faq.html).
If you have a question that is not covered in this manual, please send an email to bplim@bportugal.pt.

# Citation of this Dataset

Banco de Portugal Microdata Research Laboratory - BPLIM (2024): Central Balance Sheet Harmonized Panel. Extraction: June 2024. Version: V1. Banco de Portugal. Dataset. https://doi.org/10.17900/CB.CBHP.Jun2024.V1

<br>
<br>

To cite this dataset you can use the package biblatex with the following BibTeX entry:

```{stata}
*| eval: false
*| echo: true
*| code-fold: false
@dataset{CB.CBHP.Jun2024.V1,
author = {{Banco de Portugal Microdata Research Laboratory - BPLIM}},
publisher = {Banco de Portugal},
title = {{C}entral {B}alance {S}heet {H}armonized {P}anel},
year = {2024},
version = {{ V1, Extraction June 2024}},
doi = {10.17900/CB.CBHP.Jun2024.V1},
url = {https://doi.org/10.17900/CB.CBHP.Jun2024.V1}
}
```

# References

Banco de Portugal (2014). Quadros do Setor e Quadros da Empresa e do Setor- Notas Metodológicas Série Longa 1995-2013. Estudos da Central de Balanços. Lisboa.

Banco de Portugal (2019). Quadros do setor e quadros da empresa e do setor. Estudos da Central de Balanços. Lisboa.

# Appendix
## Balance Sheet Variables

## B001 - Formula in POC
**Total Assets**

| Variable name	| Variable description | Coefficient |
| :----: | :---------- | :---: |
| [B004](#b004---formula-in-poc) | Total non-current assets | 1 |
| [B029](#b029---formula-in-poc) | Total current assets | 1 |

[return](#assets)

------------------------------------------------------

## B004 - Formula in POC
**Total non-current assets**

| Variable name	| Variable description | Coefficient |
| :----: | :------------- | :---: |
| [B005](#b005---formula-in-poc) | Fixed tangible assets and intangible assets | 1 |
| [B025](#b025---formula-in-poc) | Financial investments	| 1 |
| [B158](#b158---formula-in-poc) | Non-current assets - Remaining non-current assets | 1 |

[return](#assets)

-----------------------------------------------------

## B005 - Formula in POC
**Fixed Tangible Assets and Intangible Assets**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03088	| Intangible assets | Q04-A0207-3-soma |	1 |
| VF03117	| Tangible fixed assets | Q04-A0218-3-soma |	1 |
| VF03587	| Investment in properties | Q05-0510-Nota10-A1489-9-soma | 1 |
| VF03642 | Amortizations and adjustments - Financial investments - Investment in properties | Q05-0510-Nota10-A1506-4-soma | -1 |

[return](#assets)

------------------------------------------------------

## B012 - Formula in POC
**Fixed Tangible Assets**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03117	| Tangible fixed assets | Q04-A0218-3-soma |	1 |
| VF03587	| Investment in properties | Q05-0510-Nota10-A1489-9-soma | 1 |
| VF03642 | Amortizations and adjustments - Financial investments - Investment in properties | Q05-0510-Nota10-A1506-4-soma | -1 |

[return](#assets)

------------------------------------------------------

## B025 - Formula in POC
**Financial Investments**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03140	| Financial investments	| Q04-A0227-3-soma | 1 |
| VF03587 |	Investment in properties | Q05-0510-Nota10-A1489-9-soma | -1 |
| VF03642 | Amortizations and adjustments - Financial investments - Investment in properties | Q05-0510-Nota10-A1506-4-soma | 1 |

[return](#assets)

-----------------------------------------------------

## B029 - Formula in POC
**Total current assets**

| Variable name	| Variable description | Coefficient |
| :----: | :---------- | :---: |
| [B032](#b032---formula-in-poc) | Current assets - Inventories and biological assets | 1 |
| [B041](#b041---formula-in-poc) | Current assets - Customers	| 1 |
| [B159](#b159---formula-in-poc) | Current assets - Remaining current assets | 1 |
| [B049](#b049---formula-in-poc) | Current assets - Cash and bank deposits | 1 |

[return](#assets)

-----------------------------------------------------

## B032 - Formula in POC
**Current Assets - Inventories and Biological Assets**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03159 | Current assets - Inventories | Q04-A0234-3-soma | 1 |

[return](#assets)

-----------------------------------------------------

## B041 - Formula in POC
**Current Assets - Customers**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03162	| Assets - Medium and long term debt - Customers (current account) | Q04-A0235-3 | 1 |
| VF03165	| Assets - Medium and long term debt - Customers - Notes receivable | Q04-A0236-3 |	1 |
| VF03168	| Assets - Medium and long term debt - Customers - Doubtful debtors	| Q04-A0237-3 | 1 |
| VF03194	| Assets - Short term debt - Customers (current account)	| Q04-A0247-3 | 1 |
| VF03197	| Assets - Short term debt - Customers - Notes receivable | Q04-A0248-3 | 1 |
| VF03200	| Assets - Short term debt - Customers - Doubtful debtors | Q04-A0249-3 | 1 |
| VF03289	| Liabilities - Medium and long term debt - Advances from customers | Q04-A0308-1 | -1 |
| VF03307	| Liabilities - Short term debt - Advances from customers	| Q04-A0326-1 | -1 |

[return](#assets)

------------------------------------------------------

## B042 - Formula in POC
**Current assets - State and other public entities**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03182 |	Assets - Medium and long term debt - State and other public entities (Net Assets) | Q04-A0243-3 | 1 |
| VF03214 | Assets - Short term debt - State and other public entities (Net Assets) | Q04-A0255-3 | 1 |

[return](#assets)

------------------------------------------------------

## B049 - Formula in POC
**Current Assets - Cash and Bank Deposits**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF05131 | Assets - Cash and bank deposits |Q04-A0268-3-soma | 1 |

[return](#assets)

------------------------------------------------------

## B060 - Formula in POC
**Equity and Liabilities**

| Variable name	| Variable description | Coefficient |
| :----: | :---------- | :---: |
| [B061](#b061---formula-in-poc) | Equity | 1 |
| [B080](#b080---formula-in-poc) | Liabilities |	1 |

[return](#equity)

---------------------------------------------------

## B061 - Formula in POC
**Equity**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03258	| Equity - Capital	| Q04-A0277-1 | 1 |
| VF03188	| Assets - Medium and long term debt - Subscribed capital	| Q04-A0245-3 | -1 |
| VF03220	| Assets - Short term debt - Subscribed capital | Q04-A0257-3 | -1 |
| VF03261	| Equity - Supplementary capital	| Q04-A0280-1 | 1 |
| VF03265	| Equity - Reserves- Legal reserves | Q04-A0284-1 | 1 |
| VF03266	| Equity - Reserves- Statutory reserves | Q04-A0285-1 | 1 |
| VF03267	| Equity - Reserves- Contractual reserves | Q04-A0286-1 | 1 |
| VF03268	| Equity - Reserves- Other reserves | Q04-A0287-1 | 1 |
| VF03269	| Equity - Retained earnings | Q04-A0288-1 | 1 |
| VF03259	| Equity - Own shares- Nominal value |	Q04-A0278-1 | 1 |
| VF03260	| Equity - Own shares- Discounts and Premiums | Q04-A0279-1 | 1 |
| VF03262	| Equity - Share Premiums | Q04-A0281-1 | 1 |
| VF03263	| Equity - Adjustments to investments in group and associated companies | Q04-A0282-1 | 1 |
| VF03264	| Equity - Revaluation reserves |	Q04-A0283-1 | 1 |
| VF04061	| Split of account Accruals and deferrals - Investment subsidies | Q06-A0666 | 1 |
| VF03270	| Equity - Net income | Q04-A0289-1 | 1 |
| VF03271	| Equity - Interim dividends |	Q04-A0290-1 | 1 |

[return](#equity)

---------------------------

## B074 - Formula in POC
**Interim dividends**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03271 | Equity - Interim dividends | Q04-A0290-1 | 1 |


[return](#equity)

------------------------------------------------------

## B080 - Formula in POC
**Liabilities - Total**

| Variable name	| Variable description | Coefficient |
| :----: | :---------- | :---: |
| [B081](#b081---formula-in-poc) | Non-current liabilities	| 1 |
| [B089](#b089---formula-in-poc) | Current liabilities	| 1 |

[return](#liabilities)

-----------------------------------

## B081 - Formula in POC
**Non-current liabilities- Total**

| Variable name	| Variable description | Coefficient |
| :----: | :---------- | :---: |
| [B085](#b085---formula-in-poc) | Non-current liabilities - Obtained funding	| 1 |
| [B160](#b160---formula-in-poc) | Non-current liabilities - Remaining non-current liabilities | 1 |
| VF03273	| Provisions- Provisions for pension liabilities (Q04-A0292-1) |	1 |

[return](#liabilities)

-----------------------------------------------------

## B085 - Formula in POC
**Non-current liabilities - Obtained Funding**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03277	| Liabilities - Medium and long term debt - Bond loans: convertible	| Q04-A0296-1 | 1 |
| VF03278	| Liabilities - Medium and long term debt - Bond loans: non-convertible	| Q04-A0297-1 | 1 |
| VF03279	| Liabilities - Medium and long term debt - Participating loans	| Q04-A0298-1 | 1 |
| VF03280	| Liabilities - Medium and long term debt - Loans from credit institutions	| Q04-A0299-1 | 1 |
| VF03286	| Liabilities - Medium and long term debt - Group companies	| Q04-A0305-1 | 1 |
| VF03287	| Liabilities - Medium and long term debt - Affiliate and participating companies	| Q04-A0306-1 | 1 |
| VF03288	| Liabilities - Medium and long term debt - Other shareholders (partners)	| Q04-A0307-1 | 1 |
| VF03290	| Liabilities - Medium and long term debt - Other loans	| Q04-A0309-1 | 1 |

[return](#liabilities)

----------------------------------------------------

## B089 - Formula in POC
**Current liabilities - Total**

| Variable name	| Variable description | Coefficient |
| :----: | :---------- | :---: |
| [B093](#b093---formula-in-poc) | Current liabilities - Suppliers	| 1 |
| [B096](#b096---formula-in-poc) | Current liabilities - Obtained funding | 1 |
| [B161](#b161---formula-in-poc) | Current liabilities - Remaining current liabilities | 1 |

[return](#liabilities)

------------------------------------------------------

## B093 - Formula in POC
**Current liabilities - Suppliers**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF05125	| Assets - Medium and long term debt - Advances to suppliers | Q04-A0241-3 | -1 |
| VF05127	| Assets - Short term debt - Advances to suppliers | Q04-A0253-3 | -1 |
| VF03282	| Liabilities - Medium and long term debt - Suppliers (current account)	| Q04-A0301-1 | 1 |
| VF03283	| Liabilities - Medium and long term debt - Suppliers - Trade accounts payable: unchecked invoices | Q04-A0302-1 | 1 |
| VF03284	| Liabilities - Medium and long term debt - Suppliers - Notes payable |	Q04-A0303-1 | 1 |
| VF03300	| Liabilities - Short term debt - Suppliers (current account) | Q04-A0319-1 | 1 |
| VF03301	| Liabilities - Short term debt - Suppliers - Trade accounts payable: unchecked invoices | Q04-A0320-1 | 1 |
| VF03302	| Liabilities - Short term debt - Suppliers - Notes payable	| Q04-A0321-1 | 1 |

[return](#liabilities)

------------------------------------------------------

## B094 - Formula in POC
**Current liabilities - State and other public entities**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03310 | Liabilities - Short term debt - State and other public sector institutions | Q04-A0329-1 | 1 |
| VF03292 | Liabilities - Medium and long term debt - State and other public sector institutions | Q04-A0311-1 | 1 |

[return](#liabilities)

------------------------------------------------------

## B096 - Formula in POC
**Current liabilities - Obtained funding**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03295	| Liabilities - Short term debt - Bond loans: convertible	| Q04-A0314-1 | 1 |
| VF03296	| Liabilities - Short term debt - Bond loans: non-convertible	| Q04-A0315-1 | 1 |
| VF03297	| Liabilities - Short term debt - Participating loans	| Q04-A0316-1 | 1 |
| VF03298	| Liabilities- Short term debt - Loans from credit institutions | Q04-A0317-1 | 1 |
| VF03304	| Liabilities - Short term debt - Group companies	| Q04-A0323-1 | 1 |
| VF03305	| Liabilities - Short term debt - Affiliate and participating companies	| Q04-A0324-1 | 1 |
| VF03306	| Liabilities - Short term debt - Other shareholders (partners) | Q04-A0325-1 | 1 |
| VF03308	| Liabilities - Short term debt - Other loans	| Q04-A0327-1 | 1 |

[return](#liabilities)

------------------------------------------------------

## B143 - Formula in POC
**Subscribed capital**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03258 | Equity - Capital | Q04-A0277-1 | 1 |


[return](#equity)

------------------------------------------------------

## B158 - Formula in POC
**Non-current assets - Remaining non-current assets**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03171	| Assets - Medium and long term debt - Group companies | Q04-A0238-3 | 1 |
| VF03174	| Assets - Medium and long term debt - Affiliate and participating companies | Q04-A0239-3 | 1 |
| VF03177	| Assets - Medium and long term debt - Other shareholders (partners) | Q04-A0240-3 | 1 |
| VF05135	| Accruals and deferrals - Deferred tax assets | Q04-A0272-3 | 1 |

[return](#assets)

-----------------------------------------------------

## B159 - Formula in POC
**Current assets - Remaining current assets**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03182	| Current assets - Medium and long term debt - State and other public sector institutions | Q04-A0243-3 | 1 |
| VF03214	| Assets - Short term debt - State and other public sector institutions | Q04-A0255-3 | 1 |
| VF05126	| Assets - Medium and long term debt - Advances to fixed assets suppliers | Q04-A0242-3 | 1 |
| VF03185	| Assets - Medium and long term debt - Other debtors | Q04-A0244-3 | 1 |
| VF05128	| Assets - Short term debt - Advances to fixed assets suppliers | Q04-A0254-3 | 1 |
| VF03217	| Assets - Short term debt - Other debtors | Q04-A0256-3 | 1 |
| VF03244	| Assets - negotiable securities | Q04-A0265-3-soma | 1 |
| VF05132	| Accruals and deferrals - Accrued profits | Q04-A0269-3 | 1 |
| VF05134	| Accruals and Deferrals- Deferred daily adjustments in futures contracts | Q04-A0271-3 | 1 |
| VF03203	| Assets - Short term debt - Group companies | Q04-A0250-3 | 1 |
| VF03206	| Assets - Short term debt - Affiliate and participating companies | Q04-A0251-3 |	1 |
| VF03209	| Assets - Short term debt - Other shareholders (partners) | Q04-A0252-3 | 1 |
| VF05133	| Accruals and deferrals - Deferred costs | Q04-A0270-3 |	1 |

[return](#assets)

------------------------------------------------------

## B160 - Formula in POC
**Non-current liabilities - Remaining non-current liabilities**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03273 | Liabilities - Provisions- Provisions for pension liabilities | Q04-A0292-1 | -1 |
| VF03276	| Liabilities - Provisions - Total | Q04-A0295-1-soma | 1 |
| VF03285	| Liabilities - Medium and long term debt - Fixed assets suppliers - notes payable | Q04-A0304-1 | 1 |
| VF03291	| Liabilities - Medium and long term debt - Fixed assets suppliers (current account) | Q04-A0310-1 | 1 |
| VF03293	| Liabilities - Medium and long term debt - Other creditors	| Q04-A0312-1 | 1 |
| VF03315	| Accruals and deferrals - Deferred tax liabilities	| Q04-A0334-1 | 1 |

[return](#liabilities)

-----------------------------------------------------

## B161 - Formula in POC
**Current liabilities - Remaining current liabilities**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03292	| Liabilities - Medium and long term debt - State and other public sector institutions | Q04-A0311-1 | 1 |
| VF03310	| Liabilities - Short term debt - State and other public sector institutions | Q04-A0329-1 | 1 |
| VF03303	| Liabilities - Short term debt - Fixed assets suppliers - Notes payable	| Q04-A0322-1 | 1 |
| VF03309	| Liabilities - Short term debt - Fixed assets suppliers (current account)	| Q04-A0328-1 | 1 |
| VF03311	| Liabilities - Short term debt - Other creditors	| Q04-A0330-1 | 1 |
| VF03313	| Accruals and deferrals - Accrued costs | Q04-A0332-1 | 1 |
| VF03281	| Liabilities - Medium and long term debt - Advances on sales | Q04-A0300-1 | 1 |
| VF03299	| Liabilities - Short Term advances on sales | Q04-A0318-1 | 1 |
| VF03314	| Accruals and deferrals - Deferred profits	| Q04-A0333-1 | 1 |
| VF04061 | Accruals and deferrals - Investment subsidies | Q06-A0666 | -1 |

[return](#liabilities)

-----------------------------------------------------

## BL005 - Formula in POC
**Legal reserves**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03265 | Equity - Reserves - Legal Reserves | Q04-A0284-1 | 1 |

[return](#equity)

-----------------------------------------------------

## BL007 - Formula in POC
**Retained earnings**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03269 | Equity - Retained earnings | Q04-A0288-1 | 1 |

[return](#equity)

------------------------------------------------------

## Profit and Loss Statement Variables
## D001 - Formula in POC
**Turnover**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03045	| Sales - goods	| Q03-A0124-1 | 1 |
| VF03046	| Sales - products | Q03-A0125-1 | 1 |
| VF03047	| Services	| Q03-A0126-1 | 1 |

[return](#b3.-profit-and-loss-statement-variables)

-----------------------------------------------

## D002 - Formula in POC
**Sales**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF05908 | Sales | [Q03-A0124-1]+[Q03-A0125-1] | 1 |

[return](#b3.-profit-and-loss-statement-variables)

-----------------------------------------------------

## D005 - Formula in POC
**Operating subsidies**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03052 | Operating subsidies | Q03-A0130-1 | 1 |

[return](#b3.-profit-and-loss-statement-variables)

-----------------------------------------------------

## D006 - Formula in POC
**Variation in production**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03049 | Variation in production | Q03-A0127-2 | 1 |

[return](#b3.-profit-and-loss-statement-variables)

------------------------------------------------------

## D007 - Formula in POC
**Capitalized production**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03050	| Capitalized production | Q03-A0128-2 | 1 |

[return](#b3.-profit-and-loss-statement-variables)

------------------------------------------------------

## D013 - Formula in POC
**Other incomes - Income from financial assets**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03972	| Revenues - Interests income | Q05-0545-Nota45-A1439-1 | 1 |
| VF05206	| Revenues - Gains in group and associated companies | Q05-0545-Nota45-A1440-1 | 1 |
| VF05207	| Revenues - Income from equity holdings | Q05-0545-Nota45-A1442-1 | 1 |
| VF03977	| Revenues - Reversals and other financial revenues | Q05-0545-Nota45-A1446-1 | 1 |
| VF04054	| Extraordinary revenues – Disposal of financial investments | Q06-A0659 | 1 |

[return](#b3.-profit-and-loss-statement-variables)

------------------------------------------------------

## D021 - Formula in POC
**Total income**

| Variable name	| Variable description | Coefficient |
| :----: | :---------- | :---: |
| [D001](#d001---formula-in-poc) | Turnover | 1 |
| [D111](#d111---formula-in-poc) | Remaining Income	| 1 |

[return](#b3.-profit-and-loss-statement-variables)

-----------------------------------------------------

## D025 - Formula in POC
**Costs of goods sold and material consumed**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03019 | Cost of goods sold and material consumed - Total | Q03-A0102-2 | 1 |

[return](#b3.-profit-and-loss-statement-variables)

-----------------------------------------------------

## D026 - Formula in POC
**Supplies and external services**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03020	| Supplies and external services | Q03-A0103-2 | 1 |

[return](#b3.-profit-and-loss-statement-variables)

-----------------------------------------------------

## D029 - Formula in POC
**Employee expenses**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03021	| Employee expenses - Salaries | Q03-A0104-1 | 1 |
| VF03022	| Employee expenses - Pensions | Q03-A0105-1 | 1 |
| VF03023	| Employee expenses - Others | Q03-A0106-1 | 1 |

[return](#b3.-profit-and-loss-statement-variables)

-----------------------------------------------------

## D030 - Formula in POC
**Employee expenses - Salaries**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03021	| Salaries | Q03-A0104-1 | 1 |

[return](#b3.-profit-and-loss-statement-variables)

------------------------------------------------------

## D041 - Formula in POC
**Expenses/reversals of depreciations and amortizations**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03025	| Depreciation of intangible and tangible fixed assets | Q03-A0107-1 | 1 |
| VF03965	| Costs - Amortizations of investment in properties | Q05-0545-Nota45-A1431-1 | 1 |

[return](#b3.-profit-and-loss-statement-variables)

-----------------------------------------------------

## D053 - Formula in POC
**Interest expenses**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03964 | Interests paid | Q05-0545-Nota45-A1429-1 | 1 |

[return](#b3.-profit-and-loss-statement-variables)

------------------------------------------------------

## D060 - Formula in POC
**Income tax**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03041 | Income tax | Q03-A0120-2 | 1 |

[return](#b3.-profit-and-loss-statement-variables)

-----------------------------------------------------

## D062 - Formula in POC
**Total expenses**

| Variable name	| Variable description | Coefficient |
| :----: | :---------- | :---: |
| [D025](#d025---formula-in-poc) | Costs of goods sold and material consumed | 1 |
| [D026](#d026---formula-in-poc) | Supplies and external services	| 1 |
| [D029](#d029---formula-in-poc) | Employee expenses | 1 |
| [D108](#d108---formula-in-poc) | Remaining expenses | 1 |
| [D041](#d041---formula-in-poc) | Expenses/reversals of depreciations and amortizations | 1 |
| [D053](#d053---formula-in-poc) | Interest expenses | 1 |
| [D060](#d060---formula-in-poc) | Income tax	| 1 |

[return](#b3.-profit-and-loss-statement-variables)

-----------------------------------------------------

## D082 - Formula in POC
**Operating net income**

| Variable name	| Variable description | Coefficient |
| :----: | :---------- | :---: |
| [D001](#d001---formula-in-poc) | Turnover	| 1 |
| [D111](#d111---formula-in-poc) | Remaining income	| 1 |
| [D112](#d112---formula-in-poc) | (Remaining expenses) of which: Impairment losses, changes in fair value and other expenses and losses in fin. invest. and fin. instrum. | 1 |
| [D013](#d013---formula-in-poc) | (Remaining income) of which: income from financial assets | -1 |
| [D025](#d025---formula-in-poc) | Costs of goods sold and material consumed | -1 |
| [D026](#d026---formula-in-poc) | Supplies and external services	| -1 |
| [D029](#d029---formula-in-poc) | Employee expenses | -1 |
| [D108](#d108---formula-in-poc) | Remaining expenses	| -1 |

[return](#b3.-profit-and-loss-statement-variables)

-----------------------------------------------------

## D084 - Formula in POC
**Earnings before interest, taxes, depreciation and amortization - EBITDA**

| Variable name	| Variable description | Coefficient |
| :----: | :---------- | :---: |
| [D001](#d001---formula-in-poc) | Turnover	| 1 |
| [D111](#d111---formula-in-poc) | Remaining Income | 1 |
| [D025](#d025---formula-in-poc) | Costs of goods sold and material consumed | -1 |
| [D026](#d026---formula-in-poc) | Supplies and external services	| -1 |
| [D029](#d029---formula-in-poc) | Employee expenses | -1 |
| [D108](#d108---formula-in-poc) | Remaining expenses | -1 |

[return](#b3.-profit-and-loss-statement-variables)

-----------------------------------------------------

## D085 - Formula in POC
**Earnings before interest and taxes - EBIT**

| Variable name	| Variable description | Coefficient |
| :----: | :---------- | :---: |
| [D084](#d084---formula-in-poc) | Earnings before Interest, Taxes, Depreciation and Amortization - EBITDA | 1 |
| [D041](#d041---formula-in-poc) | Expenses/reversals of depreciations and amortizations	| -1 |

[return](#b3.-profit-and-loss-statement-variables)

-----------------------------------------------------

## D086 - Formula in POC
**Earnings before taxes - EBT**

| Variable name	| Variable description | Coefficient |
| :----: | :---------- | :---: |
| [D085](#d085---formula-in-poc) | Earnings before Interest and Tax - EBIT | 1 |
| [D053](#d053---formula-in-poc) | Interest expenses | -1 |

[return](#b3.-profit-and-loss-statement-variables)

-----------------------------------------------------

## D087 - Formula in POC
**Net income**

| Variable name	| Variable description | Coefficient |
| :----: | :---------- | :---: |
| [D086](#d086---formula-in-poc) | Earnings before Tax - EBT | 1 |
| [D060](#d060---formula-in-poc) | Income tax	| -1 |

[return](#b3.-profit-and-loss-statement-variables)

------------------------------------------------------

## D108 - Formula in POC
**Remaining expenses**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03026 | Adjustments | Q03-A0108-1 | 1 |
| VF03034	| Depreciation and adjustments of financial fixed assets | Q03-A0114-1 | 1 |
| VF03055	| Reversals of amortizations and adjustments | Q03-A0132-1 | -1 |
| VF03965	| Costs - Amortizations of investment in properties | Q05-0545-Nota45-A1431-1 | -1 |
| VF03027	| Provisions | Q03-A0109-1 | 1 |
| VF03993	| Revenues - Provisions decreases | Q05-0546-Nota46-A1463-1 | -1 |
| VF03029	| Taxes |	Q03-A0110-1 | 1 |
| VF03030	| Other operating costs | Q03-A0111-1 | 1 |
| VF03033	| Losses in group and associated companies | Q03-A0113-2 | 1 |
| VF03035	| Interest expenses - relative to group companies | Q03-A0115-1 | 1 |
| VF03036	| Interest expenses - others |	Q03-A0116-1 | 1 |
| VF03039	| Extraordinary costs |	Q03-A0118-2 | 1 |
| VF03964	| Interests paid |	Q05-0545-Nota45-A1429-1 | -1 |

[return](#b3.-profit-and-loss-statement-variables)

----------------------------------------------------

## D111 - Formula in POC
**Remaining income**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03052 | Operating subsidies | Q03-A0130-1 | 1 |
| VF03049 | Variation in production | Q03-A0127-2 | 1 |
| VF03050	| Capitalized production | Q03-A0128-2 | 1 |
| VF03051	| Supplementary income | Q03-A0129-1 | 1 |
| VF03053	| Operating revenues | Q03-A0131-1 | 1 |
| VF03057	| Gains in group and associated companies | Q03-A0134-1 | 1 |
| VF03058	| Income from equity holdings | Q03-A0135-1 | 1 |
| VF03059	| Income from negotiable securities and other financial applications - relative to group companies | Q03-A0136-1 | 1 |
| VF03060	| Income from negotiable securities and other financial applications | Q03-A0137-1 | 1 |
| VF03061	| Interest Income and similar earnings- relative to group companies | Q03-A0138-1 | 1 |
| VF03062	| Interest Income and similar earnings - Others | Q03-A0139-1 | 1 |
| VF03065	| Extraordinary revenues | Q03-A0141-2 | 1 |
| VF03993	| Revenues - Decreases in Provisions | Q05-0546-Nota46-A1463-1 | -1 |

[return](#b3.-profit-and-loss-statement-variables)

-----------------------------------------------------

## D112 - Formula in POC
**(Remaining expenses) of which: Impairment losses, changes in fair value and other expenses and losses in financial investments and financial instruments**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF05204	| Costs - Losses in group and associated companies | Q05-0545-Nota45-A1430-1 | 1 |
| VF03970	| Costs - Other financial costs | Q05-0545-Nota45-A1436-1 | 1 |
| VF04046	| Extraordinary costs – Disposal of financial investments | Q06-A0651 | 1 |
| VF03966	| Costs - Adjustments of financial fixed assets | Q05-0545-Nota45-A1432-1 | 1 |

[return](#b3.-profit-and-loss-statement-variables)

-----------------------------------------------------

## DL002 - Formula in POC
**Other expenses - Cash discounts granted**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03968 |	Costs  - Cash discounts granted | Q05-0545-Nota45-A1434-1 |	1 |

[return](#b3.-profit-and-loss-statement-variables)

------------------------------------------------------

## DL005 - Formula in POC
**Other expenses - Other - Donations**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03978 | Costs - Donations | Q05-0546-Nota46-A1448-1 | 1 |

[return](#b3.-profit-and-loss-statement-variables)

------------------------------------------------------

## DL011 - Formula in POC
**Salaries of corporate bodies**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF04036 |	Employee expenses - Salaries of corporate bodies | Q06-A0641 | 1 |

[return](#b3.-profit-and-loss-statement-variables)

-----------------------------------------------------

## DL012 - Formula in POC
**Employee Salaries**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF04037 | Employee expenses - Salaries of employees | Q06-A0642 | 1 |

[return](#b3.-profit-and-loss-statement-variables)

-----------------------------------------------------

## DL013 - Formula in POC
**Social security expenses**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF04040 |	Employee expenses - Social security expenses | Q06-A0645 | 1 |


[return](#b3.-profit-and-loss-statement-variables)

------------------------------------------------------

## DL014 - Formula in POC
**Insurance schemes for accidents at work and occupational diseases**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF04041 |	Employee expenses - Insurance schemes for accidents at work and occupational diseases | Q06-A0646 | 1 |

[return](#b3.-profit-and-loss-statement-variables)

-----------------------------------------------------

## DL017 - Formula in POC
**Services**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03047	| Services | Q03-A0126-1 | 1 |

[return](#b3.-profit-and-loss-statement-variables)

----------------------------------------------------

## DL043 - Formula in POC
**Supplementary income**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03051	| Supplementary income | Q03-A0129-1 | 1 |

[return](#b3.-profit-and-loss-statement-variables)

------------------------------------------------------

## DL045 - Formula in POC
**Employee expenses - Other, except salaries**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF03022	| Employee expenses - Pensions | Q03-A0105-1 | 1 |
| VF03023	| Employee expenses - Others | Q03-A0106-1 | 1 |

[return](#b3.-profit-and-loss-statement-variables)

------------------------------------------------------

## DL047 - Formula in POC
**Indirect taxes**

| Variable name	| Variable description | Item in IES| Coefficient |
| :----: | :------------- | :-------------- | :---: |
| VF04032 | Indirect Taxes | Q06-A0637 | 1 |

[return](#b3.-profit-and-loss-statement-variables)

------------------------------------------------------
