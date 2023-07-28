
---
title: Central Credit Responsibility Database - Exposure, Firm, and Bank-Firm Level - Data Manual
---


`Extraction Date`: June 2019

`Manual Date`: 11 January 2021

\

**Abstract**: The Central Credit Responsibility (CCR) database reports credit supply (that is, the outstanding of credit exposure defined according to a set of variables) by all credit-granting institutions in Portugal from 1999 onwards. Data is collected monthly with the objective of supporting participants in the risk assessment of the concession credit. The microdata available to internal researchers consists of data at credit  exposure level as well as data aggregated at the firm and bank-firm level. The dataset is updated annually.

\

**Keywords**: credit exposure, firm level, bank-firm level, credit-granting institutions, bank-firm relationship, revisions.

\



# Table of Contents

1. [General Information](#general-information)

2. [Geographical Coverage](#geographical-coverage)

3. [Population](#population)

4. [Methodology](#methodology)

5. [Description of Files](#description-of-files)

     5.1. [The Credit Exposure File](#a.-the-credit-exposure-file)

     5.2. [The Bank-Firm Credit Outstanding File](#b.-the-bank-firm-credit-outstanding-file)

     5.3. [The Credit Outstanding and Bank Relationship File](#c.-the-credit-outstanding-and-bank-relationship-file)

6. [Description of Variables](#description-of-variables)

    6.1. [Identifier](#a.-identifier)

    6.2. [Credit Exposure](#b.-credit-exposure)

    6.3. [Credit Outstanding](#c.-credit-outstanding)

    6.4. [Bank Relationship](#d.-bank-relationship)

7. [Basic Descriptive Statistics](#basic-descriptive-statistics)

8. [Building Compatible Series Using Credit Exposure Data](#building-compatible-series-using-credit-exposure-data)

    8.1. [Relevant Filters](#a.-relevant-filters)

    8.2. [Compatibility Issues](#b.-compatibility-issues)

    8.2.1. [Credit Situation](#b.1.-credit-situation)

    8.2.2. [Debt Maturity](#b.2.-debt-maturity)

    8.2.3. [Exposure Restructuring](#b.3.-exposure-restructuring)

    8.2.4. [Special Characteristics](#b.4.-special-characteristics)

    8.2.5. [Guarantor](#b.5.-guarantor)

    8.2.6. [Collateral](#b.6.-collateral)

    8.2.7. [Additional Concerns](#b.7.-additional-concerns)

9. [Legislation](#legislation)

10. [Citation of This Dataset](#citation-of-this-dataset)

11. [Auxiliary Files](#auxiliary-files)

12. [Useful Links](#useful-links)

13. [Useful Ado Files](#useful-ado-files)

    13.1. [Harmonization of Variables Over Time](#a.-harmonization-of-variables-over-time)

    13.2. [Aggregation](#b.-aggregation)

    13.3. [Construction of Firm Default Profile](#b.-construction-of-firm-default-profile)

    13.4. [Construction of Bank-Firm Relationship Spells](#c.-construction-of-bank-firm-relationship-spells)

14. [Frequently Asked Questions](#frequently-asked-questions)

15. [References](#references)

16. [Appendix](#appendix)



# General Information


> `Data Type` </u>: Longitudinal Data

> `Unit of Analysis` </u>: Credit Exposure, Firm, Firm-Bank

> `Frequency` </u>: Monthly

> `Start Date` </u>: January, 1999

> `Most Recent Date` </u>: August, 2018

> `Reference Date` </u>: the last day of a month

> `Data Organization` </u>: data is organized in three datafiles: the credit exposure file (EXP), the bank-firm level credit outstanding file (CO). All files are in long format and are available in Stata format and the firm level credit outstanding & bank relationship file (COBR).

> `Version of the Data` </u>: the data made available by BPLIM corresponds to a data freeze at a certain time of the year. Therefore, all files contain the information as reported in the extraction date. The most recent update of the data occurred in April 2019.

> `Languages Available` </u>: For the exposure level data, variables labels are available in Portuguese and in English. [^1] For the firm and the bank-firm level data, variables labels are only available in English.

[^1]: To see the labels in English type the following command line in Stata: “label language en”. If you use version 14 of Stata and choose to see the labels in Portuguese, you have to translate from extended ASCII to Unicode.

> `Data Access` </u>: These datasets, after anonymization, are available to internal researchers. External researchers can access the firm level credit outstanding & bank relationship file (COBR) under certain conditions.[^2]

[^2]: Conditions for data access for external researchers are detailed in the disclosure control regulation.

>  `Digital Object Identifier`: 10.17900/CRC.FRM.Jun2019.V1;
10.17900/CRC.FRMBNK.Jun2019.V1;
10.17900/CRC.EXP.Jun2019.V1.


# Geographical Coverage

The Central Credit Responsibility (CCR) includes mainly firms operating in mainland Portugal and autonomous
regions - Azores and Madeira.

Although credit information on the indebtedness of foreign firms are
available in CCR, the obligation to provide credit information by
financial institutions (Portuguese or foreign) on foreign firms has
changed over time.

Following the Memorandum among the national central banks in the
European Union[^3], credit exposures (more than 25000 euros) of Portuguese
collective persons obtained from financial institutions located in the
subscribed countries also started to be reported in 2005. From 2006,
loans granted to foreign firms in Portugual were requested to report
according to the Instrução nº 7/2006. From 2009, credit extended to
Portuguese firms by foreign branches of Portuguese banks is identifiable
through the variable *paisbalcaoid*.[^4]


[^3]: In addition to Portugal, the countries currently subscribed include Germany, Austria, Belgium, Spain, France, Italy, Czech Republic and Romania.

[^4]: CCR only includes foreign credits originated in the MOU countries (that is, Germany, Austria, Belgium, Spain, France, Italy, Czech Republic and Romania) since 2005. The reporting threshold (25000 euros) in this case is higher than that for firms resident in Portugal (50 euros since 2009). Please note that the COBR file (firm level data) and the CO file
(bank-firm level data) do not include foreign firms.


# Population

The Central Credit Responsibility (CCR) collects data on the
indebtedness of borrowers (including collective persons, individual
entrepreneurs and private persons) as reported by credit-granting
institutions (institutions operating in Portugal or foreign branches of
Portuguese banks).

All credit obligations above the reporting threshold are included,
regardless if the credit is in good standing or in situations of
non-compliance. The current mandatory loan registration threshold in
Portuguese Credit Responsibility is 50 euros.[^5] But firms have the
discretion to file the credit below the thresholds.

The entities participating in CCR include: banks, saving banks, mutual
agricultural credit banks, financial credit institutions, leasing
companies, factoring companies, securitization companies, mutual
guarantee societies, and financial companies for credit
acquisitions.[^6]

Although the information is collected at the credit exposure level
(EXP), BPLIM also provides data aggregated at the firm (COBR) and
bank-firm level (CO). Private persons, individual entrepreneurs, and guarantors are
excluded from the COBR and CO files.

<u> **Comment** </u>: Some financial institutions in Portugal
have experienced acquisitions and/or mergers, which induced credit flows
from one institution to another. The list of participating entities have
therefore changed over time. The current list can be found [***here***](./attachments/crc_lista_entidades.pdf)

Also note that the coverage of borrowers in CCR changed over time. Some
individuals may be included in the firm version of the CCR because they
were classified as entrepreneurs. Before 2009, these individuals are
identifiable because they have the NIPC codes beginning with 8. After
2009, these individuals were reassigned NIPC codes that either begin
with 5 or 9 (consistent with a firm) or 1 or 2 (consistent with an
individual). As a result, discontinuities in the coverage of firms of
different types and a noticeable gap in firm exits and entries can be
observed in January, 2009.

[^5]: The mandatory loan registration thresholds have changed over time. It was 10 euros before 2009.
[^6]: A few institutions which do not grant credit but the Banco de Portugal sees as relevant are also included in the CCR (for example restructuring funds).


# Methodology

The Central Credit Responsibility (CCR) plays a crucial role in monitoring and assessing credit risk at the
institution and the economy levels. The participating entities are
obliged to report to the Banco de Portugal their credit balances by the
end of each month, thus reflecting the situation of the liabilities of
their customers by that date. Banco de Portugal is responsible for
centralizing and disseminating the credit information after quality
control. The identification of the debtors is cross-checked with other
sources, ensuring that the identification exists and is valid.[^7]
Besides, to ensure the accuracy of the credit reports, the reporting
banks and financial companies are required to verify and correct
erroneous reports as soon as possible.

The original dataset comprises the credit exposure data, characterized
using a predefined set of contractual conditions. All credit obligations
are included, regardless if the credit is in good standing or in
situations of non-compliance, but only those with an amount equal to or
greater than the reporting threshold must be notified. Although the
Banco de Portugal collects information at the exposure level, data
aggregated at the firm level and at the bank-firm level is also made
available.

The CCR has undergone some major revisions. Due to these revisions,
there are some series breaks that may affect analysis. Of particular
relevance is the revision in 2009, framed by Decree-Law no. 204/2008, of
October 14, which streamlined the coding for a number of categorical
variables and included data on maturity of loans, overdue loan class,
collateral and special characteristics for the first time. To make
the aggregated variables compatible over time, we have adopted necessary
steps to harmonize the data. Available variables and their construction
methods are detailed in the [*Description of Variables*](#description-of-variables) section.


[^7]: For instance, the file of the taxpayers' identification numbers (NIF) managed by the Tax and Customs Authority (TA) and the National File of Collective Persons (FNPC) managed by the Ministry of Justice) are cross checked.


Additional cleaning is conducted at BPLIM. In particular, the values that
were reported in different scales and in other currencies were converted to euros.
 Therefore, regardless of the denominated currency, the value of the exposure is always
 expressed in euros. For confidentiality, firms are anonymized through unique identifiers.

 ![**Figure 1**: Data map](.\attachments\datamap.png)


# Description of Files

Three data files are proposed: the credit exposure file (EXP), the
bank-firm level credit outstanding file (CO) and the firm
level credit outstanding & bank relationship file (COBR).

**The credit exposure file (EXP)**: Each row
corresponds to one exposure in a given month, with the exposure
characterized according to a predefined set of exposure-specific
variables (credit situation, responsibility level, financial product,
overdue class, original maturity, residual maturity, amount, and
credit's base currency, etc.).


**The bank-firm level credit outstanding file (CO)**: Each row corresponds to a bank-firm pair in a given
month.


**The firm level credit outstanding & bank relationship file (COBR)**: Each row corresponds
to a firm in a given month.


Some variables are only calculated after 2009, for example, weighted
average debt maturity (original and residual). Examples are illustrated
in [***Appendix***](#appendix).


## *A. The Credit Exposure File*

Three data files are provided for credit exposure data: the general
exposure characteristics file, the collateral information file, and the
special characteristics file.

The general exposure characteristics files (excluding collateral
information and special characteristics) are identified by the following
nomenclature:

***CRC\_A\_MFRMEXP\_YYYY\_MMMYY\_BAL\_V01.dta,***

**where *YYYY* is the reporting year; *MMMYY* is the extraction month.**

Each credit exposure is denoted by the variable *cina*.

The collateral information files (only available from 2009) report the
collateral type and the collateral value for secured credit. One can merge
the collateral information file with the exposure characteristics file
using the variable *cina*. One credit exposure may be associated with more than one collateral.

The collateral information files are identified by the following
nomenclature:

***CRC\_A\_MFRMEXP\_YYYY\_MMMYY\_COLL\_V01.dta,***

**where *YYYY* is the reporting year; *MMMYY* is the extraction month.**

The special characteristics files (only available from 2009) specify credit
exposures with special characteristics and/or credit exposures extended
according to special regimes, for instance, credit used in a
securitization operation and credit for protecting permanent housing
property (as framed by Decree-Law103/2009). One can merge
the special characteristics file with the exposure characteristics file
using the variable *cina*. One credit exposure may be
associated with more than one special characteristics.

The special characteristics files are identified
by the following nomenclature:

***CRC\_A\_MFRMEXP\_YYYY\_MMMYY\_SCHAR\_V01.dta***

**where *YYYY* is the reporting year; *MMMYY* is the extraction month.**


## *B.    The Bank-Firm Credit Outstanding File*

The bank-firm level data is organized in the credit outstanding (CO)
file and has the following nomenclature:

***CRC_A_MFRMBNK_YYYY_MMMYY_COBR_V01.dta***

**where *YYYY* is the reporting year; *MMMYY* is the extraction month.**

Bank-firm relationship variables are not presented in this data file.
The "*relationspell*" ado, provided at BPLIM, can be used to generate
these variables.


## *C.    The Credit Outstanding and Bank Relationship File*

The firm level data is organized in the credit outstanding & bank
relationship (COBR) file. Some variables are only calculated after 2009, for example,
weighted average debt maturity (original and residual).

The data files have the following nomenclature:

***CRC_A_MFRM_YYYY_MMMYY_COBR_V01.dta***

**where *YYYY* is the reporting year; *MMMYY* is the extraction month.**

Monthly dataset is presented in files with the following nomenclature:


# Description of Variables

## *A. Identifier*

-  `Debtor identifier`

Unique identifier that enables tracking debtors over time.
*tina* is the anonymized tax identification number, available in all files.
 It should be noted that reporting to CCR does not depend on the nationality of the
debtors but their country of residence. In situations where a debtor
is not resident in Portugal and does not have a tax number assigned in
Portugal, the debtor is reported through a unique code generated by the
participating institution itself, namely "Source Code".[^8] Banco de
Portugal controls the credibility of debtor identification in CCR by
cross-checking other sources[^9] to ensure that the identification
exists and is valid.

+-------------------------------------------------------+--------------------------------+
| Abbreviation                                          | Definition                     |
+:======================================================+:===============================+
| *tina*                                                | Anonymized firm identifier     |
+-------------------------------------------------------+--------------------------------+

**Availability**: January, 1999-August, 2018

-  `Creditor identifier`

Unique identifier that enables tracking creditors over time. *bina* is the anonymized bank identification number, available in the credit exposure file (EXP) and the bank-firm level credit outstanding file (CO).

+-------------------------------------------------------+--------------------------------+
| Abbreviation                                          | Definition                     |
+:======================================================+:===============================+
| *bina*                                                | Anonymized bank identifier     |
+-------------------------------------------------------+--------------------------------+

**Availability**: January, 1999-August, 2018

-  `Credit exposure identifier`

Identifier for each credit exposure.

*cina* is the anonymized credit identification number, only available in the credit exposure file (EXP).
For the same credit exposure, the code changes on a monthly basis and therefore
cannot be used to follow a credit through time. This variable is,
however, useful to merge with auxiliary data files of collateral and
special characteristics.

+-------------------------------------------------------+--------------------------------+
| Abbreviation                                          | Definition                     |
+:======================================================+:===============================+
| *cina*                                                | Anonymized credit identifier   |
+-------------------------------------------------------+--------------------------------+

**Availability**: January, 2009-August, 2018

-  `Reference date`

The reference month of the data

+-------------------------------------------------------+--------------------------------+
| Abbreviation                                          | Definition                     |
+:======================================================+:===============================+
| *date*                                                | Reference month of the data    |
+-------------------------------------------------------+--------------------------------+


**Availability**: January, 1999-August, 2018

[^8]: The use of the Source Code allows compliance with the reporting of a firm/individual’s liabilities resulting from all credit operations. However, the centralization and dissemination of centralized information for debtors reported with Source Code might be limited, since the same debtor will surely have a distinct code communicated by different institutions.
[^9]: For instance, the file of the taxpayers' identification numbers (NIF), managed by the Tax and Customs Authority (TA), and the National File of Collective Persons (FNPC), managed by the Ministry of Justice.

## *B.    Credit Exposure*

-  `Type of credit`

The type of credit, reported in CCR before 2009, characterizes general
credit status. The classification has changed over time. The first
classification regime includes only the codes 1-7, defining different
types of financial instruments. To facilitate further assessment of
credit risk in Portugal, new categories of "credit in litigation" (code
8) and "written-off credit" (code 9) were introduced in January, 1993,
and "renegotiated credit" (code 10) in November, 2001. Later, following
the Instrução nº 7/2006, additional types (codes 11-14) were
incorporated in October, 2006, including guarantees, sureties, and
credit communicated by foreign central banks.

+-------------------------------------------------------+--------------------------------+
| Abbreviation                                          | Definition                     |
+:======================================================+:===============================+
| *tipocredito*                                         | Type of credit                 |
+-------------------------------------------------------+--------------------------------+


**Availability**: January, 1999-December, 2008

+---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Classification                                    | Definition                                                                                                                  |
+:==================================================+:============================================================================================================================+
|  1                                                | Commercial                                                                                                                  |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  2                                                | Discount funding                                                                                                            |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  3                                                | Other short term funding                                                                                                    |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  4                                                | Medium and Long term funding                                                                                                |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  5                                                | Other responsibilities                                                                                                      |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  6                                                | Off balance sheet liabilities (potential indebtedness)                                                                      |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  7                                                | Overdue Credit (non-performing loans)                                                                                       |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  8                                                | Credit in litigation                                                                                                        |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  9                                                | Written-off credit                                                                                                          |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  10                                               | Renegotiated credit                                                                                                         |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  11                                               | Guarantees provided by participating entities to ensure the compliance of credit operations by other participating entities |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  12                                               | Guarantees or sureties                                                                                                      |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  13                                               | Effective credit communicated by foreign banks                                                                              |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  14                                               | Potential credit communicated by foreign banks                                                                              |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+


-  `Responsibility level`

The responsibility level characterizes the type of participation that
the client has in a credit operation, allowing to distinguish between
borrowers and sureties/guarantors and between individual and joint responsibilities.

The credit exposures for a debtor and its sureties/guarantor
 are communicated with identical characteristics,
except for the variables associated with the level of responsibility and
identification of the debtor.

The exposure of the guarantor is reported with characteristics similar
to the secured exposure in all variables except for the followings:
The identification of the party (debtor/guarantor);
The responsibility level;
The credit situation.

This variable is available from 1999 and has undergone a series of
changes in classification, as framed by the Instrução nº 16/2001, the
Instrução nº 7/2006, and the Instrução nº21/2008. To construct a
harmonized series, one can use the ado file provided by BPLIM.

+-------------------------------------------------------+--------------------------------+
| Abbreviation                                          | Definition                     |
+:======================================================+:===============================+
| *nivelresponsabilidade*                               | Responsibility level           |
+-------------------------------------------------------+--------------------------------+

**Availability**: January, 1999-August, 2018

+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Classification                                          | Definition                                                                                                                  |
+:========================================================+:============================================================================================================================+
| *from January, 1999 to October, 2001*                   |                                                                                                                   |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  1                                                      | Individual credit                                                                                                           |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  11                                                     | Individual credit - savings-emigrant - acquisition of buildings                                                             |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  12                                                     | Individual credit - savings-emigrant - other activities                                                                     |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  13                                                     | Individual credit - savings-emigrant - buildings + other activities                                                         |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  2                                                      | Joint credit (credit more than one beneficiary) - 1ºdebtor                                                                  |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  21                                                     | Joint credit 1ºdebtor. - saving-emigrant - acquisition buildings                                                            |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  22                                                     | Joint credit 1ºdebtor. - saving-emigrant - other activities                                                                 |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  23                                                     | Joint credit 1ºdebtor. - saving-emigrant - buildings + other activities                                                     |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  3                                                      | Joint credit (credit more than one beneficiary) - remaining debtors                                                         |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  31                                                     | Joint credit- remaining debtors - saving-emigrant - acquisition buildings                                                   |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  32                                                     | Joint credit - remaining debtors - saving-emigrant - other activities                                                       |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  33                                                     | Joint credit - remaining debtors - savings-emigrant - buildings+ other activities                                           |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| *from November, 2001 to September, 2006*                |                                                                                                                   |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  1                                                      | Individual credit                                                                                                           |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  11                                                     | Individual credit - savings-emigrant - acquisition of buildings                                                             |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  12                                                     | Individual credit - savings-emigrant - other activities                                                                     |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  13                                                     | Individual credit - savings-emigrant - buildings + other activities                                                         |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  14                                                     | Individual credit - credit due to operations of securitization                                                              |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  2                                                      | Joint credit (credit more than one beneficiary) - 1ºdebtor                                                                  |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  21                                                     | Joint credit 1ºdebtor. - saving-emigrant - acquisition buildings                                                            |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  22                                                     | Joint credit 1ºdebtor. - saving-emigrant - other activities                                                                 |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  23                                                     | Joint credit 1ºdebtor. - saving-emigrant - buildings + other activities                                                     |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  24                                                     | Joint credit 1ºdebtor. - credit due to operations of securitization                                                         |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  25                                                     | Joint credit 1ºdebtor. -  mortgage-backed obligations or obligations in the public sector                                   |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  3                                                      | Joint credit (credit more than one beneficiary) - remaining debtors                                                         |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  31                                                     | Joint credit- remaining debtors - saving-emigrant - acquisition buildings                                                   |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  32                                                     | Joint credit - remaining debtors - saving-emigrant - other activities                                                       |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  33                                                     | Joint credit - remaining debtors - savings-emigrant - buildings+ other activities                                           |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  34                                                     | Joint credit - remaining debtors - credit due to operations of securitization                                               |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| *from October, 2006 to December, 2008*                  |                                                                                                                   |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  1                                                      | Individual credit                                                                                                           |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  11                                                     | Individual credit - savings-emigrant - acquisition of buildings                                                             |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  12                                                     | Individual credit - savings-emigrant - other activities                                                                     |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  13                                                     | Individual credit - savings-emigrant - buildings + other activities                                                         |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  14                                                     | Individual credit - credit due to operations of securitization                                                              |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  15                                                     | Individual credit -  mortgage-backed obligations or obligations in the public sector                                        |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  2                                                      | Joint credit (credit more than one beneficiary) - 1ºdebtor                                                                  |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  21                                                     | Joint credit 1ºdebtor. - saving-emigrant - acquisition buildings                                                            |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  22                                                     | Joint credit 1ºdebtor. - saving-emigrant - other activities                                                                 |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  23                                                     | Joint credit 1ºdebtor. - saving-emigrant - buildings + other activities                                                     |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  24                                                     | Joint credit 1ºdebtor. - credit due to operations of securitization                                                         |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  25                                                     | Joint credit 1ºdebtor. -  mortgage-backed obligations or obligations in the public sector                                   |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  3                                                      | Joint credit (credit more than one beneficiary) - remaining debtors                                                         |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  31                                                     | Joint credit- remaining debtors - saving-emigrant - acquisition buildings                                                   |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  32                                                     | Joint credit - remaining debtors - saving-emigrant - other activities                                                       |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  33                                                     | Joint credit - remaining debtors - savings-emigrant - buildings+ other activities                                           |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  34                                                     | Joint credit - remaining debtors - credit due to operations of securitization                                               |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  35                                                     | Joint credit - remaining debtors –  mortgage-backed obligations or obligations in the public sector                         |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  4                                                      | Joint credit – communicated via foreign channels                                                                            |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| *from 2009 onwards*                                     |                                                                                                                   |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  1                                                      | Individual credit                                                                                                           |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  2                                                      | Joint credit – 1.º debtor                                                                                                   |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  3                                                      | Joint credit – remaining debtors                                                                                            |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  4                                                      | Individual guarantor                                                                                                        |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  5                                                      | Joint guarantor                                                                                                             |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+


-  `Credit situation`

The credit situation characterizes the exposure as to its current status of usage
and the degree of compliance with the payment of the
credit. In the case of overdue or written off credit, this variable is used to identify
the existence, validity, enforceability and enforcement of legal
proceedings.

This variable is available from 2009 onwards and underwent a major change
in classification in June, 2014, framed by the Instrução nº 17/2013.
Specifically, "Overdue credit" (code 3) is thereafter
separated into two distinct exposures, i.e., "overdue credit" (code 3)
and "overdue credit in litigation" (code 6). "Written-off credit"
 (code 4) is separated into two distinct exposures,
i.e., "written-off credit" (code 4) and "written-off credit in
litigation" (code 7). The harmonization of this variable can be
conducted using the ado file provided by BPLIM.

<u> **Comment** </u>: *Banco de Portugal* requires all
credit-granting institutions to report to the CCR their irrevocable credit obligations.
There is one important exception of an institution which stopped reporting
revocable credit card obligations in May 2013, causing a break in the
data.

+-------------------------------------------------------+--------------------------------+
| Abbreviation                                          | Definition                     |
+:======================================================+:===============================+
| *situacaocredito*                                     | Credit situation               |
+-------------------------------------------------------+--------------------------------+

+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Classification                                          | Definition                                                                                                                  |
+:========================================================+:============================================================================================================================+
|  1                                                      | Regular credit                                                                                                              |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  2                                                      | Potential Credit                                                                                                            |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  3                                                      | Overdue credit                                                                                                              |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  4                                                      | Written-off credit                                                                                                          |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  5                                                      | Renegotiated credit                                                                                                         |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  6                                                      | Overdue credit in litigation                                                                                                |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  7                                                      | Written-off credit in litigation                                                                                            |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+

**Availability**: January, 2009-August, 2018


-  `Overdue credit class`

This variable is intended to indicate the time elapsed from the time
that a credit enters into default, that is, when the credit situation is denoted as
"overdue credit" or "overdue credit in litigation".

The credit overdue class list is the same as defined for the purposes of
the banking chart of accounts (NCA and PCSB), with only the exception of
the shortest duration classes "up to 3 months", which is further divided
into three classes in the table adopted in CCR ("up to 1 month", "from 1
to 2 months" and "from 2 to 3 months"). In the case when loans are
repaid in varying installments, the total overdue amount of unpaid
installments is communicated in a single overdue credit exposure,
classified in overdue credit class corresponding to the installments
with longer overdue time.

+-------------------------------------------------------+--------------------------------+
| Abbreviation                                          | Definition                     |
+:======================================================+:===============================+
| *classecreditovencido*                                | Overdue credit class           |
+-------------------------------------------------------+--------------------------------+

+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Classification                                          | Definition                                                                                                                  |
+:========================================================+:============================================================================================================================+
|  1                                                      | Up to 1 month                                                                                                               |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  2                                                      | From 1 to 2 months                                                                                                          |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  3                                                      | From 2 to 3 months                                                                                                          |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  4                                                      | From 3 to 6 months                                                                                                          |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  5                                                      | From 6 to 9 months                                                                                                          |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  6                                                      | From 9 to 12 months                                                                                                         |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  7                                                      | From 12 to 15 months                                                                                                        |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  8                                                      | From 15 to 18 months                                                                                                        |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  9                                                      | From 18 to 24 months                                                                                                        |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  10                                                     | From 24 to 30 months                                                                                                        |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  11                                                     | From 30 to 36 months                                                                                                        |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  12                                                     | From 36 to 48 months                                                                                                        |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  13                                                     | From 48 to 60 months                                                                                                        |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  14                                                     | More than 60 months                                                                                                         |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+



**Availability**: January, 2009-August, 2018

-  `Maturity`

All credit exposures reported in the CCR after 2009 are classified based
on their original maturity, established in contractual terms, as well as on their
residual maturity, defined as the time interval between the reference
date and the maturity date of the credit agreement. The original term of
the credit characterizes the exposure in relation to
the maturity that was contracted for the full repayment of the credit,
while the residual term of the credit characterizes the exposure in
relation to the maturity between the date to which the communication
refers and the date contracted for the full amortization of the credit.

These two variables are defined in ranges, including a category
"Undetermined" (code 1) which is used to characterize credit exposures
which, by their nature, do not have a contractually defined maturity or
for which it is not possible to determine a due date.

This variable is available from 2009 onwards but has undergone a major change
in classification in December, 2013, framed by the Instrução nº 17/2013.
For example, the maturity class "1 to 5 years" (code 5) is only valid
between January, 2009 and November, 2013. From December 2013, this
category is replaced by the maturity class codes 51-54. The same applies
to the maturity class "5 to 10 years" (code 6 replaced by codes 61-65),
and the maturity class "10 to 20 years" (code 7 replaced by codes 71 and
72). The harmonization of this variable can be conducted using the ado
file provided by BPLIM.

+-------------------------------------------------------+--------------------------------+
| Abbreviation                                          | Definition                     |
+:======================================================+:===============================+
| *prazooriginal*                                       | Original maturity              |
+-------------------------------------------------------+--------------------------------+
| *prazoresidual*                                       | Residual maturity              |
+-------------------------------------------------------+--------------------------------+

**Availability**: January, 2009-August, 2018



+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Classification                                          | Definition                                                                                                                  |
+:========================================================+:============================================================================================================================+
| *before December, 2013*                                 |                                                                                                                             |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  1                                                      | Undefined                                                                                                                   |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  2                                                      | Up to 90 days                                                                                                               |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  3                                                      | From 90 days to 180 days                                                                                                    |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  4                                                      | From 180 days to 1 year                                                                                                     |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  5                                                      | From  1  to 5 years                                                                                                         |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  6                                                      | From  5  to 10 years                                                                                                        |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  7                                                      | From  10  to 20 years                                                                                                       |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  8                                                      | From 20 to 25 years                                                                                                         |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  9                                                      | From 25 to 30 years                                                                                                         |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  10                                                     | Over 30 years                                                                                                               |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| *from December, 2013 onwards*                           |                                                                                                                             |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  1                                                      | Undefined                                                                                                                   |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  2                                                      | Up to 90 days                                                                                                               |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  3                                                      | From 90 days to 180 days                                                                                                    |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  4                                                      | From 180 days to 1 year                                                                                                     |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  51                                                     | From 1  to 2 years                                                                                                          |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  52                                                     | From 2  to 3 years                                                                                                          |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  53                                                     | From 3  to 4 years                                                                                                          |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  54                                                     | From 4  to 5 years                                                                                                          |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  61                                                     | From 5  to 6 years                                                                                                          |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  62                                                     | From 6  to 7 years                                                                                                          |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  63                                                     | From 7  to 8 years                                                                                                          |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  64                                                     | From 8  to 9 years                                                                                                          |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  65                                                     | From 9  to 10 years                                                                                                         |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  71                                                     | From 10  to 15 years                                                                                                        |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  72                                                     | From 15  to 20 years                                                                                                        |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  8                                                      | From 20 to 25 years                                                                                                         |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  9                                                      | From 25 to 30 years                                                                                                         |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  10                                                     | Over 30 years                                                                                                               |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+



-  `Financial product`

The financial product characterizes the types
of credit and/or purpose of the credit. In order to facilitate the
classification of credit exposures, the nomenclature used is close to
that adopted in the chart of accounts in accordance with the NCA. The
classification covers 15 different categories covering the most
representative types of credit, based on businesses funding as well as on
individual financing. Some of the financial products are geared to
individual financing while others are mainly for businesses and other
legal persons. For instance, products such as "current account (credit
lines)", "factoring", "real estate leasing" and "financing to the
corporate activity or equivalent" are more geared to finance activities
of firms or other legal persons. Debtors characterized as individual
entrepreneurs may also have credits of typical financial product as
companies do.


+-------------------------------------------------------+--------------------------------+
| Abbreviation                                          | Definition                     |
+:======================================================+:===============================+
| *produto*                                             | Financial product              |
+-------------------------------------------------------+--------------------------------+

**Availability**: January, 2009-August, 2018


+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Classification                                          | Definition                                                                                                                  |
+:========================================================+:============================================================================================================================+
|  1                                                      | Discount and other credits secured by effects                                                                               |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  2                                                      | Current account (credit lines)                                                                                              |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  3                                                      | Overdrafts on deposit accounts                                                                                              |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  4                                                      | Recourse factoring                                                                                                          |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  5                                                      | None-recourse factoring                                                                                                     |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  6                                                      | Real estate leasing                                                                                                         |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  7                                                      | Non-real estate leasing                                                                                                     |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  8                                                      | Financing to the corporate activity or equivalent                                                                           |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  9                                                      | Credit card                                                                                                                 |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  10                                                     | Mortgage credit                                                                                                             |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  11                                                     | Consumer credit                                                                                                             |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  12                                                     | Automobile credit                                                                                                           |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  13                                                     | Other credit                                                                                                                |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  14                                                     | Bank Guarantees from other participating institutions                                                                       |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  15                                                     | Other bank guarantees                                                                                                       |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+




-  `Collateral`

As long as the collateral/guarantee exists, it is
mandatory to communicate to CCR its existence together with the credit exposure
that it ensures. The collateral/guarantee is reported to CCR on a
monthly basis, regardless of whether its value changes or not. The
collateral amounts relating to a credit are aggregated by type of collateral using the same
criteria as to the credit exposure.

This variable is available from 2009 onwards and it has undergone a
major change in classification in June, 2014, as framed by the Instrução
nº 17/2013. For example, the collateral "Real Collateral Mortgage" (code
1) is only valid in the reporting period between January 2009 and May 2014.
From June 2014, it is replaced by the categories "Real Collateral
Mortgage - Real Estate" (code 11) and "Real Collateral Mortgage --
Other" (code 12). The same applies to the categories "Financial
Collateral" (code 3) which was replaced by the codes 31-39, and
"Personal Guarantee - granted by the State or financial institution"
(code 5) which was replaced by the Codes 51 to 53. The harmonization of
this variable before and after the affecting month can be realized by
using the ado file provided by BPLIM.


+-------------------------------------------------------+--------------------------------+
| Abbreviation                                          | Definition                     |
+:======================================================+:===============================+
| *tipogarantia*                                        | Type of collateral             |
+-------------------------------------------------------+--------------------------------+
| *valorg*                                              | Amount of collateral           |
+-------------------------------------------------------+--------------------------------+

**Availability**: January, 2009-August, 2018


+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Classification                                          | Definition                                                                                                                  |
+:========================================================+:============================================================================================================================+
| *before June, 2014*                                     |                                                                                                                             |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  1                                                      | Real collateral mortgage                                                                                                    |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  2                                                      | Real collateral - not mortgaged                                                                                             |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  3                                                      | Financial collateral                                                                                                        |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  4                                                      | Personal guarantee - Provided by firm or individual                                                                         |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  5                                                      | Personal guarantee - Granted by the state or financial institution                                                          |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  6                                                      | Other guarantees                                                                                                            |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| *from Jun, 2014 onwards*                                |                                                                                                                             |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  11                                                     | Real collateral mortgage - housing                                                                                          |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  12                                                     | Real collateral mortgage - others                                                                                           |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  2                                                      | Real collateral - not mortgaged                                                                                             |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  31                                                     | Financial collateral - deposits                                                                                             |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  32                                                     | Financial collateral – Portuguese public debt                                                                               |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  33                                                     | Financial collateral – Public debt of non-residents and multinational organizations                                         |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  34                                                     | Financial collateral – Debt of other entities                                                                               |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  35                                                     | Financial collateral – Stocks and other participations in listed companies                                                  |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  36                                                     | Financial collateral – Stocks and other participations in unlisted companies                                                |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  39                                                     | Financial collateral – Other instruments                                                                                    |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  4                                                      | Personal guarantee - Provided by firm or individual                                                                         |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  51                                                     | Personal guarantee – Granted by the Portuguese State                                                                        |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  52                                                     | Personal guarantee – Granted by other governments or by multinational organizations                                         |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  53                                                     | Personal guarantee – Granted by financial institutions                                                                      |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  6                                                      | Other guarantees                                                                                                            |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+


-  `Special characteristics`

This variable characterizes special regimes to which a credit exposure belongs for
the purpose of performing supervision, financial system stability or
monetary policy analyses. New classifications are introduced over time.
For instance, the Decree-Law No. 103/2009, of 12 May, led to the
creation of a special and temporary credit line, provided by the State,
for the protection of permanent residence in cases that at least one of
the debtors is unemployed (code 10). Credit delivered as collateral for
Eurosystem credit operations (code 11) and credit with an IEB Code (code
12) are introduced according to the Instrução N.º 7/2012. In additions,
the codes 13 to 15 are included as framed by the Instrução 18/2012, the
Instrução 16/2004, the Decree law 227/2012 and the Law 58/2012.

+-------------------------------------------------------+--------------------------------+
| Abbreviation                                          | Definition                     |
+:======================================================+:===============================+
| *caracteristicas*                                     | Special characteristics        |
+-------------------------------------------------------+--------------------------------+

**Availability**: January, 2009-August, 2018


+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Classification                                          | Definition                                                                                                                  |
+:========================================================+:============================================================================================================================+
|  1                                                      | Credit conceded in a recognized securitization operation with the intervention of a resident financial vehicle              |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  2                                                      | Credit conceded in a recognized securitization operation with the intervention of a nonresident financial vehicle           |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  3                                                      | Credit conceded in an unrecognized securitization operation with the intervention of a resident financial vehicle           |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  4                                                      | Credit conceded in an unrecognized securitization operation with the intervention of a nonresident financial vehicle        |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  5                                                      | Syndicated loan                                                                                                             |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  6                                                      | Mortgage-backed loan                                                                                                        |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  7                                                      | Public loan                                                                                                                 |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  8                                                      | Credit associated with emigrant´s savings accounts for purchasing buildings                                                 |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  9                                                      | Credit associated with emigrant´s savings accounts for other purposes                                                       |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  10                                                     | Credit for protecting permanent housing property ([**Decree-Law103/2009**](./aux_files/legislation/Lei_103-2009.pdf))                                                       |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  11                                                     | Loan extended as collateral for credit operations in Eurosystem ([**Instruction N.º 7/2012**](./aux_files/legislation/Instrucao_07-2012.pdf))                                    |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  12                                                     | Loan featured with identification code (IEB) ([**Instruction N.º 7/2012**](./aux_files/legislation/Instrucao_07-2012.pdf))                                                       |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  13                                                     | Credit restructured for customers in financial difficulties ([**Instruction 18/2012**](./aux_files/legislation/Instrucao_18-2012.pdf))                                           |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  14                                                     | Credit at risk ([**Instruction 16/2004**](./aux_files/legislation/Instrucao_16-2004.pdf))                                   |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
|  15                                                     | Credit in an out-of-course renegotiation procedure (PERSI) ([**Decree-Law No. 227/2012**](./aux_files/legislation/Lei_227-2012.pdf)) or in a Special Regime ([**Law 58/2012**](./aux_files/legislation/Lei_58-2012.pdf))   |
+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+



-  `Credit amount`

This variable identifies the total amount outstanding of a credit.
Loans of the same debtor and creditor with
identical characteristics are aggregated into a single exposure.
Given different credit situations, it is possible for a credit exposure
to be divided into more than one exposures in some situations. Note that
regardless of the credit denominated currency, the value of the exposure
must always be expressed in euro units.

+-------------------------------------------------------+--------------------------------+
| Abbreviation                                          | Definition                     |
+:======================================================+:===============================+
| *valor*                                               | Credit amount                  |
+-------------------------------------------------------+--------------------------------+

**Availability**: January, 1999-August, 2018


-  `Bank's branch country`

This variable indicates the country of the branch in which a credit was
granted. Note that credit granted by foreign branches of Portuguese
banks is only reported consistently post-2009.

+-----------------------------------------------+--------------------------------------------------------+
| Abbreviation                                  | Definition                                             |
+:==============================================+:=======================================================+
| *paisbalcaoid*                                |Bank\'s branch country                                  |
+-----------------------------------------------+--------------------------------------------------------+

**Availability**: January, 2009-August, 2018


|**Country Code** |  **Country Name**  |
|:--------|:---------------|
ABW    |    Aruba    |
AFG    |    Afghanistan    |
AGO    |    Angola    |
AIA    |    Anguilla    |
ALA    |    Aland Islands    |
ALB    |    Albania    |
AND    |    Andorra    |
ANT    |    Netherlands Antilles    |
ARE    |    United Arab Emirates    |
ARG    |    Argentina    |
ARM    |    Armenia    |
ASM    |    American Samoa    |
ATA    |    Antarctica    |
ATF    |    South territories of France    |
ATG    |    Antigua and Barbuda    |
AUS    |    Australia    |
AUT    |    Austria    |
AZE    |    Azerbaijan    |
BDI    |    Burundi    |
BEL    |    Belgium    |
BEN    |    Benin    |
BFA    |    Burkina Faso    |
BGD    |    Bangladesh    |
BGR    |    Bulgaria    |
BHR    |    Bahrain    |
BHS    |    Bahamas    |
BIH    |    Bosnia Herzegovina    |
BLM    |    St. Bartholomew    |
BLR    |    Belarus    |
BLZ    |    Belize    |
BMU    |    Bermuda    |
BOL    |    Bolivia    |
BRA    |    Brazil    |
BRB    |    Barbados    |
BRN    |    Brunei    |
BTN    |    Bhutan    |
BVT    |    Bouvet Island (Norway Territory)    |
BWA    |    Botswana    |
CAF    |    Central African Republic    |
CAN    |    Canada    |
CCK    |    Cocos    |
CHE    |    Switzerland    |
CHL    |    Chile    |
CHN    |    China    |
CIV    |    Costa do Marfim    |
CMR    |    Cameroon    |
COD    |    Democratic Republic of Congo (former Zaire)    |
COG    |    Congo    |
COK    |    Cook Islands    |
COL    |    Colombia    |
COM    |    Comoros    |
CPV    |    Cape Verde    |
CRI    |    Costa Rica    |
CUB    |    Cuba    |
CUW    |    Curacao    |
CXR    |    Christmas island    |
CYM    |    Cayman Islands    |
CYP    |    Cyprus    |
CZE    |    Czech republic    |
DEU    |    Germany    |
DJI    |    Djibouti    |
DMA    |    dominica    |
DNK    |    Denmark    |
DOM    |    Dominican Republic    |
DZA    |    Algeria    |
ECU    |    Ecuador    |
EGY    |    Egypt    |
ERI    |    Eritrea    |
ESH    |    Western Sahara (former Spanish Sahara)    |
ESP    |    Spain    |
EST    |    Estonia    |
ETH    |    Ethiopia    |
FIN    |    Finland    |
FJI    |    Fiji    |
FLK    |    Falkland Islands (Malvinas)    |
FRA    |    France    |
FRO    |    Faroes Islands    |
FSM    |    Micronesia    |
GAB    |    Gabon    |
GBR    |    Great Britain (United Kingdom, UK)    |
GEO    |    Georgia    |
GGY    |    Guernsey    |
GHA    |    Ghana    |
GIB    |    Gibraltar    |
GIN    |    Guinea    |
GLP    |    Guadeloupe    |
GMB    |    Gambia    |
GNB    |    Guinea Bissau    |
GNQ    |    Equatorial Guinea    |
GRC    |    Greece    |
GRD    |    Grenade    |
GRL    |    Greenland    |
GTM    |    Guatemala    |
GUF    |    French Guiana    |
GUM    |    Guam (US Territory)    |
GUY    |    Guiana    |
HKG    |    Hong Kong    |
HMD    |    Heard and McDonald Islands (territory of Australia)    |
HND    |    Honduras    |
HRV    |    Croatia (Hrvatska)    |
HTI    |    Haiti    |
HUN    |    Hungary    |
IDN    |    Indonesia    |
IMN    |    Isle of Man    |
IND    |    India    |
IOT    |    Territory British Indian Ocean    |
IRL    |    Ireland    |
IRN    |    Will    |
IRQ    |    Iraq    |
ISL    |    Iceland    |
ISR    |    Israel    |
ITA    |    Italy    |
JAM    |    Jamaica    |
JEY    |    jersey    |
JOR    |    Jordan    |
JPN    |    Japan    |
KAZ    |    Kazakhstan    |
KEN    |    Kenya    |
KGZ    |    Kyrgyzstan    |
KHM    |    Cambodia    |
KIR    |    Kiribati    |
KNA    |    Saint Kitts and Nevis    |
KOR    |    South Korea    |
KWT    |    Kuwait    |
LAO    |    Laos    |
LBN    |    Lebanon    |
LBR    |    Liberia    |
LBY    |    Libya    |
LCA    |    Saint Lucia    |
LIE    |    Liechtenstein    |
LKA    |    Sri Lanka    |
LSO    |    Lesotho    |
LTU    |    Lithuania    |
LUX    |    Luxembourg    |
LVA    |    Latvia    |
MAC    |    Macao    |
MAF    |    St. Martin    |
MAR    |    Morocco    |
MCO    |    Monaco    |
MDA    |    Moldova    |
MDG    |    Madagascar    |
MDV    |    Maldives    |
MEX    |    Mexico    |
MHL    |    Marshall Islands    |
MKD    |    Macedonia (Republic Yugoslav)    |
MLI    |    Mali    |
MLT    |    Malta    |
MMR    |    Myanmar (former Burma)    |
MNE    |    Montenegro    |
MNG    |    Mongolia    |
MNP    |    Northern Mariana Islands    |
MOZ    |    Mozambique    |
MRT    |    Mauritania    |
MSR    |    montserrat    |
MTQ    |    Martinique    |
MUS    |    Mauritius    |
MWI    |    Malawi    |
MYS    |    Malaysia    |
MYT    |    Mayotte    |
NAM    |    Namibia    |
NCL    |    New Caledonia    |
NER    |    Niger    |
NFK    |    Norfolk Islands    |
NGA    |    Nigeria    |
NIC    |    Nicaragua    |
NIU    |    Niue    |
NLD    |    Netherlands    |
NOR    |    Norway    |
NPL    |    Nepal    |
NRU    |    Nauru    |
NZL    |    New Zealand    |
OMN    |    Oman    |
PAK    |    Pakistan    |
PAN    |    Panama    |
PCN    |    Pitcairn island    |
PER    |    Peru    |
PHL    |    Philippines    |
PLW    |    Palau    |
PNG    |    Papua New Guinea    |
POL    |    Poland    |
PRI    |    Puerto Rico    |
PRK    |    North Korea    |
PRT    |    Portugal    |
PRY    |    Paraguay    |
PSE    |    Occupied Palestinian Territories    |
PYF    |    French Polynesian    |
QAT    |    Qatar    |
REU    |    Reunion island    |
ROU    |    Romania    |
RUS    |    Russian Federation    |
RWA    |    Rwanda    |
SAU    |    Saudi Arabia    |
SDN    |    Sudan    |
SEN    |    Senegal    |
SGP    |    Singapore    |
SGS    |    South Georgia and the South Sandwich Islands    |
SHN    |    Saint Helen    |
SJM    |    Svalbard and Jan Mayen Islands    |
SLB    |    Solomon Islands    |
SLE    |    Sierra Leone    |
SLV    |    El Salvador    |
SMR    |    San Marino    |
SOM    |    Somalia    |
SPM    |    St. Pierre and Miquelon    |
SRB    |    Serbia    |
STP    |    Sao Tome and Principe    |
SUR    |    Suriname    |
SVK    |    Slovakia    |
SVN    |    Slovenia    |
SWE    |    Sweden    |
SWZ    |    Swaziland    |
SYC    |    Seychelles    |
SYR    |    Syria    |
TCA    |    Turks and Caicos Islands    |
TCD    |    Chad    |
TGO    |    Togo    |
THA    |    Thailand    |
TJK    |    Tajikistan    |
TKL    |    Tokelau Islands    |
TKM    |    Turkmenistan    |
TLS    |    East Timor (former East Timor)    |
TON    |    Tonga    |
TTO    |    Trinidad and Tobago    |
TUN    |    Tunisia    |
TUR    |    Turkey    |
TUV    |    Tuvalu    |
TWN    |    Taiwan    |
TZA    |    Tanzania    |
UGA    |    Uganda    |
UKR    |    Ukraine    |
UMI    |    US Outlying Islands    |
URY    |    Uruguay    |
USA    |    U.S    |
UZB    |    Uzbekistan    |
VAT    |    Vatican    |
VCT    |    Saint Vincent and the Grenadines    |
VEN    |    Venezuela    |
VGB    |    Virgin Islands (England)    |
VIR    |    Virgin Islands (United States)    |
VNM    |    Vietnam    |
VUT    |    Vanuatu    |
WLF    |    Wallis and Futuna Islands    |
WSM    |    Western Samoa    |
YEM    |    Yemen    |
ZAF    |    South Africa    |
ZMB    |    Zambia    |
ZWE    |    Zimbabwe    |


-  `Base currency`

After 2009, information on whether the credit was granted in a different
currency is provided. This variable is denoted using 3-digit ISO
currency code (ISO 4217). But the value of the credit (*valor* ) is always reported in
euros.

+-----------------------------------------------+--------------------------------------------------------+
| Abbreviation                                  | Definition                                             |
+:==============================================+:=======================================================+
| *moeda*                                       |Base currency                                           |
+-----------------------------------------------+--------------------------------------------------------+

**Availability**: January, 2009-August, 2018


|**Currency Code** |  **Currency Name**  |
|:--------|:---------------|
AED    |    UAE Dirham    |
ALL    |    Lek    |
AMD    |    Armenian Dram    |
ANG    |    Netherlands Antillean Guilder    |
AOA    |    Kwanza    |
ARS    |    Argentine Peso    |
AUD    |    Australian Dollar    |
AWG    |    Aruban Florin    |
AZN    |    Azerbaijan Manat    |
BAM    |    Convertible Mark    |
BBD    |    Barbados Dollar    |
BDT    |    Taka    |
BGN    |    Bulgarian Lev    |
BHD    |    Bahraini Dinar    |
BIF    |    Burundi Franc    |
BMD    |    Bermudian Dollar    |
BND    |    Brunei Dollar    |
BOB    |    Boliviano    |
BOV    |    Mvdol    |
BRL    |    Brazilian Real    |
BSD    |    Bahamian Dollar    |
BTN    |    Ngultrum    |
BWP    |    Pula    |
BYN    |    Belarusian Ruble    |
BZD    |    Belize Dollar    |
CAD    |    Canadian Dollar    |
CDF    |    Congolese Franc    |
CHE    |    WIR Euro    |
CHF    |    Swiss Franc    |
CHW    |    WIR Franc    |
CLF    |    Unidad de Fomento    |
CLP    |    Chilean Peso    |
CNY    |    Yuan Renminbi    |
COP    |    Colombian Peso    |
COU    |    Unidad de Valor Real    |
CRC    |    Costa Rican Colon    |
CUC    |    Peso Convertible    |
CUP    |    Cuban Peso    |
CVE    |    Cabo Verde Escudo    |
CZK    |    Czech Koruna    |
DJF    |    Djibouti Franc    |
DKK    |    Danish Krone    |
DOP    |    Dominican Peso    |
DZD    |    Algerian Dinar    |
EGP    |    Egyptian Pound    |
ERN    |    Nakfa    |
ETB    |    Ethiopian Birr    |
EUR    |    Euro    |
FJD    |    Fiji Dollar    |
FKP    |    Falkland Islands Pound    |
GBP    |    Pound Sterling    |
GEL    |    Lari    |
GHS    |    Ghana Cedi    |
GIP    |    Gibraltar Pound    |
GMD    |    Dalasi    |
GNF    |    Guinean Franc    |
GTQ    |    Quetzal    |
GYD    |    Guyana Dollar    |
HKD    |    Hong Kong Dollar    |
HNL    |    Lempira    |
HRK    |    Kuna    |
HTG    |    Gourde    |
HUF    |    Forint    |
IDR    |    Rupiah    |
ILS    |    New Israeli Sheqel    |
INR    |    Indian Rupee    |
IQD    |    Iraqi Dinar    |
IRR    |    Iranian Rial    |
ISK    |    Iceland Krona    |
JMD    |    Jamaican Dollar    |
JOD    |    Jordanian Dinar    |
JPY    |    Yen    |
KES    |    Kenyan Shilling    |
KGS    |    Som    |
KHR    |    Riel    |
KMF    |    Comorian Franc     |
KPW    |    North Korean Won    |
KRW    |    Won    |
KWD    |    Kuwaiti Dinar    |
KYD    |    Cayman Islands Dollar    |
KZT    |    Tenge    |
LAK    |    Lao Kip    |
LBP    |    Lebanese Pound    |
LKR    |    Sri Lanka Rupee    |
LRD    |    Liberian Dollar    |
LSL    |    Loti    |
LYD    |    Libyan Dinar    |
MAD    |    Moroccan Dirham    |
MDL    |    Moldovan Leu    |
MGA    |    Malagasy Ariary    |
MKD    |    Denar    |
MMK    |    Kyat    |
MNT    |    Tugrik    |
MOP    |    Pataca    |
MRU    |    Ouguiya    |
MUR    |    Mauritius Rupee    |
MVR    |    Rufiyaa    |
MWK    |    Malawi Kwacha    |
MXN    |    Mexican Peso    |
MXV    |    Mexican Unidad de Inversion (UDI)    |
MYR    |    Malaysian Ringgit    |
MZN    |    Mozambique Metical    |
NAD    |    Namibia Dollar    |
NGN    |    Naira    |
NIO    |    Cordoba Oro    |
NOK    |    Norwegian Krone    |
NPR    |    Nepalese Rupee    |
NZD    |    New Zealand Dollar    |
OMR    |    Rial Omani    |
PAB    |    Balboa    |
PEN    |    Sol    |
PGK    |    Kina    |
PHP    |    Philippine Peso    |
PKR    |    Pakistan Rupee    |
PLN    |    Zloty    |
PYG    |    Guarani    |
QAR    |    Qatari Rial    |
RON    |    Romanian Leu    |
RSD    |    Serbian Dinar    |
RUB    |    Russian Ruble    |
RWF    |    Rwanda Franc    |
SAR    |    Saudi Riyal    |
SBD    |    Solomon Islands Dollar    |
SCR    |    Seychelles Rupee    |
SDG    |    Sudanese Pound    |
SEK    |    Swedish Krona    |
SGD    |    Singapore Dollar    |
SHP    |    Saint Helena Pound    |
SLL    |    Leone    |
SOS    |    Somali Shilling    |
SRD    |    Surinam Dollar    |
SSP    |    South Sudanese Pound    |
STN    |    Dobra    |
SVC    |    El Salvador Colon    |
SYP    |    Syrian Pound    |
SZL    |    Lilangeni    |
THB    |    Baht    |
TJS    |    Somoni    |
TMT    |    Turkmenistan New Manat    |
TND    |    Tunisian Dinar    |
TOP    |    Pa’anga    |
TRY    |    Turkish Lira    |
TTD    |    Trinidad and Tobago Dollar    |
TWD    |    New Taiwan Dollar    |
TZS    |    Tanzanian Shilling    |
UAH    |    Hryvnia    |
UGX    |    Uganda Shilling    |
USD    |    US Dollar    |
UYU    |    Peso Uruguayo    |
UYW    |    Unidad Previsional    |
UZS    |    Uzbekistan Sum    |
VES    |    Bolívar Soberano    |
VND    |    Dong    |
VUV    |    Vatu    |
WST    |    Tala    |
XAF    |    CFA Franc BEAC    |
XCD    |    East Caribbean Dollar    |
XOF    |    CFA Franc BCEAO    |
XPF    |    CFP Franc    |
XSU    |    Sucre    |
XUA    |    ADB Unit of Account    |
YER    |    Yemeni Rial    |
ZAR    |    Rand    |
ZMW    |    Zambian Kwacha    |
ZWL    |    Zimbabwe Dollar    |



## *C.    Credit Outstanding*

The variables related to credit outstanding are calculated based on the
credit exposure data at both the firm level and the bank-firm level.
These variables characterize the amount outstanding according to a variety of
dimensions as discussed below.


-  `Global Credit`

Global credit is the sum of regular credit and potential credit, representing the total available credit that a firm accesses.

+-----------------------------------------------+--------------------------------------------------------+
| Abbreviation                                  | Definition                                             |
+:==============================================+:=======================================================+
| *valor_global*                                |Total available credit that a firm can accesses         |
+-----------------------------------------------+--------------------------------------------------------+

**Availability**: January, 1999-August, 2018

-  `Effective Credit`

Effective credit is credit effectively used in a regular or overdue situation, including overdue credit (i.e., payment delays as defined in the respective contract).


+---------------------------------------------------------------+--------------------------------------------------------+
| Abbreviation                                                  | Definition                                             |
+:==============================================================+:=======================================================+
| *valor_efectivo*                                              | Credit that a firm used effectively                    |
+---------------------------------------------------------------+--------------------------------------------------------+

**Availability**: January, 1999-August, 2018

+-----------------------------------------------------------------------------+
| **Examples of effective credit**                                                                                                                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------+
| Loans for the acquisition of financial instruments (shares, bonds, etc.)    |
+-----------------------------------------------------------------------------+
| Discount and other credits secured by effects                               |
+-----------------------------------------------------------------------------+
| Overdrafts on bank accounts                                                 |
+-----------------------------------------------------------------------------+
| Leasing and factoring                                                       |
+-----------------------------------------------------------------------------+
| Used amounts of credit cards                                                |
+-----------------------------------------------------------------------------+


-  `Potential Credit`

Potential credit represents irrevocable commitments of the participating entities.

+---------------------------------------------+--------------------------------------------------------------------------------------------------------------+
| Abbreviation                                | Definition                                                                                                   |
+:============================================+:=============================================================================================================+
| *valor_potencial*                           | Credit that a firm can access because of irrevocable commitments of the participating entities               |
+---------------------------------------------+--------------------------------------------------------------------------------------------------------------+

**Availability**: January, 1999-August, 2018

+-----------------------------------------------------------------------------+
| **Examples of potential credit**                                                                                                                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------+
| Unused amounts of credit cards                                              |
+-----------------------------------------------------------------------------+
| Lines of credit                                                             |
+-----------------------------------------------------------------------------+
| Guarantees provided by participating entities                               |
+-----------------------------------------------------------------------------+
| Guarantees and guarantees given in favor of the participating entities      |
+-----------------------------------------------------------------------------+
| Any other credit facilities likely to be converted into effective debts     |
+-----------------------------------------------------------------------------+


*Banco de Portugal* requires all credit-granting institutions to report to the CCR their outstanding loan exposure by instrument of all irrevocable credit obligations. There is one important exception of an institution which stopped reporting revocable credit card obligations in May 2013, causing a break in the data.

-  `Overdue Credit`

All outstanding credit exposures recorded as non-performing (including overdue, written off, renegotiated credit, overdue credit in litigation, and written off credit in litigation) are aggregated to calculate overdue credits.  It includes principal, interest and related fees.

For written-off credits, participating entities also have the discrepancy to file the written-off credit in court and classify the credit as “written-off credit in litigation”. Similarly, the classification occurs from the initialization of the legal proceedings until the final decision.

+---------------------------------------------------------+------------------------------------------------+
| Abbreviation                                            | Definition                                     |
+:========================================================+:===============================================+
| *valor_vencido*                                         | Non-performing credit of a firm                |
+---------------------------------------------------------+------------------------------------------------+

**Availability**: January, 1999-August, 2018

+-------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Overdue Credit Type                                                                                                                                                                                 |
+:==========================================+:=====================================================================================================================================================================+
| Overdue Credit                            | Credit exposure that remains unpaid past the due maturity date.                                                                                                      |
+-------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Written-off Credit                        | Credit exposure that has become seriously delinquent and the creditor has given up on being paid.                                                                    |
+-------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Renegotiated Credit                       | Credit exposure that is overdue and has been renegotiated without additional collateral.                                                                             |
+-------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Overdue Credit in Litigation              | Overdue credit that is filed in court. The classification starts from the initialization of the legal proceedings and ends after the final decision.                 |
+-------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Written-Off Credit in Litigation          | Written-off credit that is filed in court. Similarly, the classification should occur since the initialization of the legal proceedings until the final decision.    |
+-------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

-  `Short-term Credit`

Short-term credit is calculated using two different definitions.

In the first place, short-term credit is defined based on the term-to-maturity as agreed in the credit contract, denoted by *valor_curto_o*. Specifically, short-term credit has an original maturity of equal to or less than one year. Before 2009, the CCR dataset did not streamline credit exposure based on the maturity structure. Therefore, for the data before 2009, the short-term credit is defined as the aggregation of commercial credit, discount funding, and other short-term funding, which are short-term funding by their nature.

In the second place, short-term credit is defined based on residual maturity – the remaining time until the expiration or the repayment of the instrument, denoted by *valor_curto_r*. Specifically, it is credit with a residual maturity of equal to or less than one year. This variable is only available from 2009.

Note that potential credit is excluded for both calculations.

+-------------------------------------------------------------------+---------------------------------------------------------------------------+
| Abbreviation                                                      | Definition                                                                |
+:==================================================================+:==========================================================================+
| *valor_curto_o*                                                   | Credit with an original maturity of less than or equal to 1 year                              |
+-------------------------------------------------------------------+---------------------------------------------------------------------------+
| *valor_curto_r*                                                   | Credit with a residual maturity of less than or equal to 1 year                               |
+-------------------------------------------------------------------+---------------------------------------------------------------------------+

**Availability**: January, 1999-August, 2018 for *valor_curto_o*; January, 2009-August, 2018 for *valor_curto_r*

-  `Long-term Credit`

Similar to short-term credit, long-term credit is defined based on original and residual maturities.

More precisely, long-term credit is credit with an original or residual maturity of more than one year, denoted by *valor_longo_o* and *valor_longo_r*, respectively.

Long-term credit defined on an original maturity basis (*valor_longo_o*) for the data before 2009 is the aggregation of total credit excluding commercial credit, discount funding, and other short-term funding.

Note that potential credit is excluded for both calculations.

+-------------------------------------------------------------------+---------------------------------------------------------------------------+
| Abbreviation                                                      | Definition                                                                |
+:==================================================================+:==========================================================================+
| *valor_longo_o*                                                   | Credit with an original maturity of more than 1 year                              |
+-------------------------------------------------------------------+---------------------------------------------------------------------------+
| *valor_longo_r*                                                   | Credit with a residual maturity of more than 1 year                               |
+-------------------------------------------------------------------+---------------------------------------------------------------------------+

**Availability**: January, 1999-August, 2018 for *valor_longo_o*; January, 2009-August, 2018 for *valor_longo_r*

-  `Weighted average debt maturity`

To provide an overall picture of a firm’s rollover risk, we compute the weighted average debt maturity. These variables are only available after 2009.

+------------------------------------------------------------------+---------------------------------------------------------------------------+
| Abbreviation                                                     | Definition                                                                |
+:=================================================================+:==========================================================================+
| *prazomedia_o*                                                   | The weighted average original debt maturity                               |
+------------------------------------------------------------------+---------------------------------------------------------------------------+
| *prazomedia_r*                                                   | The weighted average residual debt maturity                               |
+------------------------------------------------------------------+---------------------------------------------------------------------------+

**Availability**: January, 2009-August, 2018

All credit exposures reported in the CCR after 2009 are classified based on their original maturity, established in contractual terms, and residual maturity, defined as the time interval between the reference date and the maturity date of the credit agreement. In other words, the original term of the credit characterizes the exposure in relation to the maturity that was contracted for the full repayment of the credit, while the residual term of the credit characterizes the exposure in relation to the maturity between the date to which the communication refers and the date contracted for the full amortization of the credit.

These two variables are defined in ranges, including a category “Undetermined” (code 1) which is used to characterize credit exposures which, by their nature, do not have a contractually defined maturity or for which it is not possible to determine a due date. In addition, the reporting of debt maturity has undergone a major change in classification in December, 2013. For example, the maturity class “1 to 5 years” (code 5) is only valid between January, 2009 and November, 2013. From December 2013, this category is replaced by the maturity class codes 51-54. The same applies to the maturity class “5 to 10 years” (code 6 replaced by codes 61-65), and the maturity class “10 to 20 years” (code 7 replaced by codes 71 and 72).

Due to these specificities, we adopt the following procedure.

Firstly, we harmonize the debt maturity information after December, 2013 using the classification of September, 2009 as the latter is less disaggregated than the former.

Secondly, we assign the midpoint maturity for each maturity classification (0.5 years for maturity less than or equal to 1 year; 3 years for maturity more than 1 year and less than or equal to 5 years; 7.5 years for maturity more than 5 year and less than or equal to 10 years; 15 years for maturity more than 10 year and less than or equal to 20 years; 22.5 years for maturity more than 20 year and less than or equal to 25 years; 27.5 years for maturity more than 25 year and less than or equal to 30 years). We assign an average value of 40 years for credit maturing in more than 30 years.

Thirdly, we calculated the average debt maturity, weighted by the credit outstanding with the corresponding maturity.

Lastly, we reassign a maturity class to the calculated weighted average maturity value:

+---------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| Maturity Class                                    | Definition                                                                                              |
+:==================================================+:========================================================================================================+
|  1                                                | Credit with a calculated weighted average maturity of less than or equal to 1 year                                          |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|  2                                                | Credit with a calculated weighted average maturity of more than 1 year and  less than or equal to 5 years                            |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|  3                                                | Credit with a calculated weighted average maturity of more than 5 years and less than or equal to 10 year                            |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|  4                                                | Credit with a calculated weighted average maturity of more than 10 years and  less than or equal to 20 year                         |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|  5                                                | Credit with a calculated weighted average maturity of more than 20 year                                         |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------+

-  `Credit by maturity structure`

For the data after 2009, we breakdown the amount of credit using various maturity classifications, as illustrated below.

+----------------------------------------------+---------------------------------------------------------------------------+
| Abbreviation                                 | Definition                                                                |
+:=============================================+:==========================================================================+
| *valor_prazo1_o*                             | Credit with an original maturity of less than or equal to 1 year                              |
+----------------------------------------------+---------------------------------------------------------------------------+
| *valor_prazo2_o*                             | Credit with an Original maturity of more than 1 year and  less than or equal to 5 years                |
+----------------------------------------------+---------------------------------------------------------------------------+
| *valor_prazo3_o*                             | Credit with an Original maturity of more than 5 years and less than or equal to 10 year                |
+----------------------------------------------+---------------------------------------------------------------------------+
| *valor_prazo4_o*                             | Credit with an Original maturity of more than 10 years and  less than or equal to 20 year             |
+----------------------------------------------+---------------------------------------------------------------------------+
| *valor_prazo5_o*                             | Credit with an Original maturity of more than 20 year                             |
+----------------------------------------------+---------------------------------------------------------------------------+

**Availability**: January, 2009-August, 2018

+------------------------------------------------+--------------------------------------------------------------------------+
| Abbreviation                                   | Definition                                                               |
+:===============================================+:=========================================================================+
| *valor_prazo1_r*                               | Credit with a residual maturity of less than or equal to 1 year                              |
+------------------------------------------------+--------------------------------------------------------------------------+
| *valor_prazo2_r*                               | Credit with a residual maturity of more than 1 year and  less than or equal to 5 years                |
+------------------------------------------------+--------------------------------------------------------------------------+
| *valor_prazo3_r*                               | Credit with a residual maturity of more than 5 years and less than or equal to 10 year                |
+------------------------------------------------+--------------------------------------------------------------------------+
| *valor_prazo4_r*                               | Credit with a residual maturity of more than 10 years and  less than or equal to 20 year             |
+------------------------------------------------+--------------------------------------------------------------------------+
| *valor_prazo5_r*                               | Credit with a residual maturity of more than 20 year                             |
+------------------------------------------------+--------------------------------------------------------------------------+

**Availability**: January, 2009-August, 2018

-  `Secured credit by collateral type`

For the data after 2009, we calculate the amount of secured credit broken down by collateral type.

+-------------------------------------------+-----------------------------------------------------------------------------------------+
| Abbreviation                              | Collateral Type                                                                         |
+:==========================================+:========================================================================================+
| *valor_g1*                                | Credit secured by real collateral mortgaged                                             |
+-------------------------------------------+-----------------------------------------------------------------------------------------+
| *valor_g2*                                | Credit secured by real collateral not mortgaged                                         |
+-------------------------------------------+-----------------------------------------------------------------------------------------+
| *valor_g3*                                | Credit secured by financial collateral                                                  |
+-------------------------------------------+-----------------------------------------------------------------------------------------+
| *valor_g4*                                | Credit secured by personal guarantee provided by firm or individual                     |
+-------------------------------------------+-----------------------------------------------------------------------------------------+
| *valor_g5*                                | Credit secured by personal guarantee granted by the state or financial institution      |
+-------------------------------------------+-----------------------------------------------------------------------------------------+
| *valor_g6*                                | Credit secured by other guarantees                                                      |
+-------------------------------------------+-----------------------------------------------------------------------------------------+

**Availability**: January, 2009-August, 2018


<u> **Comment** </u>: To guarantee the accuracy of the credit
reports, the reporting institutions are required to verify and correct
erroneous reports as soon as possible. Although the quality of the
information reported in CCR and the coverage of credit exposures have
increased over time, CCR still has some limitations due to some
specificities. For example, credit transfer can occur between group
firms. Although this does not influence group level analysis, it can
lead to abnormal changes at the level of individual firms.

## *D.    Bank Relationship*

Data types related to bank relationships are constructed at the firm
level. To obtain an extended set of relationship variables at the
bank-firm level , one can use the "relationspell" ado provided by BPLIM.


We measure bank relationships in three dimensions: number of bank relationships, largest relationship, and the concentration of bank relationship. We consider that a firm maintains a relationship with a bank using all available credit (including unused credit).

-  `Number of bank relationships`

This variable measures the size of a firm’s bank relationships. Precisely, we calculate the number of active bank relationships, i.e., the number of banks from whom a firm is able to borrow in a specific month. It means that unused credit is also taken into account in the calculation of bank relationships.

-  `Largest bank relationship`

This variable features the borrowing from a firm´s major bank. It is measured as the percentage of a firm´s available credit from the major bank to the firm´s total available credit.

-  `Concentration of bank relationships`

The concentration of bank relationship is calculated using the Herfindahl–Hirschman Index as the sum of the squares of the bank lending share for a firm.

+------------------------------------------------+---------------------------------------------------------------------------+
| Abbreviation                                   | Definition                                                                |
+:===============================================+:==========================================================================+
| *nb_relacao*                                   | The number of active bank relationships of a firm                         |
+------------------------------------------------+---------------------------------------------------------------------------+
| *max_relacao*                                  | The largest bank relationship (in percentage term) of a firm              |
+------------------------------------------------+---------------------------------------------------------------------------+
| *hhi_relacao*                                  | The concentration of a firm's bank relationships                          |
+------------------------------------------------+---------------------------------------------------------------------------+


# Basic Descriptive Statistics



**Table 1**- Number of firms over the data period (year-end) in the COBR and the CO and COBR files.

```s/
    global path1 "Z:/data/Products/CRC/2018_04/CRC_Annual/Output/Data/Firms/"
    global path2 "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/"
    global path3 "Z:/data/Products/CRC/2019_04/CRC_Annual/Output/Data/Firms/"

    quietly use "${path3}/2018/External/CRC_A_MFRM_2018_APR19_COBR_V01.dta", clear
    quietly append using "${path1}/2017/External/CRC_A_MFRM_2017_APR18_COBR_V01.dta"
    quietly keep if (year(dofm(date))<2018 & month(dofm(date))==12) | (year(dofm(date))==2018 & month(dofm(date))==8)

    quietly forval i =1999/2016 {
      quietly append using "${path2}/`i'/External/CRC_A_MFRM_`i'_APR17_COBR_V01.dta"
    }
    quietly keep if (year(dofm(date))<2018 & month(dofm(date))==12) | (year(dofm(date))==2018 & month(dofm(date))==8)
    quietly gen Year= year(dofm(date))
    table Year, contents(freq) center

```

\

**Table 2**- Number of firms over the data period (year-end) in the EXP files

```s/

    global path1 "Z:/data/Products/CRC/2018_04/CRC_Annual/Output/Data/Firms/"
    global path2 "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/"
    global path3 "Z:/data/Products/CRC/2019_04/CRC_Annual/Output/Data/Firms/"

    quietly use "${path3}/2018/CRC_A_MFRMEXP_2018_APR19_BAL_V01.dta", clear
    quietly keep tina date
    quietly bysort tina date: gen dup=cond(_N==1,0,_n)
    quietly keep if dup==0 | dup==1
    quietly drop dup

    quietly append using "${path1}/2017/CRC_A_MFRMEXP_2017_APR18_BAL_V01.dta"
    quietly keep tina date
    quietly bysort tina date: gen dup=cond(_N==1,0,_n)
    quietly keep if dup==0 | dup==1
    quietly drop dup

    quietly keep if (year(dofm(date))<2018 & month(dofm(date))==12) | (year(dofm(date))==2018 & month(dofm(date))==8)

    quietly forval i =1999/2016 {
      quietly append using "${path2}/`i'/CRC_A_MFRMEXP_`i'_APR17_BAL_V01.dta"
      quietly keep tina date
      quietly bysort tina date: gen dup=cond(_N==1,0,_n)
      quietly keep if dup==0 | dup==1
      quietly drop dup
    }
    quietly keep if (year(dofm(date))<2018 & month(dofm(date))==12) | (year(dofm(date))==2018 & month(dofm(date))==8)
    quietly gen Year= year(dofm(date))
    table Year, contents(freq) center

```


\

<u> **Comment** </u>: the data before 2002 does not contain all the firms and is not quality controlled.


# Building Compatible Series Using Credit Exposure Data

For those who are interested in building consistent time series using
the exposure level data, there are a few caveats that are important to
keep in mind.

>## *A.    Relevant filters*

-   In order not to duplicate credits, unless the analysis of interest
    is in guarantees and joint responsibilities, aggregate series should
    only include *nivelresponsabilidade* 1 and 2.

-   The variable *si* and *si\_final* classifies firms according to
    institutional sector at the moment of the data. As some firms may
    have changed from one sector to the other, in order to implement a
    consistent sample selection (such as non-financial firms), it is
    usually recommendable to keep the most recent classification only or
    only firms that never switched sectors.

-   It is only possible to create a consistent series for credit granted
    domestically, regardless of the firm's country of origin (which is
    only identifiable after 2009). Therefore, when creating aggregate
    series, only loans with *paisbalcaoid* equal to "PRT" should be
    included.

>## *B. Compatibility issues*

Definitions of the variables in CCR changed over time. To build
compatible time series, it is important to harmonize the data.[^10]

**B.1. Credit situation**

The variable of credit situation is not available before 2009. To
construct the time series for "credit situation" before 2009, one will
need to use the following correspondence table between the variable
"type of credit" (*tipo*) and the variable "credit situation"
(*situacaocredito*).



[^10]: One can fulfill this step using an ado file available at BPLIM.


Table 3 - Correspondence table between "type of credit" (before 2009) and "credit situation" (2009 onwards)

| |  **January, 1999-December, 2008**  | |**January, 2009-present**|
|:--------|:----------------|:--------|:---------------|
|Code | Type of Credit| Code | Credit Situation|
|1    |Commercial|    1|    Regular|
|2|    Discount funding|    1    |Regular|
|3    |Other short term funding|    1|    Regular|
|4    |Medium and Long term Funding|    1    |Regular|
|5    |Other responsibilities|    1|    Regular|
|6    |Off balance sheet liabilities (potential indebtedness)|    2|    Potential|
|7    |Overdue Credit (non-performing loans)|    3    |Overdue|
|8    |Credit in litigation|    6    |Overdue in litigation|
|9    |Written-off credit    |4    |Written-off credit|
|10    |Renegotiated credit|    5    |Renegotiated credit|
|11    |Guarantees    |2    |Potential|
|12    |Guarantees or sureties    |2|    Potential|
|13    |Effective credit communicated by foreign banks|    1    |Regular|
|14    |Potential credit communicated by foreign banks    |2|    Potential|


Some reporting specificities also need to be noted in order to construct
compatible series of credit.

- Credit exposures may have different states regarding their credit situation. A special caveat needs to be noted for "potential credit" (code 2), which is credit granted but not yet used, corresponding to lines of credit, or other irrevocable commitments by the credit institution. The credit exposures of guarantors and guarantors are also characterized using this code, except in cases where they are in default.

- The classification of overdue credits has implications for other characteristics of the exposure, because (1) credit in this situation is required to identify the overdue credit class and (2) the residual maturity should always be classified as "undetermined". In the case that guarantors are required to replace the debtors in the payment of credit, the participating entity informs the credit situation and set a deadline for the payment of the claim. If payment is not made within the deadline, the institution will report a situation of in-default, i.e. the credit exposure associated with that guarantee is no longer reported in situation "potential credit" (code 2) but is now reported as "overdue credit" (code 3).

- Renegotiated credit was classified as overdue at some point in the past and, at the discretion of the reporting bank, classified as renegotiated. This renegotiation may correspond to changes in loan characteristics (in particular maturity extension and interest payment reduction), but does not imply involvement of the firm. If these loans are paid regularly, they are then reclassified as regular credit after 6-12 months (depending on the bank). To identify restructured loans, it is preferable to use the special characteristic (*caracteristicas*).

- In case of having renegotiated the terms of credit payment in
regular situation, the respective exposures continue to be reported
as \"regular credit\" (code 1) instead of "renegotiated credit"
(code 5). The same rule applies to the renegotiation of credit
payment leading to a new contract or major changes, for example,
addition of new collaterals. Another aspect to be noted regarding
the communication of credits in this situation refers to other
actors other than the debtor, for example, guarantors. When the
debtor\'s credit exposure is classified as renegotiated loans (in
credit institution), the exposure relative to the responsibilities
of the guarantor, which was classified as overdue loans, will be
re-classified as a potential credit (code 2). In the case of joint
credits, the rules for the debtors of individual loans applies to
all debtors involved.

- The criteria for classifying credit as written-off is left to the discretion of the reporting institutions, so that while some banks may report written-off credit for a few months and then remove it from the CCR, others have a policy of never removing it. The values in written-off and renegotiated credit often correspond to overdue interest payments and not overdue installments or principal reductions. There are a few institutions, such as restructuring funds, which purchase non-performing loans and then revise the report to the CCR. When they do so, a number of characteristics may change, in particular the overdue amount may seem to go up due to the addition of the accumulated overdue interest payments which are not routinely reported to the CCR.

- For the classification of "overdue credit in litigation", the following aspects must be noted:

>\-  The initiation of the action corresponds to the date on which the
    institution filed the action in court, or the date of notification
    of the institution in the case of the action being filed by third
    parties;

>\-   The closure of the proceeding is considered as the date when major
    legal sequence is offered, and can be considered as a reference to
    the date of the transition to the final juridical decision;

>\-   All overdue loans whose existence, validity or enforceability is
    subject to the jurisdiction of the courts should be considered as in
    litigation;

>\-   In the cases when a third party triggers a juridical process and the
    credit exposure is found overdue, this should be reported as overdue
    loans in litigation;

>\-   In an insolvency proceedings - a universal implementation process
    that may call the credit feasibility into question, an overdue
    exposure of a debtor in insolvency proceedings should be classified
    as overdue credit in litigation;

>\-   For an overdue credit in litigation for which there is still a part
    in good standing, this part should be reported as "1 - regular
    credit", while the overdue part should be reported as "6 - overdue
    loans in litigation".


- For written-off credits, the following aspects must be noted:


>\-   The initiation of the action corresponds to the date on which the
    institution placed the action in court, or the date of notification
    of the institution in the case of the action being filed by third
    parties;

>\-   The closure of the proceeding is considered as the date when major
    legal sequence is offered, and can be considered as a reference to
    the date of the transition to the final juridical decision;

>\-   All overdue loans whose existence, validity or enforceability is
    subject to the jurisdiction of the courts should be considered as in
    litigation

>\-   In the cases where a third party triggers a juridical process and
    the credit exposure is found written off, this should be reported as
    written-off loans in litigation;

>\-   In an insolvency proceedings - a universal implementation process
    that may call the credit feasibility into question, a written-off
    exposure of a debtor in insolvency proceedings should be classified
    as written-off credit in litigation;

>\-   The classification in question does not provide any detail as to the
    characteristics of litigation in progress.

**B.2. Debt maturity**

Concerning the characterization of the contractual and residual
maturity, some rules must be noted, in particular:

1\. The original maturity is usually equal to or greater than the
residual maturity, with only the exception of renegotiated credits (for
example, the maturity is extended);

2\. The category "Undetermined" (code 001) is only used when the original
maturity is unknown or is not contractually agreed (for example, credit
lines). An "Undetermined" original maturity also implies an
"Undetermined" residual maturity;

3\. The credits in overdue or written off situations, including those in
litigation are always assigned an "Undetermined\' residual maturity,
regardless of the original maturity.

Some financial products, by their nature, may not have a defined
maturity date contract, such as "current account (credit lines)" (code
2), "overdrafts on deposit accounts" (code 3) and credit card (code 9).
In this situation, the variables "original maturity" and "residual
maturity" shall be communicated with the code 1 (Undetermined).

**B.3. Exposure Restructuring**


It is possible that in some cases, the same credit is divided into more
than one exposure. Please see the following examples:

>\-   Considering a line of credit or credit card for which part of the
    exposure is effectively used at the end of the month. The
    information communicated to the CCR is in two exposures: one in the
    amount corresponding to the portion used, classified as "regular
    credit", and the other in the amount corresponding to the unused
    portion, classified as "potential credit", given that it corresponds
    to the institution\'s credit commitment;

>\-   Considering a fully utilized credit with a periodic amortization
    schedule, with some installments overdue and the remaining part
    regular. It is necessary to communicate to the CCR two exposures:
    one in the amount corresponding to the overdue part for accounting
    purposes, and the other corresponding to the remaining part,
    classified as "regular credit";

>\-   Considering an overdue credit in which there was some room for a
    renegotiation between the lending institution and the borrower for
    the payment terms of the overdue part. It is necessary to
    communicate to CCR two exposures: one in the amount corresponding to
    the regular part, classified as "regular credit", and the other
    corresponding to the renegotiated part, classified as "renegotiated
    credit". While the agreed payment terms are respected and the
    overdue part have not been written down, the communication of the
    outstanding exposure to the CCR follows this rule.

**B.4. Special characteristics**

Each credit exposure may be associated with more than one special
characteristics. However, by its nature, the coexistence of certain
special features are not allowed on the same exposure credit. For
instance, a credit used in a securitization operation (codes 1 to 4)
cannot be used as collateral in the issuance of mortgage covered bonds
or public sector bonds (code 6 or 7); a credit used as collateral in the
issuance of mortgage covered bonds (code 6) cannot be used
simultaneously as collateral of public sector bond (code 7); a credit
used in a securitization operation (codes 1 to 4) or as collateral of
mortgage covered bonds or as collateral of public sector bonds (code 6
or 7) cannot be delivered as collateral for Eurosystem credit operations
(code 11); an integrated credit in PERSI or Special Regime (code 15)
cannot be delivered as collateral for Eurosystem credit operations (code
11).

**B.5. Guarantor**

Credit liabilities guaranteed by surety or guarantor are identified by
collateral classification - *tipoidentificacao* as "personal guarantees"
(codes 4 to 53). However, this classification is not sufficient for
identifying the respective guarantors and sureties. The responsibilities
assumed by guarantors and sureties are also reported in separate
registers, with the identical characteristics except for the following
variables:

>\-   Level of responsibility, which has the code "4" or "5", depending on
    whether the guarantor / surety is individual or conjoint;

>\-   Credit situation, which will have the code "2" (potential credit),
    except as described in 2.3;

>\-   Value, which should correspond to the amount that the
    guarantor/surety is contractually obligated to secure and can be
    different from the original exposure.

It is important to note that a guarantee or surety is never communicated
without the associated credit exposure being also reported. When there
is more than one entity to provide guarantees or sureties to the same
credit, the exposures of credit liabilities associated with all
guarantors and sureties are communicated to the CCR. In cases when a
borrower fails to meet its payment obligations and there is a guarantor
(surety or guarantor) associated with that contract, the credit
institution will notify the guarantor of the situation and set a
deadline for it to proceed to payments due by the debtor. This may
result in the following situations:

>> \(1\) The guarantor fully liquidates the loan </u>, thereby
    stopping any report to the CCR regarding the loan in question (on
    behalf of the borrower, and on behalf of guarantor/surety);

>> \(2\)The guarantor fully liquidates the overdue part of the
    loan </u>. In this situation, CCR only ceases to report the
    exposure in default. The outstanding exposure continues to be
    reported on behalf of the borrower as "regular credit" and the
    exposure associated with the guarantor/surety will be reported as
    "potential credit"; iii.

>> \(3\)The guarantor pays the loan installments regularly, instead of the
    debtor </u>. In this situation, reporting on the
    guarantor/surety remains regarding the characterization of credit
    liabilities, that is, the *level of responsibility* equal to "4"/"5"
    but the *credit* *situation* will be equal to "1". However, if the
    underlying "financial product" requires the communication of
    "monthly installment", this credit exposure should continue to be
    reported on behalf of the debtor and on behalf of the guarantor.
    This situation must ensure that the guarantor/surety respects the
    established amortization plan. So the report for the debtor will be:
    "*Responsibility Level*" = 1 (if it is an individual credit) and
    "Credit Situation" = 1 (if it is an regular credit). [^11]

If the guarantor/surety fails to fulfill its obligations after
notification by the credit institution and after a reasonable period for
the regularization of non-compliance, the report concerning the
guarantor would be: "Responsibility level" = 4 or 5 and "Credit
Situation" = 3 (overdue loans). Regarding the borrower, the report will
continue to be: "Responsibility level" = 1 (if it is an individual
credit) and "Credit Situation" = 3 (overdue loans). Note that the
existence of such periods for the guarantor before passing to report the
situation of overdue credit is ensured by the participating
institutions.

The situation exemplified above has two variants: the case when the
credit was written off and the case when there is renegotiation of
credit after default. Regarding the variable "credit situation", the
credit claims with personal guarantees or guarantees can be schematized
as follows, considering the two types of actors (debtor and guarantor
/surety):



[^11]: This classification of credit situation is based on the principle that overdue credit should not be reported to the CCR if not, for accounting purposes, classified as such. Although in this situation the borrower is not fulfilling its obligations, someone is fulfilling for him due to contractual conditions of the loan. As a result, the credit is not classified as overdue.


Table 4 - Credit claims with personal guarantees or guarantees

|**Credit situation**|**Credit situation**| **Observations**|
|:--------------------------------|:-----------|:-----------|
|**Exposure in debtor’s name** |**Exposure in guarantor’s name** ||
|1 - Regular Credit| 2 - Potential Credit| There is no default. |
|1 - Regular Credit| 2 - Potential Credit | There has been default of the debtor, and the guarantor paid the benefits due. The debtor assumed the payment of future installments, with no renegotiation of credit. |
|1 - Regular Credit|1 - Regular Credit|There has been default of the debtor, and the guarantor paid the overdue installments and also assumed the payment of future installments, with no renegotiation of credit. |
|3 - Overdue Credit|2 - Potential Credit |Default of the debtor but the guarantor has not been notified of the breach or the guarantor has been notified of the breach and its obligation to settle but the deadline for the settlement is not exhausted. |
|3 - Overdue Credit|3 - Overdue Credit|The guarantor has been notified of the default and did not pay any debt portion within the set deadline. |
|4 – Written-off credit |4 – Written-off credit |Identical to the previous case but the debt has already been written off. |
|5 – Renegotiated credit |2 - Potential Credit |Renegotiated debt, after the default of the debtor, and the agreed terms are being met. |


It is important to note that regarding the reporting of responsibilities
of guarantors and sureties, the variable "responsibility level" will
always be coded as "4" (surety or guarantor - individual) or "5"
(guarantor or guarantor - joint), regardless whether the guarantor has
to ensure the total or partial repayment of the secured loan.


**B.6. Collateral**

Each credit exposure may be associated with more than one type of
collateral and the value of the collateral corresponds to the value of
each type of collateral associated with the credit exposure. The
valuation of collateral depends on the type of collateral.

Regarding the real collateral, financial collateral, or other collateral
(codes 1- 39 and 6), the value of the collateral corresponds to the fair
value of the underlying asset (registered accounting value) and can
therefore be distinguished from credit amount. In the case of a mortgage
real collateral, its value will be limited by the mortgage amount and
may be less than the outstanding credit amount.

In the case of personal guarantees (codes 4 - 53), since these
correspond to a commitment to pay debt by third parties in the event of
default by the debtors, the collateral value should be updated as a
function of the outstanding value of the credit. The collateral can be
higher than the value of the outstanding credit if the guarantee is also
associated with the overdue interest and related expenses or with
potential credit.

In the case of financial leasing, the value of the associated collateral
(non-mortgage real collateral) is assessed by the financial institution.

> *Special cases* </u>

>\-   When the same asset is used as a collateral to more than one loan

>In the case where the same asset or good is used as collateral for more than one loan which has different characteristics, i.e., they are reported to the CCR in more than one exposure of responsibilities, the guarantee amount shall be distributed proportionally by the different exposures, according to the outstanding amounts of each one.

>\-   When a loan is guaranteed by more than one asset

>In the case where a loan is secured by more than one asset (e.g., debt securities, stocks, deposits, \...), communication of this exposure to the CCR shall include the characterization of different types of collaterals and the corresponding values, using the valuation rules mentioned above. In this situation, the sum of the collateral values attached to the loan may be different (lower or higher) from the credit value.

>\-   When a guaranteed loan has an overdue part and a due part

>For collateralized loans for which one part is overdue and the other part due, two separate exposures are communicated to the CCR. If possible, the collateral value is also distributed by the two components in order to fully cover the value of the overdue part, and the remaining affecting the due part.

**B.7. Additional concerns**

Also, as CCR only obliges the reporting of the full position of each debtor, it is sometimes difficult to unambiguously identify each
individual credit exposure for the same debtor. This restriction has
repercussions in the process of modifying or correcting the reported
credit exposures. For example, one may observe a split in credit
exposure from a month to another, which can happen when a bank
restructure the loan, e.g., one part of the loan becomes overdue.

<u> **Comment** </u>: The inclusion of some variable categories
does not always corresponds to the effective dates as defined in
legislations. For instance, for the variable "type", the classification
"10" comprises overdue credit that has been renegotiated, which was
requested to report from July, 2001. Yet, the series appeared already in
January, 2001, although it was only with one exposure. Loans that were
extended as collateral for credit operations in Euro system and loans
featured with IEB identification code were started to be reported in
September, 2010 and in April, 2011, respectively. But it was only until
November, 2012 that these two credit exposures were systematically
reported.



# Legislation

Variable definitions changed over time. Some variables, for instance, credit situation (*situacaocredito*), maturity (*prazooriginal* and *prazoresidual*), and collateral type (*tipogarantia*) have undergone major changes in classification, as framed by *Banco de Portugal*’s instructions. It is important to note that even small changes may require a infrastructural update on the part of the participating financial entities, possibly leading to a gradual implementation of the instruction even though legally all the entities should implement the instructions at the same time.
Below is a list of relevant legislations:


-    [**Decree-Law no. 47909/1967**](./aux_files/legislation/Decreto-Lei_47909.pdf), September 7 and [**Decree-Law no. 48731/1968**](./aux_files/legislation/Decreto-Lei_48731.pdf), December 4 - established the service of centralizing and disseminating credit risk information and defines its purpose and operation, given the need of credit and other financial institutions to properly assess the risks of their operations.

-    [**Carta Circular no 29/96/DOC**](./aux_files/legislation/Carta-Circular_29-96-DOC.pdf), September 18 – eliminated credit classes associated with *empréstimos de poupança-crédito*, which are now classified as *empréstimos de poupança-emigrante* (the conversion of savings-credit loans into savings-immigrant loans).

-    [**Decree-Law no. 5/1998**](./aux_files/legislation/Lei_5-1998.pdf), January 31 – amended the Organic Law of *Banco de Portugal*, with a view to its integration into the European System of Central Banks.

-    [**Decree-Law no. 67/1998**](./aux_files/legislation/Lei_67-1998.pdf), October 27 – transposed the Directive 95/46/CE of the European Parliament and the Directive of the Council in 24-10-1995 on the protection of individuals in processing and circulating data.

-    [**Instrução no. 16/2001**](./aux_files/legislation/Instrucao_16-2001_full.pdf) – reviewed the separation of potential from actual amounts of credit.

-    [**Instrução no. 11/2002**](./aux_files/legislation/Instrucao_11-2002.pdf) – establishment of a 90 day period to register a credit exposure (*sem direito de regresso*) or overdue credit (*com direito de regresso*) after invoices are due; revocable commitments (code 921) are  no longer reported as a credit of type 6 (off balance sheet commitments); factoring credit more than 90 days overdue reported as type 7 (non-performing credit) or 8 (credit in litigation). Participating entities are encouraged to provide relevant information for credit risk assessment. In addition, renegotiated credits are requested to be reported since July, 2001.

-    [**Instrução no. 15/2002**](./aux_files/legislation/Instrucao_15-2002.pdf) – made procedural changes to access and occasional communication requested by the Banco de Portugal (no analysis impact).

-    [**Decree-Law no. 53/2004**](./aux_files/legislation/Lei_53-2004.pdf), March 18 – integrated the information on court decisions regarding insolvency proceedings of collective or individual people, provided by the Ministry of Justice, following the approval of the CIRE - Insolvency Code.

-    [**Instrução no. 7/2006**](./aux_files/legislation/Instrucao_7-2006_full.pdf) – created new types of credit for the variable type (codes 11-14) which include guarantees, sureties, and credit communicated by foreign central banks.

-    [**Instrução no. 21/2008**](./aux_files/legislation/Instrucao_21-2008_full.pdf) – changed the CCR to its current format (as in *Caderno* da CCR) and defined the scope, reporting deadline, and stress the important of reporting the types of information. Some codes were significantly changed.

-    [**Instrução no. 7/2009**](./aux_files/legislation/Instrucao_7-2009.pdf) – included credit reports from the State to protect unemployed individuals’ real estate ownership and created a special classification for these credits. This revised version contains more loan-level variables. Another important consequence of the revision was the incorporation of loans to Portuguese firms granted by foreign branches of Portuguese banks.

-    [**Instrução no. 18/2010**](./aux_files/legislation/Instrucao_18-2010.pdf) – imposed mandatory reporting of credit less than 90 days overdue (*crédito sem recurso*) if used in guarantee pools in Eurosystem operations; excluded shareholder’s advances (*suprimentos*) from financial institutions; imposed mandatory reporting of securitized debt issued for a certain debtor (even if the financial institution does not have ownership) and exclusion of securitized debt in the exposure sheet of the institution.

-    [**Instrução no. 17/2013**](./aux_files/legislation/Instrucao_17-2013.pdf) – separated overdue and written-off credit in litigation – codes 6 and 7; added new maturity categories and new collateral classifications

- [**Memorandum of Understanding on the exchange of information among national central credit registers**](./aux_files/legislation/Memorandum.pdf) - included credit exposures obtained from financial institutions located in the other EU
    countries (greater than or equal to 25000 euros). In 2003, the Banco de Portugal signed the "Memorandum of Understanding on the exchange of information among national central credit registers for the purpose of passing it on to the reporting Institutions"- MoU for the purpose of exchanging information between Central Credit Registers managed by National central banks of other member states of the European Union. Following the availability of this agreement, since 2005, credit exposures of collective residents in Portugal obtained from financial institutions located in the subscribed countries are included. Currently, in addition to Portugal, the countries subscribed include Germany, Austria, Belgium, Spain, France, Italy, Czech Republic and Romania. As the disclosure *timing* of other countries' CCRs in general does not coincide with the dissemination of information by the Portuguese CCR, it is normal to have a non-lower than one-month reporting lag between the reference date of the internal credit information and the reference date of the external credit included in the same regular dissemination file.


# Citation of This Dataset
Banco de Portugal Microdata Research Laboratory (BPLIM) (2019): Central Credit Responsibility Database - Firm Level Data. Extraction: June 2019. Version: V1. BANCO DE PORTUGAL. Dataset. https://doi.org/10.17900/CRC.FRM.Jun2019.V1

Banco de Portugal Microdata Research Laboratory (BPLIM) (2019): Central Credit Responsibility Database - Bank-Firm Level Data. Extraction: June 2019. Version: V1. BANCO DE PORTUGAL. Dataset. https://doi.org/10.17900/CRC.FRMBNK.Jun2019.V1

Banco de Portugal Microdata Research Laboratory (BPLIM) (2019): Central Credit Responsibility Database - Exposure Level Data. Extraction: June 2019. Version: V1. BANCO DE PORTUGAL. Dataset. https://doi.org/10.17900/CRC.EXP.Jun2019.V1


# Auxiliary Files

For a description of each variable in each dataset (name, unit of
measurement, data and storage type, format, year of first and last
observation), an account of the changes occurred over time, summary
statistics for each dataset and a codebook for each dataset please check
the following auxiliary files:

**Table 5-** Auxiliary Files

For a description of each variable in the CO and COBR files (name, unit of measurement, data and storage type, format, year of first and last observation), an account of the changes occurred over time, summary statistics for each dataset and a codebook for each dataset, please check the following auxiliary files:


| Data File | Description of Variables | Summary Statistics | Codebook | Dataset description |
| :---- | :----: | :----: | :----: |  :----: |
| Credit Exposure File (EXP): General|    [var_ccr_bal](./aux_files/variables_description/var_crc.html) | [stat_ccr_bal](./aux_files/descriptive_statistics/stat_crc_bal.html) |     [cdbk_ccr_bal](./aux_files/codebook/cdbk_crc_bal.html) | [dscr_ccr_bal](./aux_files/describe_dataset/dscr_crc_bal.html) |
| Credit Exposure File (EXP): Collateral|    [var_ccr_coll](./aux_files/variables_description/var_crc.html) | [stat_ccr_coll](./aux_files/descriptive_statistics/stat_crc_coll.html) |     [cdbk_ccr_coll](./aux_files/codebook/cdbk_crc_coll.html) | [dscr_ccr_coll](./aux_files/describe_dataset/dscr_crc_coll.html) |
| Credit Exposure File (EXP): Special Characteristics|    [var_ccr_schar](./aux_files/variables_description/var_crc.html) | NA |     [cdbk_ccr_schar](./aux_files/codebook/cdbk_crc_schar.html) | [dscr_ccr_schar](./aux_files/describe_dataset/dscr_crc_schar.html) |
| Firm Level Credit Outstanding & Bank Relationship file (COBR)|    [var_ccr_cobr](./aux_files/variables_description/var_crc.html) | [stat_ccr_cobr](./aux_files/descriptive_statistics/stat_crc_cobr.html) |     [cdbk_ccr_cobr](./aux_files/codebook/cdbk_crc_cobr.html) | [dscr_ccr_cobr](./aux_files/describe_dataset/dscr_crc_cobr.html) |
| Bank-Firm Level Credit Outstanding File (CO)|    [var_ccr_co](./aux_files/variables_description/var_crc.html) | [stat_ccr_co](./aux_files/descriptive_statistics/stat_crc_co.html) |     [cdbk_ccr_co](./aux_files/codebook/cdbk_crc_co.html) | [dscr_ccr_co](./aux_files/describe_dataset/dscr_crc_co.html) |

The Summary Statistics, Codebook and Dataset Description files are available on BPLIM's servers.


# Useful Links

[CCR home page](https://www.bportugal.pt/area-cidadao/formulario/227)

[Statistical Bulletin](https://www.bportugal.pt/en/publicacao/statistical-bulletin)


# Useful Ado Files

We provide a handful of ado files written by BPLIM staff for researchers
to implement certain calculations and variable arrangements.

> ## A. Harmonization of Variables Over Time

`Description`

The CCR has undergone some major revisions. `harmonize ` is a Stata user-written command to help harmonize variables and make them compatible over time.

`Syntax`

```
harmonize variable

```

where `variable` is a variable to be harmonized. The harmonized variable generated by this ado is denoted as "_variable_h"


> ## B. Aggregation

`Description`

`aggregate ` is a Stata user-written command to help compute aggregates of credit and bank relationship at different frequencies (yearly and quarterly) using various methods (period-end or period average). By default, the ado should only be applied to the original CCR datasets prepared by BPLIM.


`Syntax`

```
aggregate panelvar timevar, [options]

```

where `panelvar` is a unit identifier for the panel and `timevar` identifies the time variable.


`General Options`

*YEAR*: aggregation by year.

*QUARTER*: aggregation by quarter.

*AVG*: period average.

*END*: period end.

*NOCHECK*: ignore the difference between the current dataset and the original dataset prepared by BPLIM.


> ## C. Construction of Firm Default Profile

`Description`

`default ` is a Stata user-written command to help calculate default events using information from the CCR datasets.


`Syntax`

```
default panelvar timevar overduevar benchmarkvar, [options]

```
where `panelvar` is a unit identifier for the panel, `timevar` identifies the time variable, `overduevar` identifies the variable of total overdue credit and `benchmarkvar` identifies the benchmark variable with which one can calculate the overdue intensity.


`General Options`

*THRESHOLD*: a pre-determined threshold of overdue credit ratio, 0.025 by default.

*RUNS*: a sequence/run of consecutive threshold hits for the same individual, 3 by default.

*IGNOREGAP*: allow gaps in the data when counting runs.


`Generated Variables`

Firm default variables are constructed based on the default definition of Antunes, Gonçalves and Prego (2016). By default, we flag out firm-month observations when more than 2.5% percent of total credit is reported overdue and define default event if a firm is flagged up for at least three consecutive months. For example, if a firm has overdue credit that amounts to more than 2.5% of its total credit in January and February, 2015 but later paid off the overdue credit in March, 2015, the firm will not be considered as in default in January and February, 2015. Researchers can also choose to apply an alternative threshold for the overdue credit ratio or/and an alternative duration of overdue status.

The variables generated include:

-    Overdue credit flag (*\_flag*). This is an indicator for the existence of overdue credit. It takes the follow values:

+-------------------------------------------------------------------------------+
|  0 - no credit is past due at the time                                       |
+-------------------------------------------------------------------------------+
|  1 - overdue credit is present but below the threshold                       |
+-------------------------------------------------------------------------------+
|  2 - overdue credit is above the threshold                                   |
+-------------------------------------------------------------------------------+

- Default event (*\_default*). The default event occurs when a firm has credit overdue above the threshold for a run of defined consecutive months (three months by default).

- First default event (*\_fdefault*).The first default event occurs (flagged out with the value of 1) when a firm has credit overdue above the threshold for a run of defined consecutive months for the first time.



> ## D.  Construction of Bank-Firm Relationship Spells

`Description`

`relationspell ` is a Stata user-written command to help construct bank-firm relationship variables which reflect the start,
discontinuity, and continuity of relationship between a firm and a bank.


`Syntax`

```
relationspell panelvar1 panelvar2 timevar, [options]

```

where `panelvar1` and `panelvar2` are identifiers for a firm and its bank, `timevar` identifies the time variable,



`General Options`

*STARTYR*:  start year.

*FINYEAR*:  end year.

*FREQUENCY*:  data frequency with the options of daily, monthly and annual (1, 2, and 3, respectively). The default option is monthly.

*GAPS*:  max gaps allowed in a relationship, 0 by default.


`Generated Variables`

The variables generated include:

-   Relationship ID (\_*relation*)

Relationship identification number.

-   Validity of a relationship (\_*relation\_valid*)

The status of a relationship spell. 0 denotes that the relationship is
discontinued for the given period and 1 denotes that the relationship is
active.

-   Relation spell (\_*spell*)

Relationship spell is an ordered variable for the relationship sequence
between a firm and a bank.

-   Start of a relationship spell (\_*mindate\_spell*)

The start of a relationship spell

-   End of a relationship spell (\_*maxdate\_spell*)

The end of a relationship spell

-   Length of a relationship spell (\*len\_spell*)

The length of a relationship spell

-   Start of relationship (\_*mindate*)

The start of a bank-firm relationship

-   End of relationship (\_*maxdate*)

The end of a bank-firm relationship

-   Length of relationship (\_*len\_all*)

The length of a bank-firm relationship

-   Length of active relationship (\_*len\_act*)

The length of active relationship

-   Length of inactive relationship (\_*len\_inact*)

The length of inactive relationship



# Frequently Asked Questions
The most frequently asked questions can be found [here](https://www.bportugal.pt/perguntas-frequentes/276).
If you have a question that is not covered in this manual, please send an email to bplim@bportugal.pt.


# References

Banco de Portugal (1987). Central de Responsabilidades de Crédito. Cadernos do Banco de Portugal. Lisboa.

Banco de Portugal (1993). Central de Responsabilidades de Crédito. Cadernos do Banco de Portugal. Lisboa.

Banco de Portugal (2003). Central de Responsabilidades de Crédito. Cadernos do Banco de Portugal. Lisboa.

Banco de Portugal (2010). Central de Responsabilidades de Crédito. Cadernos do Banco de Portugal. Lisboa.

Banco de Portugal (2011). Central de Responsabilidades de Crédito. Cadernos do Banco de Portugal. Lisboa.

Banco de Portugal (2014). Central de Responsabilidades de Crédito. [**Manual de Procedimentos Instrução no. 21/2008**](./iles/legislation/ManualdeprocedimentosdaCRC.pdf). Lisboa.

Banco de Portugal (2015). Central de Responsabilidades de Crédito. Cadernos do Banco de Portugal. Lisboa.

João Cadete de Matos (2015). The Portuguese Central Credit Register: a powerful multipurpose tool, relevant for many central bank functions. IFC workshop on “Combining micro and macro statistical data for financial stability analysis”. Bank for International Settlements.

Antunes, António, Homero Gonçalves, and Pedro Prego (2016). Firm Default Probabilities Revisited. Banco de Portugal Economic Studies, 2, 21-45.


# Appendix

**Appendix 1**-Typical credit exposure reported in CCR

|**Anonymized Tax Identifier Number**|**Bank ID**|**Reporting month**| **Exposure ID**| **Responsibility Level**| **Product**| **Credit Situation**| **Overdue Class**| **Original Maturity**|    **Residual Maturity**|    **Amount**|    **Currency**|
|:------|:-------|:-------|:-------|:------|:-------|:-------|:-------|:------|:-------|:-------|:-------|
| *tina*| *bina*|    *date*|    *cina*| *nivelresponsabilidade*|    *produto*|    *situacaocredito*|    *classecreditovencido*|    *prazooriginal*|    *prazoresidual*    |*valor*|    *moeda*|
|5××××××××|1×××|Jan 2014|1×××××××××|1|    2|    1||1|    1|    3589806|    EUR|
|5××××××××|1×××|Jan 2014|1×××××××××|1|    2|2||1| 1|10194|    EUR|
|5××××××××|1×××|Jan 2014|1×××××××××|1| 8| 1||6|    5|    1500000|    EUR|
|5××××××××|    1×××|    Jan 2014|    1×××××××××|    1|    9|    2||1|    1|    103970|    EUR|
|5××××××××|    1×××|    Jan 2014|    1×××××××××    |1|    9|    1||1|    1|    2508|    EUR|
|5××××××××    |2×××    |Jan 2014    |1×××××××××    |2    |1    |1||4    |3    |96000    |EUR|
|5××××××××|    2×××|    Jan 2014|    1×××××××××|    1|    8|    1||5    |5    |224985    |EUR|
|5××××××××|    3×××|    Jan 2014|    1×××××××××|    1|    3|    3    |2|    1    |1|    1550000|    EUR|
|5××××××××|    3×××|    Jan 2014|    1×××××××××|    1    |15|    2||6|    5    |567743|    EUR|
|5××××××××|    4×××|    Jan 2014|    1×××××××××|    1    |2|    1||1|    1    |2428572|    EUR|
|5××××××××|    4×××|    Jan 2014|    1×××××××××|    1    |3|    1||1|    1    |1071|    EUR|
|5××××××××|    4×××|    Jan 2014|    1×××××××××|    1    |15|    2||6    |5|    398392    |EUR|
|5××××××××|    4×××    |Jan 2014|    1×××××××××|    1|    15|    2||6|    5    |3500|    EUR|

**Appendix 2**-monthly credit outstanding at firm level (before 2009)

| **Anonymized Tax Identifier Number**|**Reporting month**| **Total available credit**| **Effective credit**| **Potential Credit**| **Overdue credit**| **Short-term  credit**| **Long-term credit**| **# Bank relationships**|    **Concentration of bank relationships**| **Largest bank relationships**|
|:------|:-------|:-------|:-------|:------|:-------|:-------|:-------|:------|:-------|:-------|
| *tina*| *date*| *valor_global*    | *valor_efectivo*|    *valor_potencial*| *valor_vencido*| *valor_curto_o*    | *valor_longo_o*    |*nb_relacao*    | *hhi_relacao*| *max_relacao*|
|5××××××××|    Jan 2007    |3249930    |438770    |2811160    |0    |290740|    148030|    6    |0.38    |0.56|
|5××××××××|    Feb 2007|    3228210    |417140    |2811070    |0    |218570    |198570|    6|    0.38|    0.56|
|5××××××××|    Mar 2007|    3509090    |362440    |3146650    |0    |179070    |183370    |6|    0.41|    0.60|
|5××××××××|    Apr 2007|    3436860    |290640|    3146220|    0    |112010    |178630    |6|    0.42|    0.61|
|5××××××××|    May 2007|    3388810    |248950    |3139860|    0    |72260    |176690|    6    |0.43|    0.62|
|5××××××××|    Jun 2007|    3485310|    638800|    2846510    |0    |475960    |162840    |6    |0.42|    0.60|
|5××××××××|    Jul 2007|    3731840    |223730    |3508110|    0    |65680    |158050    |6    |0.39    |0.56|
|5××××××××|    Aug 2007|    3724530    |208810    |3515720    |0|    52710|    156100|    6    |0.39    |0.57|

**Appendix 2** *continued* – monthly credit outstanding at firm level (after 2009)

| **Anonymized Tax Identifier Number**|**Reporting month**| **Total available credit**| **......**| **Weighted average original maturity**| **Weighted average residual maturity**| **Credit with an original/residual maturity of less than or equal to 1 year**| **Credit with a original/residual maturity of (1, 5] years**| **Credit with a original/residual maturity of (5, 10] years**|    **Credit with a original/residual maturity of (10, 20] years**| **Credit with a original/residual maturity of more than 20 years**|
|:------|:-------|:-------|:-------|:------|:-------|:-------|:-------|:------|:-------|:-------|
| *tina*| *date*| *valor_global*    | *......*|    *prazomedia_o*| *prazomedia_r*| *valor_prazo1_o*    | *valor_prazo2_o*    |*valor_prazo3_o*    | *valor_prazo4_o*| *valor_prazo5_o*|
|||||||*valor_prazo1_r*|    *valor_prazo2_r*|    *valor_prazo3_r*|    *valor_prazo4_r*|    *valor_prazo5_r*|
|5××××××××|    Jan 2014|    129849    ||    4    |4|    2621|    23702|    29209|    0|    74317|
|5××××××××|    Feb 2014|    129963    ||    4    |4|    2621|    23702    |29259|    0    |74381|
|5××××××××|    Mar 2014|    130077|    |    4|    4    |2621    |23702|    29308    |0|    74446|
|5××××××××|    Apr 2014|    130188|    |    4    |4|    2621|    23702|    29356|    0|    74509|
|5××××××××|    May 2014|    130298|    |    4|    3|    2621|    23702    |29402|    0|    74573|
|5××××××××|    Jun 2014|    130402|    |    4    |3    |2621|    23702|    29446    |0|    74633|
|5××××××××|    Jul 2014|    130507|    |    4    |3    |2621    |23702    |29490|    0|    74694|
|5××××××××|    Aug 2014|    125990|    |    4    |3    |2621    |19083    |29532|    0|    74754|

**Appendix 2** *continued* – yearly credit outstanding at firm level (before 2009)

| **Anonymized Tax Identifier Number**|**Reporting year**| **Total available credit (year end) **| **Effective Credit (year end)**| **Potential Credit (year end)**| **Overdue Credit (year end)**| **Short-term Credit (year end)**| **Long-term Credit (year end) **| **# Bank relationships (year end)**|    **Concentration of bank relationships (year end)**| **Largest bank relationships (year end)**|
|:------|:-------|:-------|:-------|:------|:-------|:-------|:-------|:------|:-------|:-------|
| *tina*|    *year*|    *valor_global*|    *valor_efectivo*|    *valor_potencia*| *valor_vencido*|    *valor_curto_o*|    *valor_longo_o*|    *nb_relacao*|    *hhi_relacao*|    *max_relacao*|
|5×××××××1|    2006|    25144    |24000|    1144|    0    |24000|    0    |1|    1|    1|
|5×××××××2|    2006|    16076304    |10530647    |5545657|    0    |7800167    |2730480    |6|    0.31|    0.46|
|5×××××××3|    2006|    279840|    269934|    9906|    0|    240400|    29534|    4|    0.28|    0.30|
|5×××××××4|    2006|    31036|    28790|    2246|    3426|    24232|    4558|    1    |1|    1|


**Appendix 2** *continued* – yearly credit outstanding at firm level (after 2009)

| **Anonymized Tax Identifier Number**|    **Reporting year**|    **Total available Credit (year end)**|    **......**|    **Weighted average original maturity (year end)**|    **Weighted average residual maturity (year end)**|    **Credit with a maturity of less than or equal to 1 year (year end)**|    **Credit with a maturity of (1, 5] years (year end)**|    **Credit with a maturity of (5, 10] years (year end)**|    **Credit with a maturity of (10, 20] years (year end)**|    **Credit with a maturity of more than 20 years (year end)**|
|:------|:-------|:-------|:-------|:----|:-------|:-------|:-------|:------|:-------|:-------|
| *tina*| *year*| *valor_global*    | *......*|    *prazomedia_o*| *prazomedia_r*| *valor_prazo1_o*    | *valor_prazo2_o*    |*valor_prazo3_o*    | *valor_prazo4_o*| *valor_prazo5_o*|
|||||||*valor_prazo1_r*|    *valor_prazo2_r*|    *valor_prazo3_r*|    *valor_prazo4_r*|    *valor_prazo5_r*|
|5×××××××1|    2013|    56452    |......    |1|    1|    50341    |3611    |0|    0|    0|
|5×××××××2|    2013|    37080    |......    |4|    3    |0    |10177    |9144    |0|    17759|
|5×××××××3|    2013|    1300    |......    |1|    1    |942    |0|    0    |0    |0|
|5×××××××4|    2013|    60968    |......    |4|    4    |155    |0    |11250|    0    |46313|

**Appendix 3** - month credit outstanding at bank-firm level (before 2009)

| **Anonymized Tax Identifier Number**|    **Bank ID**|    **Reporting month**|    **Total available credit**|    **Effective credit**|    **Potential Credit**|**Overdue credit**|    **Short-term credit**|    **Long-term credit**| **Share of a bank relationship** |    **Indicator for the largest bank relationship**|
|:------|:-------|:-------|:-------|:----|:-------|:-------|:-------|:------|:-------|:------|
| *tina*    | *bina*|    *date*|    *valor_global*|    *valor_efectivo*|    *valor_potencial*    |*valor_vencido*|    *valor_curto_o*    | *valor_longo_o*|    *share*|    *max_relacao*|
|5××××××××|    1×××|    Mar 2007|    850    |850|    0|    0    |850|    0    |0.53|    1|
|5××××××××|    1×××|    May 2007|    850    |850|    0    |0|    850|    0|    0.53|    1|
|5××××××××|    1×××|    Jul 2007|    850    |850|    0    |0|    850    |0|    0.53|    1|
|5××××××××|    2×××|    Jan 2007|    740    |0    |740|    0|    0    |0|    1|    1|
|5××××××××|    2×××|    Feb 2007|    740    |0    |740|    0    |0    |0    |1|    1|
|5××××××××|    2×××|    Mar 2007|    740    |0    |740|    0    |0|    0|    0.47|    0|
|5××××××××|    2×××|    Apr 2007|    740    |0    |740|    0    |0    |0|    1|    1|
|5××××××××|    2×××|    May 2007|    740    |0    |740|    0    |0|    0|    0.47|    0|
|5××××××××|    2×××|    Jun 2007|    740    |0    |740|    0    |0    |0    |1|    1|
|5××××××××|    2×××|    Jul 2007|    740    |0    |740|    0|    0    |0|    0.47|    0|
|5××××××××|    2×××|    Aug 2007|    740    |0    |740|    0    |0    |0    |1|    1|
|5××××××××|    2×××|    Sep 2007|    740    |0    |740|    0    |0    |0    |1    |1|
|5××××××××|    2×××|    Oct 2007|    748    |0    |748|    0    |0|    0|    1|    1|
|5××××××××|    2×××|    Nov 2007|    748    |0    |748|    0    |0    |0    |1    |1|
|5××××××××|    2×××|    Dec 2007|    748    |0    |748|    0|    0    |0|    1|    1|

**Appendix 3** *continued* – month credit outstanding at bank-firm level (after 2009)

| **Anonymized Tax Identifier Number**|    **Bank ID**| **Reporting month**| **Total available credit**|    **......**|    **Weighted average original maturity**|    **Weighted average residual maturity**| **Short-term credit**|    **Long-term credit**|    **Credit with a maturity of less than or equal to 1 year**| **Credit with a maturity of (1, 5] years**| **Credit with a maturity of (5, 10] years**| **Credit with a maturity of (10, 20] years**| **Credit with a maturity of more than 20 years**|
|:------|:-------|:-------|:-------|:----|:-------|:-------|:-------|:------|:-------|:-------|:------|:-------|:-------|
| *tina*| *bina*| *date*|    *valor_global*| *......*| *prazomedia_o*| *prazomedia_r*| *valor_curto_o*| *valor_longo_o*| *valor_prazo1_o*| *valor_prazo2_o*| *valor_prazo3_o*| *valor_prazo4_o*| *valor_prazo5_o*|
||||||||*valor_curto_r*|    *valor_longo_r*|    *valor_prazo1_r*|    *valor_prazo2_r*|    *valor_prazo3_r*|    *valor_prazo4_r*|    *valor_prazo5_r*|
|5××××××××|    1×××|    Mar 2010|    1096||        2    |1|    0|    346    |0    |346    |0|    0|    0|
|5××××××××|    1×××|    Apr 2010|    1064||        2|    1|    0    |314|    0|    314|    0    |0|    0|
|5××××××××|    2×××|    Jan 2010|    27526||    2    |2|    16683    |10843|    16683    |739|    10104|    0|    0|
|5××××××××|    2×××|    Feb 2010|    25950||        2    |2|    15199    |10751    |15199|    693|    10058|    0    |0|
|5××××××××|    2×××|    Mar 2010|    25792||    2    |2|    15133    |10659|    15133|    648    |10011    |0|    0|
|5××××××××|    2×××|    Apr 2010|    24869||        2    |2|    14304    |10565|    14304|    602|    9963|    0|    0|
|5××××××××|    2×××|    May 2010|    25896||        2    |2|    15425    |10471|    15425    |556|    9915|    0    |0|
|5××××××××|    2×××|    Jun 2010|    24198||        2    |2    |13822|    10376|    13822|    510    |9866|    0    |0|
|5××××××××|    2×××|    Jul 2010|    24042||        2    |2    |13760|    10282|    13760    |465|    9817|    0    |0|
|5××××××××|    2×××|    Aug 2010|    25947||        2    |2    |15760|    10187|    15760|    419|    9768|    0    |0|
|5××××××××|    2×××|    Sep 2010|    26025||        2    |2    |15935|    10090|    15935    |372|    9718|    0    |0|
|5××××××××|    2×××|    Oct 2010|    26223||        2|    2    |16230|    9993|    16230|    326|    9667|    0|    0|
|5××××××××|    2×××|    Nov 2010|    26320||    2|    2    |16424    |9896|    16424    |280    |9616    |0    |0|
|5××××××××|    2×××|    Dec 2010|    25801||        2    |2|    16003|    9798|    16003    |234    |9564|    0    |0|

**Appendix 4** -- The construction of weighted average debt maturity

Original and residual maturity in CCR are defined in ranges, including a
category "Undetermined" (code 1) which is used to characterize credit
exposures which, by their nature, do not have a contractually defined
maturity or for which it is not possible to determine a due date. In
addition, the reporting of debt maturity has undergone a major change in
classification in December, 2013. For example, the maturity class "1 to
5 years" (code 5) is only valid between January, 2009 and November, 2013. From December 2013, this category is replaced by the maturity
class codes 51-54. The same applies to the maturity class "5 to 10
years" (code 6 replaced by codes 61-65), and the maturity class "10 to
20 years" (code 7 replaced by codes 71 and 72).

Due to these specificities, we adopt the following procedure.

Firstly, we harmonize the debt maturity information after December, 2013
using the classification of September, 2009 as the latter is less
disaggregated than the former.

Secondly, we assign the midpoint maturity for each maturity
classification (0.5 years for maturity less than or equal to 1 year; 3 years for more than 1 year
and less than or equal to 5 years; 7.5 years for more than 5 year and less than or equal to 10 years; 15 years for more than 10
year and less than or equal to 20 years; 22.5 years for more than 20 year and less than or equal to 25 years; 27.5 years
for more than 25 year and less than or equal to 30 years). We assign an average value of 40 years
for credit maturing in more than 30 years.

Thirdly, we calculated the average debt maturity, weighted by the credit
outstanding with the corresponding maturity.

Lastly, we reassign a maturity class to the calculated weighted average
maturity value:

- Class 1 credit with a maturity of less than or equal to 1 year;

- Class 2 credit with a maturity of more than 1 year and less than or equal to 5 years;

- Class 3 credit with a maturity of more than 5 years and less than or equal to 10 year;

- Class 4 credit with a maturity of more than 10 years and less than or equal to 20 year;

- Class 5 credit with a maturity of more than 20 year.
