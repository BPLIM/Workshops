<meta charset="utf-8"/>
# Central Balance Sheet Database
# Corporate Actions File

[1. Variables Description](#variables-description)

[2. Time Series](#time-series)


## Variables Description

| Name | Description | Unit of measurement | Start Time | End time | Changes in classification |
| :--------: | :-------------: | :-------: | :-----: | :-----: | :-----: |
| ano | Year of reference | years | 2006 | 2018 | no |
| **Identifiers** |
| tina_origem | Anonymized Tax Identification Number - Firm of origin | code | 2006 | 2018 | no |
| tina_destino | Anonymized Tax Identification Number - Firm of destination | code | 2006 | 2018 | no |
| numordem | Number of Order | code | 2006 | 2018 | no |
| **Information on the Corporate Action**  |       |      |      |     |        |
| tipoacont | Type of corporate action | code | 2006 | 2018 | no |
| mesesparagem | Number of months of activity interruption | number of months | 2006 | 2018 | no |
| efeitocontas |  Effect on financial statements | dummy | 2006 | 2018 | no |
| efeitopessoal | Effect on employment information | dummy | 2006 | 2018 | no |
| efeitobalanco | Effect on balance sheet | dummy | 2006 | 2018 | no |
| efeitodemresult | Effect on profit and loss statement | dummy | 2006 | 2018 | no |




## Time Series

|     |   2006 | 2007 | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 |
| :--- |  :---: | :---: |  :---: |  :---: |  :---: |  :---: |  :---: |  :---: |  :---: |  :---: | :---: | :---: | :---: |   
| ano |	[✓] | [✓]	| [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| tina_origem | [✓] | [✓]	| [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| tina_destino | [✓] | [✓]	| [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| numordem | [✓] | [✓]	| [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| tipoacont  | [Type of Corporate Action](#type-of-corporate-action) | [Type of Corporate Action](#type-of-corporate-action)	| [Type of Corporate Action](#type-of-corporate-action) | [Type of Corporate Action](#type-of-corporate-action) | [Type of Corporate Action](#type-of-corporate-action) | [Type of Corporate Action](#type-of-corporate-action) | [Type of Corporate Action](#type-of-corporate-action) | [Type of Corporate Action](#type-of-corporate-action) | [Type of Corporate Action](#type-of-corporate-action) | [Type of Corporate Action](#type-of-corporate-action) | [Type of Corporate Action](#type-of-corporate-action) | [Type of Corporate Action](#type-of-corporate-action) | [Type of Corporate Action](#type-of-corporate-action) |
| mesesparagem | [✓] | [✓]	| [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| efeitocontas | [✓] | [✓]	| [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| efeitopessoal | [✓] | [✓]	| [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| efeitobalanco | [✓] | [✓]	| [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| efeitodemresult |  [✓] | [✓]	| [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |


| Legend |    |
| :---: | :------ |
| [✓] | Variable available in year t |
| [x] | Variable not available in year t |


## Type of Corporate Action

| Code | Designação | Designation |
| :---: | :--- | :--- |
| 10 | Fusão | Merge |
| 20 | Cisão | Split |
| 30 | Paragem prolongada em empresas sem atividade sazonal (> 3 meses, consecutivos ou não) | Activity Interruption by non-seasonal companies (>3 months, consecutive or not) |
| 62 | Encerramento de parte significativa de património produtivo sem cisão | Dissolution of a significant part of productive assets without split |
| 67 | Outros acontecimentos marcantes | Other corporate actions |
| 70 | Alienação de parte significativa do património produtivo | Disposal of a significant part of productive assets |
| 71 | Aquisição de parte significativa do património produtivo | Acquisition of a significant part of productive assets |
| 72 | Transferência de parte significativa do património produtivo | Transfer of a significant part of productive assets |
| 78 | Mudança de atividade com manutenção da atividade da empresa original  com criação de outra empresa | Change of economic activity with the creation of a new firm |
| 79 | Mudança de atividade com manutenção da atividade da empresa original  sem criação de outra empresa | Change of economic activity without the creation of a new firm |

[return](#time-series)







