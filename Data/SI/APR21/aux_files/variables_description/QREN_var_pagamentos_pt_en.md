<meta charset="utf-8"/>

# QREN
# Payment Orders File

[1. Variables Description](#variables-description)

## Variables Description

| Name | Description (Portuguese) | Description (English) | Unit of measurement | Changes in classification |
| :--------: | :-------------: | :-------------: | :-------: | :-----: |
| **Identifiers** |
| nproja | Número do projeto anonimizado | Number of the project anonymized | code | no |
| tina_promotor | Número de identificação fiscal do promotor anonimizado | Tax identification number of the promoter anonymized | code | no |
| tina_beneficiario | Número de identificação fiscal do beneficiário anonimizado | Tax identification number of the beneficiary anonymized | code | no |
| id | Número da ordem de pagamento dentro do projeto | Number of the payment order within the project | number | no |
| **Other variables** |
| dataordem | Data da ordem de pagamento | Date of the payment order | date (month/year) | no |
| dataefectivapagam | Data efectiva de pagamento | Effective date of the payment | date (month/year) | no |
| datavalorpagam | Data valor do pagamento | Value date of the payment | date (month/year) | no |
| pagamentototal | Pagamento total | Total payment | euros | no |
| [tipopagamento](#type-of-payment) | Tipo de pagamento | Type of payment | code | no |
| [subtipo](#sub-type-of-payment) | Subtipo de pagamento | Sub-type of payment | code | no |
| [situacao](#situation-of-the-payment-order) | Situação da ordem de pagamento | Situation of the payment order | code | no |


## Type of payment

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1 | 1 Adiantamento | 1 Advance payment |
| 2 | 2 Correcção | 2 Correction |
| 3 | 3 Devolução | 3 Return |
| 4 | 4 Estorno | 4 Reversal |
| 5 | 5 Reembolso Final | 5 Final reimbursement |
| 6 | 6 Reembolso Intercalar | 6 Interim reimbursement |

[return](#variables-description)

## Sub-type of payment

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

[return](#variables-description)

## Situation of the payment order

| Code | Designation (Portuguese) | Designation (English) |
| :---: | :---------- | :---------- |
| 1	| 1 Paga | 1 Paid |
| 2 | 2 Pendente | 2 Pending |

[return](#variables-description)
