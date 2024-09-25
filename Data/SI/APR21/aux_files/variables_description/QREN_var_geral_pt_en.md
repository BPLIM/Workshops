<meta charset="utf-8"/>

# QREN
# General Information File

[1. Variables Description](#variables-description)

## Variables Description

| Name | Description (Portuguese) | Description (English) | Unit of measurement |  Changes in classification |
| :--------: | :-------------: | :-------------: | :-------: | :-----: |
| **Identifiers** |
| nproja | Número do projeto anonimizado | Number of the project anonymized | code | no |
| tina_promotor | Número de identificação fiscal do promotor anonimizado | Tax identification number of the promoter anonymized | code | no |
| **Other variables** |
| [autoridadegestao](#managing-authority) | Autoridade de Gestão | Managing Authority | code | no |
| [comptrf](#with-final-reimbursement-payment) | Com Pagamento a Título de Reembolso Final | With Final Reimbursement Payment | one or missing value | no |
| data1comunicacao | Data da primeira comunicação | Date of the first communication | date (month/year) | no |
| data1decisao | Data da primeira decisão | Date of the first decision | date (month/year) | no |
| datacand | Data da candidatura | Date of the application | date (month/year) | no |
| datacontrato | Data do contrato | Date of the contract | date (month/year) | no |
| dataencerraminvestimento | Data de encerramento do investimento | Date of the investment closure | date (month/year) | no |
| dataencerramprojeto | Data do encerramento do projeto | Date of the project closure | date (month/year) | no |
| dataultdec | Data da última decisão | Date of the last decision | date (month/year) | no |
| [decisao](#decision) | Decisão | Decision | code | no |
| despesapublica | Despesa pública total | Total public expenditure | euros | no |
| [dstanl](#decommitment-or-withdrawal) | Desistência/Anulação | Decommitment / Withdrawal | code | no |
| [estado](#project-status) | Estado do projeto | Project status | code | no |
| execdespesapublica | Execução da despesa pública total | Implementation of the total public expenditure | euros | no |
| execdespesaelegcertif | Execução da despesa elegível certificada | Implementation of the certified and eligible expenditure | euros | no |
| execincentivo | Execução do incentivo | Implementation of the incentive | euros | no |
| incentivocontratadofeder | Incentivo contratado FEDER | ERDF contracted incentive | euros | no |
| incentivoencerrado | Incentivo encerrado FEDER | ERDF closed incentive | euros | no |
| incentivofeder | Incentivo FEDER | ERDF incentive | euros | no |
| incentivoformacao | Incentivo para formação | Training incentive | euros | no |
| incentivonaoreembolsavel | Incentivo não reembolsável | Non-repayable incentive | euros | no |
| incentivoreembolsavel | Incentivo reembolsável | Repayable incentive | euros | no |
| incentivototalfederfundos | Incentivo total (FEDER+Fundos Nacionais) | Total incentive (ERDF + National Funds) | euros | no |
| investcand | Investimento associado à candidatura | Application investment | euros | no |
| investimentoelegivelforma | Investimento elegível em formação | Eligible investment in training | euros | no |
| investimentoelegiveltotal | Investimento elegível total | Total eligible investment | euros | no |
| investimentoemformacao | Investimento em formação | Investment in training | euros | no |
| investimentototal | Investimento Total | Total investment | euros | no |
| [med](#incentive-system) | Sistema de Incentivos | Incentive System | code | no |
| [medida](#measure) | Medida | Measure | code | no |
| [nepontuacao](#non-eligibility-due-to-scoring-below-the-minimum-required) | Não elegibilidade devido a pontuação inferior ao patamar mínimo | Non-eligibility due to scoring below the minimum required | dummy | no |
| nultimadecisao | Número da última decisão | Number of the last decision | number | no |
| ordenspagpendentes | Ordens de pagamento pendentes | Pending payment orders | euros | no |
| pagamentostotais | Pagamentos totais | Total payments | euros | no |
| pontuacao | Pontuação do projeto | Project score | score | no |
| premio | Prémio | Achievement bonus | euros | no |


## Managing Authority

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1 | 1 PO Alentejo | 1 OP Alentejo |
| 2 | 2 PO Algarve | 2 OP Algarve |
| 3 | 3 PO Centro | 3 OP Centre |
| 4 | 4 PO Factores de Competitividade | 4 OP Thematic Factors of Competitiveness |
| 5 | 5 PO Lisboa | 5 OP Lisbon |
| 6 | 6 PO Norte | 6 OP North |

[return](#variables-description)

## With Final Reimbursement Payment

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1 |	1 Sim	| 1 Yes |

[return](#variables-description)

## Decision

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1 | 1 Elegível | 1 Eligible |
| 2 | 2 Elegível Não Seleccionado | 2 Eligible, not selected |
| 3 | 3 Não Elegível | 3 Not eligible |
| 4 | 4 Não Enquadrável | 4 Out of scope |


[return](#variables-description)

## Decommitment or Withdrawal

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1	| 1 Anulação | 1 Decommitment |
| 2 |	2 Desistência	| 2 Withdrawal |

[return](#variables-description)

## Project status

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

[return](#variables-description)

## Incentive System

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1	| 1 SI I&DT	| 1 R&D Incentives System |
| 2	| 2 SI Inovação	| 2 Innovation Incentives System |
| 3 | 3 SI Qualificação PME	| 3 Qualification Incentives System for SME’s |


[return](#variables-description)

## Measure

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

[return](#variables-description)


## Non-eligibility due to scoring below the minimum required

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 0	| 0 Não	| 0 No |
| 1 |	1 Sim	| 1 Yes |

[return](#variables-description)
