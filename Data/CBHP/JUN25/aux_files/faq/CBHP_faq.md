---
title: Central Balance Sheet Harmonized Panel Data - Frequently Asked Questions
subtitle: Extraction Date - June 2025
date: 30 June 2025
doi: 10.17900/CB.CBHP.Jun2025.V1
pdf-engine: pdflatex
execute:
  echo: false
format:
  html:
    theme: default
---

## General Questions

Q1. **May I have access to variables that are not included in the harmonized panel?**

The Central Balance Sheet Harmonized Panel contains fewer variables than the Annual Data.
If you would like to compute an harmonized variable that is not made available or uses a different formula to compute an existing variable, please identify the name of the variable(s) of Central Balance Sheet Annual Dataset (for example, VF15991 (Total Assets)) and/or the Table and respective items [*table* - *item* - *column*] that you need in the [IES form](https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/modelos_formularios/decl_anual_inf_contabilistica_fiscal/Documents/IES_DANUAL_A.pdf) and include them in the variables request.

For example, in case you are interested in the SNC variable "Ativo não corrente - Ativos biológicos (Non-current Assets - Biological Assets)", you can refer to [Q04A-A5105-1]. Q04A identifies the table, A5105 is the code of the item and column 1 reports values for the current period.

![](../../attachments/extra_var.PNG)


Q2. **This data set covers the same firms than Central Balance Sheet - Annual Data?**

Yes. The exact same firms are included in the Annual Data (CB) and in the Harmonized Panel (CBHP). These data sets contain data for Portuguese non-financial corporations reporting *Informação Empresarial Simplificada* (IES, Simplified Corporate Information).


Q3. **What can explain the discontinuities identified for some harmonized variables?**

The harmonization procedure tries to ensure the compatibility of the variables over time as much as possible. However, there may be more than one harmonization methodology and the transition between the old and the new accounting rules and concepts may take some time. For these reasons, some harmonized variables may show a clear discontinuity in the transition between *Plano Oficial de Contabilidade* (POC, Official Chart of Accounts) and *Sistema de Normalização Contabilística* (SNC, Accounting Standards System).


## Cover Sheet

Q1. **What is the difference between the variables *sitempresa* and *indactiecon*?**

*sitempresa* is the activity status as reported by the firm, while *indactiecon* is subject to quality control and cross checked with some other sources of information besides IES. Therefore, there may be some inconsistencies between them. Please check the manual on Central Balance Sheet Database (CB) - Annual Data for more information on this.
