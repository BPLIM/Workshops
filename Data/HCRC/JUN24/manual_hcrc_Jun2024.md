---
title: Harmonized Central Credit Responsibility Database (HCRC) - Data Manual
subtitle: Extraction Date - June 2024
author: BPLIM
date: July 2024
abstract: 'The Portuguese Central Credit Register (with the database prior to August 2018 known as the Old CRC) underwent a major revision in September, 2018 and was replaced by a new reporting system (known as the New CRC) which started to collect granular credit data at the instrument level, as framed by ECB''s Regulation (EU) 2016/867 of 18 May 2016 and Banco de Portugal''s Instruction No. 17/2018. This revision has important implications for researchers who are interested in analyzing Portuguese credit market covering the transition period. In particular, there are important series breaks that might affect researchers'' analysis for several reasons. First of all, the New CRC reports information on a loan-by-loan basis while the Old CRC collects data on a exposure-by-exposure basis. Second, the New CRC starts to collect credit instruments that were not mandatory for the participating institutions to report under the framework of the Old CRC. Meanwhile, some information that was previously reported in the Old CRC is no longer available in the New CRC. Third, reporting thresholds for certain credit products, such as factoring products, have changed. The Harmonized Central Credit Responsibility Database (HCRC) aims to build compatible series between the Old CRC and the New CRC by selecting a set of most relevant variables and adopting necessary steps to harmonize the data. The database covers the period from 2009 to 2023 and consists of information aggregated at the firm and bank-firm level. Data constructed at exposure level mimicking the data structure of the Old CRC is only available to internal researchers upon request. Data is prepared at monthly frequency and is updated annually.'
keywords: 'Old CRC, New CRC, revision, loan-by-loan, exposure-by-exposure, harmonized data, firm level, bank-firm level.'
doi: 10.17900/HCRC.Jun2024.V1.
execute:
  echo: false
format:
  pdf:
    toc: true
    keep_tex: true
    pdf-engine: pdflatex
  html:
    toc: true
    footnotes-hover: true
    code-fold: true
    code-copy: true
    theme: default
editor: 
  markdown: 
    wrap: 72 # This line specifies the wrap length for Markdown text
---

{{< pagebreak >}}

# General Information

> **Dataset Designation in English**: The Harmonized Central Credit
> Responsibility Database (HCRC)

> **Dataset Designation in Portuguese**: Central de Responsabilidades de
> Crédito Harmonizada (HCRC)

> **Data Type**: longitudinal data

> **Unit of Analysis**: firm, firm-bank, exposure

> **Frequency**: monthly

> **Start Date**: January, 2009[^1]

[^1]: As the data structure of the CRC before 2009 differs significant
    from that after 2009 (i.e., there are much less variables in the
    data before 2009), by default we only make available the period from
    2009 onwards for the HCRC. The data before 2009 is however available
    upon request.

> **Most Recent Date**: December, 2023

> **Reference date**: month-end

> **Data Organization**: data is organized in four datafiles: a cover
> sheet that contains firm generic information, the firm credit
> outstanding & bank relationship file, the bank-firm credit outstanding
> file, and the credit exposure file. All data files are available in
> Stata format.

> **Version of the Data**: the data made available by BPLIM corresponds
> to a data freeze at a certain time of the year. Therefore, all files
> contain information as reported at the extraction date. The most
> recent update of the data occurred in June 2024.

> **Languages Available**: variables labels are available in Portuguese
> and in English.[^2]

[^2]: To see the labels in Portuguese type the following command line in
    Stata: "label language pt".

> **Data Access**: this data set is available to external researchers
> under certain conditions.[^3]

[^3]: Conditions for data access for external researchers are detailed
    in the Guide for Researchers Using Banco de Portugal Microdata
    Research Laboratory (BPLIM) Data.

> **Digital Object Identifier**: 10.17900/HCRC.Jun2024.V1.

# Geographical Coverage

The Harmonized Central Credit Responsibility Database (HCRC) covers all
credit-granting institutions and all firms operating in mainland
Portugal and autonomous regions - Azores and Madeira. Credit
communicated by foreign central banks are excluded from the Harmonized
Central Credit Responsibility Database (HCRC).

# Population

The Harmonized Central Credit Responsibility Database (HCRC) reports
information on the indebtedness of all borrowing firms, except for
individual entrepreneurs and foreign firms operating in Portugal without
a valid Portuguese Tax Identification Number. Private persons are also
excluded from the database.

All credit obligations above the reporting threshold are included,
regardless if the credit is in good standing or in situations of
non-compliance.[^4]

[^4]: The mandatory loan registration thresholds have changed over time.
    The current mandatory loan registration threshold in Portuguese
    credit register is 50 euros.

The entities participating in CRC include: banks, saving banks, mutual
agricultural credit banks, financial credit institutions, leasing
companies, factoring companies, securitization companies, mutual
guarantee societies, and financial companies for credit acquisitions.

Some entities participating in CRC have experienced acquisitions and/or
mergers, which may have induced credit flows from one institution to
another. The list of participating entities have therefore changed over
time.

It's worthwhile to note that the coverage of borrowers in HCRC changed
over time due to the change in classifying individual entrepreneurs in
January, 2009[^5] and the cessation of reporting different
responsibility levels in the case of joint credit in September,
2018[^6].

[^5]: The Portuguese Credit Register has undergone a major revision in
    2009, framed by Decree-Law No. 204/2008 of October 14. In this
    revision, individual entrepreneurs were reassigned NIPC codes that
    either begin with 5 or 9 (consistent with a firm) or 1 or 2
    (consistent with an individual). As a result, discontinuities in the
    coverage of firms of different types and a noticeable gap in firm
    exits and entries are observed.

[^6]: Despite that fact that the New CRC, launched in September 2018,
    reports more granular data on credit, it stops distinguishing
    different responsibility levels (i.e., first debtor and the rest of
    the debtors), which has much less impact on corporate financing than
    household financing.

# Methodology

The Portuguese Credit Register has undergone several major revisions. Of
particular relevance is the revision in 2009, framed by Decree-Law no.
204/2008, of October 14, as well as the most recent revision in
September, 2018, framed by the Regulation (EU) 2016/867 of The European
Central Bank of May 2016.

The 2009 revision streamlined the coding for a number of categorical
variables and included data on maturity of loans, overdue loan class,
collateral and special characteristics for the first time.

The recent revision in September 2018 operates within the AnaCredit
statistical framework and defined the object, main concepts, scopes,
credit operations to be included/excluded, and the types of information
that needs to be reported.

Coding systems and reporting practices were significantly changed due to
these revisions, resulting in noticeable series breaks that may affect
researcher's analyses.

The main difference between the New CRC and the Old CRC is that the Old
CRC reports information on a exposure-by-exposure basis with each
exposure defined based on a set of predefined loan characteristics,
while the New CRC reports information on a loan-by-loan basis.

