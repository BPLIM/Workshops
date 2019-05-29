Data Manual
-----------

`Extraction Date`: June 2018

`Manual Date`: September 2018

**Abstract**: The Monetary Financial Institutions (MFIs) Balance Sheet
Database reports detailed information on the assets and liabilities of
the monetary financial institutions (MFIs) operating in Portugal. The
dataset is updated annually.

**Keywords**: balance sheet, asset, liabilities, instrument,
counterparty, revisions.

Table of contents
=================

1.  [General Information](#general-information)

2.  [Geographical Coverage](#geographical-coverage)

3.  [Population](#population)

4.  [Methodology](#methodology)

5.  [Description of Files](#description-of-files)

6.  [Description of Variables](#description-of-variables)

7.  [Basic Descriptive Statistics](#basic-descriptive-statistics)

8.  [Auxiliary Files](#auxiliary-files)

9.  [Useful Links](#useful-links)

10. [Legislation](#legislation)

11. [Citation of this dataset](#citation-of-this-dataset)

General Information
===================

> `Data Type`: longitudinal data

> `Unit of Analysis`: instrument-counterparty

> `Frequency`: monthly

> `Start Month`: September, 1997

> `End Month`: December, 2017

> `Reference date`: month-end

> `Data Organization`: data is organized for assets and liabilities
> separately. All data files are available in Stata format, version 15.

> `Version of the Data`: the data made available by BPLIM corresponds to
> a data freeze at a certain time of the year. Therefore, all files
> contain information as reported at the extraction date. The most
> recent update of the data occurred in June 2018.

> `Languages Available`: variables labels are available in Portuguese
> and in English. [^1^](#fn1){#fnref1 .footnote-ref}

> `Data Access`: this data set is available to external researchers
> under certain conditions.[^2^](#fn2){#fnref2 .footnote-ref}

Geographical Coverage
=====================

The MFIs Balance Sheet Database includes the assets and liabilities of
all monetary financial institutions (MFIs) operating in mainland
Portugal and autonomous regions - Azores and Madeira.

Population
==========

The MFIs Balance Sheet Database collects the balance sheet data for all
monetary financial institutions (MFIs) that were in operation in
Portugal between September 1997 and December 2017.

[**Comment**]{.underline} : Non-monetary financial agents are not
covered in the database. In case an institution stops to be classified
as MFI, data reporting will be discontinued. Some MFIs in Portugal have
experienced acquisitions and/or mergers, which induced asset/liability
flows from one institution to another.

Methodology
===========

The MFIs Balance Sheet Database has undergone a major revision in
December, 2014 which lead to the reclassification of financial
institutions and counterparties.[^3^](#fn3){#fnref3 .footnote-ref}. Due
to this revision, there are some breaks in the series. The revision also
adds an extra variable that indicates institution type.

To make variables compatible over time, we have harmonized the data
based on the correspondence table illustrated in the [*Description of
Variables*](#description-of-variables) section.

To preserve confidentiality, MFIs are anonymized through unique
identifiers and the instrument values are perturbed for external
researchers.[^4^](#fn4){#fnref4 .footnote-ref}

Description of Files
====================

The MFIs Balance Sheet Database is organized separately for assets and
liabilities in the bank balance sheet (BBS) files. Each row corresponds
to an instrument-counterparty pair in a given month.

The data files are organized with the following nomenclature:

***BBS\_METH\_BNK\_xxxx\_yyyy\_V01.dta***

where *xxxx* denotes the data range (eg: SEP1997DEC2017), *yyyy* denotes
the type of balance (ASSET for asset instruments; LIAB for liability
instrument), and *METH* denotes the method used to prepare the data
(*"A"* for Anonymized and *"P"* for Perturbed).

Identification of MFIs will be anonymized in the data. Additionally, for
external researchers the data values are perturbed.

We also provide a harmonized data set to facilitate the comparison
between the two reporting systems, i.e. before and after December, 2014.

Description of Variables
========================

`Bank identifier`

Anonymized identification number for MFI that enables tracking the MFI
over time. BPLIM provides an anonymized version of the MFIs identifier
which is denoted by *bina*.

  Abbreviation   Definition
  -------------- --------------------------------------
  *bina*         Anonymized bank identificaton number

**Availability**: 1997-2017

`Reference date`

The reference month of the data

  Abbreviation   Definition
  -------------- -----------------------------
  *date*         Reference month of the data

**Availability**: 1997-2017

`Instrument code`

Classification of the financial instrument

The classification of financial instruments was revised in December,
2014. As a result, a new categorization was applied thereafter. Below is
the correspondence table for the instrument codes between the two
reporting systems (aligned based on the previous reporting system).

  Abbreviation          Definition
  --------------------- ---------------------------------------
  *instrument\_asset*   Financial instruments: asset side
  *instrument\_liab*    Financial instruments: liability side

**Availability**: 1997-2017

**Table 2** - Correspondence Table for Financial Instruments

Panel A: Asset side (*instrument\_asset*)

  -------------------------------------------------------------------------
  **Before                              **December 2014   
  December                              onwards**         
  2014**                                                  
  ------------ ------------------------ ----------------- -----------------
  **Code**     **Designation**          **Code**          **Designation**

  10           Banknotes and coins      10                Banknotes and
                                                          coins

  20           Credit and equivalent -  20                Credit and
               up to 1 year                               equivalent - up
                                                          to 1 year

  30           Credit and equivalent -  30                Credit and
               from 1 year to 5 years                     equivalent - from
                                                          1 year to 2 years

  30           Credit and equivalent -  40                Credit and
               from 1 year to 5 years                     equivalent - from
                                                          2 year to 5 years

  40           Credit and equivalent -  50                Credit and
               more than 5 years                          equivalent - more
                                                          than 5 years

  50           Securities other than    60                Debt securities -
               equity - up to 1 year                      up to 1 year

  60           Securities other than    70                Debt securities -
               equity - from 1 year to                    from 1 year to 2
               2 years                                    years

  70           Securities other than    80                Debt securities -
               equity - more than 2                       more than 2 years
               years                                      

  80           Equity securities        90                Traded shares

  80           Equity securities        100               Untraded shares

  80           Equity securities        110               Other equities

  80           Equity securities        120               Units

  100          Properties, furnitures,  130               Properties,
               and equipments                             furnitures, and
                                                          equipments

  110          Miscellaneous assets     140               Miscellaneous
                                                          assets

  90           Units (included in       120               Units
               equity securities)                         
  -------------------------------------------------------------------------

[**Comment**]{.underline} : Before December 2014, the financial
instrument "Units" (coded 90) is also included in the financial
instrument "Equity securities" (coded 80).

**When calculating the aggregates, to avoid double counting the value
for "Unit" should be dropped.**

Panel B: Liability side (*instrument\_liab*)

  -------------------------------------------------------------------------
  **Before                              **December 2014   
  December                              onwards**         
  2014**                                                  
  ------------ ------------------------ ----------------- -----------------
  **Code**     **Designation**          **Code**          **Designation**

  130          Demand deposits          380               Demand deposits
               (excluding sight                           (excluding sight
               deposits)                                  deposits)

  140          Deposits redeemable at a 390               Deposits
               notice of up to 90 days                    redeemable at a
               (excluding sight                           notice of up to
               deposits)                                  90 days
                                                          (excluding sight
                                                          deposits)

  150          Deposits redeemable at a 400               Deposits
               notice of more than 90                     redeemable at a
               days (including sight                      notice of more
               deposits)                                  than 90 days
                                                          (including sight
                                                          deposits)

  170          Deposits and equivalent  420               Deposits and
               (excluding demand                          equivalent
               deposits, deposits                         (excluding demand
               redeemable at notice,                      deposits,
               and trading liabilities)                   deposits
               - up to 1 year                             redeemable at
                                                          notice, and
                                                          trading
                                                          liabilities) - up
                                                          to 1 year

  180          Deposits and equivalent  430               Deposits and
               (excluding demand                          equivalent
               deposits, deposits                         (excluding demand
               redeemable at notice,                      deposits,
               and trading liabilities)                   deposits
               - from 1 to 2 years                        redeemable at
                                                          notice, and
                                                          trading
                                                          liabilities) -
                                                          from 1 to 2 years

  190          Deposits and equivalent  440               Deposits and
               (excluding demand                          equivalent
               deposits, deposits                         (excluding demand
               redeemable at notice,                      deposits,
               and trading liabilities)                   deposits
               - more than 2 years                        redeemable at
                                                          notice, and
                                                          trading
                                                          liabilities) -
                                                          more than 2 years

  200          Trading liabilities      450               Trading
                                                          liabilities - up
                                                          to 1 year

  200          Trading liabilities      460               Trading
                                                          liabilities -
                                                          more than 1 year

  210          Securities other than    470               Debt securities
               capital - up to 1 year                     issued - up to 1
                                                          year

  220          Securities other than    480               Debt securities
               capital - from 1 to 2                      issued - from 1
               years                                      to 2 years

  230          Securities other than    490               Debt securities
               capital - from 2 years                     issued - more
                                                          than 2 years

  240          Capital and reserves     500               Capital and
                                                          reserves

  260          Miscellaneous            520               Miscellaneous
               liabilities                                Liabilities
  -------------------------------------------------------------------------

`Counterparty code`

Classification of counterparty

  Abbreviation            Definition
  ----------------------- ------------------------------------------------
  *counterparty\_asset*   Classification of counterparty: asset side
  *counterparty\_liab*    Classification of counterparty: liability side

**Availability**: 1997-2017

The classification of counterparties was also revised in December, 2014.
The correspondence table for the counterparty codes between the two
reporting systems (aligned based on the previous reporting system) is:

**Table 3** - Correspondence Table for Counterparties

Panel A: Asset side (*counterparty\_asset*)

  -------------------------------------------------------------------------
  **Before                              **December 2014   
  December                              onwards**         
  2014**                                                  
  ------------ ------------------------ ----------------- -----------------
  **Code**     **Designation**          **Code**          **Designation**

  10           Monetary financial       11                Central banks
               institutions                               

  10           Monetary financial       12                Money market
               institutions                               funds

  10           Monetary financial       13                Deposit
               institutions                               institutions,
                                                          excluding central
                                                          banks

  20           Other financial          18                Other financial
               intermediaries and                         intermediaries,
               financial auxiliaries                      financial
                                                          auxiliaries, and
                                                          captive financial
                                                          institutions and
                                                          money lenders

  20           Other financial          22                Investment fund,
               intermediaries and                         excluding money
               financial auxiliaries                      market funds

  30           Insurance corporations   31                Insurance
               and pension funds                          corporations

  30           Insurance corporations   32                Pension funds
               and pension funds                          

  40           Central government       40                Central
                                                          government

  50           Regional government      50                Regional
                                                          government

  60           Local government         60                Local government

  70           Social security          70                Social security

  80           Non-financial            80                Non-financial
               institutions                               institutions

  90           Individuals              91                Family

  90           Individuals              92                Non-profit
                                                          institutions
                                                          serving
                                                          households

  120          Irrelevant sector        120               Irrelevant sector
  -------------------------------------------------------------------------

Panel B: Liability side (*counterparty\_liab* )

  -------------------------------------------------------------------------
  **Before                              **December 2014   
  December                              onwards**         
  2014**                                                  
  ------------ ------------------------ ----------------- -----------------
  **Code**     **Designation**          **Code**          **Designation**

  10           Central banks            10                Central banks

  20           Institutions not subject 21                Money market
               to minimum reserves,                       funds
               namely the money market                    
               funds                                      

  30           Institutions subject to  22                Deposit
               minimum reserves                           institutions,
                                                          excluding central
                                                          banks

  40           Other financial          39                Other financial
               intermediaries and                         intermediaries,
               financial auxiliaries                      financial
                                                          auxiliaries, and
                                                          captive financial
                                                          institutions and
                                                          money lenders

  40           Other financial          43                Investment fund,
               intermediaries and                         excluding money
               financial auxiliaries                      market funds

  50           Insurance corporations   51                Insurance
               and pension funds                          corporations

  50           Insurance corporations   52                Pension funds
               and pension funds                          

  60           Central government       60                Central
                                                          government

  70           Regional government      70                Regional
                                                          government

  80           Local government         80                Local government

  90           Social security          90                Social security

  100          Non-financial            100               Non-financial
               institutions                               institutions

  110          Individuals              111               Family

  110          Individuals              112               Non-profit
                                                          institutions
                                                          serving
                                                          households

  120          Irrelevant sector        120               Irrelevant sector
  -------------------------------------------------------------------------

`Country`

Country of origin or region of the counterparty

  Abbreviation   Definition
  -------------- -------------------
  *country*      Country of origin

**Availability**: 1997-2017

**Table 4** - Counterparty Countries (*country*)

  **Code**   **Designation**
  ---------- ---------------------------------------------
  UM-PT      Monetary Union countries excluding Portugal
  TP-UM      Countries outside Monetary Union
  EUB        European Central Bank
  AUT        Austria
  BEL        Belgium
  CYP        Cyprus
  DEU        Germany
  ESP        Spain
  EST        Estonia
  FIN        Finland
  FRA        France
  GRC        Greece
  IRL        Ireland
  ITA        Italy
  LTU        Lithuania
  LUX        Luxembourg
  LVA        Latvia
  MLT        Malta
  NLD        Netherlands
  PRT        Portugal
  SVK        Slovakia
  SVN        Slovenia

[**Comment**]{.underline} : One should take caution not to double count
the Monetary Union (UM) countries when calculating the aggregates. For
example, the total assets of each bank should be aggregated only using
the following components: *Portugal, Monetary Union countries excluding
Portugal (UM-PT) and Countries outside Monetary Union (PT-UM).*

`Institution code`

Type of institution. This variable is only available from December, 2014
onwards.

  Abbreviation   Definition
  -------------- ---------------------
  *inst\_type*   Type of institution

**Availability**: 2014-2017

**Table 5** -- Institution Code (*inst\_type*)

  **Code**   **Designation**
  ---------- -----------------------------------------------------------------------
  1          Banks
  2          Saving banks
  3          Money market fund
  4          Central agricultural credit bank and mutual agricultural credit banks

`Value`

Value outstanding of a financial instrument, expressed in millions of
euros.

  Abbreviation   Definition
  -------------- ---------------------------
  *value*        Amount (in million euros)

**Availability**: 1997-2017

Basic Descriptive Statistics
============================

**Table 6** - Number of observations over the data period (as of
December)

``` {.stata}
──────────┬───────────
     Year │    Freq.  
──────────┼───────────
     1997 │    2,990  
     1998 │    3,117  
     1999 │    3,321  
     2000 │    3,014  
     2001 │    2,940  
     2002 │    2,926  
     2003 │    3,164  
     2004 │    3,194  
     2005 │    2,252  
     2006 │    2,391  
     2007 │    2,452  
     2008 │    2,545  
     2009 │    2,542  
     2010 │    2,429  
     2011 │    2,317  
     2012 │    2,326  
     2013 │    2,206  
     2014 │    2,882  
     2015 │    2,894  
     2016 │    2,857  
     2017 │    2,829  
──────────┴───────────
```

Auxiliary Files
===============

For a description of each variable in each dataset (name, unit of
measurement, data and storage type, format, year of first and last
observation), an account of the changes occurred over time, summary
statistics for each dataset and a codebook for each dataset, please
check the following auxiliary files:

**Description of Variables**:
[var\_bbs.html](./Auxiliary%20Files/variables_description/var_bbs.html)

**Summary Statistics**:
[stat\_bbs.html](./Auxiliary%20Files/descriptive_statistics/stat_bbs.html)[^5^](#fn5){#fnref5
.footnote-ref}

**Codebook**:
[cdbk\_bbs.html](./Auxiliary%20Files/codebook/cdbk_bbs.html)

**Dataset description**:
[dscr\_bbs.html](./Auxiliary%20Files/describe_dataset/dscr_bbs.html)

Useful Links
============

<https://www.bportugal.pt/EstatisticasWEB/MetadataItens/MContexto_IFM_EN.htm>

Legislation
===========

Below is a list of relevant legislations:

1.  [**Instrução no. 43/97**](./Instruções%20EMF-combine/43-97i67.pdf)

2.  [**Instrução no.
    19/2002**](./Instruções%20EMF-combine/19-2002i7.pdf)

3.  [**Instrução no.
    12/2010**](./Instruções%20EMF-combine/12-2010i4.pdf)

4.  [**Instrução no.
    20/2012**](./Instruções%20EMF-combine/20-2012i4.pdf)

5.  [**Instrução no. 25/2014**](./Instruções%20EMF-combine/25-2014m.pdf)

Citation of this dataset
========================

Banco de Portugal (2018), Monetary Financial Institutions Balance Sheet
Database. Extraction: June 2018. Microdata Research Laboratory (BPLIM)
Dataset.

::: {.section .footnotes}

------------------------------------------------------------------------

1.  ::: {#fn1}
    To see the labels in Portuguese type the following command line in
    Stata: "label language pt".[↩](#fnref1){.footnote-back}
    :::

2.  ::: {#fn2}
    Conditions for data access for external researchers are detailed in
    the *Guide for Researchers Using Banco de Portugal Microdata
    Research Laboratory (BPLIM) Data*.[↩](#fnref2){.footnote-back}
    :::

3.  ::: {#fn3}
    Please refer to the [variable
    spreadsheet](./Auxiliary%20Files/variables_description/var_bbs.html)
    for details.[↩](#fnref3){.footnote-back}
    :::

4.  ::: {#fn4}
    See the *Guide for Researchers Using Banco de Portugal Microdata
    Research Laboratory (BPLIM) Data*.[↩](#fnref4){.footnote-back}
    :::

5.  ::: {#fn5}
    Please note that the summary statistics are run based on the
    perturbed data.[↩](#fnref5){.footnote-back}
    :::
:::
