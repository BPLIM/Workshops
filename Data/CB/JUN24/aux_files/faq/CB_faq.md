---
title: Central Balance Sheet Database - Frequently Asked Questions
subtitle: Extraction Date - June 2024
date: 11 June 2024
doi: 10.17900/CB.CBA.Jun2024.V1
pdf-engine: pdflatex
execute:
  echo: false
format:
  html:
    theme: default
---

## General Questions
Q1. **There is a variable that is reported in IES but it is not included in any data file provided by BPLIM. May I request access to that variable?**

Yes. Please identify the Table and respective item that you need in the [IES form](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/modelos_formularios/decl_anual_inf_contabilistica_fiscal/Documents/ANUAL-AN-A.pdf) and send an email to bplim@bportugal.pt.
Please note that it is always possible to ask for additional variables that are not in the set of pre-selected variables that BPLIM makes available. However, these variables only have labels in Portuguese and some may not be subject to quality control.

Q2. **Do you have data at the establishment level?**

We do have data at the establishment level collected through Annex R of IES. This dataset is not available yet. However, if you are interested in working with these data please send an email to bplim@bportugal.pt.


Q3. **Is there data available for non-financial corporations before 2006?**

Yes, there is. Firms that submitted a declaration for the fiscal period of 2006 were required to fill in some information for the previous fiscal period. Therefore, there is information available for 2005 (Cover Sheet, Economic and Financial Information, Economic and Financial Indicators) for those firms reporting the financial statements of 2006.

Between 1991 and 2004, *Banco de Portugal* conducted a survey (*Inquérito Anual da Central de Balanços*) to non-financial corporations. This data set provides information on the financial statements of a sample of non-financial corporations (around 17.000 per year). To gain access to this data set please send an email to BPLIM.


Q4. **How can I deal with the break introduced by the new accounting system in 2010?**

BPLIM produces an harmonized data set with variables that are consistent over time. This data set (harmonized panel) is produced along with the annual files of *Central de Balanços*. It covers a smaller set of variables. For more information on this data please see the [manual on the harmonized panel data](https://msites-dee-bplim-prd.azurewebsites.net/content/central-balance-sheet-harmonized-panel-cbhp).


Q5. **Why are there differences between the statistics published in Sector Tables (aggregated by dimension category and sector of activity) and the ones computed using BPLIM microdata?**

Not all the firms included in the microdata that BPLIM makes available are used to compute the aggregated statistics available in Sector Tables. Namely, the information reported by holding companies and head offices is not included in those statistics. Additionally, the methodology and concepts used to compute some of the indicators published in Sector Tables have been recently revised and the formulas used to compute those variables may slightly differ from the ones currently made available by BPLIM.

Q6. **How can Holding Companies and Head Offices be identified?**

Holding companies may be identified through the Institutional Sector (variable *sectorinstfinal* available in the Cover Sheet). Holding companies are classified with the following codes of Institutional Sector:

- 302 (Public non-financial holding companies)
- 308 (Private non-financial holding companies) or
- 314 (Foreign controlled non-financial holding companies).

Head Offices may be identified through the main economic activity of the firm. Firms with the Classification of Economic Activity Rev.3 (*cae3*) equal to 70100 are considered to be head offices.


Q7. **In Sector Tables the information is available by dimension category. Which variable can I use to classify firms accordingly?**

The variable that classifies firms by dimension category is calculated according to the [Commission Recommendation 2003/361/CE, 6 May of 2003](http://ec.europa.eu/growth/smes/business-friendly-environment/sme-definition_en). This variable is available in the General Information (Cover Sheet) File: *dimcomissao*.


Q8. **Why do some firms report according to Plano Oficial de Contabilidade (POC) in 2010?**

There are a few firms reporting the financial statements using POC in 2010. These cases correspond to declarations sent in the cessation period and before or after the firm adopts a special fiscal period - a fiscal period different from calendar year (*motivodec* equals to 2, 3 or 4).


## Cover Sheet
Q1. **What is the difference between the variables *sitempresa* and *indactiecon*?**

*sitempresa* is the activity status as reported by the firm, while *indactiecon* is subject to quality control and cross checked with other sources of information besides IES. Therefore, there may be some inconsistencies between them. Please check the manual for more information on this.


## Economic and Financial Information
Q1.	**Why there is no variable available with the value of depreciation for planocont = 1 (i.e. balance sheets written according to SNC)?**

SNC is a different reporting system and, therefore, has a different scope than POC. The balance sheet written according to SNC does not have a separate item for depreciations in the balance sheet as POC did.

Q2. **A missing value means that the firm did not report the information or it may be zero?**

In the first years after IES was implemented, there were no automatic checks in place to guarantee that the firm filled in all the information. For this reason there were some variables with missing values. Over time, the criteria were adjusted and nowadays to successfully send a declaration some items have to be filled in with zero if there are no values for the variable being reported.



## Employment Information

Q1.	**Why does the variable VF03319 (number of paid and unpaid employees) take decimal values?**

Variable VF03319 takes decimal values because it is an average value: number of people employed in the last weekday of each month of the fiscal period divided by the total number of months of the fiscal period.


Q2.	**Why does the variable VF03319 (number of paid and unpaid employees) take value zero?**

This variable may take value zero in several situations. Some examples are: i) the firm only has service providers and no employees; ii) all workers are paid by another firm and so are not considered employees of the firm (i.e. the employees of the firm are temporarily working in (and therefore paid by) another firm).


## Economic and Financial Indicators
Q1. **I have a question on the measure of investment rate(*VF06041*). In particular, how is "working capital" defined? And how is total income (variable *VF05941* at the denominator) defined?**

Working capital corresponds to the sum of some assets’ items (such as Inventories, Client debts and Other operating assets) subtracted by some liabilities’ items (Cyclical operating funds).

The denominator corresponds to the sum of Sales, Provision of services, Variation in production, Capitalized production, Supplementary revenues, Operating subsidies, Operating revenues, Financial revenues, Total Extraordinary revenues minus the Cost of goods sold and material consumed, Supplies and external services, Indirect Taxes, Other operating costs, and Reduction in Provisions.

Please note that these are only the main components of the variables and not an exhaustive list of all of their components.
