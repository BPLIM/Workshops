---
title: Variables in the Monetary Financial Institutions Balance Sheet Database
subtitle: Extraction Date -  June 2024
date: June 2024
doi: 110.17900/BBS.JUN2023.V1
pdf-engine: pdflatex
execute:
  echo: false
format:
  html:
    theme: default
jupyter: nbstata
---

# Table of Contents
1. [Variable Description](#variable-description)

2. [Time Series](#time-series)


## Variable Description

| Variable                    | Designation                                                                                    | Scale of Measurement   | Data type              | Storage type           | Start                  | End                    |
| :---:                    | :---:                                                                                    | :---:  | :---:             | :---:           | :---:                  | :---:                    |
| *bina*                      | Anonymized bank identificaton number                                                           | code                   | discrete               | int                    | 1997m9                 | 2023m12               |
| *date*                      | Reference monthh                                                                               | month                  | discrete               | int                    | 1997m9                 | 2023m12               |
| *instrument_asset*          | Financial instruments: asset side                                                              | code                   | discrete               | int                    | 1997m9                 | 2023m12               |
| *instrument_liab*           | Financial instruments: liability side                                                          | code                   | discrete               | int                    | 1997m9                 | 2023m12               |
| *counterparty_asset*        | Classification of counterparty: asset side                                                     | code                   | discrete               | int                    | 1997m9                 | 2023m12               |
| *counterparty_liab*         | Classification of counterparty: liability side                                                 | code                   | discrete               | int                    | 1997m9                 | 2023m12               |
| *country*                   | Country of origin or region of the counterparty                                                | code                   | string                 | str5                   | 1997m9                 | 2023m12               |
| *inst_type*                 | Type of institution                                                                            | code                   | discrete               | byte                   | 2014m12                | 2023m12               |
| *value*                     | Amount                                                                                         | million euros          | continuous             | double                 | 1997m9                 | 2023m12               |

[Return](#table-of-contents)

## Time Series

| Variable                          | Sep 1997 - Nov 2014                                                                  | Dec 2014 - Dec 2023                                                    |
| :---:                    | :---:                                                                                    | :---:  |
| *bina*                            | [✓]                                                                                  | [✓]             | *date*                            | [✓]                                                                                  | [✓]                                                                    |
| *instrument_asset*                | [Classification 97](#asset-instrument-classification-1997)                           | [Classification 2014](#asset-instrument-classification-2014)           |
| *instrument_liab*                 | [Classification 97](#liability-instrument-classification-1997)                       | [Classification 2014](#liability-instrument-classification-2014)       |
| *counterparty_asset*              | [Classification 97](#asset-counterparty-classification-1997)                         | [Classification 2014](#asset-counterparty-classification-2014)         |
| *counterparty_liab*               | [Classification 97](#liability-counterparty-classification-1997)                     | [Classification 2014](#liability-counterparty-classification-2014)     |
| *country*                         | [Country](#country)                                                                  | [Country](#country)                                                    |
| *inst_type*                       | [X]                                                                                  | [Institution Type](#institution-type)                                  |
| *value*                           | [✓]                                                                                  | [✓]

| Legend |    |
| :---: | :------: |
| [✓] | Variable available  |
| [X] | Variable not available |

[Return](#table-of-contents)



## Asset Instrument Classification 1997

| Code |	Designação | Designation |
| :---: | :----- | :----- |
|	10	|	Notas e Moedas	|	Banknotes and coins	|
|	20	|	Créditos e equiparados - Até 1 ano	|	Credit and equivalent - up to 1 year	|
|	30	|	Créditos e equiparados - De 1 a 5 anos	|	Credit and equivalent - from 1 year to 5 years	|
|	40	|	Créditos e equiparados - A mais de 5 anos	|	Credit and equivalent - more than 5 years	|
|	50	|	Títulos exceto participações - Até 1 ano	|	Securities other than equity - up to 1 year	|
|	60	|	Títulos exceto participações - De 1 a 2 anos	|	Securities other than equity -  from 1 year to 2 years	|
|	70	|	Títulos exceto participações - A mais de 2 anos	|	Securities other than equity - more than 2 years	|
|	80	|	Participações	|	Equity securities	|
|	90	|	Participações, das quais unidades de participação	|	Units (included in equity securities)	|
|	100	|	Imóveis, mobiliário e material	|	Properties, furnitures, and equipments	|
|	110	|	Ativos diversos	|	Miscellaneous assets	|

[Return](#table-of-contents)


## Asset Instrument Classification 2014

| Code |	Designação | Designation |
| :---: | :----- | :----- |
|	10	|	Notas e moedas	|	Banknotes and coins	|
|	20	|	Créditos e equiparados - Até 1 ano	|	Credit and equivalent - up to 1 year	|
|	30	|	Créditos e equiparados - De 1 a 2 anos	|	Credit and equivalent - from 1 year to 2 years	|
|	40	|	Créditos e equiparados - De 2 a 5 anos	|	Credit and equivalent - from 2 year to 5 years	|
|	50	|	Créditos e equiparados - A mais de 5 anos	|	Credit and equivalent - more than 5 years	|
|	60	|	Títulos de dívida - Até 1 ano	|	Debt securities - up to 1 year	|
|	70	|	Títulos de dívida - De 1 a 2 anos	|	Debt securities -  from 1 year to 2 years	|
|	80	|	Títulos de dívida - A mais de 2 anos	|	Debt securities - more than 2 years	|
|	90	|	Ações cotadas	|	Traded shares	|
|	100	|	Ações não cotadas	|	Untraded shares	|
|	110	|	Outras participações	|	Other equities	|
|	120	|	Unidades de participação	|	Units	|
|	130	|	Imóveis, mobiliário e material	|	Properties, furnitures, and equipments	|
|	140	|	Ativos diversos	|	Miscellaneous assets	|


[Return](#table-of-contents)



## Liability Instrument Classification 1997

| Code |	Designação | Designation |
| :---: | :----- | :----- |
|	130	|	Responsabilidades à vista (exceto depósitos de poupança à vista)	|	Demand deposits (excluding sight deposits)	|
|	140	|	Depósitos com pré-aviso (incluindo depósitos de poupança à vista) - Até 90 dias	|	Deposits redeemable at a notice of up to 90 days  (excluding sight deposits)	|
|	150	|	Depósitos com pré-aviso (incluindo depósitos de poupança à vista) - A mais 90 dias	|	Deposits redeemable at a notice of more than 90 days  (including sight deposits)	|
|	170	|	Depósitos e equiparados (exceto responsabilidades à vista, depósitos com pré-aviso e acordos de recompra) - Até 1 ano	|	Deposits and equivalent  (excluding demand deposits, deposits redeemable at notice, and trading liabilities) - up to 1 year	|
|	180	|	Depósitos e equiparados (exceto responsabilidades à vista, depósitos com pré-aviso e acordos de recompra) - De 1 a 2 anos	|	Deposits and equivalent  (excluding demand deposits, deposits redeemable at notice, and trading liabilities) - from 1 to 2 years	|
|	190	|	Depósitos e equiparados (exceto responsabilidades à vista, depósitos com pré-aviso e acordos de recompra) - A mais de 2 anos	|	Deposits and equivalent  (excluding demand deposits, deposits redeemable at notice, and trading liabilities) - more than 2 years	|
|	200	|	Acordos de recompra	|	Trading liabilities	|
|	210	|	Títulos exceto capital - Até 1 ano	|	Secutities other than capital - up to 1 year	|
|	220	|	Títulos exceto capital - De 1 a 2 anos	|	Secutities other than capital - from 1 to 2 years	|
|	230	|	Títulos exceto capital - A mais de 2 anos	|	Secutities other than capital - from 2 years	|
|	240	|	Capital e reservas	|	Capital and reserves	|
|	260	|	Passivos diversos	|	Miscellaneous liabilities	|


[Return](#table-of-contents)


## Liability Instrument Classification 2014

| Code |	Designação | Designation |
| :---: | :----- | :----- |
|	380	|	Responsabilidades à vista (exceto depósitos de poupança à vista)	|	Demand deposits (excluding sight deposits)
|	390	|	Depósitos com pré-aviso (incluindo depósitos de poupança à vista) - Até 90 dias	|	Deposits redeemable at a notice of up to 90 days  (excluding sight deposits)
|	400	|	Depósitos com pré-aviso (incluindo depósitos de poupança à vista) - A mais de 90 dias	|	Deposits redeemable at a notice of more than 90 days  (including sight deposits)
|	420	|	Depósitos e equiparados (exceto responsabilidades à vista, depósitos com pré-aviso e acordos de recompra) - Até 1 ano	|	Deposits and equivalent  (excluding demand deposits, deposits redeemable at notice, and trading liabilities) - up to 1 year
|	430	|	Depósitos e equiparados (exceto responsabilidades à vista, depósitos com pré-aviso e acordos de recompra) - De 1 a 2 anos	|	Deposits and equivalent  (excluding demand deposits, deposits redeemable at notice, and trading liabilities) - from 1 to 2 years
|	440	|	Depósitos e equiparados (exceto responsabilidades à vista, depósitos com pré-aviso e acordos de recompra) - A mais de 2 anos	|	Deposits and equivalent  (excluding demand deposits, deposits redeemable at notice, and trading liabilities) - more than 2 years
|	450	|	Acordos de recompra - Até 1 ano	|	Trading liabilities - up to 1 year
|	460	|	Acordos de recompra - A mais de 1 ano	|	Trading liabilities - more than 1 year
|	470	|	Títulos de dívida emitidos - Até 1 ano	|	Debt securities issued - up to 1 year
|	480	|	Títulos de dívida emitidos - De 1 a 2 anos	|	Debt securities issued - from 1 to 2 years
|	490	|	Títulos de dívida emitidos - A mais de 2 anos	|	Debt securities issued - more than 2 years
|	500	|	Capital e reservas	|	Capital and reserves
|	520	|	Passivos diversos	|	Miscellaneous Liabilities


[Return](#table-of-contents)



## Asset Counterparty Classification 1997

| Code |	Designação | Designation |
| :---: | :----- | :----- |
|	10	|	Instituições financeiras monetárias	|	Monetary financial institutions	|
|	20	|	Outros intermediários financeiros e auxiliares financeiros	|	Other financial intermediaries and financial auxiliaries	|
|	30	|	Sociedades de seguros e fundos de pensões	|	Insurance corporations and pension funds	|
|	40	|	Administração central	|	Central government	|
|	50	|	Administração regional	|	Regional government	|
|	60	|	Administração local	|	Local government	|
|	70	|	Segurança social	|	Social security	|
|	80	|	Sociedades não financeiras	|	Non-financial institutions	|
|	90	|	Particulares	|	Individuals	|
|	120	|	Setorização não relevante/ não possível	|	Irrelevant sector	|


[Return](#table-of-contents)


## Asset Counterparty Classification 2014

| Code |	Designação | Designation |
| :---: | :----- | :----- |
|	11	|	Bancos Centrais	|	Central banks	|
|	12	|	Fundos do mercado monetário	|	Money market funds 	|
|	13	|	Entidades depositárias, exceto o Banco Central	|	Deposit institutions, excluding central banks	|
|	18	|	Outros intermediários financeiros, auxiliares financeiros e instituições financeiras cativas e prestamistas	|	Other financial intermediaries, financial auxiliaries, and captive financial institutions and money lenders 	|
|	22	|	Fundos de investimento, exceto fundos do mercado monetário	|	investment fund, excluding money market funds	|
|	31	|	Sociedades de seguros	|	Insurance corporations	|
|	32	|	Fundos de pensões	|	Pension funds	|
|	40	|	Administração central	|	Central government	|
|	50	|	Administração regional	|	Regional government	|
|	60	|	Administração local	|	Local government	|
|	70	|	Segurança social	|	Social security	|
|	80	|	Sociedades não financeiras	|	Non-financial institutions	|
|	91	|	Famílias	|	Family	|
|	92	|	Instituições sem fins lucrativos ao serviço das famílias	|	Non-profit institutions serving households	|
|	120	|	Setorização não relevante/ não possível	|	Irrelevant sector	|


[Return](#table-of-contents)



## Liability Counterparty Classification 1997

| Code |	Designação | Designation |
| :---: | :----- | :----- |
|	10	|	Bancos Centrais	|	Central banks	|
|	20	|	OIFM 1: instituições não sujeitas a reservas mínimas, nomeadamente os Fundos do Mercado Monetário	|	Institutions not subject to minimum reserves, namely the money market funds	|
|	30	|	OIFM 2: instituições sujeitas a reservas mínimas	|	Institutions subject to minimum reserves	|
|	40	|	Outros intermediários financeiros e auxiliares financeiros	|	Other financial intermediaries and financial auxiliaries	|
|	50	|	Sociedades de seguros e fundos de pensões	|	Insurance corporations and pension funds	|
|	60	|	Administração central	|	Central government	|
|	70	|	Administração regional	|	Regional government	|
|	80	|	Administração local	|	Local government	|
|	90	|	Segurança social	|	Social security	|
|	100	|	Sociedades não financeiras	|	Non-financial institutions	|
|	110	|	Particulares	|	Individuals	|
|	120	|	Setorização não relevante/ não possivel	|	Irrelevant sector	|


[Return](#table-of-contents)


## Liability Counterparty Classification 2014

| Code |	Designação | Designation |
| :---: | :----- | :----- |
|	10	|	Bancos Centrais	|	Central banks	|
|	21	|	Fundos do mercado monetário	|	Money market funds 	|
|	22	|	Entidades depositárias, exceto o Banco Central	|	Deposit institutions, excluding central banks	|
|	39	|	Outros intermediários financeiros, auxiliares financeiros e instituições financeiras cativas e prestamistas	|	Other financial intermediaries, financial auxiliaries, and captive financial institutions and money lenders 	|
|	43	|	Fundos de investimento, exceto fundos do mercado monetário	|	investment fund, excluding money market funds	|
|	51	|	Sociedades de seguros	|	Insurance corporations	|
|	52	|	Fundos de pensões	|	Pension funds	|
|	60	|	Administração central	|	Central government	|
|	70	|	Administração regional	|	Regional government	|
|	80	|	Administração local	|	Local government	|
|	90	|	Segurança social	|	Social security	|
|	100	|	Sociedades não financeiras	|	Non-financial institutions	|
|	111	|	Famílias	|	Family	|
|	112	|	Instituições sem fins lucrativos ao serviço das famílias	|	Non-profit institutions serving households	|
|	120	|	Setorização não relevante/ não possível	|	Irrelevant sector	|



[Return](#table-of-contents)


## Country

| Code |	Designação | Designation |
| :---: | :----- | :----- |
|	UM-PT	|	Países da União Monetária excluindo Portugal 	|	Monetary Union countries excluding Portugal 	|
|	PT-UM	|	Países Fora da União Monetária	|	Countries outside Monetary Union	|
|	EUB	|	Banco Central Europeu	|	European Central Bank	|
|	AUT	|	Austria	|	Austria	|
|	BEL	|	Bélgica	|	Belgium	|
|	CYP	|	Chipre	|	Cyprus	|
|	DEU	|	Alemanha	|	Germany	|
|	ESP	|	Espanha	|	Spain	|
|	EST	|	Estónia	|	Estonia	|
|	FIN	|	Finlândia	|	Finland	|
|	FRA	|	França	|	France	|
|	GRC	|	Grécia	|	Greece	|
|	IRL	|	Irlanda	|	Ireland	|
|	ITA	|	Itália	|	Italy	|
|	LTU	|	Lituânia	|	Lithuania	|
|	LUX	|	Luxemburgo	|	Luxembourg	|
|	LVA	|	Letónia	|	Latvia	|
|	MLT	|	Malta	|	Malta	|
|	NLD	|	Holanda	|	Netherlands	|
|	PRT	|	Portugal 	|	Portugal	|
|	SVK	|	Eslováquia	|	Slovakia	|
|	SVN	|	Eslovénia	|	Slovenia	|


[Return](#table-of-contents)



## Institution Type

| Code |	Designação | Designation |
| :---: | :----- | :----- |
|	1	|	Bancos	|	Banks	|
|	2	|	Caixas Económicas	|	Saving banks	|
|	3	|	Fundos do Mercado Monetário	|	Money market fund	|
|	4	|	Caixa Central e Caixas de Crédito Agrícola Mútuo	|	Central agricultural credit bank and mutual agricultural credit banks	|