Although, in general more granular information on credit is reported in
the New CRC, some features that are initially present in the Old CRC
stop to be reported, such as the separation of first and the rest of
debtors in the case of joint credit.

Moreover, definitions and classifications of certain variables have also
changed in the New CRC, such as financial products and collateral types.

To make the aggregated variables compatible over time, we have adopted
necessary steps to harmonize the data. Mapping strategies of categorical
variables and the construction method of the included variables are
detailed in the [*Variables Description*](#description-of-variables)
section.

Despite the efforts of maintaining the greatest possible coherence over
time, we shall still note some series breaks in the data caused by
changes in reporting regulations and accounting procedures.

In particular, the New CRC has imposed stricter requirements for banks
to report certain credit information. For example, in the Old CRC,
revocable credit is not an obligatory reporting item and non-recourse
factoring is only required to be reported if it is overdue for more than
90 days. This explains why increases in specific financial products (for
instance, factoring products) and certain types of risk exposures (for
instance, undrawn credit) are observed after September 2018.

It is also important to note that even small changes in reporting
standards may require a infrastructural update on the part of the
participating financial entities, possibly leading to a gradual
implementation of the instruction, even though legally all the entities
should implement the instructions at the same time. This may explain
some anomalies observed surrounding the transition period (i.e.,
September and October, 2018). To address this concern, some corrections
are made to the original data taking into account the modifications made
by the participating institutions on certain credit characteristics such
as instrument type and maturity when gradually complying with the
instruction. Note that the corrections only concern the period
2009-2023.

# Description of Files

The Harmonized Central Credit Responsibility Database (HCRC) is
organized by information type in four datafiles: a cover sheet that
contains firm-level generic information, the firm level credit
outstanding & bank relationship file, the bank-firm level credit
outstanding file, and the credit exposure file.

The data files are organized with the following nomenclature:

**Cover Sheet (COVER)**: ***HCRC_METH_FRM_MMMYY_COVER_version.dta***

where *METH* denotes the method used to prepare the data (*"A"* for
Anonymized and *"P"* for Perturbed), *MMMYY* denotes the extraction date
(eg: JUN24), and *version* denotes the data version (eg: V01). Each row
corresponds to a firm across a period.

**Firm Credit Outstanding & Bank Relationship File (COBR)**:

***HCRC_METH_fFRM_YYYY_MMMYY_COBR_version.dta***

where *METH* denotes the method used to prepare the data (*"A"* for
Anonymized, *"P"* for Perturbed, and *"R"* for randomized), *f* denotes
the data frequency (M for monthly frequency), *YYYY* is the reporting
year, *MMMYY* denotes the extraction date (eg: JUN2024), *COBR* denotes
credit outstanding & bank relationship, and *version* denotes the data
version (eg: V01). Each row corresponds to a firm in a given month.

**Bank-Firm Credit Outstanding File (CO)**:

***HCRC_METH_fFRMBNK_YYYY_MMMYY_CO_version.dta***

where *METH* denotes the method used to prepare the data (*"A"* for
Anonymized, *"P"* for Perturbed, and *"R"* for randomized), *f* denotes
the data frequency (M for monthly frequency), *YYYY* is the reporting
year, *MMMYY* denotes the extraction date (eg: JUN2024), *CO* denotes
credit outstanding, and *version* denotes the data version (eg: V01).
Each row corresponds to a bank-firm pair in a given month.

**Credit Exposure File (EXP)**:

***HCRC_METH_fFRMEXP_YYYY_MMMYY_PROD_version.dta***

where *METH* denotes the method used to prepare the data (*"A"* for
Anonymized, *"P"* for Perturbed, and *"R"* for randomized), *f* denotes
the data frequency (M for monthly frequency), *YYYY* is the reporting
year, *MMMYY* denotes the extraction date (eg: JUN2024), *PROD* denotes
the data product (*"BAL"* for general characteristics and *"COLL"* for
collateral), and *version* denotes the data version (eg: V01). Each row
corresponds to one exposure in a given month, with the exposure
characterized according to a set of predefined variables (responsibility
level, financial product, original maturity, residual maturity, and
overdue class).

Note that the **Credit Exposure File (EXP)** is only available to
**internal researchers**.

Whenever possible, **labels** and **value labels** are attributed to
categorical variables. To preserve confidentiality, identification of
firms, banks and credit exposures are anonymized through unique
identifiers and the variable values are perturbed/randomized for
external researchers. The anonymized firm identifier is denoted as
*tina*, the anonymized bank identifier is denoted as *bina*, and the
anonymized credit exposure identifier is denoted as *cina*.

<br>

**Table 1 - Data Files**

| **Type of information**                                 | **Product**                              | **Linking Key**        |
|:---------------------------------------|:------------------------------------------|:----------------|
| Cover Sheet (COVER)                                     | Firm Generic Information                 | *tina*                 |
| Firm Credit Outstanding & Bank Relationship File (COBR) | Credit Outstanding and Bank Relationship | *tina*                 |
| Bank-Firm Credit Outstanding File (CO)                  | Credit Outstanding                       | *tina*, *bina*         |
| Credit Exposure File (EXP)                              | General Characteristics (BAL)            | *tina*, *bina*, *cina* |
| Credit Exposure File (EXP)                              | Collateral Type and Value (COL)          | *cina*                 |

The identifiers (*tina*, *bina*, and *cina*) identifiers allow the
matching of different files, as illustrated in the above table.

# Description of Variables {#description-of-variables}

Below we provide a general description of the variables included in each
data file as referred above. For a full account of all variable
categories and changes over time see ["Auxiliary Files"
section](#auxiliary-files).

## A. Cover Sheet

### A1. Identifiers

`Firm identifier` (*tina*) - Unique firm identifier that enables
tracking firms over time. *tina* is the anonymized tax identification
number, available in all files.

`Reference dates of the data` (*mindate* and *maxdate*) - Date range of
the data

### A2. Firm Generic Information

**Table 2** - Firm Generic Information in the Cover Sheet
(**COVER**)[^7]

[^7]: The criteria to define firm's main sector of activity is the gross
    value added at factor cost. When it is not possible to use this
    information to define the main sector of activity, firms are
    requested to use turnover or the number of people permanently
    employed by the firm. From 2006 to 2008, firms reported the code of
    "The Portuguese Classification of Economic Activities - Revision
    2.1" (CAE Rev. 2.1) at the highest level of disaggregation. Since
    2009, firms report their main activity according to the "The
    Portuguese Classification of Economic Activities - Revision 3" (CAE
    Rev. 3). The Statistics Department of Banco de Portugal provides the
    information on the main sector of activity according to both
    classifications CAE Rev2.1 and CAE Rev3 whenever possible and the
    classifications are harmonized over time. The source of this
    information is the CAE registered in the "Central Registry of
    Companies" for each company. Whenever the correspondence is not
    unique, the match between codes CAE Rev. 2.1 and CAE Rev. 3 is
    implemented based on the highest frequency of the matches.

| **Variable Name** | **Variable Description**                                                                       | **Measure** | **Available Period**         |
|:-----------|:---------------------------------------|:---------------|:-------------------------------|
| *natjur*          | Firm's legal form                                                                              | Categorical | January 2009 - December 2023 |
| *si*              | Institutional sector (SEC 95)                                                                  | Categorical | January 2009 - December 2023 |
| *si_final*        | Institutional sector (SEC 2010)                                                                | Categorical | January 2009 - December 2023 |
| *cae21*           | Firm's main sector of activity: Portuguese classification of Economic activities (version 2.1) | Categorical | January 2009 - December 2023 |
| *cae3*            | Firm's main sector of activity: Portuguese classification of Economic activities (version 3)   | Categorical | January 2009 - December 2023 |
| *district*        | Firm's geographical location: District                                                         | Categorical | January 2009 - December 2023 |
| *municipality*    | Firm's geographical location: Municipality                                                     | Categorical | January 2009 - December 2023 |
| *actecon*         | Indicator of economic activities                                                               | Categorical | January 2009 - December 2023 |
| *sitemp*          | Firm status                                                                                    | Categorical | January 2009 - December 2023 |

## B. The Credit Exposure File [^8]

[^8]: The Credit Exposure File is only available to internal
    researchers.

### B1. Identifiers

`Firm identifier` (*tina*) - Unique firm identifier that enables
tracking firms over time. *tina* is the anonymized tax identification
number, available in all files.

`Bank identifier` (*bina*) - Unique identifier that enables tracking
creditors over time. *bina* is the anonymized bank identification
number, available in the bank-firm credit outstanding file (CO) and the
credit exposure file (EXP).

`Credit exposure identifier` (*cina*) - Identifier for each credit
exposure.[^9] *cina* is the anonymized credit exposure identification
number, only available in the credit exposure file (EXP). The credit
exposure identifier changes on a monthly basis, therefore cannot be used
to follow a credit over time. This variable is, however, useful to merge
the auxiliary data file of collateral (COL) with the exposure
characteristics and credit amount (BAL) file.

[^9]: Credit exposure identifiers (*cina*) are only available after
    2009.

`Reference month of the data` (*date*) - Reference month of the data

It should be noted that reporting to the Portuguese Central Credit
Register does not depend on the nationality of the debtors but their
country of residence. In situations where a debtor is not resident in
Portugal and does not have a tax number assigned in Portugal, the debtor
is reported through a unique code generated by the participating
institution itself. These firms are excluded from the Harmonized Central
Credit Responsibility Database (HCRC).

### B2. General Characteristics

**Table 3** - Exposure Characteristics and Credit Amount Variables in
the Credit Exposure File (**EXP**)

| **Variable Name**       | **Variable Description** | **Measure** | **Available Period**         |
|:-----------------------|:---------------------------|:---------------|:--------------------------------|
| *nivelresponsabilidade* | Responsibility level     | Categorical | January 2009 - December 2023 |
| *produto*               | Financial product        | Categorical | January 2009 - December 2023 |
| *classecreditovencido*  | Overdue credit class     | Categorical | January 2009 - December 2023 |
| *prazooriginal*         | Original maturity        | Categorical | January 2009 - December 2023 |
| *prazoresidual*         | Residual maturity        | Categorical | January 2009 - December 2023 |
| *prazocurto_o*          | Short original maturity  | Indicator   | January 2009 - December 2023 |
| *prazocurto_r*          | Short residual maturity  | Indicator   | January 2009 - December 2023 |
| *tipogarantia*          | Type of collateral       | Categorical | January 2009 - December 2023 |
| *valorg*                | Amount of collateral     | Amount      | January 2009 - December 2023 |
| *valor_reg*             | Regular credit           | Amount      | January 2009 - December 2023 |
| *valor_vencido*         | Overdue credit           | Amount      | January 2009 - December 2023 |
| *valor_abatv*           | Written-off credit       | Amount      | January 2009 - December 2023 |

`Responsibility level` (*nivelresponsabilidade*)

The responsibility level characterizes the type of participation that
the client has in a credit operation, allowing to distinguish between
borrowers and sureties/guarantors.

The credit exposures for a debtor and its sureties/guarantor are
communicated with identical characteristics, except for the variables
associated with the level of responsibility and identification of the
debtor. This variable underwent a major revision in 2009, which included
guarantors for the first time.

Note that joint credit is no longer identifiable in the New CRC. To make
the series compatible, we have assigned the same responsibility level
(denoted by 2) to all debtors associated with the same joint credit
contract in the Harmonized Central Credit Responsibility Database
(HCRC). We should note that this is a compromise due to data
availability, which may generate increase in credit for some borrowers.
However, the impact should be minor for firms as joint credits are less
common in firms than households.

| **Classification** | **Definition**        |
|:------------------:|:----------------------|
|         1          | Debtor: Individual    |
|         2          | Debtor: Joint         |
|         3          | Guarantor: Individual |
|         4          | Guarantor: Joint      |

`Financial product` (*produto*)

The financial product characterizes the types of credit. In order to
facilitate the classification of credit exposures, the nomenclature used
here is close to that adopted in the chart of accounts in accordance
with the NCA. The classification covers 15 different categories covering
the most representative types of credit. Some of the financial products
are geared to individual financing while others are mainly for
businesses and other legal persons. For instance, products such as
"current account (credit lines)", "factoring", "real estate leasing" and
"financing to the corporate activity or equivalent" are more geared to
finance activities of firms or other legal persons.

In some cases, Firm may also have credits of typical financial products
in household financing but for commercial purposes (such as overdrafts
and commercial mortgage loans).

This variable is only available from 2009 onwards.

| **Classification** | **Definition**                                        |
|:------------------:|:---------------------------------------------------------------------|
|         1          | Discount and other credits secured by effects         |
|         2          | Current account (credit lines)                        |
|         3          | Overdrafts on deposit accounts                        |
|         4          | Recourse factoring                                    |
|         5          | None-recourse factoring                               |
|         6          | Real estate leasing                                   |
|         7          | Non-real estate leasing                               |
|         8          | Financing to the corporate activity or equivalent     |
|         9          | Credit card                                           |
|         10         | Mortgage credit                                       |
|         11         | Consumer credit                                       |
|         12         | Automobile credit                                     |
|         13         | Other credit                                          |
|         14         | Bank Guarantees from other participating institutions |
|         15         | Other bank guarantees                                 |

The New CRC provides more granular information on the type of financial
products. To obtained a consistent classification system with CRC, we
have performed the following mapping strategy.

**Table 4** - Mapping Strategy for Financial Product

| **CRC**                       |                                                       | **AnaCredit**              |                                                                                                        |                                |                 |                                  |                                             |
|:----------|:--------------|:-----------|:---------------|:-----------|:-------------|:------------|:----------------|
| Financial product (*produto*) |                                                       | Instrument Type (*tpInst*) |                                                                                                        | Recourse Indicator (*recurso*) |                 | Financing Purpose (*finalidade*) |                                             |
| **Code**                      | **Designation**                                       | **Code**                   | **Designation**                                                                                        | **Code**                       | **Designation** | **Code**                         | **Designation**                             |
| 1                             | Discount and other credits secured by effects         | 24                         | Discount and other credits secured by effects                                                          |                                |                 |                                  |                                             |
| 2                             | Current account                                       | 14                         | Renewable credit, except for overdrafts and credit card                                                |                                |                 |                                  |                                             |
| 2                             | Current account                                       | 15                         | Renewable credit - bank checking account                                                               |                                |                 |                                  |                                             |
| 2                             | Current account                                       | 16                         | Revolving credit - credit line                                                                         |                                |                 |                                  |                                             |
| 3                             | Overdrafts on deposit accounts                        | 4                          | Credit overrunning                                                                                     |                                |                 |                                  |                                             |
| 3                             | Overdrafts on deposit accounts                        | 5                          | Overdraft facilities                                                                                   |                                |                 |                                  |                                             |
| 3                             | Overdrafts on deposit accounts                        | 6                          | Overdraft facilities - with domiciliating wages, repayment term greater than one month                 |                                |                 |                                  |                                             |
| 3                             | Overdrafts on deposit accounts                        | 7                          | Overdraft facilities - without domiciliating wages, repayment term greater than one month              |                                |                 |                                  |                                             |
| 3                             | Overdrafts on deposit accounts                        | 8                          | Overdraft facilities - with domiciliating wages, repayment term equal to or less than one month        |                                |                 |                                  |                                             |
| 3                             | Overdrafts on deposit accounts                        | 9                          | Overdraft facilities - without domiciliating wages, and repayment term equal to or less than one month |                                |                 |                                  |                                             |
| 4                             | Recourse factoring                                    | 19                         | Factoring                                                                                              | 2                              | Recourse        |                                  |                                             |
| 5                             | None-recourse factoring                               | 19                         | Factoring                                                                                              | 1                              | Non-Recourse    |                                  |                                             |
| 4                             | Recourse factoring                                    | 20                         | Confirming                                                                                             | 2                              | Recourse        |                                  |                                             |
| 5                             | None-recourse factoring                               | 20                         | Confirming                                                                                             | 1                              | Non-Recourse    |                                  |                                             |
| 4                             | Recourse factoring                                    | 21                         | Other commercial accounts receivable                                                                   | 2                              | Recourse        |                                  |                                             |
| 5                             | None-recourse factoring                               | 21                         | Other commercial accounts receivable                                                                   | 1                              | Non-Recourse    |                                  |                                             |
| 6                             | Real estate leasing                                   | 22                         | Real estate financial lease                                                                            |                                |                 |                                  |                                             |
| 7                             | Non-real estate leasing                               | 23                         | Non-real estate financial lease                                                                        |                                |                 |                                  |                                             |
| 8                             | Financing to the corporate activity or equivalent     | 17                         | Non-renewable credit                                                                                   |                                |                 |                                  |                                             |
| 8                             | Financing to the corporate activity or equivalent     | 31                         | Financing to the corporate activity or equivalent                                                      |                                |                 |                                  |                                             |
| 9                             | Credit card                                           | 10                         | Credit card                                                                                            |                                |                 |                                  |                                             |
| 9                             | Credit card                                           | 11                         | Credit card - with free-float period                                                                   |                                |                 |                                  |                                             |
| 9                             | Credit card                                           | 12                         | Credit card - without free-float period                                                                |                                |                 |                                  |                                             |
| 9                             | Credit card                                           | 13                         | Credit card - deferred debit card                                                                      |                                |                 |                                  |                                             |
| 10                            | Mortgage credit                                       | 25                         | Mortgage credit                                                                                        |                                |                 |                                  |                                             |
| 11                            | Consumer credit                                       | 27                         | Personal credit                                                                                        |                                |                 | 6                                | Personal credit - Home purpose              |
| 11                            | Consumer credit                                       | 27                         | Personal credit                                                                                        |                                |                 | 7                                | Personal credit - Education purpose         |
| 11                            | Consumer credit                                       | 27                         | Personal credit                                                                                        |                                |                 | 8                                | Personal credit - Health purpose            |
| 11                            | Consumer credit                                       | 27                         | Personal credit                                                                                        |                                |                 | 9                                | Personal credit - Renewable energy projects |
| 11                            | Consumer credit                                       | 27                         | Personal credit                                                                                        |                                |                 | 36                               | Other purposes                              |
| 11                            | Consumer credit                                       | 27                         | Personal credit                                                                                        |                                |                 | 98                               | No specific purpose                         |
| 12                            | Automobile credit                                     | 28                         | Automobile credit (excluding finance leases)                                                           |                                |                 |                                  |                                             |
| 13                            | Other credit                                          | 32                         | Other credit                                                                                           |                                |                 |                                  |                                             |
| 14                            | Bank Guarantees from other participating institutions | 29                         | Bank Guarantees from other participating institutions                                                  |                                |                 |                                  |                                             |
| 15                            | Other bank guarantees                                 | 30                         | Other bank guarantees                                                                                  |                                |                 |                                  |                                             |
| 16                            | Other credit not reported in CRC                      | 3                          | Deposits - except reverse repurchase agreements                                                        |                                |                 |                                  |                                             |
| 16                            | Other credit not reported in CRC                      | 18                         | Reverse repurchase agreements                                                                          |                                |                 |                                  |                                             |
| 16                            | Other credit not reported in CRC                      | 26                         | Multi-purpose/option credit (crédito conexo)                                                           |                                |                 |                                  |                                             |
| 16                            | Other credit not reported in CRC                      | 34                         | Shareholders loans                                                                                     |                                |                 |                                  |                                             |

Note that the above mapping applies the "approximation rule" aiming to
alleviate discontinuities in the time series. It is however not
unequivocal and does not completely eliminate the discontinuities in
2018. We also made some revisions in the mapping strategy accounting for
bank-by-bank reporting differences, especially for the instrument type
"16 Revolving credit - credit line.".

The types of instrument that were not reported in the Old CRC (i.e.,
deposits - except for reverse repurchase agreements, reverse repurchase
agreements, multi-purpose/option credit, and shareholders loans) are
excluded in the Bank-Firm Credit Outstanding File (CO) and the Firm
Credit Outstanding & Bank Relationship File (COBR).

`Overdue credit class` (*classecreditovencido*)

The overdue credit class indicates the time elapsed from the moment that
a credit enters into default.

The credit overdue class list is the same as defined for the purposes of
the banking chart of accounts (NCA and PCSB), with the only exception of
the shortest duration classes "up to 3 months", which is further divided
into three classes in the table adopted in CRC ("up to 30 days", "from
31 days to 61 days" and "from 62 days to 91 days"). In the case when
loans are repaid in various installments, the total overdue amount of
unpaid installments is communicated in a single overdue credit exposure,
classified in overdue credit class corresponding to the installments
with longer overdue time.

This variable is only available from 2009 onwards.

`Maturity` (*prazooriginal* and *prazoresidual*)

All credit exposures reported in the Old CRC after 2009 are classified
based on their original maturity, established in contractual terms
(i.e., original maturity), as well as on their residual maturity,
defined as the time interval between the reference date and the maturity
date of the credit agreement.

These two variables are defined in ranges, including a category
"Undetermined" (code 1) to characterize credit exposures which by their
nature do not have a contractually defined maturity or for which it is
not possible to determine a due date.

Instead of reporting the categorization of the maturity variables, the
New CRC reports the due date on which a borrower must pay back a loan in
full.

To harmonize the maturity variables overtime, we calculate the
term-to-maturity of an instrument based on its maturity date, then
project it onto the coding system of the Old CRC, as illustrated below.

| **Classification** | **Definition**           |
|:------------------:|:-------------------------|
|         1          | Undefined                |
|         2          | Up to 90 days            |
|         3          | From 90 days to 180 days |
|         4          | From 180 days to 1 year  |
|         5          | From 1 to 5 years        |
|         6          | From 5 to 10 years       |
|         7          | From 10 to 20 years      |
|         8          | From 20 to 25 years      |
|         9          | From 25 to 30 years      |
|         10         | More than 30 years       |

We take into account the following rules which were observed in the Old
CRC.

-   The category "Undefined" is applied to overdrafts and credit cards
    which by nature do not have a contractually defined maturity.

-   Original maturity of the same credit should always be equal to or
    greater than the residual maturity.

-   Residual maturity for overdue credit is assigned the category
    "Undefined".

-   We align the reporting practices for the maturity structure of
    current accounts over time bank-by-bank.

There is one bank that has always assigned "Undefined" to the maturity
of its current account products in the Old CRC. To achieve better
harmonization, we assign "Undefined" to the maturity of the bank's
current account products in the New CRC as well.

`Short maturity` (*prazocurto_o* and *prazocurto_r*)

Short maturity is an indicator defined based on either the
term-to-maturity as agreed in the credit contract, denoted by
*prazocurto_o*, or the residual maturity -- the remaining time until the
expiration or the repayment of the instrument, denoted by
*prazocurto_r*.

*prazocurto_o* takes the value of 1 if a credit exposure has an original
maturity of equal to or less than one year. For the data before 2009,
the short-term credit is defined as the aggregation of commercial
credit, discount funding, and other short-term funding, which are
short-term funding by their nature.

*prazocurto_r* takes the value of 1 if a credit exposure has a residual
maturity of equal to or less than one year. This variable is only
available from 2009 onwards.

| **Classification** | **Definition**                                            |
|:-----------------:|:----------------------------------------------------|
|         0          | Original/Residual maturity more than one year             |
|         1          | Original/Residual maturity equal to or less than one year |

`Credit amount` (*valor_reg*, *valor_pot*, *valor_vencido*, and
*valor_abatv*)

The credit amount variables identify the total amount outstanding of a
credit exposure in different credit situations. Loans of the same debtor
and creditor with identical characteristics are aggregated into a single
exposure.

Given different credit situations[^10], we have constructed credit
amount variables as regular credit (*valor_reg*), Overdue credit
(*valor_vencido*), and Written-off credit (*valor_abatv*).

[^10]: Regular credit (*valor_reg*) represents the total amount of
    credit in good standing. All outstanding credit recorded as
    non-performing (including overdue, renegotiated credit, and overdue
    credit in litigation) are aggregated to calculate overdue credit
    (*valor_vencido*). Written-off credit (*valor_abatv*) records credit
    that became so seriously delinquent that the creditor has given up
    on being paid. It also includes written-off credit filed in court.

Given large breaks in the time series, potential credit (*valor_pot*) is
not included in the datasets but are available upon request.[^11]

[^11]: Potential credit (*valor_pot*) represents the revocable and
    irrevocable commitments of the participating entities. Examples of
    potential credit include unused amounts of credit cards/credit
    lines, and bank guarantees.

Note that regardless of the denominated currency, the credit amount
variables are always expressed in euro units.

`Type of collateral` (*tipogarantia*)

As long as collateral/guarantee exists, it is mandatory for
participating institutions to communicate to CRC its existence together
with the credit exposure that it ensures.

The New CRC provides more granular information on the type of
collaterals than the Old CRC. To harmonize the variable overtime, we
adopt the following coding system and mapping strategy in Table 5.

| **Classification** | **Definition**                  |
|:------------------:|:--------------------------------|
|         1          | Real collateral mortgage        |
|         2          | Real collateral - not mortgaged |
|         3          | Financial collateral            |
|         4          | Personal guarantee              |
|         5          | Other guarantees                |

**Table 5** - Mapping Strategy for Type of Collateral

| **CRC**                             |                                 | **AnaCredit**                 |                                                                               |                               |                 |
|:--------------|:------------------|:------------|:---------------------|:------------|:--------------|
| Type of collateral (*tipogarantia*) |                                 | Type of collateral (*tpProt*) |                                                                               | Mortgage number (*hierqProt*) |                 |
| **Code**                            | **Designation**                 | **Code**                      | **Designation**                                                               | **Code**                      | **Designation** |
| 1                                   | Real collateral mortgage        | 15                            | Residential commercial property                                               |                               | \> 0            |
| 1                                   | Real collateral mortgage        | 16                            | Residential commercial property - meets the CRC criterion                     |                               | \> 0            |
| 1                                   | Real collateral mortgage        | 17                            | Residential commercial property - does not meet the CRC criterion             |                               | \> 0            |
| 1                                   | Real collateral mortgage        | 18                            | Retail commercial property                                                    |                               | \> 0            |
| 1                                   | Real collateral mortgage        | 19                            | Retail commercial property - meets the CRC criterion                          |                               | \> 0            |
| 1                                   | Real collateral mortgage        | 20                            | Retail commercial property - does not meet the CRC criterion                  |                               | \> 0            |
| 1                                   | Real collateral mortgage        | 21                            | Commercial property offices                                                   |                               | \> 0            |
| 1                                   | Real collateral mortgage        | 22                            | Commercial property offices - meets the CRC criterion                         |                               | \> 0            |
| 1                                   | Real collateral mortgage        | 23                            | Commercial property offices - does not meet the CRC criterion                 |                               | \> 0            |
| 1                                   | Real collateral mortgage        | 24                            | Industrial commercial property                                                |                               | \> 0            |
| 1                                   | Real collateral mortgage        | 25                            | Industrial commercial property - meets the CRC criterion                      |                               | \> 0            |
| 1                                   | Real collateral mortgage        | 26                            | Industrial commercial property - does not meet the CRC criterion              |                               | \> 0            |
| 1                                   | Real collateral mortgage        | 27                            | Other commercial property                                                     |                               | \> 0            |
| 1                                   | Real collateral mortgage        | 28                            | Other commercial property - meets the CRC criterion                           |                               | \> 0            |
| 1                                   | Real collateral mortgage        | 29                            | Other commercial property - does not meet the CRC criterion                   |                               | \> 0            |
| 1                                   | Real collateral mortgage        | 30                            | Property under construction for commercial purposes                           |                               | \> 0            |
| 1                                   | Real collateral mortgage        | 31                            | Property under construction for commercial purposes - meets the CRC criterion |                               | \> 0            |
| 1                                   | Real collateral mortgage        | 32                            | Property under construction for commercial purposes - meets the CRC criterion |                               | \> 0            |
| 1                                   | Real collateral mortgage        | 33                            | Residential properties - completed                                            |                               | \> 0            |
| 1                                   | Real collateral mortgage        | 34                            | Residential properties - under construction                                   |                               | \> 0            |
| 1                                   | Real collateral mortgage        | 35                            | Residential properties - land                                                 |                               | \> 0            |
| 1                                   | Real collateral mortgage        | 36                            | Other properties                                                              |                               | \> 0            |
| 1                                   | Real collateral mortgage        | 37                            | Other collateral of real nature                                               |                               | \> 0            |
| 2                                   | Real collateral - not mortgaged | 15                            | Residential commercial property                                               |                               | 0 or missing    |
| 2                                   | Real collateral - not mortgaged | 16                            | Residential commercial property - meets the CRC criterion                     |                               | 0 or missing    |
| 2                                   | Real collateral - not mortgaged | 17                            | Residential commercial property - does not meet the CRC criterion             |                               | 0 or missing    |
| 2                                   | Real collateral - not mortgaged | 18                            | Retail commercial property                                                    |                               | 0 or missing    |
| 2                                   | Real collateral - not mortgaged | 19                            | Retail commercial property - meets the CRC criterion                          |                               | 0 or missing    |
| 2                                   | Real collateral - not mortgaged | 20                            | Retail commercial property - does not meet the CRC criterion                  |                               | 0 or missing    |
| 2                                   | Real collateral - not mortgaged | 21                            | Commercial property offices                                                   |                               | 0 or missing    |
| 2                                   | Real collateral - not mortgaged | 22                            | Commercial property offices - meets the CRC criterion                         |                               | 0 or missing    |
| 2                                   | Real collateral - not mortgaged | 23                            | Commercial property offices - does not meet the CRC criterion                 |                               | 0 or missing    |
| 2                                   | Real collateral - not mortgaged | 24                            | Industrial commercial property                                                |                               | 0 or missing    |
| 2                                   | Real collateral - not mortgaged | 25                            | Industrial commercial property - meets the CRC criterion                      |                               | 0 or missing    |
| 2                                   | Real collateral - not mortgaged | 26                            | Industrial commercial property - does not meet the CRC criterion              |                               | 0 or missing    |
| 2                                   | Real collateral - not mortgaged | 27                            | Other commercial property                                                     |                               | 0 or missing    |
| 2                                   | Real collateral - not mortgaged | 28                            | Other commercial property - meets the CRC criterion                           |                               | 0 or missing    |
| 2                                   | Real collateral - not mortgaged | 29                            | Other commercial property - does not meet the CRC criterion                   |                               | 0 or missing    |
| 2                                   | Real collateral - not mortgaged | 30                            | Property under construction for commercial purposes                           |                               | 0 or missing    |
| 2                                   | Real collateral - not mortgaged | 31                            | Property under construction for commercial purposes - meets the CRC criterion |                               | 0 or missing    |
| 2                                   | Real collateral - not mortgaged | 32                            | Property under construction for commercial purposes - meets the CRC criterion |                               | 0 or missing    |
| 2                                   | Real collateral - not mortgaged | 33                            | Residential properties - completed                                            |                               | 0 or missing    |
| 2                                   | Real collateral - not mortgaged | 34                            | Residential properties - under construction                                   |                               | 0 or missing    |
| 2                                   | Real collateral - not mortgaged | 35                            | Residential properties - land                                                 |                               | 0 or missing    |
| 2                                   | Real collateral - not mortgaged | 36                            | Other properties                                                              |                               | 0 or missing    |
| 2                                   | Real collateral - not mortgaged | 37                            | Other collateral of real nature                                               |                               | 0 or missing    |
| 3                                   | Real collateral mortgage        | 4                             | Gold                                                                          |                               |                 |
| 3                                   | Financial collateral            | 5                             | Cash and deposits or equivalent                                               |                               |                 |
| 3                                   | Financial collateral            | 6                             | Publicly-quoted debt securities                                               |                               |                 |
| 3                                   | Financial collateral            | 7                             | Non-quoted debt securities                                                    |                               |                 |
| 3                                   | Financial collateral            | 8                             | Loans                                                                         |                               |                 |
| 3                                   | Financial collateral            | 9                             | Shares and other equity - quoted                                              |                               |                 |
| 3                                   | Financial collateral            | 10                            | Shares and other equity - non-quoted                                          |                               |                 |
| 3                                   | Financial collateral            | 11                            | Credit derivatives                                                            |                               |                 |
| 3                                   | Financial collateral            | 12                            | Financial guarantees other than credit derivatives                            |                               |                 |
| 3                                   | Financial collateral            | 13                            | Commercials receivable                                                        |                               |                 |
| 3                                   | Financial collateral            | 14                            | Pledge of life insurance                                                      |                               |                 |
| 4                                   | Personal guarantee              | 3                             | Guarantors/sureties                                                           |                               |                 |
| 5                                   | Other guarantees                | 38                            | Other guarantees                                                              |                               |                 |

The New CRC reports the number of mortgages (*hierqProt*) that are
involved in collateralization if a credit contract is mortgage-backed.
With this variable, we are able to distinguish mortgaged and
non-mortgaged real collaterals.

`Amount of collateral` (*valorg*)

The collateral amounts relating to a credit are expressed in euros and
aggregated by type of collateral using the same criteria as to the
credit exposure.

However, it is important to note that the amount of collateral were
capped at the loan amount in the Old CRC and not all banks followed the
same practice. Researchers should be fully aware of the limitation in
conducting their research using this variable.

## C. The Bank-Firm Credit Outstanding File[^12]

[^12]: The Bank-Firm Credit Outstanding File is only available to
    internal researchers.

### C1. Identifiers

`Firm identifier` (*tina*) - Unique firm identifier that enables
tracking firms over time. *tina* is the anonymized tax identification
number, available in all files.

`Bank identifier` (*bina*) - Unique identifier that enables tracking
creditors over time. *bina* is the anonymized bank identification
number, available in the credit exposure file (EXP) and the bank-firm
level credit outstanding file (CO).

`Reference month of the data` (*date*) - Reference month of the data

### C2. Credit Outstanding

**Table 6** - Credit Outstanding Variables in the Bank-Firm Credit
Outstanding File (**CO**)

| **Variable Name**       | **Variable Description**                | **Measure** | **Available Period**         |
|:---------------------|:-----------------------------|:---------------|:--------------------------------|
| *valor_reg*             | Regular credit                          | Amount      | January 2009 - December 2023 |
| *valor_vencido*         | Overdue credit                          | Amount      | January 2009 - December 2023 |
| *valor_abatv*           | Written-off credit                      | Amount      | January 2009 - December 2023 |
| *valor_reg_sto*         | Regular credit: short original maturity | Amount      | January 2009 - December 2023 |
| *valor_reg_str*         | Regular credit: short residual maturity | Amount      | January 2009 - December 2023 |
| *valor_reg_secured*     | Secured regular credit                  | Amount      | January 2009 - December 2023 |
| *valor_vencido_secured* | Secured overdue credit                  | Amount      | January 2009 - December 2023 |
| *valor_abatv_secured*   | Secured written-off credit              | Amount      | January 2009 - December 2023 |

Credit Outstanding Variables in the Bank-Firm Credit Outstanding File
(**CO**) are aggregated from the Credit Exposure File (**EXP**) at the
bank-firm level.

*valor_reg_sto* calculates the total amount of credit with an original
maturity of equal to or less than one year for the data after January,
2009. For the data before 2009, *valor_reg_sto* calculates the total
amount of commercial credit, discount funding, and other short-term
funding.

*valor_reg_str* calculates the total amount of credit with a residual
maturity of equal to or less than one year.

*valor_reg_secured*, *valor_pot_secured*, *valor_vencido_secured*, and
*valor_abatv_secured* calculate the total amount of credit with at least
one type of collateral as illustrated in **Table 5**.

Guarantors and financial products that are not available in the Old CRC
(code 16 in **Table 4**) are excluded from the Bank-Firm Credit
Outstanding File (**CO**).

## D. The Firm Credit Outstanding and Bank Relationship File

### D1. Identifiers

`Firm identifier` (*tina*) - Unique firm identifier that enables
tracking firms over time. *tina* is the anonymized tax identification
number, available in all files.

`Reference month of the data` (*date*) - Reference month of the data

### D2. Credit Outstanding and Bank Relationships

**Table 7** - Credit Outstanding and Bank Relationship Variables in the
Firm Credit Outstanding & Bank Relationship File (**COBR**)

| **Variable Name**       | **Variable Description**                | **Measure** | **Available Period**         |
|:---------------------------|:-------------------------------|:---------------|:-------------------------------|
| *valor_reg*             | Regular credit                          | Amount      | January 2009 - December 2023 |
| *valor_vencido*         | Overdue credit                          | Amount      | January 2009 - December 2023 |
| *valor_abatv*           | Written-off credit                      | Amount      | January 2009 - December 2023 |
| *nb_relacao*            | Number of bank relationships            | number      | January 2009 - December 2023 |
| *max_relacao*           | Largest bank relationship in share      | share       | January 2009 - December 2023 |
| *hhi_relacao*           | Concentration of bank relationships     | index       | January 2009 - December 2023 |
| *valor_reg_sto*         | Regular credit: short original maturity | Amount      | January 2009 - December 2023 |
| *valor_reg_str*         | Regular credit: short residual maturity | Amount      | January 2009 - December 2023 |
| *valor_reg_secured*     | Secured regular credit                  | Amount      | January 2009 - December 2023 |
| *valor_vencido_secured* | Secured overdue credit                  | Amount      | January 2009 - December 2023 |
| *valor_abatv_secured*   | Secured written-off credit              | Amount      | January 2009 - December 2023 |

Credit Outstanding Variables in the Firm Credit Outstanding and Bank
Relationship File (**COBR**) are aggregated from the Credit Exposure
File (**EXP**) at the firm level. Guarantors and financial products that
are not available in the Old CRC (code 16 in **Table 4**) are also
excluded.

*valor_reg_sto*, *valor_reg_str*, *valor_reg_secured*,
*valor_pot_secured*, *valor_vencido_secured*, and *valor_abatv_secured*
are defined in the same way as in the Bank-Firm Credit Outstanding File
(**CO**).

*nb_relacao* measures the number of a firm's bank relationships.
Precisely, we calculate the number of active bank relationships, i.e.,
the number of banks from whom a firm borrows in a specific month. Unused
credit is also taken into account in the calculation of bank
relationships.

*max_relacao* features the borrowing share from a firm's major bank. It
is measured as the percentage of a firm's available credit from the
major bank to the firm's total available credit.

*hhi_relacao* captures the concentration of bank relationship. It is
calculated using the Herfindahl--Hirschman Index as the sum of the
squares of bank's lending share to a firm.

# Auxiliary Files {#auxiliary-files}

For a description of each variable in each dataset, summary statistics
for each dataset and a metafiles for each dataset, please check the
following auxiliary files:

| **Data File**                                                 |                                 **Metafiles**                                 |                    **Variables Description**                     |                                        **Summary Statistics**                                        |
|:-----------------------------------|:---------------:|:----------------------:|:--------------------:|
| Credit Exposure File (EXP): General                           |  [meta_hcrc_bal](./aux_files/metafiles/HCRC_meta_MFRMEXP_JUN24_BAL_V01.xlsx)  | [var_hcrc_bal](./aux_files/variables_description/var_hcrc.html)  |  [stat_hcrc_bal](.aux_files/descriptive_statistics/HCRC_metastats_MFRMEXP_2023_JUN24_BAL_V01.xlsx)   |
| Credit Exposure File (EXP): Collateral                        | [meta_hcrc_coll](./aux_files/metafiles/HCRC_meta_MFRMEXP_JUN24_COLL_V01.xlsx) | [var_hcrc_coll](./aux_files/variables_description/var_hcrc.html) | [stat_hcrc_coll](./aux_files/descriptive_statistics/HCRC_metastats_MFRMEXP_2023_JUN24_COLL_V01.xlsx) |
| Firm Level Credit Outstanding & Bank Relationship file (COBR) |  [meta_hcrc_cobr](./aux_files/metafiles/HCRC_meta_MFRM_JUN23_COBR_V01.xlsx)   | [var_hcrc_cobr](./aux_files/variables_description/var_hcrc.html) |  [stat_hcrc_cobr](./aux_files/descriptive_statistics/HCRC_metastats_MFRM_2023_JUN24_COBR_V01.xlsx)   |
| Bank-Firm Level Credit Outstanding File (CO)                  |   [meta_hcrc_co](./aux_files/metafiles/HCRC_meta_MFRMBNK_JUN24_CO_V01.xlsx)   |  [var_hcrc_co](./aux_files/variables_description/var_hcrc.html)  |   [stat_hcrc_co](./aux_files/descriptive_statistics/HCRC_metastats_MFRMBNK_2023_JUN24_CO_V01.xlsx)   |

The Summary Statistics and Dataset Description files are available on
BPLIM's servers.

# Legislation

Below we list a list of relevant legislations:

-   [**Instrução no.
    16/2001**](./aux_files/legislation/Instrucao_16-2001_full.pdf) --
    reviewed the separation of potential from actual amounts of credit.

-   [**Instrução no.
    11/2002**](./aux_files/legislation/Instrucao_11-2002.pdf) --
    establishment of a 90 day period to register a credit exposure (*sem
    direito de regresso*) or overdue credit (*com direito de regresso*)
    after invoices are due; revocable commitments (code 921) are no
    longer reported as a credit of type 6 (off balance sheet
    commitments); factoring credit more than 90 days overdue reported as
    type 7 (non-performing credit) or 8 (credit in litigation).
    Participating entities are encouraged to provide relevant
    information for credit risk assessment. In addition, renegotiated
    credits are requested to be reported since July, 2001.

-   [**Instrução no.
    15/2002**](./aux_files/legislation/Instrucao_15-2002.pdf) -- made
    procedural changes to access and occasional communication requested
    by the Banco de Portugal (no analysis impact).

-   [**Decree-Law no.
    53/2004**](./aux_files/legislation/Lei_53-2004.pdf), March 18 --
    integrated the information on court decisions regarding insolvency
    proceedings of collective or individual people, provided by the
    Ministry of Justice, following the approval of the CIRE - Insolvency
    Code.

-   [**Instrução no.
    7/2006**](./aux_files/legislation/Instrucao_7-2006_full.pdf) --
    created new types of credit for the variable type (codes 11-14)
    which include guarantees, sureties, and credit communicated by
    foreign central banks.

-   [**Instrução no.
    21/2008**](./aux_files/legislation/Instrucao_21-2008_full.pdf) --
    changed the CRC to its format up to August, 2018 (as in *Caderno* da
    CRC) and defined the scope, reporting deadline, and stress the
    important of reporting the types of information. Some codes were
    significantly changed.

-   [**Instrução no.
    7/2009**](./aux_files/legislation/Instrucao_7-2009.pdf) -- included
    credit reports from the State to protect unemployed individuals'
    real estate ownership and created a special classification for these
    credits. This revised version contains more loan-level variables.
    Another important consequence of the revision was the incorporation
    of loans to Portuguese firms granted by foreign branches of
    Portuguese banks.

-   [**Instrução no.
    18/2010**](./aux_files/legislation/Instrucao_18-2010.pdf) -- imposed
    mandatory reporting of credit less than 90 days overdue (*crédito
    sem recurso*) if used in guarantee pools in Eurosystem operations;
    excluded shareholder's advances (*suprimentos*) from financial
    institutions; imposed mandatory reporting of securitized debt issued
    for a certain debtor (even if the financial institution does not
    have ownership) and exclusion of securitized debt in the exposure
    sheet of the institution.

-   [**Instrução no.
    17/2013**](./aux_files/legislation/Instrucao_17-2013.pdf) --
    separated overdue and written-off credit in litigation -- codes 6
    and 7; added new maturity categories and new collateral
    classifications.

-   [**Regulation (EU) 2016/867 of The European Central
    Bank**](./aux_files/legislation/EU_2016.867_en.pdf) -- provided
    guidance to report granular credit and credit risk data in a
    consistent and effective way across the members of the euro area.

-   [**Instrução no.
    17/2018**](./aux_files/legislation/Instrucao_17-2018.pdf) -- set out
    the Portuguese AnaCredit statistical framework and defined the
    object, main concepts, reporting obligations concerning the
    communication scope, credit operations to be included and excluded,
    and the types of information that needs to be reported.

# References

Below is a list of main references:

1.  Banco de Portugal (2003). Central de Responsabilidades de Crédito.
    Cadernos do Banco de Portugal. Lisboa.

2.  Banco de Portugal (2010). Central de Responsabilidades de Crédito.
    Cadernos do Banco de Portugal. Lisboa.

3.  Banco de Portugal (2011). Central de Responsabilidades de Crédito.
    Cadernos do Banco de Portugal. Lisboa.

4.  Banco de Portugal (2014). Central de Responsabilidades de Crédito.
    [**Manual de Procedimentos Instrução no.
    21/2008**](./aux_files/legislation/ManualdeprocedimentosdaCRC.pdf).
    Lisboa.

5.  Banco de Portugal (2015). Central de Responsabilidades de Crédito.
    Cadernos do Banco de Portugal. Lisboa.

6.  João Cadete de Matos (2015). The Portuguese Central Credit Register:
    a powerful multipurpose tool, relevant for many central bank
    functions. IFC workshop on "Combining micro and macro statistical
    data for financial stability analysis". Bank for International
    Settlements.

7.  Banco de Portugal (2015). [**Operational Support
    Guide**](./attachments/GuiaApoioTecnicoOperacional_v1.0.pdf).
    Lisboa.

# Useful Links

[CRC home page](https://www.bportugal.pt/en/area-cidadao/formulario/227)

[Statistical
Bulletin](https://www.bportugal.pt/en/publications/banco-de-portugal/all/123)

[ECB Guidelines on
AnaCredit](https://www.ecb.europa.eu/stats/money_credit_banking/anacredit/html/index.en.html)

# Citation of this dataset

Banco de Portugal Microdata Research Laboratory (BPLIM) (2024):
Harmonized Central Credit Responsibility Database. Extraction: June
2024. Version: V1. Banco de Portugal - BPLIM. Dataset.
https://doi.org/10.17900/HCRC.Jun2024.V1

To cite this data set you can use the package biblatex with the
following BibTeX entry:

```         
@dataset{HCRC.Jun2024.V1, 
author = {{Banco de Portugal Microdata Research Laboratory (BPLIM)}}, 
publisher = {Banco de Portugal - BPLIM.Dataset}, 
title = {{H}armonized {C}entral {C}redit {R}esponsibility {D}atabase}, 
year = {2024}, 
version = {{ V1, Extraction: June 2024}},
doi = {10.17900/HCRC.Jun2024.V1}, 
url = {https://doi.org/10.17900/HCRC.Jun2024.V1} 
}
```
