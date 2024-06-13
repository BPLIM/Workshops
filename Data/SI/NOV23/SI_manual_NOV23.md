---
title: Incentives Systems Data - Data Manual
subtitle: Extraction Date - November 2023
author: BPLIM
date: 30 November 2023
abstract: The Incentives Systems data include information for projects submitted to the incentives systems funded by the European Regional Development Fund (ERDF) within the QREN (2007-2013) framework and the European Regional Development Fund and European Social Fund (ESF) within the PT2020 (2014-2020) framework. The data include information on both approved and non-approved applications.
doi: 10.17900/SI.Nov2023.V1
pdf-engine: pdflatex
execute:
  echo: false
format:
  pdf:
    toc: true
  html:
    toc: true
    embed-resources: true
    footnotes-hover: true
    code-fold: true
    code-copy: true
    theme: default
jupyter:
  kernelspec:
    display_name: Stata
    language: stata
    name: stata
---

# General Information

> **Dataset Designation in English**: Incentives Systems (SI)

> **Dataset Designation in Portuguese**: *Sistemas de Incentivos* (SI)

> **Data Type**: Cross-section data

> **Unit of Analysis**: Projects

> **Data Organization**: The QREN data is organized in three files (see the figure below):
- General Information,
- Closure Data,
- Payment Orders.
The PT2020 data is organized in one file with General Information about the project and the promoter/beneficiary.
In all files each row corresponds to one project [^1]. All files are available in Stata format, version 17.

[^1]: For ’Payment Orders File’ available in the QREN data, there may be multiple project entries since a project may have more than one payment order. Therefore, each payment order is identified by the number of order, which is project specific.

> **Version of the data**: The data made available by BPLIM corresponds to a data freeze at a certain moment. The QREN data will no longer be subject to updates and correspond to a freeze that occurred on September 2017. The PT2020 data is updated on an annual basis and the most recent freeze occurred on December 2021. Therefore, all files contain the information as reported in the extraction date.

> **Languages Available**: Variable labels and value labels are available in Portuguese and English. [^2]

[^2]: To see the labels in English type the following command line in Stata: 'label language en'.

