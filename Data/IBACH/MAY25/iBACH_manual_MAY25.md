---
title: Spanish and Portuguese Companies Microdata (iBACH) - Data Manual
subtitle: Extraction Date - May 2025
author: BPLIM
date: 11 June 2025
abstract: 'The Spanish and Portuguese Companies Microdata contain economic and financial granular information on non-financial Spanish and Portuguese corporations from iBACH. This dataset derives from BACH dataset. BACH is a database of aggregated and harmonized accounting data of non-financial companies, based on national accounting standards (individual annual accounts).'
doi: 10.17900/iBACH.May2025.V1 | 10.48719/BELab.iBACH0823_01
pdf-engine: pdflatex
execute:
  echo: false
format:
  pdf:
    toc: true
    code-overflow: wrap
  html:
    toc: true
    embed-resources: true
    footnotes-hover: true
    code-fold: true
    code-copy: true
    theme: default
    code-overflow: wrap
jupyter: nbstata
---

# General Information

> **Dataset Designation in English**: Spanish and Portuguese Companies Microdata (iBACH)

> **Data Type**: Longitudinal Data

> **Unit of Analysis**: Firms

> **Frequency**: Annual

> **Start Year**: 2008

> **Most recent year**: 2023

> **Reference date**: The data reports to the fiscal period declared by the firm. The reference period is defined as the year with the larger number of days of the exercise.

> **Data Organization**: Data is organized in one file per country and reference year. In all files each row corresponds to one firm in a given year. All files are available in .csv format.

> **Version of the data**: The data made available by BPLIM and BELab corresponds to a data freeze at a certain time of the year. Therefore, all files contain the information as reported in the extraction date. The most recent update of the data occurred in May 2025.

> **Languages Available**: Variable labels and value labels are available in English.

> **Related Datasets**: BPLIM also makes available the *Central Balance Sheet Annual Data* and the *Central Balance Sheet Harmonized Panel Data* with more detailed economic and financial information for Portuguese non-financial corporations.

> **Digital Object Identifier**: 10.17900/iBACH.May2025.V1 | 10.48719/BELab.iBACH0823_01

