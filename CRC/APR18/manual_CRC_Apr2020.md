
---
title: Central Credit Responsibility Database - Firm Level - Data Manual
---


`Extraction Date`: June 2019

`Manual Date`: 17 April 2020

\

**Abstract**: The *Central Credit Responsibility (CCR)*/*Central de Responsabilidades de Crédito* (CRC) database reports credit supply by all credit-granting institutions in Portugal.[^1] Data is collected monthly with the objective of supporting participants in the risk assessment of the concession credit. Although *Banco de Portugal* collects information at the credit exposure level, the microdata available to external researchers consists of a set of files with data aggregated at the firm level from 1999. The dataset is updated annually.

[^1]: Some institutions which do not grant credit but *Banco de Portugal* sees as relevant are also included in the CCR (for example restructuring funds). For more information contact bplim@bportugal.pt.

\

**Keywords**: Credit outstanding, firm level, credit-granting institutions, bank relationship, revisions.

\



# Table of Contents

1. [General Information](#general-information)

2. [Geographical Coverage](#geographical-coverage)

3. [Population](#population)

4. [Methodology](#methodology)

5. [Description of Files](#description-of-files)

6. [Description of Variables](#description-of-variables)

    6.1. [Cover Sheet](#a.-cover-sheet)

    6.2. [Credit Outstanding and Bank Relationships](#b.-credit-outstanding-and-bank-relationships)

7. [Basic Descriptive Statistics](#basic-descriptive-statistics)

8. [Legislation](#legislation)

9. [Citation of This Dataset](#citation-of-this-dataset)

10. [Auxiliary Files](#auxiliary-files)

11. [Useful Links](#useful-links)

12. [Useful Ado Files](#useful-ado-files)

    12.1. [Construction of Firm Default Profile](#a.-construction-of-firm-default-profile)

    12.2. [Aggregation](#b.-aggregation)

13. [Frequently Asked Questions](#frequently-asked-questions)

14. [References](#references)

15. [Appendix](#appendix)



# General Information

>  `Data Type`: Longitudinal Data

>  `Unit of Analysis`: Firm

>  `Frequency`: Monthly

>  `Start Date`: January, 1999

>  `Most Recent Date`: August, 2018

>  `Reference Date`: The last day of a month

>  `Data Organization`: There is a single file that contains firm-level generic information (*COVER*) and yearly files that contain monthly information on credit outstanding & bank relationship (*COBR*) for each firm. All data files are available in Stata format.

>  `Version of the Data`: The data made available by BPLIM corresponds to a data freeze at a certain time of the year. Therefore, all files contain the information as reported in the extraction date. The most recent update of the data occurred in April 2019.

>  `Languages Available`: variables labels are available in English.

>  `Data Access`: This data set is available to external researchers under certain conditions.[^2]

[^2]: Conditions for data access for external researchers are detailed in the disclosure control regulation.

>  `Digital Object Identifier`: 10.17900/CRC.FRM.Jun2019.V1.

# Geographical Coverage

CCR includes all firms operating in mainland Portugal and autonomous regions - Azores and Madeira.


# Population
The Central Credit Responsibility (CCR) database collects and aggregates the data on the indebtedness of borrowers as reported by credit-granting institutions (institutions operating in Portugal or foreign branches of Portuguese banks).
All credit obligations above the reporting threshold are included, regardless if the credit is in good standing or in situations of non-compliance.[^3]
Although *Banco de Portugal* collects information at the credit exposure level, the micro data available to external researchers only consists of a set of files with data aggregated at the firm level.
Private persons and individual entrepreneurs are therefore excluded.

[^3]: The current mandatory loan registration threshold in Portuguese credit register is 50 euros. It was 10 euros from 1999 to 2008.

The entities participating in CCR include: banks, saving banks, mutual agricultural credit banks, financial credit institutions, leasing companies, factoring companies, securitization companies, mutual guarantee societies, and financial companies for credit acquisitions.
Note that some financial institutions in Portugal have experienced acquisitions and/or mergers, which induced credit flows from one institution to another. The list of participating entities have therefore changed over time. The current list can be found [here](https://www.bportugal.pt/sites/default/files/crc_lista_entidades.pdf).


# Methodology

Although *Banco de Portugal* collects information at the credit exposure level, only data aggregated at the firm level is made available to external researchers. These firm level datasets were constructed using the exposure level data extracted from *Banco de Portugal*’s CCR database.

The CCR has undergone some major revisions. Due to these revisions, there are some series breaks that may affect analysis. Of particular relevance is the revision in 2009, framed by Decree-Law no. 204/2008, of October 14, which streamlined the coding for a number of categorical variables and included data on maturity of loans, overdue loan class, collateral and special characteristics for the first time.[^4] To make the variables compatible over time, we have adopted necessary steps to harmonize the data. Available variables and their construction methods are detailed in the section [“Description of Variables”](#description-of-variables).

[^4]: Please refer to the legislation section for a detailed discussion.


Further, additional cleaning is conducted. In particular, the values that were reported in different scales and in other currencies were converted to euros. Therefore, regardless of the denominated currency, the value of the exposure is always expressed in euros. To preserve consistency credit granted to Portuguese firms by foreign banks and credit granted to foreign firms were removed.

To preserve confidentiality, firm identifications are anonymized and the credit outstanding variables are perturbed. The figure below explains how we construct the firm-level *COBR* file from the exposure-level data.

![**Figure 1**: Aggregation of exposure level data to firm level data](.\attachments\aggregationfirmlevel.png)



# Description of Files

Firm-level generic information is organized in the cover sheet (COVER) file. Each row corresponds to a firm for the information period.

The data file has the following nomenclature:

*CRC_A_FRM_MMMYY_COVER_V01.dta*

**where *MMMYY* is the extraction month.**

\

The firm level CCR data is organized in the credit outstanding & bank relationship (COBR) file. The data is reported at the monthly frequency and each row corresponds to a firm in a given month.

The monthly data files are appended to yearly dataset with the following nomenclature:

*CRC_P_MFRM_YYYY_MMMYY_COBR_V01.dta*

**where *YYYY* is the reporting year; *MMMYY* is the extraction month.**

Some variables are only calculated after 2009, for example, weighted average debt maturity (original and residual). Examples are illustrated in Appendix.


# Description of Variables

## A. Cover Sheet

Below we provide a general description of the variables included in the Cover Sheet (*COVER*) . For a full account of all variable categories and changes over time see [“Auxiliary Files” section](#auxiliary-files).

-  `Legal form`

Firm’s legal form.

+-------------------------------------------------------+--------------------------------+
| Abbreviation                                          | Definition                     |
+:======================================================+:===============================+
| *natjur*                                              | Legal form                     |
+-------------------------------------------------------+--------------------------------+

**Availability**: January, 1999-August, 2018

For a complete list of codes, see the auxiliary file [var_crc.html](./aux_files/variables_description/var_crc.html)

-  `Classification of economic activities`

Firm’s main sector of activity. The criteria to define the main sector of activity is the gross value added at factor cost. When it is not possible to use this information to define the main sector of activity, firms are requested to use turnover or the number of people permanently employed by the firm. From 2006 to 2008, firms reported the code of “The Portuguese Classification of Economic Activities - Revision 2.1” (CAE Rev. 2.1) at the highest level of disaggregation. Since 2009, firms report their main activity according to the “The Portuguese Classification of Economic Activities - Revision 3” (CAE Rev. 3). The Statistics Department of Banco de Portugal provides the information on the main sector of activity according to both classifications CAE Rev2.1 and CAE Rev3 whenever possible and the classifications are harmonized over time. The source of this information is the CAE registered in the “Central Registry of Companies” for each company. Whenever the correspondence is not unique, the match between codes CAE Rev. 2.1 and CAE Rev. 3 is implemented based on the highest frequency of the matches.[^6]

[^6]: For more information on firm’s sector of activity please see [SICAE Website](http://www.sicae.pt/Default.aspx)

+------------------------------------------+----------------------------------------------------------------------------------------------+
| Abbreviation                             | Definition                                                                                   |
+:=========================================+:=============================================================================================+
| *cae21*                                  | Portuguese classification of Economic activities (version 2.1).                              |
+------------------------------------------+----------------------------------------------------------------------------------------------+
| *cae3*                                   | Portuguese classification of Economic activities (version 3).                                |
+------------------------------------------+----------------------------------------------------------------------------------------------+

**Availability**: January, 1999-August, 2018

For a complete list of codes, see the auxiliary file [var_crc.html](./aux_files/variables_description/var_crc.html)


-  `Geographical location`

Firm's geographical location (district and municipality in which a firm is located).

+-------------------------------------------------------+--------------------------------+
| Abbreviation                                          | Definition                     |
+:======================================================+:===============================+
| *district*                                            | District                       |
+-------------------------------------------------------+--------------------------------+
| *municipality*                                        | Municipality                   |
+-------------------------------------------------------+--------------------------------+

**Availability**: January, 1999-August, 2018

For a complete list of codes, see the auxiliary file [var_crc.html](./aux_files/variables_description/var_crc.html)


-  `Institutional sector`

Firm's institutional sector. The algorithm to allocate a firm to a specific institutional sector is based on the classification of economic activity, the name of the firm and other variables available at *Banco de Portugal*. Therefore, in some cases the institutional sector may not be in line with the sector of economic activity.

+-------------------------------------------------------+------------------------------------------------------------------------------------------------+
| Abbreviation                                          | Definition                                                                                     |
+:======================================================+:===============================================================================================+
| *si*                                                  | Institutional sector (SEC 95)                                                                  |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------+
| *si_final*                                            | Institutional sector ([**SEC 2010**](./aux_files/legislation/SEC2010.pdf))               |
+-------------------------------------------------------+------------------------------------------------------------------------------------------------+

**Availability**: January, 1999-August, 2018

For a complete list of codes, see the auxiliary file [var_crc.html](./aux_files/variables_description/var_crc.html)


-  `Information date`

The start date and end date of the identified information

+------------------------------------------+----------------------------------------------------------------------------------------------+
| Abbreviation                             | Definition                                                                                   |
+:=========================================+:=============================================================================================+
| *mindate*                                | Start date of the information                                                                |
+------------------------------------------+----------------------------------------------------------------------------------------------+
| *maxdate*                                | End date of the information                                                                  |
+------------------------------------------+----------------------------------------------------------------------------------------------+

**Availability**: January, 1999-August, 2018


## B. Credit Outstanding and Bank Relationships

Below we provide a general description of the variables included in the credit outstanding & bank relationship (*COBR*) file. For a full account of all variable categories and changes over time see [“Auxiliary Files” section](#auxiliary-files).

-  `Firm identifier`

Unique identifier that enables tracking borrowing firms over time. *tina* is the anonymized tax identification number, available in all files.
In the original credit exposure data, Portuguese firms are identified by the tax identification number (NIPC). *Banco de Portugal* control the credibility of debtor identification in CCR by cross-checking other sources to ensure that the identification exists and is valid. It should also be noted that reporting to CCR does not depend on the nationality of the debtors but their country of residence.[^5]

+-------------------------------------------------------+--------------------------------+
| Abbreviation                                          | Definition                     |
+:======================================================+:===============================+
| *tina*                                                | Anonymized firm identifier     |
+-------------------------------------------------------+--------------------------------+

**Availability**: January, 1999-August, 2018

[^5]: For instance, the file of the taxpayers' identification numbers managed by the Tax and Customs Authority (TA) and the national file of Collective Persons (FNPC) managed by the Ministry of Justice are often cross-checked to ensure consistency.

-  `Reference date`

The reference month of the data

+------------------------------------------+--------------------------------+
| Abbreviation                             | Definition                     |
+:=========================================+:===============================+
| *date*                                   | Reference month of the data.   |
+------------------------------------------+--------------------------------+

**Availability**: January, 1999-August, 2018

-  `Global Credit`

The credit outstanding variables characterize the amount outstanding according to a variety of dimensions.

Global credit is the sum of regular credit and potential credit, representing the total available credit that a firm accesses.

+-----------------------------------------------+--------------------------------------------------------+
| Abbreviation                                  | Definition                                             |
+:==============================================+:=======================================================+
| *valor_global*                                |Total available credit that a firm can access         |
+-----------------------------------------------+--------------------------------------------------------+

**Availability**: January, 1999-August, 2018

-  `Regular Credit`

Regular credit is credit effectively used in a regular situation, i.e., without payment delays as defined in the respective contract.

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
| *valor_curto_o*                                                   | Credit with an original maturity of less than or equal to 1 year          |
+-------------------------------------------------------------------+---------------------------------------------------------------------------+
| *valor_curto_r*                                                   | Credit with a residual maturity of less than or equal to 1 year           |
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
| *valor_longo_o*                                                   | Credit with an original maturity of more than 1 year                      |
+-------------------------------------------------------------------+---------------------------------------------------------------------------+
| *valor_longo_r*                                                   | Credit with a residual maturity of more than 1 year                       |
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

Secondly, we assign the midpoint maturity for each maturity classification (0.5 years for maturity less than or equal to 1 year; 3 years for more than 1 year and less than or equal to 5 years; 7.5 years for more than 5 year and less than or equal to 10 years; 15 years for more than 10 year and less than or equal to 20 years; 22.5 years for more than 20 year and less than or equal to 25 years; 27.5 years for more than 25 year and less than or equal to 30 years). We assign an average value of 40 years for credit maturing in more than 30 years.

Thirdly, we calculated the average debt maturity, weighted by the credit outstanding with the corresponding maturity.

Lastly, we reassign a maturity class to the calculated weighted average maturity value:

+---------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| Maturity Class                                    | Definition                                                                                              |
+:==================================================+:========================================================================================================+
|  1                                                | Credit with a calculated weighted average maturity of less than or equal to 1 year                      |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|  2                                                | Credit with a calculated weighted average maturity of more than 1 year and less than or equal to 5 years|
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|  3                                                | Credit with a calculated weighted average maturity of more than 5 years and less than or equal to 10 year|
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|  4                                                | Credit with a calculated weighted average maturity of more than 10 years and less than or equal to 20 year|
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------+
|  5                                                | Credit with a calculated weighted average maturity of more than 20 year                                |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------+


-  `Credit by maturity structure`

For the data after 2009, we breakdown the amount of credit using various maturity classifications, as illustrated below.

+----------------------------------------------+---------------------------------------------------------------------------+
| Abbreviation                                 | Definition                                                                |
+:=============================================+:==========================================================================+
| *valor_prazo1_o*                             | Credit with an original maturity of less than or equal to 1 year          |
+----------------------------------------------+---------------------------------------------------------------------------+
| *valor_prazo2_o*                             | Credit with an Original maturity of more than 1 year and less than or equal to 5 years   |
+----------------------------------------------+---------------------------------------------------------------------------+
| *valor_prazo3_o*                             | Credit with an Original maturity of more than 5 years and less than or equal to 10 year  |
+----------------------------------------------+---------------------------------------------------------------------------+
| *valor_prazo4_o*                             | Credit with an Original maturity of more than 10 years and less than or equal to 20 year |
+----------------------------------------------+---------------------------------------------------------------------------+
| *valor_prazo5_o*                             | Credit with an Original maturity of more than 20 year                     |
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
| *valor_prazo4_r*                               | Credit with a residual maturity of more than  10 years and  less than or equal to 20 year             |
+------------------------------------------------+--------------------------------------------------------------------------+
| *valor_prazo5_r*                               | Credit with a residual maturity of more than  20 year                             |
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
\

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

Table 1- Number of firms over the data period (year-end) in the credit outstanding & bank relationship file[^7]

```s/
    global path1 "Z:/data/Products/CRC/2018_04/CRC_Annual/Output/Data/Firms/"
    global path2 "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/"
    global path3 "Z:/data/Products/CRC/2019_04/CRC_Annual/Output/Data/Firms/"

    quietly use "${path3}/2018/External/CRC_A_MFRM_2018_APR19_COBR_V01.dta", clear
    quietly append using "${path1}/2017/External/CRC_A_MFRM_2017_APR18_COBR_V01.dta"
    quietly keep if (year(dofm(date))<2018 & month(dofm(date))==12) | (year(dofm(date))==2018 & month(dofm(date))==8)

    quietly forval i =1999/2016 {
      quietly append using "${path2}/`i'/External/CRC_A_MFRM_`i'_APR17_COBR_V01.dta"
      quietly keep if (year(dofm(date))<2018 & month(dofm(date))==12) | (year(dofm(date))==2018 & month(dofm(date))==8)
    }

    quietly gen Year= year(dofm(date))
    quietly sort tina Year
    table Year, contents(freq) center
```

[^7]: The credit outstanding & bank relationship data is only available until August, 2018 due the transition from CCR to AnaCredit.

# Legislation
Variable definitions changed over time. Some variables, for instance, credit situation (*situacaocredito*), maturity (*prazooriginal* and *prazoresidual*), and collateral type (*tipogarantia*) have undergone major changes in classification, as framed by *Banco de Portugal*’s instructions. It is important to note that even small changes may require a infrastructural update on the part of the participating financial entities, possibly leading to a gradual implementation of the instruction even though legally all the entities should implement the instructions at the same time.
Below is a list of relevant legislations:


-	[**Decree-Law no. 47909/1967**](./aux_files/legislation/Decreto-Lei_47909.pdf), September 7 and [**Decree-Law no. 48731/1968**](./aux_files/legislation/Decreto-Lei_48731.pdf), December 4 - established the service of centralizing and disseminating credit risk information and defines its purpose and operation, given the need of credit and other financial institutions to properly assess the risks of their operations.

-	[**Carta Circular no 29/96/DOC**](./aux_files/legislation/Carta-Circular_29-96-DOC.pdf), September 18 – eliminated credit classes associated with *empréstimos de poupança-crédito*, which are now classified as *empréstimos de poupança-emigrante* (the conversion of savings-credit loans into savings-immigrant loans).

-	[**Decree-Law no. 5/1998**](./aux_files/legislation/Lei_5-1998.pdf), January 31 – amended the Organic Law of *Banco de Portugal*, with a view to its integration into the European System of Central Banks.

-	[**Decree-Law no. 67/1998**](./aux_files/legislation/Lei_67-1998.pdf), October 27 – transposed the Directive 95/46/CE of the European Parliament and the Directive of the Council in 24-10-1995 on the protection of individuals in processing and circulating data.

-	[**Instrução no. 16/2001**](./aux_files/legislation/Instrucao_16-2001_full.pdf) – reviewed the separation of potential from actual amounts of credit.

-	[**Instrução no. 11/2002**](./aux_files/legislation/Instrucao_11-2002.pdf) – establishment of a 90 day period to register a credit exposure (*sem direito de regresso*) or overdue credit (*com direito de regresso*) after invoices are due; revocable commitments (code 921) are  no longer reported as a credit of type 6 (off balance sheet commitments); factoring credit more than 90 days overdue reported as type 7 (non-performing credit) or 8 (credit in litigation). Participating entities are encouraged to provide relevant information for credit risk assessment. In addition, renegotiated credits are requested to be reported since July, 2001.

-	[**Instrução no. 15/2002**](./aux_files/legislation/Instrucao_15-2002.pdf) – made procedural changes to access and occasional communication requested by the Banco de Portugal (no analysis impact).

-	[**Decree-Law no. 53/2004**](./aux_files/legislation/Lei_53-2004.pdf), March 18 – integrated the information on court decisions regarding insolvency proceedings of collective or individual people, provided by the Ministry of Justice, following the approval of the CIRE - Insolvency Code.

-	[**Instrução no. 7/2006**](./aux_files/legislation/Instrucao_7-2006_full.pdf) – created new types of credit for the variable type (codes 11-14) which include guarantees, sureties, and credit communicated by foreign central banks.

-	[**Instrução no. 21/2008**](./aux_files/legislation/Instrucao_21-2008_full.pdf) – changed the CCR to its current format (as in *Caderno* da CCR) and defined the scope, reporting deadline, and stress the important of reporting the types of information. Some codes were significantly changed.

-	[**Instrução no. 7/2009**](./aux_files/legislation/Instrucao_7-2009.pdf) – included credit reports from the State to protect unemployed individuals’ real estate ownership and created a special classification for these credits. This revised version contains more loan-level variables. Another important consequence of the revision was the incorporation of loans to Portuguese firms granted by foreign branches of Portuguese banks.

-	[**Instrução no. 18/2010**](./aux_files/legislation/Instrucao_18-2010.pdf) – imposed mandatory reporting of credit less than 90 days overdue (*crédito sem recurso*) if used in guarantee pools in Eurosystem operations; excluded shareholder’s advances (*suprimentos*) from financial institutions; imposed mandatory reporting of securitized debt issued for a certain debtor (even if the financial institution does not have ownership) and exclusion of securitized debt in the exposure sheet of the institution.

-	[**Instrução no. 17/2013**](./aux_files/legislation/Instrucao_17-2013.pdf) – separated overdue and written-off credit in litigation – codes 6 and 7; added new maturity categories and new collateral classifications


# Citation of this dataset
Banco de Portugal Microdata Research Laboratory (BPLIM) (2019): Central Credit Responsibility Database - Firm Level Data. Extraction: June 2019. Version: V1. BANCO DE PORTUGAL. Dataset. https://doi.org/10.17900/CRC.FRM.Jun2019.V1


# Auxiliary Files
For a description of each variable in each dataset (name, unit of measurement, data and storage type, format, year of first and last observation), an account of the changes occurred over time, summary statistics for each dataset and a codebook for each dataset, please check the following auxiliary files:

| Data File | Description of Variables | Summary Statistics | Codebook | Dataset description |
| :---- | :----: | :----: | :----: |  :----: |
| Central Credit Responsibility Firm (CCR_FRM) |	[var_crc.html](./aux_files/variables_description/var_crc.html) | [stat_crc.html](./aux_files/descriptive_statistics/stat_crc.html) | 	[cdbk_crc.html](./aux_files/codebook/cdbk_crc.html) | [dscr_crc.html](./aux_files/describe_dataset/dscr_crc.html) |


The Summary Statistics, Codebook and Dataset Description files are available on BPLIM's servers.

# Useful Links

[CCR home page](https://www.bportugal.pt/area-cidadao/formulario/227)

[Statistical Bulletin](https://www.bportugal.pt/en/publicacao/statistical-bulletin)


# Useful Ado Files

 ## A. Construction of Firm Default Profile

`Description`

`default ` is a Stata user-written command to help calculate default events using information from the  datasets.


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

-	Overdue credit flag (*\_flag*). This is an indicator for the existence of overdue credit. It takes the follow values:

+-------------------------------------------------------------------------------+
|   0 - no credit is past due at the time                                      |
+-------------------------------------------------------------------------------+
|   1 - overdue credit is present but below the threshold                      |
+-------------------------------------------------------------------------------+
|   2 - overdue credit is above the threshold                                  |
+-------------------------------------------------------------------------------+

- Default event (*\_default*). The default event occurs when a firm has credit overdue above the threshold for a run of defined consecutive months (three months by default).

- First default event (*\_fdefault*).The first default event occurs (flagged out with the value of 1) when a firm has credit overdue above the threshold for a run of defined consecutive months for the first time.



 ## B. Aggregation

`Description`

`aggregate ` is a Stata user-written command to help compute aggregates of credit and bank relationship at different frequencies (yearly and quarterly) using various methods (period-end or period average). By default, the ado should only be applied to the original  datasets prepared by BPLIM.


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



# Frequently Asked Questions
The most frequently asked questions can be found [here](https://www.bportugal.pt/perguntas-frequentes/276).
If you have a question that is not covered in this manual, please send an email to bplim@bportugal.pt.


## References
Banco de Portugal (2003). Central de Responsabilidades de Crédito. Cadernos do Banco de Portugal. Lisboa.

Banco de Portugal (2010). Central de Responsabilidades de Crédito. Cadernos do Banco de Portugal. Lisboa.

Banco de Portugal (2011). Central de Responsabilidades de Crédito. Cadernos do Banco de Portugal. Lisboa.

Banco de Portugal (2014). Central de Responsabilidades de Crédito. [**Manual de Procedimentos Instrução no. 21/2008**](./aux_files/legislation/ManualdeprocedimentosdaCRC.pdf). Lisboa.

Banco de Portugal (2015). Central de Responsabilidades de Crédito. Cadernos do Banco de Portugal. Lisboa.

João Cadete de Matos (2015). The Portuguese Central Credit Register: a powerful multipurpose tool, relevant for many central bank functions. IFC workshop on “Combining micro and macro statistical data for financial stability analysis”. Bank for International Settlements.

Antunes, António, Homero Gonçalves, and Pedro Prego (2016). Firm Default Probabilities Revisited. Banco de Portugal Economic Studies, 2, 21-45.


## Appendix
![**Appendix 1**: Monthly credit outstanding at firm level: before 2009](.\attachments\appendix1.png)

![**Appendix 2**: Monthly credit outstanding at firm level: after 2009](.\attachments\appendix2.png)


------------------------------------------------------------------------------------------------------------
Footnotes
