<meta charset="utf-8"/>

# PT2020 database
# General Information File

[1. Variables Description](#variables-description)

## Variables Description

| Name | Description (Portuguese) | Description (English) | Unit of measurement |  Changes in classification |
| :--------: | :-------------: | :-------------: | :-------: | :-----: |
| **Identifiers** |
| codopa | Código de operação anonimizado | Anonymized operation code | code | no |
| tina | Número de identificação fiscal anonimizado | Anonymized tax identification number | code | no |
| **Other variables** |
| ano_aac | Ano do aviso de abertura de candidatura | Year of the call for applications | year | no |
| [apoiado](#funded-project) | Projeto apoiado | Funded project | dummy | no |
| [comexecucao](#project-in-implementation) | Projeto com execução | Project in implementation | dummy | no |
| [compagamentos](#project-with-payments) | Projeto com pagamentos | Project with payments | dummy | no |
| data_aprov | Data de aprovação | Date of approval | date (month/year) | no |
| datacand | Data da candidatura | Date of the application | date (month/year) | no |
| dataenc | Data de aprovação do encerramento | Date of the project closure approval | date (month/year) | no |
| datatermoaceit | Data do termo de aceitação/contrato | Date of the grant agreement/contract | date (month/year) | no |
| dataultdec | Data da última decisão | Date of the last decision | date (month/year) | no |
| dec_datainiproj | Data de início do projeto (prevista à data de decisão) | Date of project start (predicted at the decision date) | date (month/year) | no |
| dec_datafimproj | Data de fim do projeto (prevista à data de decisão) | Date of project end (predicted at the decision date) | date (month/year) | no |
| dec_despesapublica | Despesa pública aprovada (à data de decisão) | Approved public expenditure (at the decision date) | euros | no |
| dec_incentivoaprov | Incentivo aprovado (à data de decisão) | Approved incentive (at the decision date) | euros | no |
| dec_incentivonaoreemb | Incentivo não reembolsável (à data de decisão) | Non-repayable incentive (at the decision date) | euros | no |
| dec_incentivoreemb | Incentivo reeembolsável (à data de decisão) | Repayable incentive (at the decision date) | euros | no |
| dec_investaprov | Investimento aprovado (à data de decisão) | Approved investment (at the decision date) | euros | no |
| dec_investeleg | Investimento elegível aprovado (à data de decisão) | Eligible approved investment (at the decision date) | euros | no |
| [dstanl](#decommitment-or-withdrawal) | Desistência/Anulação | Decommitment / Withdrawal | code | no |
| [comenc](#closed-project) | Projeto com encerramento | Closed project | dummy | no |
| enc_datainiproj | Data de início do projeto (à data de encerramento) | Date of project start (at the closure date) | date (month/year) | no |
| enc_datafimproj | Data de fim do projeto (à data de encerramento) | Date of project end (at the closure date) | date (month/year) | no |
| enc_despesapublica | Despesa pública aprovada (à data de encerramento) | Approved public expenditure (at the closure date) | euros | no |
| enc_incentivoaprov | Incentivo aprovado (à data de encerramento) | Approved incentive (at the closure date) | euros | no |
| enc_incentivonaoreemb | Incentivo não reembolsável (à data de encerramento) | Non-repayable incentive (at the closure date) | euros | no |
| enc_incentivoreemb | Incentivo reembolsável (à data de encerramento) | Repayable incentive (at the closure date) | euros | no |
| enc_investaprov | Investimento aprovado (à data de encerramento) | Approved investment (at the closure date) | euros | no |
| enc_investeleg | Investimento elegível aprovado (à data de encerramento) | Eligible approved investment (at the closure date) | euros | no |
| exec_despesapublica | Despesa pública executada | Implemented public expenditure | euros | no |
| exec_incentivofundo | Incentivo/fundo executado | Implemented incentive/fund | euros | no |
| exec_investeleg | Investimento elegível executado | Implemented eligible investment | euros | no |
| exec_outrasfontesfinanc | Outra(s) fontes de financiamento executado | Other source(s) of funding implemented | euros | no |
| [fonte](#source-of-the-data) | Fonte dos dados | Source of the data | code | no |
| [fundo](#european-structural-and-investment-fund) | Fundo Europeu Estrutural e de Investimento | European structural and investment fund | code | no |
| incentivocontrat | Incentivo contratado | Contracted incentive | euros | no |
| [instrumento](#incentive-system) | Sistema de Incentivos | Incentive System | code | no |
| investcand | Investimento associado à candidatura | Application investment | euros | no |
| [medida](#measure) | Medida | Measure | code | no |
| [nprojaprov](#active-project) | Projeto ativo | Active project | dummy | no |
| [ot](#thematic-objective) | Objetivo temático | Thematic Objective | code | no |
| pagadiantcertif | Pagamentos adiantados certificáveis | Certifiable advance payments | euros | no |
| pagadiantnaocertif | Pagamentos adiantados não certificáveis | Non-certifiable advance payments | euros | no |
| pagamentos_reembolso | Pagamentos por reembolso | Refund payments | euros | no |
| [pi](#investment-priority) | Prioridade de investimento | Investment priority | code | no |
| [pofinan](#operational-programme) | Programa operacional | Operational programme | code | no |
| pontuacao | Pontuação do projeto | Project score | code | no |
| [comta](#project-with-grant-agreement) | Projeto com termo de aceitação | Project with grant agreement | dummy | no |
| [ti](#intervention-typology) | Tipologia de intervenção | Intervention typology | code | no |
| totpagam_realizado | Pagamento total realizado | Total payments | euros | no |



## Funded project

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 0	| 0 Não	| 0 No |
| 1 | 1 Sim	| 1 Yes |

[return](#variables-description)

## Project in implementation

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 0	| 0 Não	| 0 No |
| 1 | 1 Sim	| 1 Yes |

[return](#variables-description)


## Project with payments

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 0	| 0 Não	| 0 No |
| 1 | 1 Sim	| 1 Yes |

[return](#variables-description)

## Decommitment or Withdrawal

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1	| 1 Anulação | 1 Decommitment |
| 2 | 2 Desistência | 2 Withdrawal |


[return](#variables-description)

## Closed project

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 0	| 0 Não	| 0 No |
| 1 | 1 Sim	| 1 Yes |

[return](#variables-description)

## Source of the data

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1 |	1 SGO	| 1 SGO |
| 2 | 2 SIFSE	| 2 SIFSE |

[return](#variables-description)

## European structural and investment fund

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1	| 1 Fundo Europeu de Desenvolvimento Regional	| 1 European Regional Development Fund |
| 2 | 2 Fundo Social Europeu | 2 European Social Fund |


[return](#variables-description)

## Incentive System

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1	| 1 Formação Autónoma	| 1 Autonomous Training |
| 2	| 2 Sistema de Incentivos à I&D Empresarial	| 2 Enterprise R&D Incentive System |
| 3	| 3 Sistema de Incentivos à Inovação Empresarial | 3 Innovation Incentive System |
| 4 | 4 Sistema de Incentivos à Qualificação e Internacionalização de PME | 4 Incentive System for the Qualification and Internationalization of SMEs |

[return](#variables-description)

## Measure

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

[return](#variables-description)

## Active project

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 0	| 0 Não	| 0 No |
| 1 | 1 Sim	| 1 Yes |

[return](#variables-description)

## Thematic Objective

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1 | 01 OT 1 - Reforçar a investigação, o desenvolvimento tecnológico e a inovação | 01 TO 1 – Strengthening research, technological development and innovation |
| 2 | 02 OT 3 - Reforçar a competitividade das pequenas e médias empresas | 02 TO 3 – Enhancing the competitiveness of small and medium-sized enterprises |
| 3 | 03 OT 8 – Promover a sustentabilidade e a qualidade do emprego e apoiar a mobilidade laboral | 03 TO 8 – Promoting sustainable and quality employment and supporting labour mobility |

[return](#variables-description)

## Investment priority

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1 | 1 PI 1.2 - Promoção do investimento das empresas em inovação e investigação | 1 IP 1.2 - Promoting enterprise investment in innovation and research |
| 2 | 2 PI 3.1 - Promoção do espírito empresarial | 2 IP 3.1 - Promoting entrepreneurship |
| 3 | 3 PI 3.2 - Desenvolvimento e aplicação de novos modelos empresariais para as PME | 3 IP 3.2 - Development and application of new business models for SMEs |
| 4 | 4 PI 3.3 - Apoio à criação e alargamento de capacidades avançadas de desenvolvimento de produtos e serviços | 4 IP 3.3 - Supporting the creation and extension of advanced capabilities in the development of products and services |
| 5 | 5 PI 8.5 - Adaptação de trabalhadores, empresas e empresários à mudança | 5 IP 8.5 - Adaptability of workers, enterprises and entrepreneurs to change |

[return](#variables-description)

## Operational programme

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1 | 1 PO Alentejo | 1 OP Alentejo |
| 2 | 2 PO Algarve | 2 OP Algarve |
| 3 | 3 PO Competitividade e Internacionalização | 3 OP Competitiveness and Internationalization |
| 4 | 4 PO Centro | 4 OP Centre |
| 5 | 5 PO Lisboa | 5 OP Lisbon |
| 6 | 6 PO Norte | 6 OP North |

[return](#variables-description)

## Project with grant agreement

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 0	| 0 Não	| 0 No |
| 1 | 1 Sim	| 1 Yes |

[return](#variables-description)

## Intervention typology

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

[return](#variables-description)
