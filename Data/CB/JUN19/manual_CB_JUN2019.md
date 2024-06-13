<meta charset="utf-8"/>

---
title: Central Balance Sheet Database - Data Manual
---


`Extraction Date`: June 2019

`Manual Date`: 17 August 2020



**Abstract**: The Central Balance Sheet Database (CB) is constructed and made available by *Banco de Portugal* and provides economic and financial information on non-financial corporations operating in Portugal. This dataset contains annual data from 2006 onwards and is mostly based on information reported through *Informação Empresarial Simplificada* (IES, Simplified Corporate Information). Until 2009 the data was reported according to the Plano Oficial de Contabilidade (POC, Official Chart of Accounts). Starting in 2010, the data is reported according to a new accounting system, the Sistema de Normalização Contabilística (SNC, Accounting Standards System). This is a significant structural change that is reflected in the way the data is organized. \




# Table of Contents
1. [General Information](#general-information)
2. [Geographical Coverage](#geographical-coverage)
3. [Population](#population)
4. [Methodology](#methodology)
    1. [Changes in the Accounting System in Portugal](#a.-changes-in-the-accounting-system-in-portugal)
    2. [What can change with a new extraction?](#b.-what-can-change-with-a-new-extraction)
    3. [Changes introduced with the extraction of June 2019](#c.-changes-introduced-with-the-extraction-of-june-2019)
5. [Description of Files](#description-of-files)
6. [Description of Variables](#description-of-variables)
    1. [General Information File (Cover Sheet)](#a.-general-information-file-cover-sheet)
    2. [Economic and Financial Information File](#b.-economic-and-financial-information-file)
    3. [Employment Information File](#c.-employment-information-file)
    4. [Trade Information per Market File](#d.-trade-information-per-market-file)
    5. [Corporate Actions File](#e.-corporate-actions-file)
    6. [Economic and Financial Indicators File](#f.-economic-and-financial-indicators-file)
    7. [Cash-Flows File](#g.-cash-flows-file)
    8. [Information by Sector of Activity File](#h.-information-by-sector-of-activity-file)
7. [Basic Descriptive Statistics](#basic-descriptive-statistics)
8. [Legislation](#legislation)
9. [Auxiliary Files](#auxiliary-files)
10. [Useful Links](#useful-links)
11. [Frequently Asked Questions](#frequently-asked-questions)
12. [Citation of this Dataset](#citation-of-this-dataset)
13. [References](#references)



# General Information

> `Dataset Designation in English`: Central Balance Sheet Database (CB)

> `Dataset Designation in Portuguese`: *Central de Balanços* (CB)

> `Data Type`: Longitudinal Data

> `Unit of Analysis`: Firms

> `Frequency`: Annual

> `Start Year`: 2006 [^1]

>`Most recent year`: 2017

> `Reference date`: The data reports to the fiscal period declared by the firm. For most cases, the fiscal period coincides with the civil year. For those firms with fiscal period different from the civil year, the reference year is the one covering most of the days of the fiscal period.

> `Data Organization`: Data is organized in eight files per year (see Figure below):

- General Information on the firm (Cover Sheet),
- Economic and Financial Information (Balance Sheet and Profit and Loss Statements),
- Employment Information,
- Trade Information per Market,
- Corporate Actions,
- Economic and Financial Indicators,
- Cash-Flows,
- Information by Sector of Activity.

In all files each row corresponds to one firm in a given year.[^2] All files are available in Stata format, version 15.

[^1]: From 1991 to 2004 the source of CB was a survey conducted by *Banco de Portugal*, covering approximately 5% of firms. For 2005 there is data available from IES but with some limitations. These datasets are also available at BPLIM. For more information contact bplim@bportugal.pt.

[^2]: For \'Corporate Actions\' and \'Information by Sector of Activity\' data files, there may be multiple firm entries per year since the firm may report more than one event or Economic Activity for the same reference year, respectively.

> `Version of the Data`: The data made available by BPLIM corresponds to a data freeze at a certain time of the year.[^3] Therefore, all files contain the information as reported in the extraction date. The most recent update of the data occurred in June 2019.

[^3]: For more information, see the Section “Methodology”.

> `Languages Available`: Variable labels and value labels are available in Portuguese and for most of the variables also in English. [^4]

[^4]: To see the labels in English type the following command line in Stata: 'label language en'.

> `Related Datasets`: BPLIM also makes available the *Central Balance Sheet Harmonized Panel Data* which contains only variables that are consistent over time either because they were not affected by the POC to SNC change or because it was possible to construct harmonized variables based on the two different accounting systems.

> `Digital Object Identifier`: 10.17900/CB.CBA.Jun2019.V1

![](./attachments/structure_CB.PNG)


# Geographical Coverage
The data refers to firms located in the Mainland Portugal and Autonomous Regions – Azores and Madeira.


# Population
CB covers the population of all Portuguese non-financial corporations. The classification of non-financial corporations follows the guidelines on the “European System of National and Regional Accounts” ([ESA 2010](http://ec.europa.eu/eurostat/web/esa-2010)). It includes market producers mainly dedicated to the production of non-financial goods and/or services, such as private and public corporations, cooperatives and partnerships recognized as independent legal entities, non-profit institutions or associations serving non-financial corporations, public independent legal entities, private and public quasi-corporations, and head offices.[^5]

[^5]: When the main activity of the group of corporations (measured at the value added) is the production of non-financial goods and services.


# Methodology
The annual data of CB is collected through *Informação Empresarial Simplicada* (IES). IES is mandatory and contains tax, accounting and statistical information at the firm and establishment level. IES is composed of 21 Annexes:

![Source: IES forms, Banco de Portugal, 2014; Oliveira, 2016](./attachments/ies_annexes.PNG)



CB contains the information reported on Annexes A (Firm Level Data) and R (Establishment Level Data) by non-financial corporations. Firms submit IES electronically to the Ministry of Finance every year.[^6] The deadline to submit the information was initially set at the last working day of the 6th month after the end of the fiscal year and, since 2009, [^7] at the 15th day of the 7th month after the end of the fiscal year. Firms support a monetary cost when they register the financial statements under IES.[^8]

After the firm submits the data, the system implements some validation checks and generate an alert if it finds an inconsistency. In that case the firm has 30 days to correct it.[^9] Firms may also correct the information previously reported by sending a replacement version of the Annexes along with the “Cover Sheet”. In case the correction is made to Annex A (Balance Sheet or Loss and Profit Statement) or to Annex R (Establishment Level Data), the firm is required to re-send both Annexes even if the information reported in one of them remains unchanged. If the firm changes the fiscal period it is also required to send a declaration before and after the change. The Tax Authority (AT) [^10] sends the information collected through IES in an electronic format to the Institute of Registration and Notary Affairs (IRN).[^11] This institute is responsible for sending the information to *Banco de Portugal*, National Statistics Institute (INE) [^12] and Directorate-General for Economic Activities (DGAE).[^13]

![](./attachments/information_flow.PNG)

The information reported by these firms is then subject to a quality control procedure by the Statistics Department of *Banco de Portugal*. The quality control is operated at three levels (Banco de Portugal, 2009):

- **Temporal consistency**: the information reported over the last three years is used to check the temporal consistency of the reported variables. The outliers identified are then subject to further validation;

- **Internal consistency**: this criterion verifies whether the information is reported according to the accounting rules and concepts in place;

- **External consistency**: the information reported in IES is compared to the information available in other datasets managed by *Banco de Portugal*, such as: the Quarterly Survey of Non-financial Corporations (ITENF),[^14] the Central Credit Responsibility Database (CRC)[^15], the Communication of External Transactions and Positions (COPE)[^16] and the Securities Statistics Integrated System (SIET).[^17] This verification may also resort to public information such as official and specialized websites and national or international news.

-    In some cases Banco de Portugal will directly contact the firm to validate the information.

Every year around the month of June, after the quality control process takes place, BPLIM creates a data freeze. The most recent version of the data was extracted on June 2019.


[^6]: According to Decree-Law no. 8/2007, the reporting of financial statements is mandatory for Commercial Companies, Civil Companies under a commercial form, European Public Limited Liability Companies, Public Companies, Foreign Companies with permanent representation in Portugal and Individual Limited Liability Establishments.
[^7]: According to the changes introduced by Decree-Law no. 292/2009.
[^8]: This cost was equal to 85€ for fiscal periods up to 2011 and 80€ for fiscal periods after 2012.
[^9]: According to Ordinance no. 370/2015.
[^10]: Autoridade Tributária e Aduaneira.
[^11]: Instituto dos Registos e do Notariado.
[^12]: Instituto Nacional de Estatística.
[^13]: Direção Geral das Atividades Económicas.
[^14]: Inquérito Trimestral às Empresas Não Financeiras which is conducted jointly with INE.
[^15]: Central Responsabilidades de Crédito.
[^16]: Comunicação de Operações e Posições com o Exterior.
[^17]: Sistema Integrado de Estatísticas de Títulos.



## A.    Changes in the Accounting System in Portugal
Until 2009 the data was reported according to the *Plano Oficial de Contabilidade* (POC, Official Chart of Accounts). In 2009, a new accounting system, the *Sistema de Normalização Contabilística* (SNC, Accounting Standards System) was approved by the Decree-Law no. 158/2009. The main goal of SNC is to make the reporting of accounting information compliable with International Accounting Standards (IAS). Thus, all data reported afterwards follows the SNC.[^35] This is a significant structural change that is reflected in the way the dataset is organized and poses some challenges in the comparability of the variables over time, especially in the Balance Sheet and Profit and Loss Statement. The introduction of SNC was reflected in IES in several dimensions, such as:

1. some accounting items were simply redenominated;
2. some variables were aggregated or disaggregated, For example, the variables “Statutory reserves”, “Contractual reserves” and “Other reserves” in the Balance Sheet on POC accounting system are reported in an aggregated manner on SNC accounting system in the variable “Other reserves”.[^18];
3. Some tables were added to the survey in 2010, such as, the Cash-Flows Statement and Statement of Changes in Equity;
4. SNC introduces different reporting standards for firms.[^19] In practical terms, this means that Micro-Entities may report some variables at a more aggregated level of detail and be exempt from reporting some tables such as Changes in Equity and Cash-Flows Statement.
The variable “regime” in the “General Information” Files captures the reporting standards indicated by the firm.[^20] In the auxiliary files “variables_*.html”, the column “Accounting Regime” identifies the applicable reporting standards to each variable (N - International Accounting Standards; S - Accounting and Financial Reporting Standards and Accounting and Financial Reporting Standards for Small-Sized Entities; M - Accounting and Financial Reporting Standards for Micro-Entities).

[^18]: For a more detailed comparison of SNC versus POC see [POCvsSNC](https://www.occ.pt/pt/a-ordem/publicacoes/poc-versus-snc)
[^19]: See Decree-Law no. 158/2009 and Law no. 35/2010.
[^20]: For a brief description of the eligibility criteria for the accounting regimes see the Section “Legislation”, Decree-Law no. 158/2009, Law no. 35/2010 and Decree-Law no. 36-A/2011.
[^35]: In 2010 some declarations were reported according to POC. This situation occurs mostly for declarations sent in the cessation period and before or after the firms adopts a special fiscal period - a fiscal period different from the calendar year.

## B. What can change with a new extraction?
The CB database at the *Banco de Portugal* is updated continuously. Firms send IES declarations for the new fiscal year as well as declarations for previous years.
BPLIM performs a single data extraction every year. Around June a data freeze is produced to include the information reported by the firms for a new reference year. This new data freeze includes all available data since 2006.
With a new extraction the number of observations for a given year may be slightly different. This discrepancy may be more relevant for recent years of the data. This may occur because in the meantime firms may have sent in declarations for years that were missing at the time of the last extraction. Another reason why there may be differences in the number of observations across extractions is if the firm is reclassified as non-financial or financial corporation and therefore it is (in/ex)cluded from the data.
It is also possible that for the same firm and year the reported values for some variables differ across extractions. This will occur if the firm replaces the declaration sent at the time of the last extraction (substitution declaration) or if the information is subject to quality control in the meantime.
Finally, after internal revision, BPLIM may decide to add new variables or exclude existing ones.


## C. Changes introduced with the extraction of June 2019

The main changes introduced in the extraction of *June 2019* relatively to the previous one (*June 2018*) are:

1. **General Information file** [^21]:

    1.1. Three new variables are available: *liquidacao*, *sucursal* and *exporta*

    The variables *liquidacao* and *sucursal* are constructed based on the information contained in the company's name. The variable *liquidacao* allows to identify firms in liquidation, complementing the information in the indicator of economic activity (*indactiecon*) and firm's situation (*sitempresa*). The variable *sucursal* allows to identify branches of foreign companies.
    Finally, the variable *exporta* is built based on the information reported in the Trade Information per Market Files and allows to easily identify whether the firms are exporting to the European Union (EU) and/or to Extra-EU Markets.

    1.2. The variable reporting the founding date of the firm (*ancon*) was replaced by the one constructed by the Statistics Department of *Banco de Portugal*

    This variable replaces the information reported through the Central Registry of Companies (Ministry of Justice). This new variable has a lower number of missing values because it is complemented with other sources of information available at *Banco de Portugal*.

2. **Corporate Actions** [^22]:

    In the current extraction, we provide a dataset produced by the Statistics Department of *Banco de Portugal* that is subject to quality control and uses not only the information reported through IES but also other complementary sources.

[^21]: For more detailed information see the description of the variables in the [General Information File](#a.-general-information-file-cover-sheet).

[^22]: For more detailed information see the description of the variables in the [Corporate Actions File](#e.-corporate-actions-file).


# Description of Files
The firm level data in CB is organized in eight files. Each file provides a different type of information, namely:

| Type of Information | File Name |
| :------ | :----------- |
| **A.    General Information (Cover sheet)** | CB_A_YFRM_yyyy_eeee_ROSTO_V01.dta |
| **B.    Economic and Financial Information** | CB_A_YFRM_yyyy_eeee_CONTAS_V01.dta |
| **C.    Employment Information** | CB_A_YFRM_yyyy_eeee_PESSOAL_V01.dta |
| **D.    Trade Information per Market** | CB_A_YFRM_yyyy_eeee_MG_V01.dta |
| **E. Corporate Actions** | CB_A_YFRM_yyyy_eeee_AMARC_V01.dta |
| **F.    Economic and Financial Indicators** | CB_A_YFRM_yyyy_eeee_INDIC_V01.dta |
| **G.    Cash-Flows** | CB_A_YFRM_yyyy_eeee_FLUXOSCAIXA_V01.dta |
| **H.    Information by Sector of Activity** | CB_A_YFRM_yyyy_eeee_BYCAE_V01.dta |



Where *A* stands for Anonymized and *yyyy*=2006,…,2017 and *eeee* reports the extraction date.

All files contain a unique firm identifier (*tina*) allowing the matching of the different types of information by firm. Whenever possible, labels and value labels were attributed to all categorical variables. All datasets are anonymized.

# Description of Variables
Below we provide a general description of the variables included in each of the eight files referred above. For a full account of all variable categories and changes over time see [“Auxiliary Files” section](#auxiliary-files). The variables whose label ends in “(QS)” are those used to produce [*Quadros do Sector* (QS)](https://www.bportugal.pt/en/page/sector-tables), a publication by the Statistics Department of *Banco de Portugal*, which is composed of a set of financial and economic indicators by sector of activity and dimension class.
When applicable, we distinguish between variables reported according to the former Accounting System (POC) and the one introduced in 2010 (SNC).

## A.    General Information File (Cover Sheet)
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
| 1 |    SNC | Accounting Standards System |


`Reporting Standards` (*regime*) – with the introduction of SNC firms must choose their reporting standards. Therefore this variable is only available after 2009.

| Code | Designation |
| :------: | :----------- |
| -1 | Not specified |
| 1 | International Accounting Standards (IAS) |
| 2 | Accounting and Financial Reporting Standards |
| 3 | Accounting and Financial Reporting Standards for Small-Sized Entities |
| 4 | Accounting and Financial Reporting Standards for Micro-Entities |


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

`Firm in liquidation` (*liquidacao*) - identifies firms in liquidation. According to the [Article 146 of the Portuguese Code of Commercial Companies](https://dre.pt/web/guest/legislacao-consolidada/-/lc/116042191/201906302305/73599989/diploma/indice), dissolved firms are required to add the expression "Em liquidação" to the their name while they are in the liquidation process. This variable is created by BPLIM using the information contained in the company's name as reported by the firm in IES forms. It takes value one if the expression "em liquida" is found in the company's name.

`Share of turnover of the main economic activity` (*pervvn*) – indicates the proportion of turnover that the main economic activity represents among all the activities carried on by the firm.

`District` (*distrito*) – provides information on the district in which the firm is located. For a complete list of codes see the auxiliary file [var_rosto.html](./aux_files/variables_description/var_rosto.html).

`Branch` (*sucursal*) - dummy variable that takes value one for branches of foreign firms located in Portugal. Branch offices are identified using the information contained in the name as reported by the firm in IES and the tax identification number of the company. Notably, the legislation states that the name of these companies includes expressions such as "Sucursal" or "Representação Permanente" (see, for example, [Article 21 of Ordinance n. 1416-A/2006](https://dre.pt/pesquisa/-/search/235919/details/maximized) or [Article 5 of Decree-Law n. 73/2008](https://dre.pt/pesquisa/-/search/249803/details/maximized)) and the firms are assigned with tax identification numbers started by "98".

`Exporting Firm` (*exporta*) - categorical variable created by BPLIM to identify firms exporting to the European Union or Extra-European Union Markets. This variable is constructed based on the information reported in the Trade Information per Market files, according to the formulas below:

| Code | Designation | Formula using POC variables | Formula using SNC variables |
| ---- | ------------ | --------------- | ----------------- |
| 0 | Does not Export [^34] | VF03953 = 0 ***and*** VF03954 = 0 ***and*** VF03957 = 0 ***and*** VF03958 = 0 | VF15620 = 0 ***and*** VF15624 = 0 ***and*** VF15621 = 0  ***and*** VF15625 = 0 |
| 1 | Exports to EU Market | VF03953 (EU Market - Total sales) $>$ 0 ***or*** VF03954 (EU Market - Total services) $>$ 0 | VF15620 (EU Market - Total sales) $>$ 0 ***or*** VF15624 (EU Market - Total services) $>$ 0|
| 2 | Exports to Extra-EU Market | VF03957 (Extra-EU Market - Total sales) $>$ 0 ***or*** VF03958 (Extra-EU Market - Total services) $>$ 0 |  VF15621 (Extra-EU Market - Total sales) $>$ 0 ***or*** VF15625 (Extra-EU Market - Total services) $>$ 0 |
| 3 | Exports to EU and Extra-EU Market | (VF03953 ***or*** VF03954) $>$ 0 ***and*** (VF03957 ***or*** VF03958) $>$ 0 | (VF15620 ***or*** VF15624) $>$ 0 ***and*** (VF15621 ***or*** VF15625) $>$ 0 |

[^34]: Missing values in the referred variables are treated as zeros.

### A3. Variables created by the Statistics Department of *Banco de Portugal*

`Institutional Sector` (*sectorinstfinal*):

*sectorinstfinal* - reports the institutional sector to which the firm belongs to. As explained in the Sections “Population” and “Methodology”, CB only includes non-financial corporations. Therefore, this variable identifies the type of non-financial corporation, such as public, private or holding company. The algorithm to allocate firms according to the institutional sector is based on the classification of economic activity, the name of the firm and other variables available at *Banco de Portugal*. Therefore, in some cases the institutional sector may not be in line with the sector of economic activity.

| Code | Designation |
| :----: | :----------- |
| 348500002 | Non-financial corporations |
| 348500003 | Public non-financial corporations |
| 348500004 | Private non-financial corporations |
| 348500005 | Foreign controlled non-financial corporations |
| 348500006 | Non-financial corporations of central government - Enterprises |
| 348500007 | Non-financial corporations of central government - Other entities |
| 348500008 | Non-financial corporations of the regional government of Madeira - Enterprises |
| 348500009 | Non-financial corporations of the regional government of Madeira - Other entities |
| 348500010 | Non-financial corporations of the regional government of Azores - Enterprises |
| 348500011 | Non-financial corporations of the regional government of Azores - Other entities |
| 348500012 | Non-financial corporations of the local government of Mainland Portugal - Enterprises |
| 348500013 | Non-financial corporations of the local government of Mainland Portugal - Other entities |
| 348500014 | Non-financial corporations of the local government of Azores - Enterprises |
| 348500015 | Non-financial corporations of the local government of Azores - Other entities |
| 348500016 | Non-financial corporations of the local government of Madeira - Enterprises |
| 348500017 | Non-financial corporations of the local government of Madeira - Other entities |
| 348500302 | Public non-financial holding companies |
| 348500308 | Private non-financial holding companies |
| 348500314 | Foreign controlled non-financial holding companies |



`Indicator of Economic Activity` (*indactiecon*) – this variable reports the firm situation revised by the Statistics Departments of *Banco de Portugal*. It is constructed using the information reported by the firm in IES (*sitempresa*) and complemented with other sources. Notably, it takes into account whether the firm contracts new loans, maintains commercial transactions with firms abroad or pays and settles the Value Added Tax, among others.


| Code | Designation |
| :------: | :----------- |
| 0  | Unknown |
| 10 | Awaiting business start |
| 20 | In business |
| 30 | Suspended activity |
| 40 | Ceased activity |
| 97 | Invalid |
| 98 |    Not specified|


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

`Legal form` (*natju*) – this variable reports firm’s legal form. For a complete list of codes see the auxiliary file [var_rosto.html](./aux_files/variables_description/var_rosto.html).

`Sector of Activity` (*cae21*, *cae3*, *caekotu*):

`Main Sector of Activity` (*cae21* and *cae3*) - reports firm's main sector of activity. The criteria to define the main sector of activity is the gross value added at factor cost. When it is not possible to use this information to define the main sector of activity, firms are requested to use turnover or the number of people permanently employed by the firm. From 2006 to 2008, firms reported the code of “The Portuguese Classification of Economic Activities - Revision 2.1” (CAE Rev. 2.1) at the highest level of disaggregation. Since 2009, firms report their main activity according to the “The Portuguese Classification of Economic Activities - Revision 3” (CAE Rev. 3). The Statistics Department of *Banco de Portugal* provides the information on the main sector of activity according to both classifications CAE Rev2.1 and CAE Rev3 whenever possible. The source of this information is the CAE registered in the “Central Registry of Companies” for each company. Whenever the correspondence is not unique, the match between codes CAE Rev. 2.1 and CAE Rev. 3 is implemented based on the highest frequency of the matches.[^26] For a complete list of codes see the auxiliary file [var_rosto.html](./aux_files/variables_description/var_rosto.html).


`CAE sections K, O, T or U` (*caekotu*) - this variable was created by BPLIM using the information in *cae3* (Classification of Economic Activity Rev. 3). It takes value one if the main economic activity of the firm is within one of the following sections of economic activity:

- K- Financial and insurance activities,
- O-Public administration and defence; compulsory social security,
- T-Activities of households as employers; undifferentiated goods- and services-producing activities of households for own use,
- U-Activities of extraterritorial organizations and bodies.

This variable allows for the identification of the cases in which the information on the sector of economic activity reported by the firm is not in line with the institutional sector to which the firm is allocated by the Statistics Department of *Banco de Portugal*. This may happen because *Banco de Portugal* uses complementary sources of information besides the classification of economic activities to classify firms as non-financial corporations.


[^23]: *Ficheiro Central de Pessoas Colectivas*.
[^24]: All establishments, including those in which  no productive activity is carried on are included.
[^25]: Establishment is defined as an enterprise or part of an enterprise that carries on economic activities in a geographically identified place, with one or more workers.
[^26]: For more information on firm’s sector of activity please see [SICAE Website](http://www.sicae.pt/Default.aspx).

## B.    Economic and Financial Information File
The variables may be classified in two groups: Balance Sheet and Profits and Losses Statement variables. The filling instructions for these variables can be found in the Decree-Law no. 410/89 for POC variables and Ordinance no. 986/2009 for SNC variables. For a full account of all variable characteristics see the auxiliary file [var_contas.html](./aux_files/variables_description/var_contas.html). The missing values in Stata of some variables in this file were coded as ".a" whenever the reporting is not mandatory for the accounting standards adopted by the firm.

### B1. Identifiers
`Firm identifier` (*tina*) – Unique identifier that enables tracking the legal entity over time. *tina* is the anonymized tax identification number.

`Reference year of the data` (*ano*) – Reference year of the data.

### B2. Balance Sheet - Variables reported according to POC

**ASSETS**

| Variable Name | Variable Description | Type of reporting [^27] |
| :------: | :------- | :--- |
| VF05681 | **Total Assets** | Net |
| VF05737 | > **Tangible and intangible assets (excluding fixed assets work-in-progress)** | Gross |
| VF05739 | > > Intangible assets | Gross |
| VF05750 | > **Fixed assets work-in-progress (including tangible, intangible and financial investments)** | Net/Gross |
| VF05743 | > > Tangible fixed assets | Gross |
| VF05685 | > **Financial Assets** | Gross |
| VF05751 | > **Current Assets - Inventories** | Gross |
| VF05759 | > > Current Assets - Inventories - Finished and intermediate products; Subproducts, wastes and scrap; Products and work in progress) | Gross |
| VF03141 | > > Current Assets - Inventories - Raw and subsidiary materials and consumables - Gross Assets | Gross |
| VF03153 | > > Current Assets - Inventories - Goods - Gross Assets | Gross |
| VF05696 | > **Other Debts** | Gross |
| VF05709 | > > Other debts | Gross |
| VF05763 | > > Accruals and deferrals (Assets) | Net/Gross |
| VF03156 | > > Current Assets - Inventories - Advances for purchases | Net/Gross |
| VF05700 | > > Other Loans Granted - Trade Credit and Advances | Gross |
| VF05702 | > > > Client debts | Gross |
| VF05822 | > > > Advances from clients | Net |
| VF05697 | > > *Short-term accounts receivable* | Gross |
| VF03253 | > **Total depreciation** | n.a. |
| VF03254 | > **Total adjustments** | n.a. |
| VF03242 | > **Current Assets - Negotiable securities - Gross Assets** | Gross |
| VF03247 | > **Current Assets - Cash and cash equivalents** | Net/Gross |
| VF03088 | Intangible assets - Net Assets | Net |
| VF03117 | Tangible fixed assets - Net Assets | Net |
| VF03140 | Financial Assets - Net Assets | Net |
| VF05753 | Inventories - Net Assets (BACH) | Net |
| VF05762 | Other Inventories - Net Assets (BACH) | Net |
| VF03143 | Current Assets - Inventories - Raw and subsidiary materials and consumables - Net Assets | Net |
| VF05701 | Trade Credits Granted - Net Assets (BACH) | Net |
| VF05710 | Other accounts receivable - Net Assets (BACH) | Net |
| VF03223 | Short-term accounts receivable - Net Assets | Net |
| VF03244 | Current Assets - Negotiable securities - Net Assets | Net |

[^27]: In POC, firms are required to report the gross value and the amortization and adjustment of the assets. Therefore, this column states whether each variable is reported in net or gross terms and identify the variables that do not have amortization or adjustments to be deducted and, therefore, are equivalent in net and gross terms (net/gross).


**EQUITY**

| Variable Name | Variable Description |
| :------: | :------- |
| VF05773 | **Total Equity** |
| VF05775 | > **Shares and other Equity - Capital Accounts** |
| VF03258 | > > Equity- Capital |
| VF03261 | > > > Equity- Supplementary capital |
| VF03262 | > > Equity- Share Premiums |
| VF03259 | > > Equity- Own shares- Nominal value |
| VF03260 | > > Equity- Own shares- Discounts and Premiums |
| VF05786 | > **Shares and other Equity - Reserves and Retained Earnings** |
| VF03269 | > > Equity- Retained earnings |
| VF03271 | > > Equity- Interim dividends |
| VF03263 | > > Equity- Adjustments to investments in group and associated companies |
| VF03264 | > > Equity-Revaluation reserves |
| VF03265 | > > Equity- Reserves- Legal reserves |
| VF03266 | > > Equity- Reserves- Statutory reserves |
| VF03267 | > > Equity- Reserves- Contractual reserves |
| VF03268 | > > Equity- Reserves- Other reserves |
| VF03270 | > **Equity- Net income** |


**LIABILITIES**

| Variable Name | Variable Description |
| :------: | :------- |
| VF05766 | **Total liabilities** |
| VF05799 | > **Provisions (total)** |
| VF03273 | > > Provisions- Provisions for pension liabilities |
| VF05810 | > **Financial Debt- including securities and excluding shares** |
| VF05813 | > **Financial Debt- Bank loans** |
| VF03280 | > > Debt- Medium and long term loans from credit institutions |
| VF03298 | > > Debt- Short term loans from credit institutions |
| VF05824 | > **Supplier debts** |
| VF05827 | > **Other debts** |
| VF03299 | > > Debt- Short Term advances on sales  |
| VF05836 | > **Other loans** |
| VF05850 | > **Accruals and Deferrals (Liabilities)** |
| VF05704 | > **Advance Payments to suppliers (Assets)** |


### B3. Balance Sheet - Variables reported according to SNC

**ASSETS**

| Variable Name | Variable Description |
| :------: | :------- |
| VF15991    | **Total Assets (QS)** |
| VF15994    | > **Total non-current assets (QS)** |
| VF15995    | > > **Fixed tangible assets and intangible assets** |
| VF16001    | > > > Non-current Assets- Intangible assets (including Goodwill) |
| VF12982    | > > > > Goodwill |
| VF16002    | > > > Tangible fixed assets |
| VF16003    | > > > > Non-current assets - Land and buildings |
| VF16004    | > > > > Non-current assets- Basic equipment |
| VF16005    | > > > > Non-current assets-Other fixed assets |
| VF16006    | > > > > Non-current assets- Payments on account of fixed assets |
| VF16015    | > > **Financial investments** |
| VF16016    | > > > Non-current assets - investments in subsidiary and associated companies |
| VF16017    | > > > Non-current assets - Financial investments (excepting investments in subsidiary and associated companies) |
| VF18510    | > > **Non-current assets - Remaining non-current assets** |
| VF16018    | > > > Non-current assets - Shareholders |
| VF16041    | > > > Non-current assets - Deferred tax assets |
| VF16019    | > **Total Current assets (QS)** |
| VF16022 |    > > **Current assets - Inventories and biological assets** |
| VF16023    | > > > Inventories - Raw and subsidiary materials and consumables |
| VF16024    | > > > Inventories - Advances for purchases |
| VF16025    | > > > Current assets- Inventories (excepting Raw and subsidiary materials and consumables) |
| VF16031    | > > **Current assets - Customers** |
| VF16035    | > > **Net non-current assets held for sale** |
| VF16039    | > > **Current assets - Cash and bank deposits** |
| VF18511    | > > **Current assets - Remaining current assets** |
| VF16032    | > > > Current assets - State and other public entities |
| VF16033    | > > > Other current assets |
| VF16034    | > > > Current assets - Shareholders |
| VF16046    | > > > Current assets - Deferred expense |

**EQUITY**

| Variable Name | Variable Description |
| :------: | :------- |
| VF16050    | **Equity and Liabilities (QS)** |
| VF16051    | > **Equity (QS)** |
| VF16052    | > > **Equity - Paid-up capital** |
| VF16053    | > > **Equity - Other equity instruments** |
| VF16056    | > > **Equity - Reserves and retained earnings** |
| VF13024    | > > > Equity- Legal reserves |
| VF13025    | > > > Equity- Other reserves |
| VF13026    | > > > Retained earnings |
| VF16057    | > > **Equity - Other items of equity** |
| VF13021    | > > Equity- Own shares |
| VF13023    | > > Equity- Share Premiums |
| VF13027    | > > Adjustments on financial investments |
| VF13028    | > > Revaluation surplus |
| VF13030 |    > > Other variations in equity- R2 |
| VF13029    | > > Other variations in equity- R1 |
| VF13031 |    > > Other variations in equity- R3 |
| VF13032 |    > > Other variations in equity- R4 |
| VF16063 |    > **Equity - Net income** |
| VF16064 |    > **Equity - Interim dividends** |


**LIABILITIES**

| Variable Name | Variable Description |
| :------: | :------- |
| VF16070 |    > **Liabilities (QS)** |
| VF16071 |    > > **Non-current liabilities** |
| VF16075 |    > > > Non-current liabilities - Obtained funding |
| VF16076 |    > > > Non-current liabilities -Post-employment benefits |
| VF18512 |    > > > Non-current liabilities - Remaining non-current liabilities |
| VF16074 | > > > >    Non-current liabilities - Provisions |
| VF16077 |    > > > > Non-current liabilities - Other accounts payable |
| VF16107 |    > > > > Non-current liabilities - Deferred tax liabilities |
| VF16079 |    > > **Current liabilities (QS)** |
| VF16083 |    > > > Current liabilities - Suppliers |
| VF16086 |    > > > Current liabilities - Obtained funding |
| VF18513 |    > > > Current liabilities - Remaining current liabilities |
| VF16084 |    > > > > Current liabilities - State and other public entities |
| VF16108 |    > > > > Current liabilities - Deferred income |
| VF16085 | > > > > Current liabilities - Other current liabilities |


### B4. Profits and Losses Statement - Variables reported according to POC
| Variable Name | Variable Description |
| :------: | :------- |
| VF05908    | **Sales** |
| VF03045    | > Sales - goods |
| VF03046    | > Sales - products |
| VF03047    | **Provision of services** |
| VF03049    | **Variation in production** |
| VF03050    | **Capitalized production** |
| VF03051    | **Supplementary revenues** |
| VF03052    | **Operating subsidies** |
| VF03053    | **Operating revenues** |
| VF03055    | **Reversals of amortizations and adjustments** |
| VF05898    | **Operating revenues** |
| VF05863    | **Cost of goods sold and material consumed** |
| VF03017    | > Cost of goods sold |
| VF03018    | > Cost of material consumed |
| VF05873    | **Employee costs** |
| VF05881    | **Depreciations (including adjustments)** |
| VF03025    | > Depreciation of intangible and tangible fixed assets |
| VF03026    | > Adjustments |
| VF03027    | **Provisions** |
| VF03020    | **Supplies and external services** |
| VF03029    | **Taxes** |
| VF03030    | **Other operating costs** |
| VF05857    | **Operating costs** |
| VF05925    | **Operating profit or loss** |
| VF05918    | **Financial revenues** |
| VF03057    | > Gains in group and associated companies |
| VF03058    | > Income from equity holdings |
| VF03059    | > Income from negotiable securities and other financial applications – relative to group companies |
| VF03060    | > Income from negotiable securities and other financial applications |
| VF03061    | > Interest Income and similar earnings- relative to group companies |
| VF03062    | > Interest Income and similar earnings - Others |
| VF05888    | **Financial costs** |
| VF03033    | > Losses in group and associated companies |
| VF03034    | > Depreciation and adjustments of financial fixed assets |
| VF03035    | > Interest and related expense - relative to group companies |
| VF03036    | > Interest and related expense - others |
| VF05935    | **Financial profit or loss** |
| VF03065    | **Extraordinary revenues** |
| VF03039    | **Extraordinary costs** |
| VF05940    | **Extraordinary items** |
| VF03041    | **Income tax** |
| VF06011    | **Costs** |
| VF06012    | **Revenues** |
| VF03043 | **Net income** |


### B5. Profits and Losses Statement - Variables reported according to SNC
| Variable Name    | Variable Description |
| :------: | :------- |
| VF16132    | **Turnover** |
| VF16133    | > Sales |
| VF16134    | > Services |
| VF16136    | **Operating subsidies** |
| VF16137    | **Variation in production** |
| VF16138    | **Capitalized production** |
| VF16140    | **Other incomes** |
| VF16156    | **Costs of goods sold and material consumed** |
| VF16157    | **Supplies and external services** |
| VF16160    | **Employee expenses** |
| VF16166    | **Impairment (losses/reversals) and changes (gains/losses) in fair value** |
| VF16173    | **Provisions (increases/decreases)** |
| VF16175    | **Other expenses** |
| VF16215    | **Earnings before Interest, Taxes, Depreciation and Amortization - EBITDA** |
| VF16172    | **Expenses/reversals of depreciations and amortizations** |
| VF16216    | **Earning before Interest and Tax - EBIT** |
| VF16150    | Interest income |
| VF16184    | Interest expenses |
| VF16191    | Income tax |
| VF16152    | **Total income** |
| VF16193    | **Total Expenses** |
| VF16218    | **Net income** |
| VF16219    | **Net income from discontinued operations** |


## C.    Employment Information File
This file contains information on the average number of employees and number of hours worked during the months in which the firm was in business by employment contract arrangement, gender and working time arrangement. This file also provides information on employee expenses.

### C1. Identifiers
`Firm identifier` (*tina*) – Unique identifier that enables tracking the legal entity over time. *tina* is the anonymized tax identification number.

`Reference year of the data` (*ano*) – Reference year of the data.


### C2. Variables reported according to POC
| Variable Name |    Variable Description |
| :------: | :------- |
| VF03319    |Number of (paid and unpaid) employees |
| VF03320    | > Number of (paid and unpaid) full-time employees |
| VF04904    | > Number of (paid and unpaid) part-time employees |
| VF03321    | Number of paid employees |
| VF04903    | > Number of paid full-time employees |
| VF03324    | > Number of paid part-time employees |
| VF03322    | Number of paid apprentices |
| VF03323    | Number of paid homeworkers |
| VF04902    | > Number of unpaid employees |
| VF03325    | Service providers |
| VF03326    | Number of employees allocated to research and development |
| VF03327    | Temporary Agency Employment |
| VF03328    | Number of hours worked by paid and unpaid employees |
| VF03329    | > Number of hours worked by paid and unpaid full-time employees |
| VF04907    | > Number of hours worked by paid and unpaid part-time employees |
| VF03330    | Number of hours worked by paid employees |
| VF04906    | > Number of hours worked by paid full-time employees |
| VF03331    | > Number of hours worked by paid part-time employees |
| VF04905    | Number of hours worked by unpaid employees |
| VF03332    | Number of hours worked by service providers |
| VF05990    | Total Hours Worked |
| VF04036    | Compensation of corporate bodies |
| VF04037    | Salaries |
| VF04038    | Pensions |
| VF04039    | Retirement benefits and pension premiums |
| VF04040    | Social security expenses |
| VF04041    | Insurance schemes for accidents at work and occupational diseases |
| VF04042    | Expenses with social actions |
| VF04043 |    Other employee expenses    |


### C3. Variables reported according to SNC
| Variable Name |    Variable Description |
| :------: | :------- |
| VF15532    | Number of (paid and unpaid) employees |
| VF15534    | > Number of paid employees |
| VF15536    | > Number of unpaid employees |
| VF15538    | Number of (paid and unpaid) full-time employees |
| VF15540    | > Number of paid full-time employees |
| VF15542    | Number of (paid and unpaid) part-time employees |
| VF15544    | > Number of paid part-time employees |
| VF15546    | Number of (paid and unpaid) male employees |
| VF15548    | Number of (paid and unpaid) female employees |
| VF15550    | Number of employees allocated to research and development |
| VF15551    | Service providers |
| VF15553    | Temporary Agency Employment |
| VF15533    | Number of hours worked by paid and unpaid employees |
| VF15535    | > Number of hours worked by paid employees |
| VF15537    | > Number of hours worked by unpaid employees |
| VF15539    | Number of hours worked by paid and unpaid full-time employees |
| VF15541    | > Number of hours worked by paid full-time employees |
| VF15543    | Number of hours worked by paid and unpaid part-time employees |
| VF15545    | > Number of hours worked by paid part-time employees |
| VF15547    | Number of hours worked by male employees |
| VF15549    | Number of hours worked by female employees |
| VF15552    | Number of hours worked by service providers |
| VF15555    | Compensation of corporate bodies |
| VF15556    | Compensation of corporate bodies- of which participation in profits |
| VF15557    | Salaries |
| VF15558    | Salaries - of which participation in the profits |
| VF15559    | Post-employment benefits |
| VF15560    | Pension premiums |
| VF15561    | Other benefits |
| VF15562    | Post-employment benefits- Other benefits: of which defined contribution pension plans - corporate bodies |
| VF15563    | Post-employment benefits- Other benefits: of which defined contribution pension plans - other |
| VF15564    | Indemnities |
| VF15565    | Social security expenses |
| VF15566    | Insurance schemes for accidents at work and occupational diseases |
| VF15567    | Expenses with social actions |
| VF15568    | Other employee expenses |
| VF15569    | Training expenses |
| VF15570    | Other expenses- Expenses with uniforms |
| VF18834 | Expenses with defined pension plans |


### C4. Relevant definitions
**Average number of employees**: results from the sum of the number of people employed in the last weekday of each month of the fiscal period divided by the total number of months included in the fiscal period.

**Paid employees**: include all employees receiving a salary with the exception of self-employed workers, service providers and the people working at the firm but paid by other firms. It includes apprentices and homeworkers.

**Unpaid employees**: include all those working at the firm without receiving a wage, such as partners, family workers and unpaid managers.

**Service providers**: service providers working for the firm on a regular basis.

**Apprentices**: employees learning an administrative, commercial, productive or other task.

**Homeworkers**: employees working from home.

**Employees allocated to research and development**: employees dedicated to activities of R&D.

**Full-time employees**: full-time workers are those working the normal period of work in the firm for a certain occupation or occupational category.

**Part-time employees**: part-time workers include the employees that work less than the normal period of work in the firm for a certain occupation or occupational category.

**Temporary Agency Employment**: includes the people working for the firm and receiving a salary paid by other firm.

**Hours worked**: the firm reports the number of hours worked in the year. This variable is defined as the number of hours worked (normal or overtime) by the firm’s employees. [^28] It does not include the paid or unpaid hours in which the workers were absent.

[^28]: IES survey states that the hours worked include the time spent in the preparation of work tools and instruments and paid hours not effectively worked due to occasional absence, machinery stop, accident, coffee breaks.


## D.    Trade Information per Market File
Firms are required to provide information on Total Sales, Total Services, Total Purchases and Total Supplies and External Services for each Geographical Market.
The territory is divided in three geographical markets: internal market, European Union (EU) market and Extra-EU market. The EU Market includes all European Union countries with the exception of Portugal. All other countries are included in the Extra-EU Market.[^29] The values reported for each geographical market have to sum up to the totals reported at the firm level.

## D1. Identifiers
`Firm identifier` (*tina*) – Unique identifier that enables tracking the legal entity over time. *tina* is the anonymized tax identification number.

`Reference year of the data` (*ano*) – Reference year of the data.

## D2. Variables reported according to POC
| Variable Name | Variable Description |
| :------: | :------- |
| VF03949    | Internal Market - Total sales |
| VF03950    | Internal Market - Total services |
| VF03951    | Internal Market - Total purchases |
| VF03952    | Internal Market - Total supplies and external services |
| VF03953    | EU-Market - Total sales |
| VF03954    | EU-Market - Total services |
| VF03955    | EU-Market - Total purchases |
| VF03956    | EU-Market - Total supplies and external services |
| VF03957    | Extra EU-Market - Total sales |
| VF03958    | Extra EU-Market - Total services |
| VF03959    | Extra EU-Market - Total purchases |
| VF03960    | Extra EU-Market - Total supplies and external services |
| VF03961    | Total - Total sales |
| VF03962    | Total - Total purchases |
| VF05195    | Total - Total services |
| VF05196    | Total - Total supplies and external services |

## D3. Variables reported according to SNC
| Variable Name    | Variable Description |
| :------: | :------- |
| VF15619 |    Internal Market - Total sales |
| VF15623 |    Internal Market - Total services |
| VF15627 |    Internal Market - Total purchases |
| VF15631 |    Internal Market - Total supplies and external services |
| VF15635 |    Internal Market - Acquisition of tangible fixed assets |
| VF15639 |    Internal Market - Acquisition of investment properties |
| VF15643 |    Internal Market - Acquisition of intangible assets |
| VF15620 |    EU-Market - Total sales |
| VF15624 |    EU-Market - Total services |
| VF15628 |    EU-Market - Total purchases |
| VF15632 |    EU-Market - Total supplies and external services |
| VF15636 |    EU-Market - Acquisition of tangible fixed assets |
| VF15640 |    EU-Market - Acquisition of investment properties |
| VF15644 |    EU-Market - Acquisition of intangible assets |
| VF15621 |    Extra EU-Market - Total sales |
| VF15625 |    Extra EU-Market - Total services |
| VF15629 |    Extra EU-Market - Total purchases |
| VF15633 |    Extra EU-Market - Total supplies and external services |
| VF15637 |    Extra EU-Market - Acquisition of tangible fixed assets |
| VF15641 |    Extra EU-Market - Acquisition of investment properties |
| VF15645 |    Extra EU-Market - Acquisition of intangible assets |
| VF15622 | Total - Total sales |
| VF15626 |    Total - Total services |
| VF15630 |    Total - Total purchases |
| VF15634 |    Total - Total supplies and external services |
| VF15638 |    Total - Total acquisition of tangible fixed assets |
| VF15642 |    Total - Total acquisition of investment properties |
| VF15646 |    Total - Total acquisition of intangible assets |

[^29]: Note that the EU Market includes 24 countries in 2006 (25 European Union members with the exception of Portugal), 26 countries in 2007 and 27 countries since 2013.


## E. Corporate Actions File

The Corporate Actions files contain information on firm actions that occurred during the fiscal period altering the structure of the firm and affecting the comparability of the economic and financial information over time. This table is subject to quality control by the Statistics Department of *Banco de Portugal* and relies on the information reported in IES and other complementary sources. The data has a significant but not exhaustive coverage of the corporate actions that have an impact on the structure of the non-financial corporations included in CB.


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

*efeitopessoal* - dummy variable taking value one ("Yes") if the corporate action has an impact on the Number of Paid and Unpaid Employees.[^30]

*efeitobalanco* - dummy variable taking value one ("Yes") if the corporate action has an impact on Total Assets.

*efeitodemresult* - dummy variable taking value one ("Yes") if the corporate action has an impact on Turnover.

*efeitocontas* - dummy variable taking value one ("Yes") if the corporate action has an impact on the overall economic and financial statements.


[^30]: Please note that the variable Number of Paid and Unpaid Employees is only reported in IES from 2006 onwards. Therefore, it is not possible to assess the effects of the corporate actions reported in 2006 on employment information (*efeitopessoal*). For this reason, the variable *efeitocontas* may also be understated in 2006.


### E3. Relevant definitions
**Merge**- This corporate action occurs if two or more companies combine into a newly created company or an existing one. In this last case, the firm is simultaneously the Firm of Origin and the Firm of Destination.

**Split** – This corporate action occurs when a company divides its activity into two or more existing and/or newly created companies. If the firm splitting its activity stay in business then this firm is simultaneously the Firm of Origin and the Firm of Destination.

**Change of Economic Activity (with/without the creation of a new firm)** - structural change on the firm affecting the comparability of the information over time. For example, a firm being assigned a new Tax Identification Number due to changes in firm's legal form, sector of activity or institutional sector.

**Dissolution of a significant part of productive assets without split** - significant diminution in the economic activity of the firm that is not explained by the transfer of productive assets to an existing or newly created firm.


## F.    Economic and Financial Indicators File
This file provides some indicators calculated using variables of CB. For more information on how each indicator is calculated see the auxiliary file [var_indicadores.html](./aux_files/variables_description/var_indicadores.html).

### F1. Identifiers
`Firm identifier` (*tina*) – Unique identifier that enables tracking the legal entity over time. *tina* is the anonymized tax identification number.

`Reference year of the data` (*ano*) – Reference year of the data.


### F2. Variables calculated according to POC
| Variable Name | Variable Description |
| :------: | :------- |
| VF06027   | Gross operating margin rate |
| VF06028   | Days in receivables (number of days) |
| VF06032   | Days in accounts payable (number of days) |
| VF06036   | Inventories turnover (times) |
| VF06037   | Working capital turnover (times) |
| VF06038   | Growth rate of turnover |
| VF06039   | Growth rate of gross value added (GVA) |
| VF06041   | Investment rate |
| VF06043 |   Coverage rate of investment by self-financing |
| VF06045 |   Capital ratio |
| VF06050 |   Coverage of fixed assets |
| VF06052 |   Coverage of medium and long term investment |
| VF06054 |   Debt to equity ratio |
| VF06056 |   Current ratio |
| VF06057 |   Quick ratio |
| VF06058 |   Return on assets |
| VF06060 |  Asset turnover (times) |
| VF06062 |  Return on sales |
| VF06066 |  Gross economic profitability |
| VF06067 |  Gross value added rate (GVA) |
| VF06071 |  Return on equity |
| VF06079 |  Compound leverage factor |
| VF06080 |  Interest burden (QS) |
| VF06082 |  Leverage ratio |
| VF06083 |  Extraordinary income factor |
| VF06085 |  Tax burden (QS) |
| VF06087 |  Income distribution - Employees |
| VF06089 |   Income distribution - Banks and other funders |
| VF06091 |   Income distribution - State |
| VF06093 |   Income distribution - Enterprise (self-financing) |
| VF06095 |  Income distribution - Other |
| VF06097 |  Coefficient GVA / Property, plant and equipment (euros) |
| VF06099 |   Coefficient GVA / Employee costs (euros) |
| VF06104 |   Coefficient capital / Employee costs (euros) |


### F3. Variables calculated according to SNC
| Variable Name | Variable Description |
| :------: | :------- |
| VF16318 |   Current ratio |
| VF16319 |   Quick ratio |
| VF16320 |   Capital ratio (QS) |
| VF16323 |   Assets to equity ratio |
| VF16324   | Solvency ratio QS |
| VF16326 |   Non-current assets coverage ratio |
| VF16331 |   Obtained funding over total liabilities (QS) |
| VF16338 |  Cost of obtained funding |
| VF16340 |   Financial Cost Effect |
| VF16345 |   Operating effect |
| VF16346   | Other financial income effect |
| VF16348   | Compound leverage factor - QS |
| VF16350   | Tax burden |
| VF16351 |   Return on sales |
| VF16353 |   Return on assets |
| VF16355 | GVA over output - QS |
| VF16357   | EBITDA over Turnover |
| VF16358   | Degree of combined leverage |
| VF16359   | Degree of operating leverage |
| VF16360  | Degree of other financial income leverage |
| VF16361   | Degree of financial leverage |
| VF16362   | Days sales outstanding (days) |
| VF16363  | Days sales outstanding concerning non-residents (days) |
| VF16364  | Days payable outstanding (days) |
| VF16365  | Days payable outstanding concerning non-residents (days) |
| VF16366  | Days sales of inventory (days) |
| VF16367  | Asset turnover (times) - QS |
| VF16369  | Net working capital requirements over turnover |
| VF16370  | Coefficient GVA over fixed non-financial assets |
| VF16371  | Coefficient GVA over employee costs |
| VF16373   | Coefficient Fixed non-financial assets over employee expenses |
| VF16374   | Suppliers - QS |
| VF16375   | Employees - QS |
| VF16376   | Banks and other sources of funding - QS |
| VF16377   | State - QS |
| VF16378   | Enterprise - self-financing - QS |
| VF16379   | Others - QS |
| VF16426   | Interest expenses / EBITDA |
| VF17747   | Asset turnover ratio |
| VF17749   | Profit or loss of the year before taxes (EBT) / Equity |
| VF17750   | Gross value added / Net turnover |
| VF17752   | Profit or loss of the year before taxes (EBT) / Net turnover |
| VF17753  | Equity / Total assets |
| VF17754  | Trade payables / Total assets |
| VF17755   | Total income / Net turnover |
| VF17756  | Total expenses / Net turnover |
| VF17757  | Financial fixed assets / Total assets |
| VF17758  | Trade receivables / Total assets |
| VF17759   | Other financial assets and cash and bank / Total assets |


## G.    Cash-Flows File
With the introduction of SNC, firms are required to report all cash (and equivalents) receipts and payments by type of activity: operating, investing and financing activities. Therefore, this file contains information from 2010 onwards. According to the filling instructions, the reporting of the cash-flow information is only required for firms reporting under two regimes: International Accounting Standards (*regime*=1) and Accounting and Financial Reporting Standards (*regime*=2). The missing values in Stata of all the variables in this file were coded as ".a" whenever the reporting is not mandatory for the accounting standards adopted by the firm.

### G1. Identifiers
`Firm identifier` (*tina*) – Unique identifier that enables tracking the legal entity over time. *tina* is the anonymized tax identification number.

`Reference year of the data` (*ano*) – Reference year of the data.

### G2. Variables reported according to SNC
| Variable Name | Variable Description |
| :------: | :------- |
| VF13265    | Operating Activities - Cash receipts from customers |
| VF13266    | Operating Activities - Cash payments to suppliers    |
| VF13267    | Operating Activities - Cash payments to employees    |
| VF13268    | Operating Activities - Total cash generated from operating activities    |
| VF13269    | Operating Activities - Cash payments/receipts from income tax    |
| VF13270    | Operating Activities - Other cash payments/receipts    |
| VF13271    | Operating Activities - Total cash-flows from operating activities    |
| VF13272    | Investing Activities - Cash payments relating to tangible fixed assets |
| VF13273    | Investing Activities - Cash payments relating to intangible assets |
| VF13274    | Investing Activities - Cash payments relating to financial fixed assets |
| VF13275    | Investing Activities - Cash payments relating to other assets |
| VF13276    | Investing Activities - Cash receipts from tangible fixed assets |
| VF13277    | Investing Activities - Cash receipts from intangible assets |
| VF13278    | Investing Activities - Cash receipts from financial fixed assets |
| VF13279    | Investing Activities - Cash receipts from other assets |
| VF13280    | Investing Activities - Cash receipts from investment subsidies |
| VF13281    | Investing Activities - Cash receipts from interest income |
| VF13282    | Investing Activities - Cash receipts from dividends    |
| VF13283    | Investing Activities - Total cash-flows from investing activities |
| VF13284    | Financing Activities - Cash receipts from obtained funding |
| VF13285    | Financing Activities - Cash receipts from paid-up capital and other equity instruments |
| VF13286    | Financing Activities - Cash receipts from loss coverage    |
| VF13287    | Financing Activities - Cash receipts from donations    |
| VF13288    | Financing Activities - Cash receipts from other financial operations |
| VF13289    | Financing Activities - Cash payments relating to obtained funding    |
| VF13290    | Financing Activities - Cash payments relating to interest expenses    |
| VF13291    | Financing Activities - Cash payments relating to dividends |
| VF13292    | Financing Activities - Cash payments relating to capital reduction and other equity instruments    |
| VF13293    | Financing Activities - Cash payments relating to other financing activities    |
| VF13294    | Financing Activities - Total cash-flows from financing activities    |
| VF13295    | Total - Net increase in cash and cash equivalents |
| VF13296    | Total - Effect of currency exchange differences |
| VF13297    | Total - Cash and cash equivalents at the beginning of the period |
| VF13298    | Total - Cash and cash equivalents at the end of the period |




## H.    Information by Sector of Activity File
This file contains information for each economic activity carried on by the firm. All economic activities should be considered, including the production and supply of goods and services and support activities such as accounting and administrative services. Values reported according to POC detail information by sector of activity and geographic market. The values reported for each activity have to sum up to the overall values reported by the firm.

### H1. Identifiers
`Firm identifier` (*tina*) – Unique identifier that enables tracking the legal entity over time. *tina* is the anonymized tax identification number.

`Reference year of the data` (*ano*) – Reference year of the data.

`Number of order of the sector` (*numordem*) - Number of order identifying each sector of activity of the firm in that year.

### H2. Sector of activity

`Portuguese classification of economic activities` (*VF6105*) - categorical variable providing information on the economic activity. This variable is available when the firm reports information according to POC. It suffers a change in classification in 2008, when the Revision 2.1 of the Classification of Economic Activities is replaced by the Revision 3 of that classification.

`Portuguese classification of economic activities (Rev. 3)` (*VF53120*) - categorical variable providing information on the economic activity. This variable follows the Revision 3 of the Classification of Economic Activities. It is available since 2010, when firms report the information according to SNC.

For a complete list of codes see the variables *cae2* and *cae3* in the auxiliary file [var_rosto.html](./aux_files/variables_description/var_rosto.html).

### H3. Variables reported according to POC
| Variable Name |    Variable Description |
| :---: | :-----|
| VF04106 |    Internal Market - Total sales by sector |
| VF04107 |    Internal Market - Total services by sector |
| VF04108 |    Internal Market - Total purchases by sector |
| VF04109 |    Internal Market - Total supplies and external services by sector |
| VF04110 |    EU Market - Total sales by sector |
| VF04111 |    EU Market - Total services by sector |
| VF04112 |    EU Market - Total purchases by sector |
| VF04113 |    EU Market - Total supplies and external services by sector |
| VF04114 |    Extra-EU Market - Total sales by sector |
| VF04115 |    Extra-EU Market - Total services by sector |
| VF04116 |    Extra-EU Market - Total purchases by sector |
| VF04117 |    Extra-EU Market - Total supplies and external services by sector |
| VF04118 |    Total sales by sector |
| VF04119 |    Total services by sector |
| VF04120 |    Total purchases by sector |
| VF04121 |    Total supplies and external services by sector |
| VF04124 |    Total cost of goods sold and material consumed by sector |
| VF04122 |    Cost of goods sold by sector |
| VF04123 |    Cost of material consumed by sector |
| VF04125 |    Variation in production by sector |
| VF04126 |    Average number of employees by sector |
| VF04129 |    Total employee costs by sector |
| VF04127 |    Employee costs - Salaries by sector |
| VF04128 |    Employee costs - Others by sector |


### H4. Variables reported according to SNC
| Variable Name | Variable Description |
| :---: | :-------------|
| VF15571    | Total sales by sector |
| VF15572    | Sales - Goods by sector |
| VF15573    | Sales - Finished and intermediate products; Subproducts, wastes and scrap; Products and work in progress by sector |
| VF15574    | Sales - Biological assets by sector |
| VF15575    | Services by sector |
| VF15576    | Purchases by sector |
| VF15577    | Supplies and external services by sector |
| VF15578    | Total cost of goods sold and material consumed by sector |
| VF15579    | Cost of goods sold and material consumed - Goods by sector |
| VF15580    | Cost of goods sold and material consumed - Raw and subsidiary materials and consumables by sector |
| VF15581    | Cost of goods sold and material consumed - Biological assets (purchases) by sector |
| VF15582    | Variation in production by sector |
| VF15583    | Average number of employees by sector |
| VF15584    | Total employee expenses by sector |
| VF15585    | Employee expenses - Salaries by sector |
| VF15586 |    Employee expenses - Others (including pensions) by sector |



# Basic Descriptive Statistics

Table 2- Number of firms over the data period (as of June 2019 extraction)

```
    quietly use "S:/data/Products/CB/2019_06/CB_Annual/Output/Data/Firms/2006/CB_A_YFRM_2006_JUN19_ROSTO_V01.dta", clear
    quietly append using "S:/data/Products/CB/2019_06/CB_Annual/Output/Data/Firms/2007/CB_A_YFRM_2007_JUN19_ROSTO_V01.dta"
    quietly append using "S:/data/Products/CB/2019_06/CB_Annual/Output/Data/Firms/2008/CB_A_YFRM_2008_JUN19_ROSTO_V01.dta"
    quietly append using "S:/data/Products/CB/2019_06/CB_Annual/Output/Data/Firms/2009/CB_A_YFRM_2009_JUN19_ROSTO_V01.dta"
    quietly append using "S:/data/Products/CB/2019_06/CB_Annual/Output/Data/Firms/2010/CB_A_YFRM_2010_JUN19_ROSTO_V01.dta"
    quietly append using "S:/data/Products/CB/2019_06/CB_Annual/Output/Data/Firms/2011/CB_A_YFRM_2011_JUN19_ROSTO_V01.dta"
    quietly append using "S:/data/Products/CB/2019_06/CB_Annual/Output/Data/Firms/2012/CB_A_YFRM_2012_JUN19_ROSTO_V01.dta"
    quietly append using "S:/data/Products/CB/2019_06/CB_Annual/Output/Data/Firms/2013/CB_A_YFRM_2013_JUN19_ROSTO_V01.dta"
    quietly append using "S:/data/Products/CB/2019_06/CB_Annual/Output/Data/Firms/2014/CB_A_YFRM_2014_JUN19_ROSTO_V01.dta"
    quietly append using "S:/data/Products/CB/2019_06/CB_Annual/Output/Data/Firms/2015/CB_A_YFRM_2015_JUN19_ROSTO_V01.dta"
    quietly append using "S:/data/Products/CB/2019_06/CB_Annual/Output/Data/Firms/2016/CB_A_YFRM_2016_JUN19_ROSTO_V01.dta"
    quietly append using "S:/data/Products/CB/2019_06/CB_Annual/Output/Data/Firms/2017/CB_A_YFRM_2017_JUN19_ROSTO_V01.dta"
    label language en
    table ano, contents(freq) center
```

# Legislation
The most relevant legislation for IES that may have an impact on CB is presented below:

-    **Decree-Law no. 8/2007**, January 17 – this Decree-Law creates IES, which is a platform allowing firms to fulfill four different reporting duties: to send the Annual Declaration on Accounting and Tax Information to the Ministry of Finance, the Financial Statements to the Ministry of Justice and the obligation to provide statistical information to the National Statistics Institute and to *Banco de Portugal*;

  [Internal Link](./aux_files/legislation/Decreto-Lei_8-2007.pdf) /
  [External Link](https://dre.pt/web/guest/pesquisa/-/search/522813/details/normal?l=1)

-    **Ordinance no. 208/2007**, February 16 – this ordinance approves the form used by firms to report information on IES. The form is composed by a cover sheet and the following Annexes: A, A1, B, B1, C, C1, D, E, F, G, H, I, L, M, N, O, P, Q, R, S, T. These changes apply to the fiscal year of 2006 onwards;

  [Internal Link](./aux_files/legislation/Portaria_208_2007.pdf) /
  [External Link](https://dre.pt/pesquisa/-/search/517868/details/maximized)

-    **Ordinance no. 499/2007**, April 30 – establishes how firms are required to submit IES electronically. This Ordinance also clarifies that the Directorate General for Informatics and Assistance to Taxation and Custom Services (Ministry of Finance and Public Administration) is responsible to send the relevant information to the Institute of Registration and Notary Affairs (IRN) (Ministry of Justice). The latter is then required to send the data to the National Statistics Institute and *Banco de Portugal*;

  [Internal Link](./aux_files/legislation/Portaria_499-2007.pdf) /
  [External Link](https://dre.pt/pesquisa/-/search/521203/details/maximized)

-    **Ordinance no. 562/2007**, April 30 – regulates the submission of the financial statements using IES and establishes a submission fee of 85€ that needs to be paid within 5 working days;

  [Internal Link](./aux_files/legislation/Portaria_562-2007.pdf) /
  [External Link](https://dre.pt/pesquisa/-/search/521224/details/maximized)

-    **Ordinance no. 8/2008**, January 3 – approves a new form that firms are required to fill in to submit IES after January 1st 2008 independently of the fiscal year being reported. It changes the cover sheet and the following Annexes of IES: A, A1, B, C, C1, F, L, M, N, R, S, T. All other annexes remain unchanged;

  [Internal Link](./aux_files/legislation/Portaria_8-2008.pdf) /
  [External Link](https://dre.pt/web/guest/pesquisa/-/search/386794/details/maximized)

-    **Ordinance no. 245/2008**, March 27 – changes the Ordinance no. 499/2007 by establishing that those firms reporting the information using the International Accounting Standards or those with consolidated accounts are required to scan the documentation and send it electronically. This applies to the fiscal period of 2007 onwards;

  [Internal Link](./aux_files/legislation/Portaria_245_2008.pdf) /
  [External Link](https://dre.pt/pesquisa/-/search/246371/details/maximized)

-    **Ordinance no. 64-A/2011**, February 3 – to accommodate the changes on the accounting system, this ordinance approves new versions of the following Annexes of IES: A, B, C, D, F, G, I, L, M , R;

  [Internal Link](./aux_files/legislation/Portaria_64-A_2011.pdf) /
  [External Link](https://dre.pt/pesquisa/-/search/666701/details/maximized)

-    **Ordinance no. 271/2014**, December 23 – the cover sheet and Annexes A, B, C, D, I of IES are changed to accommodate the alterations to the legislation on the Corporate Income Tax and complement the statistical information;

  [Internal Link](./aux_files/legislation/Portaria_271_2014.pdf) /
  [External Link](https://dre.pt/home/-/dre/65983202/details/maximized?p_auth=8AGl1gr6)

-    **Ordinance no. 370/2015**, October 20 – revokes Ordinance no. 499/2007 and establishes that the Tax Authority (Ministry of Finance) is required to send the information collected through IES electronically to the Institute of Registration and Notary Affairs (IRN) (Ministry of Justice). Subsequently, the latter is responsible to send the information to *Banco de Portugal*, National Statistics Institute and Directorate-General for Economic Activities.

  [Internal Link](./aux_files/legislation/Portaria_370_2015.pdf) /
  [External Link](https://dre.pt/home/-/dre/70748594/details/maximized?p_auth=q6uHsEL4)

Given that *Central de Balanços* provides financial information such as Balance Sheet and Profits and Losses Statement data, the legislation implementing changes to the accounting standards should also be briefly enumerated:

-    **Decree-Law no. 158/2009**, July 13 – revokes the Official Chart of Accounts (POC) and creates the Accounting Standards System (SNC).[^31]  Starting in the first fiscal period after January 1, 2010 firms are required to adopt the “Accounting and Financial Reporting Standards” or the “Accounting and Financial Reporting Standards for Small-Sized Entities” when reporting the financial statements. If the firm chooses to report according to the “Accounting and Financial Reporting Standards for Small-Sized Entities” then it is required to report a smaller number of variables. This option is available for firms satisfying at least two of the following conditions: i) total assets below 500.000 euros; ii) total gross sales and other income lower than 1.000.000 euros or; iii) average number of employees less than 20;

  [Internal Link](./aux_files/legislation/Decreto-Lei_158_2009.pdf) /
  [External Link](https://dre.pt/pesquisa/-/search/492428/details/maximized)

- **Ordinance no. 986/2009**, September 7 - approves the financial statements under the Accounting Standards System (SNC) (Balance Sheet, Profit and Loss Statement itemized and by activity, Statement of Changes in Equity and Cash Flows);

  [Internal Link](./aux_files/legislation/Portaria_986_2009.pdf) /
  [External Link](https://dre.pt/pesquisa/-/search/489212/details/maximized)

-    **Law no. 35/2010**, September 2 – introduces a new simplified reporting standard for Micro-Entities, the "Accounting and Financial Reporting Standards for Micro-Entities”. A micro-entity is defined as a firm that falls below in at least two of the following criteria at the balance sheet date: i) total assets equal to 500.000 euros; ii) net turnover equal to 500.000 euros; or iii) average number of employees equal to 5. If a firm does not comply for two consecutive fiscal periods with at least two of the criteria to be considered a Micro-Entity, it is no longer subject to a simplified reporting standard. Only after complying again with at least two of the criteria for two consecutive fiscal periods, the firm is entitled to report according to the "Accounting and Financial Reporting Standards for Micro-Entities”;

  [Internal Link](./aux_files/legislation/Lei_35_2010.pdf) /
  [External Link](https://dre.pt/pesquisa/-/search/344271/details/normal?q=Lei+n%C2%BA35%2F2010%2C%20de+2+de+setembro)

-    **Decree-Law no. 36-A/2011**, March 9 – approves the “Accounting and Financial Reporting Standards for Micro-Entities”. Micro-Entities are only required to report a modified version of the Balance Sheet, the Profits and Losses Statement and the respective Annexes. They are exempt to fill in, for example, the Cash-Flows Statement and Changes in Equity.

  [Internal Link](./aux_files/legislation/Decreto-Lei_36-A_2011.pdf) /
  [External Link](https://dre.pt/pesquisa/-/search/647296/details/maximized)

[^31]: The Accounting Standards System is not mandatory for individuals carrying on a commercial, industrial or agricultural activity with a three-year average turnover of less than 150.000 euros.


# Auxiliary Files
For a description of each variable in each dataset (name, unit of measurement, data and storage type, format, year of first and last observation), an account of the changes occurred over time, summary statistics for each dataset and a codebook for each dataset please check the following auxiliary files[^32]:

| File | Description of Variables | Summary Statistics | Codebook | Dataset Description |
| :---- | :----: | :----: | :----: |  :----: |
| Summary of all variables (Portuguese and English labels) | [variables_pt_en.html](./aux_files/variables_description/variables_pt_en.html) |
| General Information File | [var_rosto](./aux_files/variables_description/var_rosto.html) | [stat_Rosto](./aux_files/descriptive_statistics/stat_Rosto.html) | [cdbk_Rosto](./aux_files/codebook/cdbk_Rosto.html) | [dscr_Rosto](./aux_files/describe_dataset/dscr_Rosto.html) |
| Economic and Financial Information File |    [var_contas](./aux_files/variables_description/var_contas.html) | [stat_Contas](./aux_files/descriptive_statistics/stat_Contas.html) |     [cdbk_Contas](./aux_files/codebook/cdbk_Contas.html) | [dscr_Contas](./aux_files/describe_dataset/dscr_Contas.html) |
| Employment Information File |    [var_emprego](./aux_files/variables_description/var_emprego.html) | [stat_Pessoal](./aux_files/descriptive_statistics/stat_Pessoal.html) |     [cdbk_Pessoal](./aux_files/codebook/cdbk_Pessoal.html) | [dscr_Pessoal](./aux_files/describe_dataset/dscr_Pessoal.html) |
| Trade Information per Market File |    [var_mg](./aux_files/variables_description/var_mg.html) | [stat_MG](./aux_files/descriptive_statistics/stat_MG.html) |     [cdbk_MG](./aux_files/codebook/cdbk_MG.html) | [dscr_MG](./aux_files/describe_dataset/dscr_MG.html) |
| Corporate Actions File | [var_amarc](./aux_files/variables_description/var_AMARC.html) | [stat_amarc](./aux_files/descriptive_statistics/stat_AMARC.html) | [cdbk_amarc](./aux_files/codebook/cdbk_AMARC.html) | [dscr_amarc](./aux_files/describe_dataset/dscr_AMARC.html) |
| Economic and Financial Indicators File |    [var_indicadores](./aux_files/variables_description/var_indicadores.html) | [stat_Indic](./aux_files/descriptive_statistics/stat_Indic.html) |     [cdbk_Indic](./aux_files/codebook/cdbk_Indic.html) | [dscr_Indic](./aux_files/describe_dataset/dscr_Indic.html) |
| Cash Flows File |    [var_cashflow](./aux_files/variables_description/var_cashflow.html) | [stat_FluxosCaixa](./aux_files/descriptive_statistics/stat_FluxosCaixa.html) |     [cdbk_FluxosCaixa](./aux_files/codebook/cdbk_FluxosCaixa.html) | [dscr_FluxosCaixa](./aux_files/describe_dataset/dscr_FluxosCaixa.html) |
| Information by Sector of Activity File |    [var_bycae](./aux_files/variables_description/var_bycae.html) | [stat_byCAE](./aux_files/descriptive_statistics/stat_byCAE.html) |     [cdbk_byCAE](./aux_files/codebook/cdbk_byCAE.html) | [dscr_byCAE](./aux_files/describe_dataset/dscr_byCAE.html) |


[^32]: The Summary Statistics, Codebook and Dataset Description files are available on BPLIM's servers.

# Useful Links
[Sector Tables (Quadros de Setor)](https://www.bportugal.pt/en/page/sector-tables)

[Informação Empresarial Simplificada (IES)](http://www.ies.gov.pt/site_IES/site/home.htm)

[Statistical Bulletin](https://www.bportugal.pt/en/publications/banco-de-portugal/all/123)


# Frequently Asked Questions
The most frequently asked questions can be found [here](./aux_files/FAQ/faq.html).
If you have a question that is not covered in this manual, please send an email to bplim@bportugal.pt.


# Citation of this dataset
Banco de Portugal Microdata Research Laboratory (BPLIM) (2019): Central Balance Sheet Annual Data. Extraction: June 2019. Version: V1. BANCO DE PORTUGAL. Dataset. https://doi.org/10.17900/CB.CBA.Jun2019.V1


## References
Banco de Portugal (2009). Estatísticas das Sociedades Não Financeiras da Central de Balanços- Documento Metodológico. Departamento de Estatística.

Banco de Portugal (2014). Quadros do Setor e Quadros da Empresa e do Setor- Notas Metodológicas Série Longa 1995-2013. Estudos da Central de Balanços. Lisboa.

Banco de Portugal (2015). Central de Balanços. Cadernos do Banco de Portugal. Lisboa

Oliveira, Mariana (2016). Bases de Microdados com Informação Económico-Financeira da IES (Informação Empresarial Simplificada). Tese de Mestrado. Faculdade de Economia da Universidade do Porto. Porto.