> **Data Producer**: [Agência para o Desenvolvimento e Coesão](https://www.adcoesao.pt/) and [Autoridade de Gestão do Programa Operacional Competitividade e Internacionalização - COMPETE 2020](https://www.compete2020.gov.pt/)

> **Access**: These data sets are also made available by [Statistics Portugal (INE)](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_main&xlang=en).

> **Digital Object Identifier**: 10.17900/SI.Nov2023.V1

![Structure of QREN Data](./images/qren_structure.png)

# Geographical Coverage
The data covers the projects submitted to the incentives systems for Mainland Portugal.

# Population
The data include the applications to the incentives systems funded by the European Regional Development Fund (ERDF) submitted within the QREN (2007-2013) framework and the European Regional Development Fund (ERDF) and European Social Fund (ESF) submitted within the PT2020 (2014-2020) framework.

# Methodology

The data include information on the two following multiannual financial frameworks within the Incentives Systems funded by the [European Regional Development Fund](https://ec.europa.eu/regional_policy/en/funding/erdf/) and the [European Social Fund](https://ec.europa.eu/esf/home.jsp):

- **QREN**, which is the National Strategic Reference Framework (*Quadro de Referência Estratégico Nacional*) governing the application of the Community Policy of economic and social cohesion in Portugal between 2007 and 2013.

- **Portugal 2020**, which is the designation of the [Partnership Agreement between the European Commission and Portugal](https://ec.europa.eu/info/publications/partnership-agreement-portugal-2014-20_en) governing the application of the European Structural and Investment Funds and considering the economic, social, territorial and environmental development policy for the period between 2014 and 2020.

The data is made available for research purposes by BPLIM under a protocol signed with [Agência para o Desenvolvimento e Coesão](https://www.adcoesao.pt/) and [Autoridade de Gestão do Programa Operacional Competitividade e Internacionalização - COMPETE 2020](https://www.compete2020.gov.pt/). The data correspond to a data freeze in a given moment. The **QREN data** report to the closure moment of QREN and the submission of the Final Declaration of Expenditure to the European Commission on September 2017. This data set will no longer be subject to any update. The **PT2020 data** refer to December 31, 2021 and will be subject to yearly updates.

The data include information about the life-cycle of all projects between the submission to the closure moments.

After receiving the data, BPLIM makes the following changes to the original data, which may justify potential differences with respect to the data made available by other data providers:

- All variables originally measured in thousand euros are converted to euros,

- All string variables are encoded to a numeric format,

- All categorical variables are attributed with value labels in Portuguese and English,

- All dates correspond to the month and year of the event and omit the day for confidentiality purposes.

## What changes in this new extraction?

This new extraction updates and replaces the data for PT2020 previously made available:

- There are three new measures included in the data Autonomous Training - Enterprises; Training Clusters - Autonomous; and Training Clusters - Joint.

- Correction to the payment variables by the data producer.

## General Concepts

In this subsection we present some of the most relevant concepts:

**Application** - Formal request for public funding summitted by the beneficiary to the Managing Authority of the Operational Programme or Intermediate Body.

**Beneficiary** - any private or public entity, a cooperative or a profit or non-profit organization fulfilling the conditions specified in the regulations of each incentive system.

**Promoter** - Beneficiary entity submitting a project.

**Call for applications** - The applications are submitted within a specific Call for Proposals. The Call is the announcement of a tender and specifies the requirements that the applications should meet to receive funding within a certain Operational Programme. The call includes information about the deadlines to present the proposals, selection conditions, the available budget, the intervention typology, and the region (when applicable).

**Intermediate body** - Public or private body in which the managing authority delegated competences and that may fulfill some tasks with respect to the beneficiaries that implement the operations.


For a more detailed description of the main definitions please see [QREN glossary](http://www.pofc.qren.pt/glossario), [PT2020 glossary](https://portugal2020.pt/glossario-lista/), and Article 2 of the [Regulation (EU) No 1303/2013](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32013R1303&from=en).

# Description of Files
The data is organized in one file for each incentives system and type of information:

| Incentives system | Type of information | File Name |
| :-------: | :------- | :---------------------------------------------------------- |
| QREN | General information | QREN_A_MPRJ_20072013_*eeee*_GERAL_V01 |
| QREN | Closure Data | QREN_A_MPRJ_20072013_*eeee*_INVESTENC_V01 |
| QREN | Payment Orders | QREN_A_MPRJ_20072013_*eeee*_PAGAMENTOS_V01 |
| | | |
| PT2020 | General information | PT2020_A_MPRJ_20142021_*eeee*_GERAL_V01 |

where *A* stands for anonymized, *MPRJ* represents monthly project level data, and *eeee* reports the extraction date. The extraction date is April 2021 (APR21) for QREN data and November 2023 (NOV23) for PT2020 data.

Labels and value labels were attributed to all categorical variables. All datasets are anonymized.

<br>

# Description of Variables

Below we provide a general description of the variables included in the data.[^5] For a full account of all variable categories see the [“Auxiliary Files” section](#auxiliary-files).

[^5]: There are other variables available, such as promoter and project characteristics that are excluded from the data, but may be made available upon request (bplim@bportugal.pt).

## QREN

### General information

This file provides information about the promoter and the project, such as the amount of investment, incentives and project type.

#### A1. Identifiers

`Number of the project anonymized` (*nproja*) - Unique anonymized identifier of the project.

<br>
<br>

`Firm identifier` (*tina_promotor*) – Unique identifier of the project promoter/beneficiary, which corresponds to the anonymized tax identification number. [^6]

[^6]: The anonymized tax identification number preserves the first digit of the tax identification number. This first digit contains relevant information about the type of firm: 1,2 or 3-natural person (*pessoa singular*); 5-private corporation (*pessoa colectiva*); 6-public corporation (*pessoa colectiva pública*); 7-other miscellaneous cases; 9- irregular corporation (*pessoa colectiva irregular*).

<br>
<br>

#### A2. Project characteristics

`Date of the application` (*datacand*) - Month and year in which the beneficiary submitted the funding application.

<br>
<br>

`Incentive System` (*med*) - Incentive system to which the project was submitted. The data include projects submitted to specific measures of three Incentives Systems: i) Incentives System for Research and Technological Development, ii) Innovation Incentives System, and iii) Qualification and Internationalization of Small and Medium Enterprises.

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1	| 1 SI I&DT	| 1 R&D Incentives System |
| 2	| 2 SI Inovação	| 2 Innovation Incentives System |
| 3 | 3 SI Qualificação PME	| 3 Qualification Incentives System for SMEs |

<br>
<br>

`Measure` (*medida*) - Specific measure within the respective incentives system in which the project is considered.

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1 | 1 1.2.1.1 - I&DT Empresas/Projectos Individuais | 1 1.2.1.1 – Enterprise R&D/Individual Projects |
| 2 | 2 1.2.1.2 - I&DT Empresas/Projectos em Co-promoção | 2 1.2.1.2 – Enterprise R&D/Projects in Co-promotion |
| 3 | 3 1.2.1.3 - I&DT Empresas/Projectos Mobilizadores | 3 1.2.1.3 – Enterprise R&D/Mobilizing Projects |
| 4 | 4 1.2.1.4 - I&DT Empresas/Vale I&DT | 4 1.2.1.4 – Enterprise R&D/R&D Voucher |
| 5 | 5 1.2.1.5 - I&DT Empresas/Projectos Individuais/Regime Especial | 5 1.2.1.5 – Enterprise R&D/Individual Projects/Special Regime |
| 6 | 6 1.2.1.6 - I&DT Empresas/Projectos em Co-promoção/Regime Especial | 6 1.2.1.6 – Enterprise R&D/Projects in Co-promotion/Special Regime |
| 7 | 7 1.2.2 - I&DT Colectiva | 7 1.2.2 – Collective R&D |
| 8 | 8 1.2.3.1 - Criação e Reforço de competências Internas de I&DT/Núcleos de I&DT | 8 1.2.3.1 – Creation and Reinforcement of R&D internal competences/R&D Core Units |
| 9 | 9 1.2.3.2 - Criação e Reforço de competências Internas de I&DT/Centros de I&DT | 9 1.2.3.2 – Creation and Reinforcement of R&D internal competences/R&D Centres |
| 10 | 10 1.2.4.1 - Valorização de I&DT/Projectos Demonstradores | 10 1.2.4.1 – Valorization of R&D/Demonstrative Projects |
| 11 | 11 2.1.1 - SI Inovação/Inovação Produtiva | 11 2.1.1 – Innovation Incentive System/Productive Innovation |
| 12 | 12 2.1.2 - SI Inovação/Projectos do Regime Especial | 12 2.1.2 – Innovation Incentive System/Special Regime Projects |
| 13 | 13 2.1.3 - SI Inovação/Projectos de Interesse Estratégico | 13 2.1.3 – Innovation Incentive System/Strategic Interest Projects |
| 14 | 14 2.1.4 - SI Inovação/Empreendedorismo Qualificado | 14 2.1.4 - Innovation Incentive System/Qualified Entrepreneurship |
| 15 | 15 2.2.1 - SI Qualificação PME/Projectos Individuais e de Cooperação | 15 2.2.1 - Qualification Incentives System for SME’s/Individual and Cooperative Projects |
| 16 | 16 2.2.2 - SI Qualificação PME/Projectos Conjuntos | 16 2.2.2 - Qualification Incentives System for SME’s/Joint Projects |
| 17 | 17 2.2.3 - SI Qualificação PME/Vale Inovação | 17 2.2.3 - Qualification Incentives System for SME’s/Innovation Voucher |
| 18 | 18 2.3 - Projectos transitados do QCA III | 18 2.3 – Transferred Projects from CSF III |

<br>
<br>

`Managing Authority` (*autoridadegestao*) - Public authority at a national, regional or local level or a public or private body designated by the member-state to manage the Operational Programme (*OP*).

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1 | 1 PO Alentejo | 1 OP Alentejo |
| 2 | 2 PO Algarve | 2 OP Algarve |
| 3 | 3 PO Centro | 3 OP Centre |
| 4 | 4 PO Factores de Competitividade | 4 OP Thematic Factors of Competitiveness |
| 5 | 5 PO Lisboa | 5 OP Lisbon |
| 6 | 6 PO Norte | 6 OP North |

The data only covers the projects submitted to the regional Operational Programmes of Mainland Portugal and the [Operational Programme "Thematic Factors of Competitiveness" (TFC)](https://ec.europa.eu/regional_policy/en/atlas/programmes/2007-2013/portugal/operational-programme-thematic-factors-of-competitiveness). According to the [Decree-Law no 312/2007, 17 September](https://dre.pt/pesquisa/-/search/640354/details/maximized) each regional operational programme of Mainland Portugal covers the respective NUTS II (Nomenclature of territorial units for statistics) region and are co-funded by the European Regional Development Fund (ERDF). The Operational Programme "Thematic Factors of Competitiveness" is also co-funded by ERDF and covers the NUTS II regions of Norte, Centro and Alentejo.

<br>
<br>

`Project status` (*estado*) - Categorical variable with information about the project status. The project lifecycle includes several steps: the applications are firstly analysed by the Intermediate Body that issues a report to be sent to the Selection Committee [^4]. After the decision to support the project is taken, the promoters sign the incentives contract and start implementing the project. After the implementation, the promoters request the closure of the investment and the project. The status are defined according to the table below:

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1 | 1 Com Decisão - não Apoiado | 1 With a decision – not supported |
| 2 | 2 Com Encerramento de Investimento | 2 With Investment Closure |
| 3 | 3 Com Encerramento de Projecto | 3 With Project Closure |
| 4 | 4 Em Análise - sem Parecer ORG | 4 Under analysis – without the Intermediate Body report |
| 5 | 5 Em CS - com Parecer ORG, sem CS | 5 In Selection Committee (SC) – with Intermediate Body report, no SC |
| 6 | 6 Em Decisão - com CS, sem Decisão | 6 Under decision – with Selection Committee, without Decision |
| 7 | 7 Em Execução - com Contrato, sem OP emitidas | 7 Under implementation – with contract, without payment orders issued |
| 8 | 8 Em Execução - com OP emitidas, sem Encerramento | 8 Under implementation – with payment orders issued, without closure |
| 9 | 9 Por Contratar - com Decisão, sem Contrato | 9 Not yet contracted – with a decision, without contract |

**Comments:** The supported projects that do not have investment and project closure at the time of the data freeze correspond mostly to projects that were withdrawn/decommitted.

[^4]: The Selection Committee issues opinions about the opening of new tenders and about the proposals for funding decisions.

<br>
<br>

`Decision` (*decisao*) - Decision about the eligibility of the application for funding. Among the eligible applications there may be some non-selected due to the total budget available.

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1 | 1 Elegível | 1 Eligible |
| 2 | 2 Elegível Não Seleccionado | 2 Eligible, not selected |
| 3 | 3 Não Elegível | 3 Not eligible |
| 4 | 4 Não Enquadrável | 4 Out of scope |

<br>
<br>

`Project score` (*pontuacao*) - Score attributed to the project based on the formula announced in the Call for Applications.

**Comments:** Some projects may have scores above 5 due to the specificities in the selection methodology as presented in the Call for Applications. For example, in the case of simplified projects, such as vouchers, the criteria to order the applications may correspond to the number of employees.

<br>
<br>

`Non-eligibility due to scoring below the minimum required` (*nepontuacao*) - Dummy variable taking value one if the project was considered to be not eligible due to having a score below the minimum required. This variable takes value zero if the non-eligibility is related to other reasons.

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 0	| 0 Não	| 0 No |
| 1 |	1 Sim	| 1 Yes |

<br>
<br>

`Decommitment / Withdrawal` (*dstanl*) - Categorical variable that signals whether the project was decommitted or withdrawn. While the withdrawal occurs before the funding decision at the initiative of the beneficiary, the decommitment occurs after the funding decision at the initiative of the beneficiary or the Operational Programme.

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1	| 1 Anulação | 1 Decommitment |
| 2 |	2 Desistência	| 2 Withdrawal |

<br>
<br>

`Application Investment` (*investcand*) - All the eligible co-funded and not co-funded and the non-eligible expenses necessary to attain the goals of the project foreseen in the application. This variable is measured in euros.

<br>
<br>

`Date of the first decision` (*data1decisao*) - Date of the first decision about the application.

<br>
<br>

`Date of the first communication` (*data1comunicacao*) - Date of the first communication of the decision to the applicant.

<br>
<br>

`Date of the contract` (*datacontrato*) - Date of the formalization of the written contract that defines the terms of the project's funding.

<br>
<br>

`Number of the last decision` (*nultimadecisao*) - This variable indicates the number of decisions taken regarding the project and the one with effect at the data freeze. In the project life cycle, the initial decision may have to be adjusted to accommodate changes to the financial or time schedule, for example.

<br>
<br>

`Date of the last decision` (*dataultdec*) - Date in which the last decision related to the project was taken.

<br>
<br>

`Contracted incentive – ERDF` (*incentivocontratadofeder*) - Amount of the incentive funded by the European Regional Development Fund (ERDF) as defined in the incentives contract. This variable is measured in euros.

<br>
<br>

`Date of the investment closure` (*dataencerraminvestimento*) - Date of the investment closure.

<br>
<br>

`Closed incentive – ERDF` (*incentivoencerrado*) - Total amount of the incentive funded by the European Regional Development Fund of a closed project or a project with closed investment. This variable is measured in euros.

<br>
<br>

`Date of the project closure` (*dataencerramprojeto*) - Date of the project closure.

<br>
<br>

`Total Investment` (*investimentototal*) - All the effective eligible co-funded and not co-funded and the non-eligible expenses necessary to attain the goals of the project. This variable is measured in euros.

<br>
<br>

`Total eligible investment` (*investimentoelegiveltotal*) - All the expenses necessary to implement the project that follow the national and Community rules and are eligible for Community co-funding. This variable is measured in euros.

<br>
<br>

`Total Incentive (ERDF + National Funds)` (*incentivototalfederfundos*) - Total amount funded by the European Regional Development Fund and national funds. This variable is measured in euros.

<br>
<br>

`ERDF incentive` (*incentivofeder*) - Total amount, measured in euros, funded by the European Regional Development Fund.

<br>
<br>

`Non-repayable incentive` (*incentivonaoreembolsavel*) - Non-repayable grants paid to the beneficiary upon the fulfillment of the goals defined in the contract. This variable is measured in euros.

<br>
<br>

`Repayable incentive` (*incentivoreembolsavel*) - Interest-free loan (temporary financial support) granted to the beneficiary that will be subject to reimbursement according to the timeline of the project previously agreed upon. This variable is measured in euros.

<br>
<br>

`Investment in training` (*investimentoemformacao*) - Total amount of eligible co-funded and not co-funded and the non-eligible expenses in training. This variable is measured in euros.

<br>
<br>

`Eligible investment in training` (*investimentoelegivelforma*) - Amount of investment in training that is eligible for the Community co-funding. This variable is measured in euros.

<br>
<br>

`Training incentive` (*incentivoformacao*) - Amount allocated to training, measured in euros, co-funded by Community or national funds.

<br>
<br>

`Total Public Expenditure` (*despesapublica*) - Total amount corresponding to the public participation on the project funding including that from the State budget, Social Security budget, local or regional authorities and public bodies budget or the European Structural and Investment Funds. This variable is measured in euros.

<br>
<br>

`Achievement bonus` (*premio*) - Bonus attributed to projects within the Innovation Incentives System. This bonus represents the conversion of a refundable incentive into a non-refundable one and it is attributed upon the (total or partial) fulfillment of certain goals established at the decision moment. This variable is measured in euros.

<br>
<br>

`Implementation of the certified and eligible expenditure` (*execdespesaelegcertif*) - Expenses incurred in an approved project that are presented for reimbursement and are certified by the Certification Authority [^7] as being eligible and justified by invoices, receipts or equivalent accounting documents. This variable is measured in euros.

[^7]: The Certification Authority is a public body designated by the Member State to certify the expenditure declarations and the payment requests before these are sent to the European Commission.

<br>
<br>

`Implementation of the total public expenditure` (*execdespesapublica*) - It corresponds to the total public expenditure that is implemented in the approved project. This variable is measured in euros.

<br>
<br>

`Implementation of the incentive` (*execincentivo*) - It corresponds to the amount of the incentive that is implemented. This variable is measured in euros.

<br>
<br>

`Total payments` (*pagamentostotais*) - Total amount of direct transfers to the beneficiaries corresponding to reimbursement or advance payments. This variable is measured in euros.

<br>
<br>

`Pending payment orders` (*ordenspagpendentes*) - Amount of the pending payment orders measured in euros.

<br>
<br>

`With Final Reimbursement Payment` (*comptrf*) - This variable takes value one if the final reimbursement payment of the eligible investment expenses has already been made and a missing value otherwise.

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1 |	1 Sim	| 1 Yes |

<br>
<br>

### Closure Data

This file provides information about the total and the eligible investment disaggregated by year.

#### B1. Identifiers

`Number of the project anonymized` (*nproja*) - Unique anonymized identifier of the project.

<br>
<br>

#### B2. Investment variables

The remaining variables represent the annual amount of investment (*invest*) and annual eligible investment (*elegivel*) measured in euros [^9]:

| Variable Name | Type of Information | Reference date |
| :----: | :------------: | :---: |
| *invest_antes2007* | Total investment | before 2007 |
| *elegivel_antes2007* | Eligible investment | before 2007 |
| *invest_2007* | Total investment | 2007 |
| *elegivel_2007* | Eligible investment | 2007 |
| *invest_2008* | Total investment | 2008 |
| *elegivel_2008* | Eligible investment | 2008 |
| *invest_2009* | Total investment | 2009 |
| *elegivel_2009* | Eligible investment | 2009 |
| *invest_2010* | Total investment | 2010 |
| *elegivel_2010* | Eligible investment | 2010 |
| *invest_2011* | Total investment | 2011 |
| *elegivel_2011* | Eligible investment | 2011 |
| *invest_2012* | Total investment | 2012 |
| *elegivel_2012* | Eligible investment | 2012 |
| *invest_2013* | Total investment | 2013 |
| *elegivel_2013* | Eligible investment | 2013 |
| *invest_2014* | Total investment | 2014 |
| *elegivel_2014* | Eligible investment | 2014 |
| *invest_2015* | Total investment | 2015 |
| *elegivel_2015* | Eligible investment | 2015 |
| *invest_2016* | Total investment | 2016 |
| *elegivel_2016* | Eligible investment | 2016 |

[^9]: The variables for the reference years of 2017, 2018 and posterior to 2018 take value zero for all observations and are, therefore, dropped from the data.

<br>
<br>
<br>
<br>

### Payment Orders

This file provides detailed information on the payment orders for each approved project.

#### C1. Identifiers

`Number of the project anonymized` (*nproja*) - Unique anonymized identifier of the project.

<br>
<br>

`Anonymized Tax Identification Number of the promoter` (*tina_promotor*) –  Unique identifier of the project promoter, which corresponds to the anonymized tax identification number.

<br>
<br>

`Anonymized Tax Identification Number of the beneficiary` (*tina_beneficiario*) -  Unique identifier of the project beneficiary, which corresponds to the anonymized tax identification number. [^6]

<br>
<br>

`Number of the payment order within the project` (*id*) - Sequential number attributed to each payment order within each project.

<br>
<br>


#### C2. Payment orders characteristics

`Date of the payment order` (*dataordem*) - Date of the payment order.

<br>
<br>

`Effective date of the payment` (*dataefectivapagam*) - Effective date of the payment.

<br>
<br>

`Value date of the payment` (*datavalorpagam*) - Date in which the payment is available to the beneficiary.

<br>
<br>

`Total payment` (*pagamentototal*) - Amount, in euros, of the direct transfer to the beneficiary.

<br>
<br>

`Type of payment` (*tipopagamento*) - Categorical variable to identify the type of the payment.

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1 | 1 Adiantamento | 1 Advance payment |
| 2 | 2 Correcção | 2 Correction |
| 3 | 3 Devolução | 3 Return |
| 4 | 4 Estorno | 4 Reversal |
| 5 | 5 Reembolso Final | 5 Final reimbursement |
| 6 | 6 Reembolso Intercalar | 6 Interim reimbursement |

<br>
<br>

`Sub-type of payment` (*subtipo*) - Categorical variable to identify the sub-type of the payment.

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1	| 1 30 Dias	| 1 30 days |
| 2 | 2 Anulação | 2 Decommitment |
| 3	| 3 Com Isenção de Garantia	| 3 With Guarantee Exemption |
| 4	| 4 Contra Contrato/TA | 4 Against contract/grant agreement |
| 5	| 5 Contra Despesa | 5 Against expenditure |
| 6 | 6 Contra Garantia | 6 Counter-guarantee |
| 7 | 7 Encerramento | 7 Closure |
| 8 | 8 Outros | 8 Others |

<br>
<br>

`Situation of the payment order` (*situacao*) - Situation of the payment order, which can be paid or pending, at the moment of the data freeze.

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1	| 1 Paga | 1 Paid |
| 2 | 2 Pendente | 2 Pending |

<br>
<br>
<br>
<br>

## PT2020

### General information

The general information file provides a set of variables characterizing the promoter and the project.

#### D1. Identifiers
`Anonymized operation code` (*codopa*) - Unique anonymized identifier of the operation.

<br>
<br>

`Firm identifier` (*tina*) – Unique identifier of the applicant, which corresponds to the anonymized tax identification number. [^6]

<br>
<br>

### D2. Project characteristics

`Date of the application` (*datacand*) - Month and year in which the beneficiary submitted the funding application.

<br>
<br>

`European structural and investment fund` (*fundo*) - Categorical variable with information about the European Structural and Investment Fund of the investment priority considered in the application: the European Regional Development Fund or the European Social Fund.

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1	| 1 Fundo Europeu de Desenvolvimento Regional	| 1 European Regional Development Fund |
| 2 | 2 Fundo Social Europeu | 2 European Social Fund |

<br>
<br>

`Incentive System` (*instrumento*) - Incentives system to which the project was submitted. The data include projects submitted to specific measures of four Incentives Systems (instruments): i) Autonomous Training, ii) Enterprise R&D Incentive System, iii) Innovation Incentive System, and iv) Incentive System for the Qualification and Internationalization of SMEs.

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1	| 1 Formação Autónoma	| 1 Autonomous Training |
| 2	| 2 Sistema de Incentivos à I&D Empresarial	| 2 Enterprise R&D Incentive System |
| 3	| 3 Sistema de Incentivos à Inovação Empresarial | 3 Innovation Incentive System |
| 4 | 4 Sistema de Incentivos à Qualificação e Internacionalização de PME | 4 Incentive System for the Qualification and Internationalization of SMEs |

