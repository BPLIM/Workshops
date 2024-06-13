<meta charset="utf-8"/>

---
title: Fast and Exceptional Enterprise Survey - Data Manual
---


`Extraction Date`: July 2020

`Manual Date`: 31 July 2020



**Abstract**: The Fast and Exceptional Enterprise Survey was launched by Statistics Portugal (INE) and the Banco de Portugal aiming to identify the main effects of the COVID-19 pandemic on key aspects of the enterprises activity, such as firm's turnover, workforce, prices, credit conditions and the use of Government support measures. The data started being collected with a weekly frequency on April 6-10, 2020 and refers to a fortnight from May onwards. The survey was suspended after the 1st fortnight of July 2020.


<br>
<br>

# Table of Contents
1. [General Information](#general-information)
2. [Geographical Coverage](#geographical-coverage)
3. [Population](#population)
4. [Methodology](#methodology)
5. [Description of Files](#description-of-files)
6. [Description of Variables](#description-of-variables)
    1. [Identifiers](#a1.-identifiers)
    2. [Variables reported by the firm through COVID-IREE](#a2.-variables-reported-by-the-firm-through-covid-iree)
        1. [Firm Situation](#a2.1-firm-situation)
        2. [Impact on Turnover](#a2.2-impact-on-turnover)
        3. [Impact on Firm Closure](#a2.3-impact-on-firm-closure)
        4. [Impact on the Workforce](#a2.4-impact-on-the-workforce)
        5. [Use of the Support Measures](#a2.5-use-of-the-support-measures)
        6. [Use of Credit and Credit Conditions](#a2.6-use-of-credit-and-credit-conditions)
        7. [Prices](#a2.7-prices)
        8. [Hygiene and Safety Requirements](#a2.8-hygiene-and-safety-requirements)
        9. [Activity of the Firm](#a2.9-activity-of-the-firm)
        10. [Liquidity](#a2.10-liquidity)
      3. [Sample variables](#a3.-sample-variables)
7. [Basic Descriptive Statistics](#basic-descriptive-statistics)
8. [Legislation](#legislation)
9. [Auxiliary Files](#auxiliary-files)
10. [Auxiliary Tools](#auxiliary-tools)
11. [Useful Links](#useful-links)
12. [Citation of this Dataset](#citation-of-this-dataset)
13. [References](#references)

<br>
<br>

# General Information

> `Dataset Designation in English`: Fast and Exceptional Enterprise Survey (COVID-IREE)

> `Dataset Designation in Portuguese`: *Inquérito Rápido e Excecional às Empresas* (COVID-IREE)

> `Data Type`: Longitudinal Data

> `Unit of Analysis`: Firms

> `Frequency`: weekly/fortnightly

> `Start date`: April 6-10 2020 (edition 15)

>`Most recent date`: 1st fortnight of July (edition 23)

> `Reference date`: The data reports to the week of reference in April. From May onwards the data refers to a fortnight.

> `Collection method`: Electronic form

> `Data Organization`: The data is organized in one file for each edition of the survey. All files are available in Stata format, version 16.

> `Languages Available`: Variable labels, notes and value labels are available in Portuguese and English. [^1]

[^1]: To see the labels in English type the following command line in Stata: 'label language en'.

> `Access`: This dataset is also made available by [Statistics Portugal (INE)](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_main&xlang=en).

<br>
<br>

# Geographical Coverage
The data refers to firms located in the Mainland Portugal and Autonomous Regions – Azores and Madeira.

<br>
<br>

# Population

The population of COVID-IREE corresponds to the non-financial firms located in Portugal with the main activity included in one of the following sectors [^2]:

- Manufacturing and energy (sections B, C, D, and E of the Classification of Economic Activities (CAE, Rev.3))
- Construction and real estate (sections F and L of CAE Rev.3)
- Distributive trade (section G of CAE Rev.3)
- Transportation and storage (section H of CAE Rev.3)
- Accommodation and food services (section I of CAE Rev.3)
- Information and communication (section J of CAE Rev.3)
- Other services (sections M, N, P, Q, R, and S of CAE Rev.3)

The population is the same as of the Business Surveys (*Inquéritos de Conjuntura às Empresas*) conducted by Statistics Portugal (INE).

[^2]: Firms in the Madeira Free Zone (*Zona Franca da Madeira*) are excluded.

<br>
<br>

# Methodology

COVID-IREE is an electronic survey addressed to a representative sample of non-financial firms located in Portugal.

The survey contains nine editions. It was launched in the week of 6-10 of April 2020 and remained with a weekly frequency until the end of April. From May onwards the survey reports to a fortnight. It was suspended after July and the last edition available refers to the first fortnight of July.

The sample was constructed based on the samples of the monthly industry, construction, distributive trade and services turnover surveys plus approximately 300 enterprises of the remaining sectors of activity covered in the population. [^3] The sample was designed to represent approximately 80% of total turnover within each economic activity.

As detailed in INE (2020), the sampling frame considers firms with turnover equal or larger than the maximum value between the 20% quantile of total turnover and 150,000 euros. The sample was stratified by number of employees (NPS) and turnover within each sector of activity. All firms accounting for more than 80% or 90% [^4] of the cumulative frequency of the total number of employees or turnover are exhaustively included in the sample.

The final sample includes 8.883 firms which account for 1,138,424 employees and 207,599 million euros of turnover. The response rate in each reference period is presented in the table below:

| Week | Reference period | Response interval | Valid responses | Representativeness in terms of NPS (% of the sample) | Representativeness in terms of turnover (% of the sample) |
| :----: | :------: | :------: | :--------: | :-----------------: | :-----------------: |
| edition 15 | 6-10 April 2020 | 6-12 April 2020 | 5,010 (56.4%) | 57.4 | 68.8 |
| edition 16 | 13-17 April 2020 | 13-19 April 2020 | 5,973 (67.2%) | 72.3 | 80.0 |
| edition 17 | 20-24 April 2020 | 20-26 April 2020 | 5,928 (66.7%) | 71.8 | 81.0 |
| edition 18 | 27 April - 1 May 2020 | 27 April - 3 May 2020 | 5,571 (62.7%) | 64.7 | 77.9 |
| edition 19 | 1st fortnight of May | 11-17 May 2020 | 5,628 (63.4%) | 66.4 | 77.2 |
| edition 20 | 2nd fortnight of May | 25-31 May 2020 | 5,424 (61.1%) | 65.5 | 77.4 |
| edition 21 | 1st fortnight of June | 8-16 June 2020 | 5,785 (65.1%) | 69.1 | 79.3 |
| edition 22 | 2nd fortnight of June | 22-28 June 2020 | 4,920 (55.4%) | 60.7 | 70.5 |
| edition 23 | 1st fortnight of July | 20-26 July 2020 | 4,850 (54.6%) | 59.0 | 69.0 |

<br>

As stated in the methodological notes micro and small enterprises are less likely to answer the survey. There is no significant difference in the survey response probability according to the sector of activity.
From the second week onwards the survey included the answers of the previous reference period to try to ensure the consistency of the report.


BPLIM prepares a dataset for each edition of the survey. We assigned short labels and provide notes with the complete description of each variable both in Portuguese and English. [^5] All categorical variables have value labels available both in Portuguese and English.
Some questions were in(ex)cluded from the survey over time as briefly presented in the section [Description of Variables](#description-of-variables).


[^3]: These correspond to the following sections of the Classification of Economic Activities (Revision 3): P (Education), Q (Human health and social work activities), R (Arts, entertainment, sports and recreation activities) and S (Other service activities).
[^4]: This percentage varies according to the sector of activity.
[^5]: To see the notes for all variables type the following command line in Stata: 'notes' and for a specific variable type 'notes *varname*'.

<br>
<br>

# Description of Files
The data in COVID-IREE is organized in one file for each survey's edition:

    IREE_A_WFRM_ww2020_JUL20_V01.dta

where *A* stands for Anonymized and *ww* corresponds to the edition of the survey (15,...,23). The most recent version of the data was extracted on July 2020 (JUL20) and contains the final revised data up to the first fortnight of July.

Labels and value labels were attributed to all categorical variables. All datasets are anonymized.

<br>
<br>

# Description of Variables
Below we provide a general description of the variables included in the data. For a full account of all variable categories and changes over time see [“Auxiliary Files” section](#auxiliary-files).
The information collected in the survey refers to: 1) the firm situation; 2) the impact of COVID-19 on turnover; 3) the impact of COVID-19 on firm closure; 4) the impact of COVID-19 on the workforce; 5) the use of Government support measures; 6) the use of credit and credit conditions; 7) the impact of COVID-19 on prices; 8) the capacity to comply with the hygiene and safety requirements; 9) the impact of COVID-19 on the firm's activity; and 10) liquidity.

### A1. Identifiers
`Firm identifier` (*tina*) – Unique identifier that enables tracking the legal entity over time. *tina* is the anonymized tax identification number. [^6]

[^6]: *tina* preserves the first digit of the tax identification number. This first digit contains relevant information about the type of firm: 1,2 or 3-natural person (*pessoa singular*); 5-private corporation (*pessoa colectiva*); 6-public corporation (*pessoa colectiva pública*); 7-other miscellaneous cases; 8- sole proprietorship (*empresário em nome individual*); 9- irregular corporation (*pessoa colectiva irregular*).

<br>
<br>

`Code of the survey's edition` (*p_infra_cod*) – It provides information about the edition of the survey. The first edition of the survey occurred in week 15 and the numbering of editions is sequential afterwards. The data refers to a week if *p_infra_cod* is lower than 19 and to a fortnight if *p_infra_cod* takes value 19 to 23.

> Classification:

| Code | Designation |
| :---: | :---------- |
| 15 | Week of April 6 |
| 16 | Week of April 13 |
| 17 | Week of April 20 |
| 18 | Week of April 27 |
| 19 | 1st fortnight of May |
| 20 | 2nd fortnight of May |
| 21 | 1st fortnight of June |
| 22 | 2nd fortnight of June |
| 23 | 1st fortnight of July |

<br>
<br>

`Reference year` (*ano*) - variable that reports the reference year of the data.

### A2. Variables reported by the firm through COVID-IREE

#### A2.1 Firm Situation

`Relevant event` (*BC015*) - dummy variable taking value one in case a relevant event occurred in the reference period

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Yes |
| 2 | No |

<br>
<br>

`Date of the relevant event` (*BC020*) - date in which the relevant event occurred

<br>
<br>

`Situation of the enterprise` (*V1010*)

> Question: What situation best describes the enterprise in the reference period?

> Report: all editions

> Classification:

| Code | Designation |
| :------: | :--------------- |
| 1	| Remains, even partially, in production or operation |
| 2 |	Temporarily closed |
| 3 |	Definitely closed |

> Comment: From edition 15 to edition 18, the question refers to the current week and from edition 19 onwards it refers to the moment of answering the survey. From edition 18 onwards, a comment was introduced clarifying that the category "Definitely Closed" should be used by firms that will not resume the activity once the situation is normalized.

<br>
<br>

#### A2.2 Impact on Turnover

`Impact of COVID-19 on turnover in the reference period` (*V2010*)

> Question: In the reference period, is the COVID-19 pandemic having an impact on the enterprise's turnover when compared with the expected situation in the absence of the effects of the pandemic?

> Report: all editions

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Yes, a reduction |
| 2 | Yes, an increase |
| 3 | No impact |
| 8 | Does not know / does not answer |

<br>
<br>

`Estimate of the reduction in turnover in the reference period` (*V2110*)

> Question: Please indicate the best estimate for the reduction in the enterprise's turnover in the reference period

> Report: all editions

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Less than 10% |
| 2 | Between 10% and 25% |
| 3 | Between 26% and 50% |
| 4 | Between 51% and 75% |
| 5 | More than 75% |

<br>
<br>

`Estimate of the increase in turnover in the reference period` (*V2120*)

> Question: Please indicate the best estimate for the increase in the enterprise's turnover in the reference period

> Report: all editions

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Less than 10% |
| 2 | Between 10% and 25% |
| 3 | Between 26% and 50% |
| 4 | Between 51% and 75% |
| 5 | More than 75% |

<br>
<br>

`Time needed for turnover to return to the normal level` (*V3A110*)

> Question: How long do you think it will take for the enterprises' turnover to return to normal comparing with the expected situation in the absence of the pandemic effects?

> Report: edition 21 (1st fortnight of June)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Less than one month |
| 2 | One or two months |
| 3 | Three to six months |
| 4 | Over six months |
| 5 | Turnover should not return to the normal level |
| 8 | Does not know / does not answer |

<br>
<br>

`Impact of the restrictions in the emergency state on the reduction in turnover` (*V3110*)

> Question: What is the impact of the restrictions in the context of the emergency state for reducing the turnover of the enterprise?

> Report: from edition 15 (6-10 April) to edition 18 (27 April-1 May)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Too much impact |
| 2 | Some impact |
| 3 | No impact |
| 8 | Does not know / does not answer |
| 9 | Not applicable |

<br>
<br>

`Impact of the unexpected shortage of staff on the reduction in turnover` (*V3120*)

> Question: What is the impact of the unexpected shortage of staff for reducing the turnover of the enterprise?

> Report: from edition 15 (6-10 April) to edition 18 (27 April-1 May)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Too much impact |
| 2 | Some impact |
| 3 | No impact |
| 8 | Does not know / does not answer |
| 9 | Not applicable |


<br>
<br>

`Impact of the supply chain problems on the reduction in turnover` (*V3130*)

> Question: What is the impact of the supply chain problems for reducing the turnover of the enterprise?

> Report: from edition 15 (6-10 April) to edition 18 (27 April-1 May)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Too much impact |
| 2 | Some impact |
| 3 | No impact |
| 8 | Does not know / does not answer |
| 9 | Not applicable |

<br>
<br>

`Impact of the absence of orders/clients on the reduction in turnover` (*V3140*)

> Question: What is the impact of the absence of orders/clients for reducing the turnover of the enterprise?

> Report: from edition 15 (6-10 April) to edition 18 (27 April-1 May)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Too much impact |
| 2 | Some impact |
| 3 | No impact |
| 8 | Does not know / does not answer |
| 9 | Not applicable |

<br>
<br>

`Evolution of turnover in the reference period` (*V4020*)

> Question: How is the enterprise's turnover evolving in the reference period when compared with the previous reference period?

> Report: from edition 19 (1st fortnight of May) to edition 22 (2nd fortnight of June)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Increased a lot |
| 2 | Increased slightly |
| 3 | No change |
| 4 | Decreased slightly |
| 5 | Decreased a lot |
| 8 | Does not know / does not answer |

<br>
<br>

`Impact of the evolution of the containment measures for turnover` (*V5110*)

> Question: Impact of the evolution of the containment measures for the evolution of the enterprise's turnover in the reference period comparing with the previous reference period

> Report: from edition 19 (1st fortnight of May) to edition 22 (2nd fortnight of June)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Very positive impact |
| 2 | Positive impact |
| 3 | No impact |
| 4 | Negative impact |
| 5 | Very negative impact |
| 8 | Does not know / does not answer |
| 9 | Not applicable |

<br>
<br>

`Impact of the variations of orders/customers for turnover` (*V5120*)

> Question: Impact of the variation of orders/customers for the evolution of the enterprise's turnover in the reference period comparing with the previous reference period

> Report: from edition 19 (1st fortnight of May) to edition 22 (2nd fortnight of June)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Very positive impact |
| 2 | Positive impact |
| 3 | No impact |
| 4 | Negative impact |
| 5 | Very negative impact |
| 8 | Does not know / does not answer |
| 9 | Not applicable |

<br>
<br>

`Impact of the changes in supply chain for turnover` (*V5130*)

> Question: Impact of the changes in the supply chain for the evolution of the enterprise's turnover in the reference period comparing with the previous reference period

> Report: from edition 19 (1st fortnight of May) to edition 22 (2nd fortnight of June)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Very positive impact |
| 2 | Positive impact |
| 3 | No impact |
| 4 | Negative impact |
| 5 | Very negative impact |
| 8 | Does not know / does not answer |
| 9 | Not applicable |

<br>
<br>

`Impact of variations in the enterprise's staff for turnover` (*V5140*)

> Question: Impact of the variations in the enterprise's staff for the evolution of the enterprise's turnover in the reference period comparing with the previous reference period

> Report: from edition 19 (1st fortnight of May) to edition 22 (2nd fortnight of June)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Very positive impact |
| 2 | Positive impact |
| 3 | No impact |
| 4 | Negative impact |
| 5 | Very negative impact |
| 8 | Does not know / does not answer |
| 9 | Not applicable |

<br>
<br>

#### A2.3 Impact on Firm Closure

`Impact of the restrictions in the context of the emergency state on the firm closure` (*V3210*)

> Question: What is the impact of the restrictions in the context of the emergency state for the definitive closure of the enterprise?

> Report: all editions

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Too much impact |
| 2 | Some impact |
| 3 | No impact |
| 8 | Does not know / does not answer |
| 9 | Not applicable |

> Comments: This question was slightly reformulated to the impact of the *restrictions in the context of the containment measures* for the definitive closure of the enterprise in the 1st fortnight of July due to the end of the emergency state

<br>
<br>

`Impact of the unexpected shortage of staff on the firm closure` (*V3220*)

> Question: What is the impact of the unexpected shortage of staff for the definitive closure of the enterprise?

> Report: all editions

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Too much impact |
| 2 | Some impact |
| 3 | No impact |
| 8 | Does not know / does not answer |
| 9 | Not applicable |

<br>
<br>

`Impact of the supply chain problems on the firm closure` (*V3230*)

> Question: What is the impact of the supply chain problems for the definitive closure of the enterprise?

> Report: all editions

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Too much impact |
| 2 | Some impact |
| 3 | No impact |
| 8 | Does not know / does not answer |
| 9 | Not applicable |

<br>
<br>

`Impact of the absence of orders/clients on the firm closure` (*V3240*)

> Question: What is the impact of the absence of orders/clients for the definitive closure of the enterprise?

> Report: all editions

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Too much impact |
| 2 | Some impact |
| 3 | No impact |
| 8 | Does not know / does not answer |
| 9 | Not applicable |

<br>
<br>

#### A2.4 Impact on the workforce

`Impact of COVID-19 on persons employed effectively working in the reference period` (*V4010*)

> Question: Is the COVID-19 pandemic having an impact on the number of persons employed effectively working in the enterprise in the reference period when compared with the expected situation in the absence of the effects of the pandemic?

> Report: all editions

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Yes, a reduction |
| 2 | Yes, an increase |
| 3 | No impact |
| 8 | Does not know / does not answer |

> Comment: An instruction to consider both the persons employed working at the enterprise's facilities and those working from home was introduced from edition 16 onwards

<br>
<br>

`Estimate of the reduction in the number of employees in the reference period` (*V4110*)

> Question: Please indicate the best estimate for the reduction in persons employed by the enterprise in the reference period

> Report: all editions

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Less than 10% |
| 2 | Between 10% and 25% |
| 3 | Between 26% and 50% |
| 4 | Between 51% and 75% |
| 5 | More than 75% |

<br>
<br>

`Estimate of the increase in the number of employees in the reference period` (*V4120*)

> Question: Please indicate the best estimate for the increase in persons employed by the enterprise in the reference period

> Report: all editions

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Less than 10% |
| 2 | Between 10% and 25% |
| 3 | Between 26% and 50% |
| 4 | Between 51% and 75% |
| 5 | More than 75% |

<br>
<br>

`Most relevant situation for the reduction of persons employed effectively working` (*V5010*)

> Question: Which situation is more relevant to reducing the number of persons employed effectively working?

> Report: from edition 15 (6-10 April) to edition 17 (20-24 April)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Simplified layoff |
| 2 | Dismissal of the staff with permanent contracts |
| 3 | Non-renewal of fixed-term contracts |
| 4 | Absences due to the state of emergency, because of illness or to support the family |
| 7 | None of the above |
| 8 | Does not know / does not answer |

<br>
<br>

`Importance of the simplified layoff for the reduction of the number of employees effectively working` (*V5A110*)

> Question: Relevance of the simplified layoff for the reduction of the number of persons employed effectively working

> Report: edition 18 (27 April - 1 May)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Very relevant |
| 2 | Relevant |
| 3 | Little or nothing relevant |
| 8 | Does not know / does not answer |
| 9 | Not applicable |

<br>
<br>

`Importance of the dismissal of permanent contracts (OEC) for the reduction of the number of employees effectively working` (*V5A120*)

> Question: Relevance of the dismissal of the staff with permanent contracts for the reduction of the number of persons employed effectively working

> Report: edition 18 (27 April - 1 May)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Very relevant |
| 2 | Relevant |
| 3 | Little or nothing relevant |
| 8 | Does not know / does not answer |
| 9 | Not applicable |

<br>
<br>

`Importance of the non-renewal of fixed-term contracts (FTC) for the reduction of the number of employees effectively working` (*V5A130*)

> Question: Relevance of the non-renewal of fixed-term contracts for the reduction of the number of persons employed effectively working

> Report: edition 18 (27 April - 1 May)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Very relevant |
| 2 | Relevant |
| 3 | Little or nothing relevant |
| 8 | Does not know / does not answer |
| 9 | Not applicable |

<br>
<br>

`Importance of the absences for the reduction of the number of employees effectively working` (*V5A140*)

> Question: Relevance of the absences due to the state of emergency, because of illness or to support the family for the reduction of the number of persons employed effectively working

> Report: edition 18 (27 April - 1 May)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Very relevant |
| 2 | Relevant |
| 3 | Little or nothing relevant |
| 8 | Does not know / does not answer |
| 9 | Not applicable |

<br>
<br>

`Importance of other situations for the reduction of the number of employees effectively working` (*V5A150*)

> Question: Relevance of other situations for the reduction of the number of persons employed effectively working

> Report: edition 18 (27 April - 1 May)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Very relevant |
| 2 | Relevant |
| 3 | Little or nothing relevant |
| 8 | Does not know / does not answer |
| 9 | Not applicable |

<br>
<br>

`Share of persons employed effectively working in remote working` (*V5B010*)

> Question: Indicate the share of persons employed effectively working in remote working in the reference period

> Report: from edition 18 (27 April - 1 May) to edition 23 (1st fortnight of July)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Less than 10% |
| 2 | Between 10% and 25% |
| 3 | Between 26% and 50% |
| 4 | Between 51% and 75% |
| 5 | More than 75% |
| 6 | No persons in this situation |

<br>
<br>

`Share of persons employed effectively working with alternate presence` (*V5B020*)

> Question: Indicate the share of persons employed effectively working with alternate presence at the enterprise's facilities in the reference period

> Report: from edition 19 (1st fortnight of May) to edition 23 (1st fortnight of July)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Less than 10% |
| 2 | Between 10% and 25% |
| 3 | Between 26% and 50% |
| 4 | Between 51% and 75% |
| 5 | More than 75% |
| 6 | No persons in this situation |

<br>
<br>

`Evolution in number of persons employed effectively working` (*V7020*)

> Question: How is evolving the number of persons effectively working in the enterprise in the reference period comparing with the previous fortnight?

> Report: from edition 19 (1st fortnight of May) to edition 22 (2nd fortnight of June)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Increased a lot |
| 2 | Increased slightly |
| 3 | No change |
| 4 | Decreased slightly |
| 5 | Decreased a lot |
| 8 | Does not know / does not answer |

<br>
<br>

`Impact of the change in the number of employees in layoff for the evolution of the number of employees effectively working` (*V8150*)

> Question: Impact of the change in the number of persons employed in layoff for the evolution of the number of persons employed effectively working in the reference period (compared to the previous fortnight)

> Report: from edition 19 (1st fortnight of May) to edition 22 (2nd fortnight of June)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Very positive impact |
| 2 | Positive impact |
| 3 | No impact |
| 4 | Negative impact |
| 5 | Very negative impact |
| 8 | Does not know / does not answer |
| 9 | Not applicable |

<br>
<br>

`Impact of the variation in the number of permanent contracts (OEC) for the evolution of the number of employees effectively working` (*V8160*)

> Question: Impact of the variation in the number of permanent contracts for the evolution of the number of persons employed effectively working in the reference period (compared to the previous fortnight)

> Report: from edition 19 (1st fortnight of May) to edition 22 (2nd fortnight of June)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Very positive impact |
| 2 | Positive impact |
| 3 | No impact |
| 4 | Negative impact |
| 5 | Very negative impact |
| 8 | Does not know / does not answer |
| 9 | Not applicable |

<br>
<br>

`Impact of the variation in fixed-term contracts (FTC) for the evolution of the number of employees effectively working` (*V8170*)

> Question: Impact of the variation in the number of fixed-term contracts for the evolution of the number of persons employed effectively working in the reference period (compared to the previous fortnight)

> Report: from edition 19 (1st fortnight of May) to edition 22 (2nd fortnight of June)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Very positive impact |
| 2 | Positive impact |
| 3 | No impact |
| 4 | Negative impact |
| 5 | Very negative impact |
| 8 | Does not know / does not answer |
| 9 | Not applicable |

<br>
<br>

`Impact of the variation in absences for the evolution of the number of employees effectively working` (*V8180*)

> Question: Impact of the variation in the days of absence because of illness or to support the family for the evolution of the number of persons employed effectively working in the reference period (compared to the previous fortnight)

> Report: from edition 19 (1st fortnight of May) to edition 22 (2nd fortnight of June)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Very positive impact |
| 2 | Positive impact |
| 3 | No impact |
| 4 | Negative impact |
| 5 | Very negative impact |
| 8 | Does not know / does not answer |
| 9 | Not applicable |

<br>
<br>

`Evolution of the number of employees since the beginning of the pandemic` (*V8020*)

> Question: Since the beginning of the pandemic, what was the evolution of the total number of employees (effectively working or not)?

> Report: edition 23 (1st fortnight of July)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Decreased |
| 2 | No change |
| 3 | Increased |
| 8 | Does not know / does not answer |

> Comment: The pandemic was declared on 11 March 2020.

<br>
<br>


`Estimate for the decrease in the number of employees (NPS) since March 11 to the 1st fortnight of July` (*V8220*)

> Question: Please indicate the best estimate for the decrease of the total number of employees between March 11 and the 1st fortnight of July 2020

> Report: edition 23 (1st fortnight of July)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Less than 5% |
| 2 | Between 5% and 10% |
| 3 | Between 11% and 15% |
| 4 | Between 16% and 20% |
| 5 | More than 20% |

<br>
<br>

`Estimate for the increase in the number of employees (NPS) since March 11 to the 1st fortnight of July` (*V8230*)

> Question: Please indicate the best estimate for the increase of the total number of employees between March 11 and the 1st fortnight of July 2020

> Report: edition 23 (1st fortnight of July)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Less than 5% |
| 2 | Between 5% and 10% |
| 3 | Between 11% and 15% |
| 4 | Between 16% and 20% |
| 5 | More than 20% |

<br>
<br>

`Expected change in the number of jobs until the end of the year` (*V12010*)

> Question: What is the expected change in the number of jobs until the end of the year?

> Report: edition 23 (1st fortnight of July)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | The firm plans to decrease the number of jobs |
| 2 | The firm plans to maintain the number of jobs |
| 3 | The firm plans to increase the number of jobs |
| 8 | Does not know / does not answer |

<br>
<br>

#### A2.5 Use of the Support Measures

`Use of the moratorium for the payment of interests and principal on existing loans` (*V6010*)

> Question:	The enterprise benefited or is planning to benefit from the moratorium for the payment of interests and principal on existing loans?

> Report: from edition 15 (6-10 April) to edition 22 (2nd fortnight of June)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Has already benefited |
| 2 | Plans to benefit |
| 3 | Has not benefited or plans to benefit |
| 7 | Not eligible |
| 8 | Does not know / does not answer |

> Comment: The category "Not eligible" was introduced from edition 16 onwards.

<br>
<br>

`Use of the access to new loans with low interest or State guarantees` (*V6020*)

> Question: The enterprise benefited or is planning to benefit from the access to new loans with low interest or State guarantees?

> Report: from edition 15 (6-10 April) to edition 22 (2nd fortnight of June)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Has already benefited |
| 2 | Plans to benefit |
| 3 | Has not benefited or plans to benefit |
| 7 | Not eligible |
| 8 | Does not know / does not answer |

> Comment: The category "Not eligible" was introduced from edition 16 onwards.

<br>
<br>

`Use of the suspension of the payment of tax and contributory obligations` (*V6030*)

> Question: The enterprise benefited or is planning to benefit from the suspension of the payment of tax and contributory obligations?

> Report: from edition 15 (6-10 April) to edition 22 (2nd fortnight of June)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Has already benefited |
| 2 | Plans to benefit |
| 3 | Has not benefited or plans to benefit |
| 7 | Not eligible |
| 8 | Does not know / does not answer |

> Comment: The category "Not eligible" was introduced from edition 16 onwards.

<br>
<br>

`Use of other measures presented by the Government` (*V6040*)

> Question: The enterprise benefited or is planning to benefit from other measures presented by the Government due to the COVID-19 pandemic?

> Report: from edition 15 (6-10 April) to edition 22 (2nd fortnight of June)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Has already benefited |
| 2 | Plans to benefit |
| 3 | Has not benefited or plans to benefit |
| 7 | Not eligible |
| 8 | Does not know / does not answer |

> Comment: The category "Not eligible" was introduced from edition 16 onwards. From the edition 18 onwards this question indicates the exclusion of the simplified layoff from the definition of other measures

<br>
<br>

`How long can remain in activity without additional liquidity support measures` (*V7010*)

> Question: In the absence of additional liquidity support measures, for how long can the enterprise remain in activity?

> Report: from edition 15 (6-10 April) to edition 17 (20-24 April) and edition 23 (1st fortnight of July)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Less than one month |
| 2 | One or two months |
| 3 | Three to six months |
| 4 | Over six months |
| 8 | Does not know / does not answer |

<br>
<br>

`Did the firm benefit from the simplified layoff?` (*V9020*)

> Question: Did the firm benefit from the simplified layoff?

> Report: edition 23 (1st fortnight of July)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Yes |
| 2 | No |

<br>
<br>


`How would the number of employees have changed without the simplified layoff?` (*V10110*)

> Question: Since the beginning of the pandemic and in the absence of the use of the simplified layoff measure, what would have been the change in the number of employees?

> Report: edition 23 (1st fortnight of July)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | It would have decreased |
| 2 | It would have remained unchanged |
| 8 | Does not know / does not answer |

<br>
<br>

`Estimate for the decrease in the number of employees (NPS) without the use of the simplified layoff` (*V10120*)

> Question: Please indicate the best estimate for the decrease in the number of employees in the absence of the use of the simplified layoff measure

> Report: edition 23 (1st fortnight of July)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Less than 5% |
| 2 | Between 5% and 10% |
| 3 | Between 11% and 15% |
| 4 | Between 16% and 20% |
| 5 | More than 20% |

<br>
<br>

`Option to take in August given the changes to the simplified layoff measure` (*V11110*)

> Question: Considering the announced changes to the simplified layoff measure, what is the intention of the enterprise in August?

> Report: edition 23 (1st fortnight of July)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | The enterprise intends to keep using the simplified layoff or to use the support for the gradual resumption of the activity |
| 2 | The enterprise intends to use the extraordinary incentive to the normalization of the activity following the end of the simplified layoff regime |
| 3 | The enterprise will no longer use the simplified layoff and does not intend to use any support measure |
| 8 | Does not know / does not answer |


<br>
<br>

#### A2.6 Use of Credit and Credit Conditions

`Did the firm recourse to additional credit due to the COVID-19 pandemic?` (*V8010*)

> Question: Due to the effects of the COVID-19 pandemic, did the enterprise increase its use of bank credit or other types of credit?

> Report: from edition 15 (6-10 April) to edition 20 (2nd fortnight of May)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Yes |
| 2 | No |
| 8 | Does not know / does not answer |

> Comment: This question refers to the previous week until the edition 18 and it refers to the current fortnight from the edition 19 onwards.

<br>
<br>

`Conditions of the financial institutions credit` (*V8110*)

> Question: Indicate under what conditions the company accessed to the financial institutions credit compared to those previously practiced

> Report: from edition 15 (6-10 April) to edition 20 (2nd fortnight of May)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | More burdensome |
| 2 | Similar |
| 3 | More favourable |
| 8 | Does not know / does not answer |
| 9 | Not applicable |

> Comment: This question refers to the previous week until the edition 18 and it refers to the current fortnight from the edition 19 onwards.

<br>
<br>

`Conditions of the supplier credit` (*V8120*)

> Question:  Indicate under what conditions the company accessed to the supplier credit compared to those previously practiced

> Report: from edition 15 (6-10 April) to edition 20 (2nd fortnight of May)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | More burdensome |
| 2 | Similar |
| 3 | More favourable |
| 8 | Does not know / does not answer |
| 9 | Not applicable |

> Comment: This question refers to the previous week until the edition 18 and it refers to the current fortnight from the edition 19 onwards.

<br>
<br>

`Conditions of the other type of credit` (*V8190*)

> Question: Indicate under what conditions the company accessed to the other type of credit compared to those previously practiced

> Report: from edition 15 (6-10 April) to edition 20 (2nd fortnight of May)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | More burdensome |
| 2 | Similar |
| 3 | More favourable |
| 8 | Does not know / does not answer |
| 9 | Not applicable |


> Comment: This question refers to the previous week until the edition 18 and it refers to the current fortnight from the edition 19 onwards.

<br>
<br>

`Reason for not using additional credit` (*V8210*)

> Question: Indicate why the enterprise did not increase the credit.

> Report: from edition 15 (6-10 April) to edition 18 (27 April - 1 May)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Because did not intend to |
| 2 | Because the conditions were unfavourable |
| 3 | Because didn't find funders |
| 9 | Other reasons |

<br>
<br>

#### A2.7 Prices

`Expectation for the prices charged by the enterprise` (*V9010*)

> Question: Expectation for the prices charged by the enterprise

> Report: from edition 15 (6-10 April) to edition 17 (20-24 April) and edition 23 (1st fortnight of July)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Increase a lot |
| 2 | Increase slightly |
| 3 | Stay about the same |
| 4 | Fall slightly |
| 5 | Fall a lot |
| 8 | Does not know / does not answer |

> Comment: From edition 15 to edition 17 the question refers to the expectation for the current week. In the edition 23, the question refers to the expected situation without the pandemic.

<br>
<br>

#### A2.8 Hygiene and Safety Requirements

`Importance of the availability of individual protection material` (*V10010*)

> Question: Relevance of the availability of individual protection material (masks, visors, disinfectant, etc.) in the difficulty in complying with the hygiene and safety requirements necessary for the resumption of the activity

> Report: from edition 19 (1st fortnight of May) to edition 20 (2nd fortnight of May)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Very relevant |
| 2 | Relevant |
| 3 | Little or nothing relevant |
| 8 | Does not know / does not answer |
| 9 | Not applicable |

<br>
<br>

`Importance of the restrictions on physical space` (*V10020*)

> Question: Relevance of the restrictions on physical space in the difficulty in complying with the hygiene and safety requirements necessary for the resumption of the activity

> Report: from edition 19 (1st fortnight of May) to edition 20 (2nd fortnight of May)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Very relevant |
| 2 | Relevant |
| 3 | Little or nothing relevant |
| 8 | Does not know / does not answer |
| 9 | Not applicable |

<br>
<br>

`Importance of the high costs` (*V10030*)

> Question: Relevance of the high costs in the difficulty in complying with the hygiene and safety requirements necessary for the resumption of the activity

> Report: from edition 19 (1st fortnight of May) to edition 20 (2nd fortnight of May)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Very relevant |
| 2 | Relevant |
| 3 | Little or nothing relevant |
| 8 | Does not know / does not answer |
| 9 | Not applicable |

<br>
<br>

`Importance of the lack of information on the necessary requirements` (*V10040*)

> Question: Relevance of the lack of information on necessary requirements in the difficulty in complying with the hygiene and safety requirements necessary for the resumption of the activity

> Report: from edition 19 (1st fortnight of May) to edition 20 (2nd fortnight of May)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Very relevant |
| 2 | Relevant |
| 3 | Little or nothing relevant |
| 8 | Does not know / does not answer |
| 9 | Not applicable |

<br>
<br>

`Importance of the lack of technical skills in hygiene and safety at work` (*V10050*)

> Question: Relevance of the lack of technical skills in hygiene and safety at work in the enterprise in the difficulty in complying with the hygiene and safety requirements necessary for the resumption of the activity

> Report: from edition 19 (1st fortnight of May) to edition 20 (2nd fortnight of May)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Very relevant |
| 2 | Relevant |
| 3 | Little or nothing relevant |
| 8 | Does not know / does not answer |
| 9 | Not applicable |

<br>
<br>

#### A2.9 Activity of the firm

`Intention to reinforce the investment in information technology` (*V11010*)

> Question: Do you intend to permanently change the activity of the enterprise due to the COVID-19 pandemic? Reinforce the investment in information technology

> Report: edition 21 (1st fortnight of June)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Very likely |
| 2 | Unlikely |
| 3 | Not likely |
| 8 | Does not know / does not answer |

<br>
<br>

`Intention to increase the use of remote working` (*V11020*)

> Question: Do you intend to permanently change the activity of the enterprise due to the COVID-19 pandemic? Increase the use of remote working

> Report: edition 21 (1st fortnight of June)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Very likely |
| 2 | Unlikely |
| 3 | Not likely |
| 8 | Does not know / does not answer |

<br>
<br>

`Intention to change supply chains` (*V11030*)

> Question: Do you intend to permanently change the activity of the enterprise due to the COVID-19 pandemic? Change supply chains

> Report: edition 21 (1st fortnight of June)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Very likely |
| 2 | Unlikely |
| 3 | Not likely |
| 8 | Does not know / does not answer |

<br>
<br>

`Intention to increase the stocks of needed products for the activity` (*V11040*)

> Question: Do you intend to permanently change the activity of the enterprise due to the COVID-19 pandemic? Increase the stocks of needed products for the activity

> Report: edition 21 (1st fortnight of June)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Very likely |
| 2 | Unlikely |
| 3 | Not likely |
| 8 | Does not know / does not answer |

<br>
<br>

`Intention to redirect target markets` (*V11050*)

> Question: Do you intend to permanently change the activity of the enterprise due to the COVID-19 pandemic? Redirect target markets

> Report: edition 21 (1st fortnight of June)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Very likely |
| 2 | Unlikely |
| 3 | Not likely |
| 8 | Does not know / does not answer |

<br>
<br>

`Intention to change the range of products sold/services provided` (*V11060*)

> Question: Do you intend to permanently change the activity of the enterprise due to the COVID-19 pandemic? Change the range of products sold/services provided

> Report: edition 21 (1st fortnight of June)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Very likely |
| 2 | Unlikely |
| 3 | Not likely |
| 8 | Does not know / does not answer |

<br>
<br>

`Intention to change the main activity of the enterprise` (*V11070*)

> Question: Do you intend to permanently change the activity of the enterprise due to the COVID-19 pandemic? Change the main activity of the enterprise

> Weeks: edition 21 (1st fortnight of June)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Very likely |
| 2 | Unlikely |
| 3 | Not likely |
| 8 | Does not know / does not answer |

<br>
<br>

`Diversification/modification of production due to COVID pandemic` (*V2A10*)

> Question: Due to the COVID-19 pandemic is the enterprise modifying/diversifying the way it develops its activity? Diversification/modification of production

> Report: from edition 16 (13-17 April) to edition 17 (20-24 April)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Yes, totally |
| 2 | Yes, partially |
| 3 | No |
| 9 | Not applicable |

<br>
<br>

`Change/reinforce distribution channels (online, takeaway,…) due to the pandemic` (*V2A20*)

> Question: Due to the COVID-19 pandemic is the enterprise modifying/diversifying the way it develops its activity? Change/reinforce distribution channels (online, takeaway,…)

> Report: from edition 16 (13-17 April) to edition 17 (20-24 April)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Yes, totally |
| 2 | Yes, partially |
| 3 | No |
| 9 | Not applicable |

<br>
<br>


#### A2.10 Liquidity

`Importance of the simplified layoff to liquidity` (*V6110*)

> Question: What is the importance of the simplified layoff for the current liquidity situation of the enterprise?

> Report: edition 23 (1st fortnight of July)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Very relevant |
| 2 | Little relevant |
| 3 | Did not benefit from this measure |
| 8 | Does not know / does not answer |

<br>
<br>

`Importance of the moratorium for the payment of interests and principal on existing loans to liquidity` (*V6120*)

> Question: What is the importance of the moratorium for the payment of interests and principal on existing loans for the current liquidity situation of the enterprise?

> Report: edition 23 (1st fortnight of July)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Very relevant |
| 2 | Little relevant |
| 3 | Did not benefit from this measure |
| 8 | Does not know / does not answer |

<br>
<br>

`Importance of the access to new loans with low-interest or State guarantees to liquidity` (*V6130*)

> Question: What is the importance of the access to new loans with low-interest or State guarantees for the current liquidity situation of the enterprise?

> Report: edition 23 (1st fortnight of July)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Very relevant |
| 2 | Little relevant |
| 3 | Did not benefit from this measure |
| 8 | Does not know / does not answer |

<br>
<br>

`Importance of the suspension of tax and contributory obligations to liquidity` (*V6140*)

> Question: What is the importance of the suspension of the payment of tax and contributory obligations for the current liquidity situation of the enterprise?

> Report: edition 23 (1st fortnight of July)

> Classification:

| Code | Designation |
| :---: | :---------- |
| 1 | Very relevant |
| 2 | Little relevant |
| 3 | Did not benefit from this measure |
| 8 | Does not know / does not answer |


### A3. Sample variables

The variables below provide characteristics about the firms in the sample:


`Firm size` (*AGDIM*) -	categorical variable reporting the size-class of the enterprise

> Classification:

| code | Designation | Definition |
| :---: | :---------- | :----------------------:
| 1 | Microenterprise | Number of employees<10 and turnover<=2 million euros |
| 2 | Small enterprise | Number of employees<50 and turnover<=10 million euros |
| 3 | Medium-sized enterprise | Number of employees<250 and turnover<=50 million euros |
| 4 | Large enterprise | Number of employees>=250 and turnover>50 million euros |

<br>
<br>

`Sector of economic activity` (*AGCAE*) - main sector of activity defined using the Sections of the Classification of Economic Activities (CAE, Revision 3).

| code | Designation | Definition (using CAE-Rev.3 Sections) |
| :---: | :---------- | :---------- |
| 1 | Agriculture | Agriculture, farming of animals, hunting and forestry (A) |
| 2 | Manufacturing and energy | Mining and quarrying (B), Manufacturing (C), Electricity, gas, steam, cold and hot water and cold air (D) and Water collection, treatment and distribution; sewerage, waste management and remediation activities (E) |
| 3 | Construction and real estate | Construction (F) and Real estate activities (L) |
| 4 | Distributive trade | Wholesale and retail trade; repair of motor vehicles and motorcycles (G) |
| 5 | Transportation and storage | Transportation and storage (H) |
| 6 | Accommodation and food services | Accommodation and food service activities (I) |
| 7 | Information and communication | Information and communication activities (J) |
| 8 | Other services | Consultancy, scientific and technical activities (M), Administrative and support service activities (N), Education (P), Human health and social work activities (Q), Arts, entertainment, sports and recreation activities (R) and Other service activities (S) |

<br>
<br>

`Exporting profile` (*P_EXPORT*) - this variable takes value one if the firm is classified as having an exporting profile. This is the case if the exports of goods and services account for at least 50% of turnover or if the exports of goods and services are larger than 150,000 euros and account for at least 10% of turnover.

<br>
<br>

# Basic Descriptive Statistics

Table 2- Number of firms over the data period (as of July 2020 extraction)

```
    quietly use "S:/data/Products/COVID/2020_07/Output/Data/152020/IREE_I_WFRM_152020_JUL20_V01.dta", clear
    quietly append using "S:/data/Products/COVID/2020_07/Output/Data/162020/IREE_I_WFRM_162020_JUL20_V01.dta"
    quietly append using "S:/data/Products/COVID/2020_07/Output/Data/172020/IREE_I_WFRM_172020_JUL20_V01.dta"
    quietly append using "S:/data/Products/COVID/2020_07/Output/Data/182020/IREE_I_WFRM_182020_JUL20_V01.dta"
    quietly append using "S:/data/Products/COVID/2020_07/Output/Data/192020/IREE_I_WFRM_192020_JUL20_V01.dta"
    quietly append using "S:/data/Products/COVID/2020_07/Output/Data/202020/IREE_I_WFRM_202020_JUL20_V01.dta"
    quietly append using "S:/data/Products/COVID/2020_07/Output/Data/212020/IREE_I_WFRM_212020_JUL20_V01.dta"
    quietly append using "S:/data/Products/COVID/2020_07/Output/Data/222020/IREE_I_WFRM_222020_JUL20_V01.dta"
    quietly append using "S:/data/Products/COVID/2020_07/Output/Data/232020/IREE_I_WFRM_232020_JUL20_V01.dta"
    label language en
    table p_infra_cod, contents(freq) center
```

<br>
<br>

# Legislation

Some of the Portuguese legislation related to the COVID-19 pandemic is presented below [^7]:

- **Order 2836-A/2020**, March 2 - determines that all public employers must formulate a contingency plan following the guidelines of the Directorate-General of Health to prevent the risk of contagion of COVID-19 within the following five working days.

  [Internal Link](./aux_files/legislation/despacho_2836A_2020.pdf) /
  [External Link](https://dre.pt/web/guest/home/-/dre/129793730/details/maximized)

- **Order No. 3298-B/2020**, March 13 - Declares the alert situation in the national territory from March 13, 2020 to April 9, 2020

  [Internal Link](./aux_files/legislation/despacho_3298B_2020.pdf) /
  [External Link](https://dre.pt/web/guest/home/-/dre/130243048/details/maximized)

- **Resolution of the Council of Ministers No. 10-A/2020**, March 13 - approves a set of measures aimed at citizens, enterprises, public and private entities, health establishments and their employees. These measures intend to support enterprises liquidity, maintain jobs and reinforce the capacity to react and contain the COVID-19 propagation.

  [Internal Link](./aux_files/legislation/resolucao_10A_2020.pdf) /
  [External Link](https://dre.pt/web/guest/pesquisa/-/search/130243054/details/maximized)

- **Ordinance 71-A/2020**, March 15 - define the conditions to attribute extraordinary, temporary and provisional support measures to employees and employers affected by the COVID-19 pandemic.

  [Internal Link](./aux_files/legislation/portaria_71A_2020.pdf) /
  [External Link](https://dre.pt/web/guest/legislacao-consolidada/-/lc/130326119/view?w=2020-03-18)

- **Decree of the President of the Republic 14-A/2020**, March 18 - declares the state of emergency in the national territory from March 19, 2020 to April 2, 2020.

  [Internal Link](./aux_files/legislation/dpr_14A_2020.pdf) /
  [External Link](https://dre.pt/web/guest/pesquisa/-/search/130399862/details/maximized)

- **Decree no. 2-A/2020**, March 20 – following the declaration of the state of emergency, this Decree lists the essential services that will remain in operation, establishes the general duty to stay home, determines the closure of establishments within certain sectors of activity, and determines that remote working is mandatory for all tasks possible.

  [Internal Link](./aux_files/legislation/decreto_2A_2020.pdf) /
  [External Link](https://dre.pt/web/guest/legislacao-consolidada/-/lc/130531803/view?q=Decreto+n.%C2%BA%202-A%2F2020%2C%20de+20+de+mar%C3%A7o)

- **Decree-Law No. 10-J/2020**, March 26 - approves a moratorium until September 30, 2020. It forbids the revocation of contracted credit lines and provides for the extension or suspension of credits until the end of the period. It also introduces a regime of personal guarantees of the
State.

  [Internal Link](./aux_files/legislation/decreto_lei_10J_2020.pdf) /
  [External Link](https://dre.pt/web/guest/pesquisa/-/search/130779509/details/normal?l=1)


- **Decree of the President of the Republic No. 17-A/2020**, April 2 - renews the state of emergency from April 3, 2020 to April 17, 2020.

  [Internal Link](./aux_files/legislation/dpr_17A_2020.pdf) /
  [External Link](https://dre.pt/web/guest/home/-/dre/131068115/details/maximized)

- **Decree of the President of the Republic No. 20-A/2020**, April 17 - renews the declaration of the state of emergency between April 18, 2020 and May 2, 2020.

  [Internal Link](./aux_files/legislation/dpr_20A_2020.pdf) /
  [External Link](https://dre.pt/web/guest/pesquisa/-/search/131908497/details/maximized)

- **Ordinance No. 95/2020**, April 18 - creates the Incentives System to the Productive Innovation in the context of COVID-19.

  [Internal Link](./aux_files/legislation/portaria_95_2020.pdf) /
  [External Link](https://dre.pt/web/guest/pesquisa/-/search/131908530/details/maximized)

- **Resolution of the Council of Ministers No. 33-A/2020**, April 30- declares the state of calamity between May 3, 2020 and May 17, 2020.

  [Internal Link](./aux_files/legislation/resolucao_33A_2020.pdf) /
  [External Link](https://dre.pt/web/guest/pesquisa/-/search/132883344/details/maximized)

- **Resolution of the Council of Ministers No. 33-C/2020**, April 30- it establishes a progressive de-confinement strategy.

  [Internal Link](./aux_files/legislation/resolucao_33C_2020.pdf) /
  [External Link](https://dre.pt/web/guest/pesquisa/-/search/132883346/details/maximized)

- **Decree Law No. 20-G/2020**, May 14 - introduces the Program ADAPTAR, which is a system of incentives for micro and small and medium enterprises to adapt business activity to the context of the COVID-19.

  [Internal Link](./aux_files/legislation/decreto_lei_20G_2020.pdf) /
  [External Link](https://dre.pt/web/guest/pesquisa/-/search/133723684/details/maximized)

- **Resolution of the Council of Ministers No. 38/2020**, May 17 - renews the state of calamity until May 31, 2020 and establishes new measures of de-confinement.

  [Internal Link](./aux_files/legislation/resolucao_38_2020.pdf) /
  [External Link](https://dre.pt/pesquisa/-/search/133914977/details/maximized)

- **Resolution of the Council of Ministers No. 40-A/2020**, May 29 -renews the state of calamity until June 14, 2020.

  [Internal Link](./aux_files/legislation/resolucao_40A_2020.pdf) /
  [External Link](https://dre.pt/web/guest/pesquisa/-/search/134889278/details/maximized)

- **Resolution of the Council of Ministers No. 41/2020**, June 6 - approves the Economic and Social Stabilization Program.

  [Internal Link](./aux_files/legislation/resolucao_41_2020.pdf) /
  [External Link](https://dre.pt/web/guest/pesquisa/-/search/135391594/details/maximized)

- **Resolution of the Council of Ministers No. 43-B/2020**, June 12 - Extends the declaration of the situation of calamity until June 28, 2020.

  [Internal Link](./aux_files/legislation/resolucao_43B_2020.pdf) /
  [External Link](https://dre.pt/web/guest/pesquisa/-/search/135711302/details/maximized)

- **Resolution of the Council of Ministers No. 51-A/2020**, June 26 - declares the state of calamity in 19 civil parishes in Lisbon, the state of contingency in the Metropolitan Area of Lisbon and the state of alert in the remaining areas of the national territory until July 14, 2020.

  [Internal Link](./aux_files/legislation/resolucao_51A_2020.pdf) /
  [External Link](https://dre.pt/web/guest/pesquisa/-/search/136788888/details/maximized)

  <br>
  <br>

[^7]: A complete list of all the legislation is available in [Diário da República Electrónico](https://dre.pt/legislacao-covid-19-por-data-de-publicacao)

# Auxiliary Files
For a description of each variable in each dataset (name, unit of measurement, data and storage type, format, moment of first and last observation), an account of the changes occurred over time, summary statistics for each dataset and a codebook for each dataset please check the following auxiliary files[^8]:

| File | Description of Variables | Summary Statistics | Codebook | Dataset Description |
| :---- | :----: | :----: | :----: |  :----: |
| Summary of all variables (Portuguese and English labels) | [variables_pt_en.html](./aux_files/variables_description/iree_vars_pt_en.html) | | | |
| General Information File | [iree_vars](./aux_files/variables_description/iree_vars.html) | [iree_stat](./aux_files/descriptive_statistics/iree_stat.html) | [iree_cdbk](./aux_files/codebook/iree_cdbk.html) | [iree_dscr](./aux_files/describe_dataset/iree_dscr.html) |


[^8]: The Summary Statistics, Codebook and Dataset Description files are available on BPLIM's servers.

# Auxiliary Tools

The Stata ado-file [*ireepanel.ado*](https://github.com/BPLIM/Tools/tree/master/ados/IREE/ireepanel) is available upon request. This command allows to assemble the panel data set of the Fast and Exceptional Enterprise Survey - COVID-19 (COVID-IREE) using the data files for each survey's edition made available by BPLIM.

The ado constructs the panel data set by appending the data for each survey's edition and allows to arrange the data in the long or wide format. Please note that the change in the reference period from a week to a fortnight from Edition 19 onwards and the reformulation of some questions as detailed in the section [Description of Variables](#description-of-variables) may affect the comparability of the data over time.
The command applies labels and value labels in Portuguese and English to all variables and recodes the missing values of the questions that were not included in a given edition of the survey to ".a".


# Useful Links

- [INE's information about COVID-19](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_cont_inst&INST=429957064)

- [Banco de Portugal's webpage dedicated to the IREE survey](https://www.bportugal.pt/page/quais-os-impactos-do-covid-19-na-economia-portuguesa)

- Monitoring Reports:

| Monitoring Reports | Link |
| :------ | :----------------------: |
| edition 15 (6-10 April 2020) | [PT](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_destaques&DESTAQUESdest_boui=428264268&DESTAQUESmodo=2&xlang=pt)  /  [EN](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_destaques&DESTAQUESdest_boui=428264268&DESTAQUESmodo=2&xlang=en) |
| edition 16 (13-17 April 2020) | [PT](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_destaques&DESTAQUESdest_boui=429164016&DESTAQUESmodo=2&xlang=pt)  /  [EN](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_destaques&DESTAQUESdest_boui=429164016&DESTAQUESmodo=2&xlang=en) |
| edition 17 (20-24 April 2020) | [PT](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_destaques&DESTAQUESdest_boui=430126865&DESTAQUESmodo=2&xlang=pt)  /  [EN](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_destaques&DESTAQUESdest_boui=430126865&DESTAQUESmodo=2&xlang=en) |
| edition 18 (27 April - 1 May 2020) | [PT](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_destaques&DESTAQUESdest_boui=431948930&DESTAQUESmodo=2&xlang=pt)  /  [EN](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_destaques&DESTAQUESdest_boui=431948930&DESTAQUESmodo=2&xlang=en) |
| edition 19 (1st fortnight of May) | [PT](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_destaques&DESTAQUESdest_boui=433558745&DESTAQUESmodo=2&xlang=pt)  /  [EN](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_destaques&DESTAQUESdest_boui=433558745&DESTAQUESmodo=2&xlang=en) |
| edition 20 (2nd fortnight of May) | [PT](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_destaques&DESTAQUESdest_boui=436445521&DESTAQUESmodo=2&xlang=pt)  /  [EN](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_destaques&DESTAQUESdest_boui=436445521&DESTAQUESmodo=2&xlang=en) |
| edition 21 (1st fortnight of June) | [PT](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_destaques&DESTAQUESdest_boui=438549283&DESTAQUESmodo=2&xlang=pt) / [EN](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_destaques&DESTAQUESdest_boui=438549283&DESTAQUESmodo=2&xlang=en) |
| edition 22 (2nd fortnight of June) | [PT](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_destaques&DESTAQUESdest_boui=440673085&DESTAQUESmodo=2&xlang=pt) / [EN](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_destaques&DESTAQUESdest_boui=440673085&DESTAQUESmodo=2&xlang=en) |
| edition 23 (1st fortnight of July) | [PT](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_destaques&DESTAQUESdest_boui=442426360&DESTAQUESmodo=2) / [EN](https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_destaques&DESTAQUESdest_boui=442426360&DESTAQUESmodo=2&xlang=en) |

- [Measures presented by the Government due to the COVID-19 pandemic](https://covid19estamoson.gov.pt/medidas-de-apoio-emprego-empresas/)

- [Simplified Layoff](https://www.dgert.gov.pt/covid-19-perguntas-e-respostas-para-trabalhadores-e-empregadores-faq/medidas-excecionais-e-temporarias-de-resposta-a-epidemia-covid-19)

- Conselho Nacional de Supervisores Financeiros (2020). [Principais medidas adotadas para mitigação dos impactos da pandemia de COVID-19: uma análise comparativa.](https://www.cmvm.pt/pt/CMVM/CNSF/ConselhoNacionalDeSupervisoresFinanceiros/Documents/Nota%20sobre%20as%20principais%20medidas%20adotadas%20para%20mitiga%C3%A7%C3%A3o%20dos%20impactos%20da%20pandemia%20de%20COVID-19%20-%20uma%20an%C3%A1lise%20comparativa.pdf)


# Citation of this dataset
Statistics Portugal and Bank of Portugal (2020): Fast and Exceptional Enterprise Survey – COVID-19. Extraction: July 2020. Version: V1.

# References

INE (2020). [Documento Metodológico: Inquérito Rápido e Excecional às Empresas - COVID19. Versão 1.0.](http://smi.ine.pt/DocumentacaoMetodologica/Detalhes/1593)