> **Access**: This dataset is also made available by [BELab data laboratory](https://www.bde.es/wbe/en/para-ciudadano/servicios/belab/).

> **New in this extraction**: Data for 2023 is now available for Portugal and Spain. The Portuguese iBACH data was revised for the period 2019-2022 and a new classification for the variable `dregio` was introduced for the whole period (NUTS III - version 2024).

# Geographical Coverage

The data refers to firms located in Portugal and Spain.

# Population

iBACH covers the population of all Portuguese non-financial corporations and a sample of Spanish non-financial companies with coverage exceeding 50% of Gross Value Added and Employment.

# Methodology

BACH (Bank for the Accounts of Companies Harmonized) is managed by the European Committee of Central Balance-Sheet Data Offices (ECCBSO). The ECCBSO is an informal body of experts from National Central Banks and National Statistical Institutes of Europe. Under the aegis of the ECCBSO, the BACH Working Group is responsible for maintaining and improving the BACH database.

*Banco de Portugal* and *Banco de España* celebrated a Protocol to provide the Portuguese and Spanish BACH microdata (iBACH) for research purposes. This data set contains economic and financial information for non-financial corporations of both countries.

The **Spanish data** come from the mandatory deposits of annual accounts in the Mercantile Registries, on the basis of the Agreement signed between the Banco de España and CORPME. Analytical variables are offered, constructed by the Central Balance Sheet Data Office on the basis of the basic information in the annual accounts.

The **Portuguese data** come from the Annual data of the Central Balance-Sheet Database. The information is gathered from Annex A of IES - Simplified Corporate Information (*Informação Empresarial Simplificada*, in the Portuguese acronym).

In December of year N the information for the year N-1 is uploaded for the first time and year N-2 is updated for the last time.

Every year BPLIM and BELab create a data freeze. The most recent version of the data was extracted on May 2025 and includes data from 2008 to 2023.

This manual summarizes the variables available. For more complete information please see the [BACH's User Guide](https://www.bach.banque-france.fr/documents/Summary_Userguide.pdf).

# Description of Files

The iBACH data is organized in one file per country and reference year:

| Type of Information  | File Name |
| :--- | :--- |
| **iBACH - Portugal** | BPLIM_IBACH_A_YFRM_*yyyy*_*eeee*_PT_V01.csv |
| **iBACH - Spain** | BELab_iBACH0823_01_*yyyy*_ES_Anonimized.csv  |

Where *A* stands for anonymized, *yyyy* corresponds to the reference year, and *eeee* reports the extraction date.

All files contain a unique firm identifier (*did*) that does not allow the matching with other datasets available at BPLIM or BELab. All datasets are anonymized.

Files are provided in a *.csv* file with all the metadata available in the file:
[ibach_meta_YFRM_MAY25_PTES_V01](./aux_files/metafiles/ibach_meta_YFRM_MAY25_PTES_V01.xlsx).

# Description of Variables

Below we provide a general description of the variables included in the data. The metadata files and more detailed information about each variable is available in the [“Auxiliary Files” section](#auxiliary-files).

## General Information

### Identifiers

`Firm identifier` (*did*) – Unique identifier that enables tracking the legal entity over time.[^7] *did* is the anonymized firm identifier, which is country specific.

`Reference year of the data` (*dyear*) – Period of reference for the accounting exercise.

[^7]: The identifier may change for a residual number of Spanish companies over time.

<br>
<br>

`Localization of the firm` (*dregio*) - Localization of the firm (or the headquarter of the firm), at NUTS-3 level. For a complete list of codes see the metadata file [iBACH_meta_YFRM_MAY25_PTES_V01](./aux_files/metafiles/iBACH_meta_YFRM_MAY25_PTES_V01.xlsx). Codes started by "1" are specific to Spain and by "2" to Portugal.

<br>
<br>

`Country of the firm` (*dcountry*) - Country where the firm is located according to the 3-digit numeric code ISO 3166-1.

| Code | Designation |
| :---: | :--- |
| 620 | 620 Portugal |
| 724 | 724 Spain |

<br>
<br>

`Legal form` (*dnlegal*) - Legal form, which results from the combination of a two-letter ISO code and letters identifying the legal form according to a national classification scheme. Codes started by "1" are specific to Spain and by "2" to Portugal.

| Code | Designation |
| :---: | :--- |
| 101 | 101 ESA Public limited companies |
| 102 | 102 ESB Private limited companies |
| 103 | 103 ESC Collective companies |
| 104 | 104 ESD Limited partnership companies |
| 105 | 105 ESF Cooperative companies |
| 106 | 106 ESG Associations |
| 107 | 107 ESN Foreign Entities |
| 108 | 108 ESQ Public organizations |
| 109 | 109 ESV Others |
| 110 | 110 ESW Permanent Establishments of Non-Resident Entities in Spain  |
| 201 | 201 PTACEEIE Complementary Grouping of Companies and European Economic Interest Grouping |
| 202 | 202 PTBranc Branch companies |
| 203 | 203 PTCooper Cooperative companies |
| 204 | 204 PTLda Private limited companies |
| 205 | 205 PTNProf Non-profit organizations |
| 206 | 206 PTOthers Others |
| 207 | 207 PTS.A. Public limited companies |
| 208 | 208 PTSocPro Professional societies |

<br>
<br>

`Sector of activity` (*dsector*) - Main economic activity of the firm, according to the NACE Rev. 2 classification at 4-digit level.[^5] For a complete list of codes see the metadata file [iBACH_meta_YFRM_MAY25_PTES_V01](./aux_files/metafiles/iBACH_meta_YFRM_MAY25_PTES_V01.xlsx).

[^5]: There are some codes that are invalid according to NACE Rev. 2 classification, but valid according to each country's national classifications. This is the case of codes *5511* and *5512* ('Hotels and similar establishments with restaurant' and 'Hotels and similar establishments without restaurant', respectively) for Portuguese data. The same occurs in the Spanish data, for example, with codes *1021* and *1022* ('Processing of fish, crustaceans and molluscs' and 'Manufacture of canned and preserved fish', respectively).

<br>
<br>

`Year of birth or incorporation` (*dyincorp*) - Year of birth. With few exceptions, it corresponds to the year of incorporation in the register or the database used to fill in the financial statements.

<br>
<br>

`Firm´s status of activity`(*dcease*) - Firm´s status of activity.

| Code | Designation |
| :---: | :--- |
| 1	| 1 Still exists |
| 2	| 2 Has been merged with other firms |
| 3 | 3 Has been liquidated |

<br>
<br>

`Year of liquidation of the firm`(*dyliquid*) - Year when the firm ceased its activity (when applicable).

<br>
<br>

`Number of employees for the reference period`(*dnumberempl*) - Number of employees for the reference period (the year), with regards to the firm's payroll. In the Spanish data this correspond to the number of employees in full time equivalents (FTE). The Portuguese data includes unpaid employees and employees working in establishments located abroad.

<br>
<br>

`Number of months for the account exercise` (*dnumbermth*) - Number of months on which the account exercise has been conducted.

<br>
<br>

`Non-response treatment` (*dunrt*) - Non-response treatment for the full data of the firm.

| Code | Designation |
| :---: | :--- |
| 0	| 0 Reported |
| 1 | 1 Estimated |

<br>
<br>

`Active firm` (*dactive*) - Non-active firms are those that meet one of the conditions[^3]:
    (i) Assets and Liabilities >0 and all the items of the profit & loss account =0, or
    (ii) whenever `dcease`= 2 or `dcease`=3

| Code | Designation |
| :---: | :--- |
| 0	| 0 Non-active |
| 1 | 1 Active |

[^3]: Condition is not considered to be met when the affected profit & loss account variables have been rounded to zero in iBACH database, but are originally different to this value.

<br>
<br>

`Accounting regime` (*dregime*) - Type of accounting report of the firms.

| Code | Designation |
| :---: | :--- |
| 1	| 1 Ordinary |
| 2	| 2 Abridged |
| 3 | 3 Micro |

<br>
<br>

## Economic and Financial Variables

The blocks of information that the user can access are the income statement and the balance sheet. The variables are presented in **thousands of euros**.[^4]

[^4]: Zero does not mean missing value. In some cases it is not possible to distinguish between zeros and missing values.

### Income Statement

| Variable name | Short description | Full description |
| :---: | :--- | :---------------------- |
| i0100 | Net turnover | Includes sales of goods and services net of returns, deductions and rebates. Sales are net of VAT and Excise taxes. |
| i0200 | Variation in stocks of finished goods and work in progress | Includes change in inventories of production recognized in the income statement. |
| i0300 | Capitalised production  | Includes costs capitalized by the entity recognized as income in the period. |
| i0400 | Other income | Includes other income not identified in previous items (i0100, i0200 and i0300). |
| i0410 |    Of which: Operating subsidies and supplementary operating income  | Details of other income relating to operating subsidies and supplementary operating income. |
| i0420 |    Of which: Financial income | Details of other income relating to financial income. |
| i0500 | Cost of goods sold, materials and consumables  | Includes cost of materials and consumables used and the cost of goods sold in the period. |
| i0600 | External supplies and services | Includes expenses with external supplies and services in the period. The costs of external human resources (outsourcing) are included in this item. |
| i0700 | Staff costs | Includes expenses with the staff recognized in the period.  |
| i0800 | Other expenses | Includes other expenses not identified in previous items (i0500, i0600 and i0700). |
| i0810 | Of which: Operating taxes and other operating charges | Details of other expenses relating to operating taxes and other operating charges. |
| i0820 | Of which: Provisions (net of reversals) | Details of other expenses relating to Provisions (net of reversals) |
| i0830 | Of which: Financial expenses other than interests on financial debt | Details of other expenses relating to financial expenses, except interests on financial debts (included in i1000) |
| i0840 | Of which: Extraordinary expenses and impairments (net of reversals), except on inventories and receivables | Details of other expenses relating to extraordinary expenses and reduction/increase in fair value and impairment charges (net of reversals), except impairments (net of reversals) included in i0850 |
| i0850 | Of which: Impairments (net of reversals) on inventories and receivables | Details of other expenses relating to impairment charges (net of reversals) on inventories and receivables |
| i0900 | Depreciation and amortization on intangible and tangible fixed assets | Includes depreciation and amortization of assets included in the items a1100 and a1200 recognized in the period. |
| i1000 | Interests on financial debts | Includes financing costs recognized in the period. |
| i1100 | Tax on profit  | Includes income taxes recognized in the period. |
| it100 | Total income  | (i0100+i0200+i0300+i0400) |
| it200 | Total expenses  | (i0500+i0600+i0700+i0800+i0900+i1000+i1100) |
| it300 | Net profit or loss for the period  | (it100-it200) |
| i0120 | Exports | Total exports by the firm (goods or services produced in the entity's country that are sold to someone in another country) |
| i0130 |    Imports | Total imports by the firm (foreign goods and services bought) |
| f1000 |    Dividends paid | Payments to shareholders. This variable is only reported since 2010 for Portugal. |
| f2000 | Cash flow | Variation in Cash and bank (a7000). This variable is only reported since 2010 for Portugal. |
| f2100 | Operating cash flow | Cash flow from the operating activities. This variable is only reported since 2010 for Portugal and 2013 for Spain. |
| f2200 | Investing cash flow | Cash flow from investment activities. This variable is only reported since 2010 for Portugal and 2013 for Spain. |
| f2300 | Financing cash flow | Cash flow from financing activities. This variable is only reported since 2010 for Portugal and 2013 for Spain. |

### Balance Sheet - Assets [^6]

| Variable name | Short description | Full description |
| :---: | :--- | :---------------------- |
| a1000 | Fixed assets |  (a1100+a1200+a1300) |
| a1100 | Intangible fixed assets | Includes brands, patents, copyrights, licenses, etc., even if such assets are held under finance lease contracts. This item also includes the Goodwill recognized separately. |
| a1200 | Tangible fixed assets | Includes Lands, buildings, machineries, administration and transport equipments, etc., even if such assets are held under finance lease contracts. This item also includes the bearer biological assets and investment properties. |
| a1300 | Financial fixed assets | Includes holdings of shares in the capital of other entities on a continuing basis, as well as loans made to such entities. |
| a1310 | of which: Shares in affiliated undertakings and participating interests | Details of financial fixed assets relating to investments in (holdings of shares in the capital of) associates, subsidiaries and jointly controlled entities. |
| a2000 | Inventories | Includes raw materials and consumables, goods, work in progress and finished products, as well as consumable biological assets. |
| a2100 | of which: Payments on account | Details of inventories relating to payments on account. |
| a3000 | Trade receivables | Includes credit granted to customers for sales or services net of advances received (except for payments received on account of orders, included in l5000). |
| a4000 | Other receivables | Includes other accounts receivable (except trade receivables), as well as non-current assets held for sale (net of any associated liabilities). |
| a4100 | Current |  |
| a5000 | Deferred assets | Includes deferred tax assets and expenses to be recognized in future periods. |
| a6000 | Other financial assets, current | Includes financial assets held for trading and derivatives. |
| a7000 | Cash and bank | Includes the amount available in cash, demand deposits and other deposits in financial institutions. |
| a0000 | **TOTAL BALANCE SHEET** |  (a1000+a2000+a3000+a4000+a5000+a6000+a7000)=e0000+l0000 |

<br>

[^6]: Assets are presented at net value of accumulated depreciation, accumulated impairment losses and other adjustments.

### Balance Sheet - Equity and Liabilities

| Variable name | Short description | Full description |
| :---: | :--- | :---------------------- |
| e1000 | Capital, reserves, earnings and other equity instruments | Includes paid capital, reserves, treasury stock and other equity instruments. Subscribed capital but not paid is deducted from this item. This item also includes the cumulative net income of prior periods, the net income for the period as well as dividends paid in advance. |
| e1100 |    Of which: Paid capital | Amount of capital "paid in" by investors during common or preferred stock issuances, including the par value of the shares themselves. Paid-in capital represents the funds raised by the business from selling its equity and not from ongoing operations. |
| e1200 |    Of which: Reserves other than revaluations, adjustments on financial investments and other comprehensive income | Accumulated capital surplus of a company reinvested in the company. It includes both  legal reserves and voluntary reserves. |
| e2000 | Revaluations, adjustments on financial investments and other comprehensive income | Includes surplus revaluation of tangible and intangible assets, adjustments on financial assets recognized in equity and other changes in equity. |
| e0000 | **TOTAL EQUITY**  | (e1000+e2000) |
| lp000 | Provisions | Includes all provisions. |
| lp100 | of which: Provisions for pensions and similar obligations | Details of provisions relating to liability for post-employment benefits. |
| l1000 | Bonds and similar obligations | Includes bonds and similar securities issued by the entity. |
| l1100 | Current | Bonds and similar securities due to be settled within 12 months after the reporting period |
| l1200 | Non-current | Bonds and similar securities not due to be settled within 12 months after the reporting period |
| l2000 | Amounts owed to credit institutions | Includes debt of the entity vis-à-vis credit institutions (includes financial leasing) |
| l2100 | Current | Amounts owed to credit institutions due to be settled within 12 months after the reporting period |
| l2200 | Non-current | Amounts owed to credit institution not due to be settled within 12 months after the reporting period |
| l3000 | Other creditors   | (l3100+l3200) |
| l3100 | Other financial creditors | Includes the remaining funding from other financial creditors not identified in l1000 and l2000, mainly intra-group debt. |
| l3110 | Current | Funding from other financial creditors due to be settled within 12 months after the reporting period |
| l3120 | Non-current | Funding from other financial creditors not due to be settled within 12 months after the reporting period |
| l3200 | Other non-financial creditors | Includes other accounts payables (except trade payables and payables to other financial creditors), mainly tax and social security payables, staff debt and active dividends to be paid |
| l3210 | Current | Funding from other non-financial creditors due to be settled within 12 months after the reporting period |
| l4000 | Trade payables | Includes debts to suppliers of goods and services, net of advances made (except for payments on account, included in a2100) |
| l5000 | Payments received on account of orders, current | Includes payments received by the entity on account of orders |
| l6000 | Deferred liabilities | Includes income to be recognized in future periods, including deferred tax liabilities |
| l0000 | **TOTAL LIABILITIES**  | (lp000+l1000+l2000+l3000+l4000+l5000+l6000) |

### Ratios and Derived Variables

Ratios and derived variables are calculated based on the information available. For an overview of the formulas used to
compute these variables check the auxiliary file [ratios_formulas.xlsx](./aux_files/formulas/ratios_formulas.xlsx). A Stata ado file
(ibachdev.ado) is provided by BPLIM and BELab upon request to compute the variables listed below.

| Variable Name | Variable Description |
| :--- | :--- |
| **Financial Structure Ratios** | |
| r0110 | Assets to Equity ratio |
| r0120 | Liabilities to Equity ratio |
| r0140 | Other financial assets and cash and bank / Total assets |
| | |
| **Financial and Debt Service Ratios** | |
| r0210 | Financial income net of charges other than interest over EBITDA |
| r0220 | EBITDA over Interest on financial debt |
| r0230 | Interest burden |
| r0240 | Interest and similar charges / Net turnover |
| r0250 | Interest and similar charges / Gross operating profit |
| r0260 | Net financial income / Gross operating profit |
| r0270 | Gross operating profit / Total net debt |
| r0280 | Credit institutions net indebtness ratio |
| r0290 | Financing cost (strict sense definition) |
| r2900 | Financing cost (broad definition) |
| | |
| **Profitability Ratios** | |
| r0310 | Gross value added  / Net turnover |
| r0320 | Gross operating profit / Net turnover (ROS) |
| r0330 | EBITDA  / Net turnover |
| r0340 | Net operating profit / Net turnover |
| r0350 | EBIT / Net turnover |
| r0360 | EBT  / Net turnover |
| r0370 | Net financial income / Net turnover |
| r0380 | Return on equity |
| r0390 | Net operating profit / Total assets |
| r3100 | Profit or loss of the year before taxes / Equity |
| r3110 | EBITDA - Return on investments |
| r3120 | Return on sales |
| | |
| **Activity and Technical Ratios** | |
| r0410 | Asset turnover ratio |
| r0420 | Coefficient Employee expenses over Gross value added |
| | |
| **Working Capital Ratios** | |
| r0510 | Inventories / Net turnover |
| r0520 | Trade receivables / Net turnover |
| r0530 | Trade payables / Net turnover |
| r0540 | Operating working capital / Net turnover |
| r0550 | Days Sales Outstanding |
| r0560 | Days Payables Outstanding |
| | |
| **Derived variables - Income statement** | |
| d1001 | Financial income net of charges other than interest |
| d1002 | Interest and similar charges |
| d1003 | Net financial income |
| d1004 | Gross Value Added (GVA) |
| d1005 | Gross Operating Profit |
| d1006 | Net Operating Profit |
| d1007 | EBITDA |
| d1008 | EBIT |
| d1009 | EBT |
| | |
| **Derived variables - Balance sheet** | |
| d2001 | Other financial assets and cash and bank |
| d2006 | Financial liabilities (strict sense definition) |
| d2007 | Financial liabilities (broad definition) |
| d2008 | Non financial liabilities (strict sense definition) |
| d2009 | Non financial liabilities (broad definition) |
| d2010 | Total net debt |
| d2011 | Operating working capital |

# Basic Descriptive Statistics

```{stata}
*| output: false
*| echo: false
*| scrolled: true
local extraction="MAY25"
local ref="2025_05"
local startyr="2008"
local finyear="2023"
local version="V01"
local file1="YFRM"
```

Table 1- Number of firms over the data period - Portugal (as of May 2025 extraction)

```{stata}
*| output: true
*| echo: false
*| ExecuteTime: {end_time: '2023-06-19T16:42:24.254523Z', start_time: '2023-06-19T16:41:31.483892Z'}
forval yy=`startyr'/`finyear' {
    quietly import delimited using "../../../output/data/BPLIM_IBACH_A_YFRM_`yy'_`extraction'_PT_V01.csv", delimiter(";") varnames(1) clear
    tempfile pt_`yy'
    quietly save `pt_`yy''
}

clear
forval yy=`startyr'/`finyear' {
    quietly append using `pt_`yy''
}

table dyear, statistic(frequency)
```

Table 2- Number of firms over the data period - Spain (as of May 2025 extraction)

```{stata}
*| output: true
*| echo: false
forval yy=`startyr'/`finyear' {
    if `yy'<2023 {
        local per "0822"
}
    if `yy'==2023 {
        local per "0823"
}

    quietly import delimited using "../../../output/data/BELab_iBACH`per'_01_`yy'_ES_Anonimized.csv", delimiter(";") varnames(1) clear
    tempfile es_`yy'
    quietly save `es_`yy''
}

clear
forval yy=`startyr'/`finyear' {
    quietly append using `es_`yy''
}

table dyear, statistic(frequency)
```

A **dashboard** with some basic descriptive statistics is available on [BELab website](https://app.powerbi.com/view?r=eyJrIjoiMzZjNzNkYmQtNzgzNi00NGU0LTg3NzYtOGI0ZTYwOTQ3Nzc5IiwidCI6IjZhYjE1MmQ1LTllZDEtNDkwNi1iNWMyLWMwMjJhNzRhMzU2ZSIsImMiOjl9).

# Auxiliary Files

For a description of each variable please check the metadata file [ibach_meta_YFRM_MAY25_PTES_V01](./aux_files/metafiles/ibach_meta_YFRM_MAY25_PTES_V01.xlsx).

Summary statistics for each data set are available on BPLIM's servers:

| File | Summary Statistics |
| :--- | :---: |
| Portugal | [stat_Portugal](./aux_files/descriptive_statistics/Portugal/) |
| Spain | [stat_Spain](./aux_files/descriptive_statistics/Spain/) |

# Reading the data in Stata

Files are provided in a *.csv* file with all the metadata available in the file:
[ibach_meta_YFRM_MAY25_PTES_V01](./aux_files/metafiles/ibach_meta_YFRM_MAY25_PTES_V01.xlsx).

`metaxl` Stata package, which can be installed from [BPLIM's Github repository](https://github.com/BPLIM/Tools/tree/master/ados/General/metaxl), can be used to apply the metadata to the data.

For example, using the file with Portuguese data for 2023:

```{stata}
*| eval: false
*| echo: true
*| code-fold: false
import delimited using "./BPLIM_IBACH_A_YFRM_2023_MAY25_PT_V01.csv", ///
clear varnames(1) delimiter(";")
metaxl clear, force
metaxl apply, meta(ibach_meta_YFRM_MAY25_PTES_V01)
describe
```

# Useful Links

[BACH database](https://www.bach.banque-france.fr/#/login)

[The Bank for the Accounts of Companies Harmonized  (BACH) database - ECB Statistics Paper Series](https://www.ecb.europa.eu/pub/pdf/scpsps/ecbsp11.en.pdf)

# Citation of this Dataset

Any study or other document that uses the iBACH data provided by BPLIM or BELab has to properly cite the data source as:

Banco de Portugal Microdata Research Laboratory (BPLIM) (2025): Portuguese Companies Microdata (iBACH). Extraction: May 2025. Version: V1. Banco de Portugal - BPLIM. Dataset. https://doi.org/10.17900/iBACH.May2025.V1

BELab. Banco de España/CORPME, Colegio de Registradores de la Propiedad y Mercantiles de España. Spanish Companies Microdata (iBACH). DOI: 10.48719/BELab.iBACH0823_01

<br>
<br>

To cite this dataset you can use the package biblatex with the following two BibTeX entries:

```{stata}
*| eval: false
*| echo: true
*| code-fold: false
@dataset{iBACH.May2025.V1,
author = {{Banco de Portugal Microdata Research Laboratory (BPLIM)}},
publisher = {Banco de Portugal - BPLIM. Dataset},
title = {{P}ortuguese {C}ompanies {M}icrodata (iBACH)},
year = {2025},
version = { V1, Extraction: May 2025},
doi = {10.17900/iBACH.May2025.V1},
url = {https://doi.org/10.17900/iBACH.May2025.V1}
}
```

```{stata}
*| eval: false
*| echo: true
*| code-fold: false
@dataset{BELab.iBACH0823_01,
author = {{BELab. Banco de Espa\~{n}a/CORPME, Colegio de Registradores
    de la Propiedad y Mercantiles de Espa\~{n}a}},
publisher = {Banco de Espa\~{n}a},
title = {{S}panish {C}ompanies {M}icrodata (iBACH)},
year = {2025},
doi = {10.48719/BELab.iBACH0823_01},
url = {https://doi.org/10.48719/BELab.iBACH0823_01}
}
```