<br>
<br>

`Measure` (*medida*) - Specific measure within the respective incentives system in which the operation is considered.

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1 | 01 ADAPTAR PME | 01 ADAPTAR PME |
| 2 | 02 Formação Autónoma | 02 Autonomous Training |
| 3 | 03 Formação-Ação para PME | 03 Training-action for SME |
| 4 | 04 I&D - Copromoção - COVID-19 | 04 R&D – Co-development - COVID-19 |
| 5 | 05 I&D - Individuais - COVID-19 | 05 R&D - Individual – COVID-19 |
| 6 | 06 I&D - Infraestruturas de Ensaio e Otimização - COVID-19 | 06 R&D – Testing and Optimization Infrastructures (upscaling) – COVID 19 |
| 7 | 07 I&DT - Copromoção | 07 TR&D – Co-development |
| 8 | 08 I&DT - Copromoção - RCI | 08 TR&D – Co-development - Contractual investment regime |
| 9 | 09 I&DT - Demonstradores Copromoção | 09 TR&D – Co-development demonstrators |
| 10 | 10 I&DT - Demonstradores Individuais | 10 TR&D – Individual demonstrators |
| 11 | 11 I&DT - Individuais | 11 TR&D – Individual |
| 12 | 12 I&DT - Individuais - RCI | 12 TR&D – Individual – Contractual investment regime |
| 13 | 13 I&DT - Internacionalização | 13 TR&D – Internationalization |
| 14 | 14 I&DT - Núcleos Copromoção | 14 TR&D – Co-development centers |
| 15 | 15 I&DT - Núcleos Individuais | 15 TR&D – Individual centers |
| 16 | 16 I&DT - Programas Mobilizadores | 16 TR&D – Mobiliser programmes |
| 17 | 17 I&DT - Propriedade Industrial | 17 TR&D – Industrial Property |
| 18 | 18 I&DT - Vales | 18 TR&D – Vouchers |
| 19 | 19 Inovação -  Produtiva - COVID-19 | 19 Innovation -  Productive - COVID-19 |
| 20 | 20 Inovação - Empreendedorismo | 20 Innovation – Entrepreneurship |
| 21 | 21 Inovação - Produtiva | 21 Innovation – Productive |
| 22 | 22 Inovação - RCI | 22 Innovation – Contractual investment regime |
| 23 | 23 Inovação - Vales | 23 Innovation – Vouchers |
| 24 | 24 QI PME - Conjuntos | 24 QI SME – Joint |
| 25 | 25 QI PME - Individuais | 25 QI SME – Individual |
| 26 | 26 QI PME - Vales | 26 QI SME – Vouchers |
| 27 | 27 Formação Autónoma - Empresas | 27 Autonomous Training - Enterprises |
| 28 | 28 Formação Clusters - Autónomos | 28 Training Clusters - Autonomous |
| 29 | 29 Formação Clusters - Conjuntos | 29 Training Clusters - Joint |

<br>
<br>

`Year of the call for applications` (*ano_aac*) - Year of the call for applications.

<br>
<br>

`Operational programme` (*pofinan*) - Operational Programme to which the project is submmitted.

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1 | 1 PO Alentejo | 1 OP Alentejo |
| 2 | 2 PO Algarve | 2 OP Algarve |
| 3 | 3 PO Competitividade e Internacionalização | 3 OP Competitiveness and Internationalization |
| 4 | 4 PO Centro | 4 OP Centre |
| 5 | 5 PO Lisboa | 5 OP Lisbon |
| 6 | 6 PO Norte | 6 OP North |

The data only covers the projects submitted to the regional Operational Programmes of Mainland Portugal and the [Operational Programme "Competitiveness and Internationalization"](https://www.compete2020.gov.pt/documentacao/detalhe/POCI-vrs-adaptada).

<br>
<br>

`Thematic Objective` (*ot*) - Thematic Objective as defined by the Article 9 of the [Regulation (EU) No 1303/2013](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32013R1303&from=pt). The data cover three thematic objectives: i) Strengthening research, technological development and innovation, ii) Enhancing the competitiveness of small and medium-sized enterprises, and iii) Promoting sustainable and quality employment and supporting labour mobility.

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1 | 1 OT 1 - Reforçar a investigação, o desenvolvimento tecnológico e a inovação | 1 TO 1 – Strengthening research, technological development and innovation |
| 2 | 2 OT 3 - Reforçar a competitividade das pequenas e médias empresas | 2 TO 3 – Enhancing the competitiveness of small and medium-sized enterprises |
| 3 | 3 OT 8 – Promover a sustentabilidade e a qualidade do emprego e apoiar a mobilidade laboral | 3 TO 8 – Promoting sustainable and quality employment and supporting labour mobility |

<br>
<br>

`Investment priority` (*pi*) - Categorical variable corresponding to a higher disaggregation level of the *Thematic Objective* (*ot*). For the complete description of each investment priority please see the [Partnership Agreement 2014-2020 (available in Portuguese)](https://portugal2020.pt/wp-content/uploads/1._ap_portugal_2020_28julho_0.pdf).

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1 | 1 PI 1.2 - Promoção do investimento das empresas em inovação e investigação | 1 IP 1.2 - Promoting enterprise investment in innovation and research |
| 2 | 2 PI 3.1 - Promoção do espírito empresarial | 2 IP 3.1 - Promoting entrepreneurship |
| 3 | 3 PI 3.2 - Desenvolvimento e aplicação de novos modelos empresariais para as PME | 3 IP 3.2 - Development and application of new business models for SMEs |
| 4 | 4 PI 3.3 - Apoio à criação e alargamento de capacidades avançadas de desenvolvimento de produtos e serviços | 4 IP 3.3 - Supporting the creation and extension of advanced capabilities in the development of products and services |
| 5 | 5 PI 8.5 - Adaptação de trabalhadores, empresas e empresários à mudança | 5 IP 8.5 - Adaptability of workers, enterprises and entrepreneurs to change |

<br>
<br>

`Intervention typology` (*ti*) - Categorical variable with information about the intervention typology, which aggregates specific objectives of the same type within a given investment priority (*pi*).

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1 | 1 TI 47 – Atividades de I&D empresarial | 1 TI 47 – Corporate R&D activities |
| 2 | 2 TI 49 – Investimento empresarial em inovação de não PME | 2 TI 49 – Corporate investment in innovation of non-SME  |
| 3 | 3 TI 51 – Empreendedorismo qualificado e criativo | 3 TI 51 – Qualified and creative entrepreneurship |
| 4 | 4 TI 52 – Internacionalização das PME | 4 TI 52 – Internationalization of SMEs |
| 5 | 5 TI 53 – Qualificação e inovação das PME | 5 TI 53 – Qualification and innovation of SMEs |
| 6 | 6 TI 60 - Formação de empresários e trabalhadores das empresas | 6 TI 60 – Training of entrepreneurs and employees |
| 7 | 7 TI B7 – CRII – Atividades de I&D Empresarial | 7 TI B7 – CRII – Corporate R&D activities |
| 8 | 8 TI B8 - CRII - Investimento empresarial em inovação de não PME | 8 TI B8 - CRII – Corporate investment in innovation of non-SME |
| 9 | 9 TI B9 – CRII – Qualificação e inovação das PME | 9 TI B9 – CRII – Qualification and innovation of SMEs |

<br>
<br>

`Source of the data` (*fonte*) - Categorical variable with information about the source of the data. The data is reported in two different information systems: SGO - COMPETE 2020 Information System (*Sistema de Informação do COMPETE 2020*) and SIFSE - Integrated System of the European Social Fund (*Sistema Integrado do Fundo Social Europeu*). SIFSE covers some operations within the investment priority 8.5 and has fewer variables available.

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1 |	1 SGO	| 1 SGO |
| 2 | 2 SIFSE	| 2 SIFSE |

<br>
<br>

`Funded project` (*apoiado*) - Dummy variable taking value one in case the operation was supported and zero otherwise. When this variable is not reported the final decision about the application was not yet taken at the moment of the data freeze.

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 0	| 0 Não	| 0 No |
| 1 | 1 Sim	| 1 Yes |

<br>
<br>

`Active project` (*nprojaprov*) - Dummy variable that takes value one if the project is active and zero otherwise (for example, if the funded operation was subject to withdrawal or decommitment).

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 0	| 0 Não	| 0 No |
| 1 | 1 Sim	| 1 Yes |

<br>
<br>

`Decommitment / Withdrawal` (*dstanl*) - Categorical variable that signals whether the project was decommitted or withdrawn. While the withdrawal occurs before the funding decision at the initiative of the beneficiary, the decommitment occurs after the funding decision at the initiative of the beneficiary or the Operational Programme.

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1	| 1 Anulação | 1 Decommitment |
| 2 | 2 Desistência | 2 Withdrawal |

<br>
<br>

`Project score` (*pontuacao*) - Score attributed to the project based on the formula announced in the Call for Applications.

<br>
<br>

`Date of approval` (*data_aprov*) - Date of the decision on the application's approval.

<br>
<br>

`Date of the last decision` (*dataultdec*) - Date in which the last decision related to the operation was taken.

<br>
<br>

`Project with grant agreement` (*comta*) - Dummy variable taking value one if the operation has a grant agreement, which corresponds to the commitment taken by the beneficiary to implement the operation according to the conditions defined in the decision of approval, including the obligations and the consequences of non-compliance.

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 0	| 0 Não	| 0 No |
| 1 | 1 Sim	| 1 Yes |

<br>
<br>

`Date of the grant agreement/contract` (*datatermoaceit*) - Date of the formalization of the written document (grant agreement or contract) that establishes the funding conditions.

<br>
<br>

`Application investment` (*investcand*) - All the eligible co-funded and not co-funded and the non-eligible expenses necessary to attain the goals of the operation foreseen in the application. This variable is measured in euros.

<br>
<br>

`Contracted incentive` (*incentivocontrat*) - Amount of the incentive funded by the European Regional Development Fund (ERDF) or the European Social Fund (ESF) as defined in the incentives contract. This variable is measured in euros.

<br>
<br>

### D3. - Variables at the decision moment

The variables below report to the moment of the decision about the application:

`Date of project start (predicted at the decision date)` (*dec_datainiproj*) - Expected date for the beginning of the operation at the decision moment or at the date of the grant agreement. The date of project start corresponds to the date of investment start.

<br>
<br>

`Date of project end (predicted at the decision date)` (*dec_datafimproj*) - Expected date for the end of the project upon the decision moment or at the grant agreement. The date of project end corresponds to the date of investment completion.

<br>
<br>

`Approved investment (at the decision date)` (*dec_investaprov*) - Total investment that was approved at the decision moment. This variable is measured in euros.

<br>
<br>

`Eligible approved investment (at the decision date)` (*dec_investeleg*) - Total eligible expenses approved to be considered for Community co-funding at the decision moment. This variable is measured in euros.

<br>
<br>

`Approved public expenditure (at the decision date)` (*dec_despesapublica*) - It corresponds to the total public expenditure approved at the moment of the decision about the application. This variable is measured in euros.

<br>
<br>

`Approved incentive (at the decision date)` (*dec_incentivoaprov*) - Total amount of the incentive approved at the moment of the decision. This variable is measured in euros.

<br>
<br>

`Repayable incentive (at the decision date)` (*dec_incentivoreemb*) - Interest-free loan (temporary financial support) granted to the beneficiary that will be subject to reimbursement according to the timeline of the operation. This variable is measured in euros and reports to the decision moment.

<br>
<br>

`Non-repayable incentive (at the decision date)` (*dec_incentivonaoreemb*) - Non-repayable grants paid to the beneficiary upon the fulfillment of the goals. This variable is measured in euros and reports to the decision moment.

<br>
<br>

### D4. - Variables at the closure moment

The following variables report to the moment of project closure:

`Date of the project closure approval` (*dataenc*) - Date of the project closure.

<br>
<br>

`Closed project` (*comenc*) - Dummy variable taking value one if the operation is closed and zero otherwise.

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 0	| 0 Não	| 0 No |
| 1 | 1 Sim	| 1 Yes |

<br>
<br>

`Date of project start (at the closure date)` (*enc_datainiproj*) - Date of the operation start reported at the moment of project closure.

<br>
<br>

`Date of project end (at the closure date)` (*enc_datafimproj*) - Date of the operation closure.

<br>
<br>

`Approved investment (at the closure date)` (*enc_investaprov*) - Total approved investment as reported at the date of the operation closure. This variable is measured in euros.

<br>
<br>

`Eligible approved investment (at the closure date)` (*enc_investeleg*) - Total eligible expenses approved and considered for Community co-funding at the operation closure date. This variable is measured in euros.

<br>
<br>

`Approved public expenditure (at the closure date)` (*enc_despesapublica*) - It corresponds to the approved public expenditure at the operation closure date. This variable is measured in euros.

<br>
<br>

`Approved incentive (at the closure date)` (*enc_incentivoaprov*) - Total amount of the incentive approved reported at the date of the operation closure. This variable is measured in euros.

<br>
<br>

`Repayable incentive (at the closure date)` (*enc_incentivoreemb*) - Interest-free loan (temporary financial support) granted to the beneficiary that will be subject to reimbursement according to the timeline of the project previously agreed upon. This variable is measured in euros and reports to the operation closure date.

<br>
<br>

`Non-repayable incentive (at the closure date)` (*enc_incentivonaoreemb*) - Non-repayable grants paid to the beneficiary upon the fulfillment of the goals. This variable is measured in euros and reports to the operation closure date.

<br>
<br>

### D5. - Variables at the execution moment

The following variables report to the execution of the operation:

`Project in implementation` (*comexecucao*) - Dummy variable taking value one if the operation is in implementation and zero otherwise.

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 0	| 0 Não	| 0 No |
| 1 | 1 Sim	| 1 Yes |

<br>
<br>

`Implemented eligible investment` (*exec_investeleg*) - Amount of the eligible investment that is already implemented. This variable is measured in euros.

<br>
<br>

`Implemented public expenditure` (*exec_despesapublica*) -  It corresponds to the total public expenditure (European Investment Funds and other sources) already implemented. This variable is measured in euros.

<br>
<br>

`Implemented incentive/fund` (*exec_incentivofundo*) - It corresponds to the incentive that is already implemented. This variable is measured in euros.

<br>
<br>

`Other source(s) of funding implemented` (*exec_outrasfontesfinanc*) - It corresponds to other sources of funding other than the European Investment Funds that are already implemented. This variable is measured in euros.

<br>
<br>

### D6. - Payments

The payment requests are presented by the beneficiaries to the Managing Authority that approved the operation. The payments are direct transfers to the beneficiaries and there are two payment types: advance and refund payments.

`Project with payments` (*compagamentos*) - Dummy variable taking value one in case there were payments already issued and zero otherwise.

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 0	| 0 Não	| 0 No |
| 1 | 1 Sim	| 1 Yes |

<br>
<br>

`Total payments` (*totpagam_realizado*) - Total amount of the payments issued.

<br>
<br>

`Refund payments` (*pagamentos_reembolso*) - Total amount of refund payments, which include the expenses paid by the beneficiaries and validated by the Managing Authority or the Intermediate Body.

<br>
<br>

`Certifiable advance payments` (*pagadiantcertif*) - Amount of advance payments paid to the beneficiaries by the paying entity or the intermediate bodies as long as it is supported by a bank guarantee.

<br>
<br>

`Non-certifiable advance payments` (*pagadiantnaocertif*) - Amount of advance payments to the beneficiaries that do not fulfill the requirements of the expenditure statements submitted to the European Commission.

<br>
<br>
<br>
<br>

# Basic Descriptive Statistics

Table 1 - QREN: Distribution of applications by Incentives System (as of April 2021 extraction)

```{stata}
*| output: asis
*| echo: false
set linesize 200
local extraction="2021_04"
local ref="APR21"
local startyr=2007
local finyear=2013
local version="V01"
quietly use "S:/data/Products/INCENTIVOS/QREN/`extraction'/Output/Data/QREN_I_MPRJ_`startyr'`finyear'_`ref'_GERAL_`version'.dta", clear
label language en
format %75.0f med
```

```{stata}
*| scrolled: true
groups med, show(f)
```

Table 2 - PT2020: Distribution of applications by Incentives System (as of November 2023 extraction)

```{stata}
*| output: asis
*| echo: false
local extraction="2023_11"
local ref="NOV23"
local startyr=2014
local finyear=2020
local version="V01"
quietly use "S:/data/Products/INCENTIVOS/PT2020/`extraction'/Output/Data/PT2020_I_MPRJ_`startyr'`finyear'_`ref'_GERAL_`version'.dta", clear
label language en
format %75.0f instrumento
```

```{stata}
groups instrumento, show(f)
```

# Legislation

Some selected legislation governing the European Structural and Investment Funds is presented below:

- **Notice No. 2006/C 323/1**, December 30 – defines the Community Framework for State aid for Research and Development and Innovation.

  [Internal Link](./aux_files/legislation/Notice_2006_C_323_01_ec.pdf) /
  [External Link](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:52006XC1230(01)&from=EN)

- **Resolution of the Council of Ministers No. 86/2007**, July 3 – approves and presents the National Strategic Reference Framework (QREN, *Quadro de Referência Estratégico Nacional*), for the period 2007-2013.

  [Internal Link](./aux_files/legislation/RCM_86_2007.pdf) /
  [External Link](https://data.dre.pt/home/-/dre/635817/details/maximized)

- **Decree-Law No. 287/2007**, August 17 – approves the framework for the Incentives Systems in Mainland Portugal for the period 2007-2013.

  [Internal Link](./aux_files/legislation/Decreto-Lei_287_2007.pdf) /
  [External Link](https://dre.pt/home/-/dre/637175/details/maximized)

- **Ordinance No. 1462/2007**, November 15 – approves the specific regulation for the R&D Incentives System.

  [Internal Link](./aux_files/legislation/Portaria_1462_2007.pdf) /
  [External Link](https://dre.pt/home/-/dre/628518/details/maximized)

- **Ordinance No. 1463/2007**, November 15 – approves the specific regulation for the Qualification Incentives System for SMEs.

  [Internal Link](./aux_files/legislation/Portaria_1463_2007.pdf) /
  [External Link](https://dre.pt/home/-/dre/628519/details/maximized)

- **Ordinance No. 1464/2007**, November 15 – approves the specific regulation for the Innovation Incentives System.

  [Internal Link](./aux_files/legislation/Portaria_1464_2007.pdf) /
  [External Link](https://dre.pt/home/-/dre/628507/details/maximized)

- **Regulation (EU) No. 1303/2013 of the European Parliament and of the Council**, December 17 – defines common and general provisions on the European Structural and Investment Funds, including the European Regional Development Fund and the European Social Fund among others.

  [Internal Link](./aux_files/legislation/R_1303_2013_ec.pdf) /
  [External Link](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32013R1303&from=pt)

- **Decree-Law No. 137/2014**, September 12 – defines the governance model for the European Structural and Investment Funds for the period 2014-2020.

  [Internal Link](./aux_files/legislation/Decreto-Lei_137_2014.pdf) /
  [External Link](https://dre.pt/web/guest/legislacao-consolidada/-/lc/115287303/201906150247/73537179/diploma/indice)

- **Decree-Law No. 159/2014**, October 27 – establishes the general rules for implementing the Operational Programmes funded by the European Structural and Investment Funds for the period 2014-2020.

  [Internal Link](./aux_files/legislation/Decreto-Lei_159_2014.pdf) /
  [External Link](https://dre.pt/web/guest/legislacao-consolidada/-/lc/130791175/202104211819/73801462/diplomaExpandido/indice?q=159%2F2014)

- **Ordinance No. 263/2014**, December 16 – approves the regulations for the refund payments within QREN's Incentive Systems.

  [Internal Link](./aux_files/legislation/Portaria_263_2014.pdf) /
  [External Link](https://dre.pt/home/-/dre/65891076/details/maximized)

- **Decree-Law No. 6/2015**, January 8 – approves the framework for the creation of Incentives Systems for firms of Mainland Portugal.

  [Internal Link](./aux_files/legislation/Decreto-Lei_6_2015.pdf) /
  [External Link](https://dre.pt/web/guest/pesquisa/-/search/66108237/details/normal?l=1)

- **Ordinance No. 57-A/2015**, February 27 – establishes the specific regulation of PT2020 for the intervention field of Competitiveness and Internationalization.

  [Internal Link](./aux_files/legislation/Portaria_57-A_2015.pdf) /
  [External Link](https://dre.pt/web/guest/legislacao-consolidada/-/lc/115726886/201711230000/73551350/diplomaExpandido/indice)

# Auxiliary Files

For a description of each variable in each dataset (name, unit of measurement, data and storage type and format), summary statistics and a codebook for each data set please check the following auxiliary files[^32]:

**QREN:**

| File | Metafiles | Summary Statistics | Codebook | Dataset Description |
| :--- | :---: | :---: | :---: |  :---: |
| General Information File | [meta_geral](./aux_files/metafiles/QREN_meta_MPRJ_APR21_GERAL_V01.xlsx) | [stat_geral](./aux_files/descriptive_statistics/QREN_stat_geral.html) | [cdbk_geral](./aux_files/codebook/QREN_cdbk_geral.html) | [dscr_geral](./aux_files/describe_dataset/QREN_dscr_geral.html) |
| Closure data File | [meta_investenc](./aux_files/metafiles/QREN_meta_MPRJ_APR21_INVESTENC_V01.xlsx) | [stat_investenc](./aux_files/descriptive_statistics/QREN_stat_investenc.html) | [cdbk_investenc](./aux_files/codebook/QREN_cdbk_investenc.html) | [dscr_investenc](./aux_files/describe_dataset/QREN_dscr_investenc.html) |
| Payment Orders File | [meta_pagam](./aux_files/metafiles/QREN_meta_MPRJ_APR21_PAGAMENTOS_V01.xlsx) | [stat_pagam](./aux_files/descriptive_statistics/QREN_stat_pagamentos.html) | [cdbk_pagam](./aux_files/codebook/QREN_cdbk_pagamentos.html) | [dscr_pagam](./aux_files/describe_dataset/QREN_dscr_pagamentos.html) |


**PT2020:**

| File | Metafiles | Summary Statistics | Codebook | Dataset Description |
| :--- | :---: | :---: | :---: |  :---: |
| General Information File | [meta_geral](./aux_files/metafiles/PT2020_meta_MPRJ_NOV23_GERAL_V01.xlsx) | [stat_geral](./aux_files/descriptive_statistics/PT2020_stat_geral.html) | [cdbk_geral](./aux_files/codebook/PT2020_cdbk_geral.html) | [dscr_geral](./aux_files/describe_dataset/PT2020_dscr_geral.html) |


[^32]: The Summary Statistics, Codebook and Dataset Description files are available on BPLIM's servers. BPLIM staff also produce some data checks that are available upon request.

# Useful Links

[Portugal 2020 - Acordo de Parceria 2014-2020](https://www.historico.portugal.gov.pt/media/1489775/20140730%20Acordo%20Parceria%20UE.pdf)

[Current Situation - Incentives for enterprises Portugal 2020 (Data reported on 31 May 2020) - PT version](https://waf.compete2020.gov.pt/admin/fileman/Uploads/PS/20200617_PS_Incentivos-Rel-202005.pdf)

[Current Situation - Incentives for enterprises Portugal 2020 (Data reported on 31 December 2021) - PT version](https://www.compete2020.gov.pt/admin/fileman/Uploads/PS/20220113_PSitIncentivos-Rel-202112.pdf)

[Indústria 4.0](https://www.ani.pt/media/3828/4_industria_40.pdf)

[European Structural and Investment Funds Data](https://cohesiondata.ec.europa.eu/)

[Payment Rules - PT2020](https://portugal2020.pt/wp-content/uploads/norma-12-2015.pdf)

# Citation of this Dataset

Banco de Portugal Microdata Research Laboratory (BPLIM) (2023): Incentives Systems Data. Extraction: November 2023. Version: V1. Banco de Portugal - BPLIM. Dataset. https://doi.org/10.17900/SI.Nov2023.V1

<br>
<br>
<br>
<br>

To cite this dataset you can use the package biblatex with the following BibTeX entry:

```{stata}
*| eval: false
*| echo: true
*| code-fold: false
@dataset{SI.Nov2023.V1,
author = {{Banco de Portugal Microdata Research Laboratory - BPLIM}},
publisher = {Banco de Portugal},
title = {{I}ncentives {S}ystems {D}ata},
year = {2023},
version = {{ V1, Extraction November 2023}},
doi = {10.17900/SI.Nov2023.V1},
url = {https://doi.org/10.17900/SI.Nov2023.V1}
}
```
