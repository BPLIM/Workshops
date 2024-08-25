---
title: Variables in the Harmonized Central Credit Responsibility Database (HCRC)
subtitle: Extraction Date -  June 2024
date: June 2024
doi: 110.17900/HCRC.JUN2024.V1
pdf-engine: pdflatex
execute:
  echo: false
format:
  html:
    theme: default
jupyter: nbstata
---





# Table of Contents

[Cover Sheet](#cover-sheet)

[Credit Exposure](#credit-exposure)

[Bank-Firm Credit Outstanding](#bank-firm-credit-outstanding)

[Firm Credit Outstanding and Bank Relationship](#firm-credit-outstanding-and-bank-relation)

## Cover Sheet

| Variable                    | Designation                                                                                    | Scale of Measurement   | Data type              | Storage type           | Start                  | End                    |
| :---:                    | :---:                                                                                    | :---:  | :---:             | :---:           | :---:                  | :---:                    |
| *tina*                      | Anonymized tax identificaton number                                                            | code                   | discrete               | long                   | 2009m1                 | 2023m12               |
| *date*                      | Reporting date                                                                                 | month                  | discrete               | float                  | 2009m1                 | 2023m12               |
| *natjur*                    | Legal form                                                                                     | categorical            | discrete               | int                    | 2009m1                 | 2023m12               |
| *cae21*                     | Portuguese classification of Economic activities (version 2.1)                                 | categorical            | discrete               | long                   | 2009m1                 | 2023m12               |
| *cae3*                      | Portuguese classification of Economic activities (version 3)                                   | categorical            | discrete               | long                   | 2009m1                 |  2023m12               |
| *district*                  | District                                                                                       | categorical            | discrete               | byte                   | 2009m1                 |  2023m12               |
| *municipality*              | Municipality                                                                                   | categorical            | discrete               | int                    | 2009m1                 |  2023m12               |
| *si*                        | Institutional sector (SEC 95)                                                                  | categorical            | discrete               | long                   | 2009m1                 | 2023m12               |
| *si_final*                  | Institutional sector (SEC 2010)                                                                | categorical            | discrete               | long                   | 2009m1                 | 2023m12               |
| *mindate*                   | Start date of the information                                                                  | month                  | discrete               | int                    | 2009m1                 | 2023m12               |
| *maxdate*                   | End date of the information                                                                    | month                  | discrete               | int                    | 2009m1                 | 2023m12

[Return](#table-of-contents)


## Credit Exposure

|Name | Label  | Scale of Measurement   | Data type              | Storage type           | Start                  | End                    |
| :---:                    | :---:                                                                                    | :---:  | :---:             | :---:           | :---:                  | :---:                    |
| *tina*                                         | Anonymized tax identification number                                                           | code                          | discrete             | long           | 2009m1               | 2023m12   |
| *bina*                                         | Creditor identification number                                                                 | int                           | discrete             | long           | 2009m1               | 2023m12   |
| *cina*                                         | Credit exposure identifier                                                                     | code                          | discrete             | double         | 2009m1               | 2023m12   |
| *date*                                         | Reporting date                                                                                 | month                         | discrete             | int            | 2009m1               | 2023m12   |
| *nivelresponsabilidade*                        | Responsability level                                                                           | categorical                   | discrete             | byte           | 2009m1               | 2023m12   |
| *produto*                                      | Financial product                                                                              | categorical                   | discrete             | byte           | 2009m1               | 2023m12   |
| *classecreditovencido*                         | Overdue class                                                                                  | categorical                   | discrete             | byte           | 2009m1               | 2023m12   |
| *prazooriginal*                                | Original maturity                                                                              | categorical                   | discrete             | byte           | 2009m1               | 2023m12   |
| *prazoresidual*                                | Residual maturity                                                                              | categorical                   | discrete             | byte           | 2009m1               | 2023m12   |
| *prazocurto_o*                                 | Short original maturity                                                                        | indicator                     | discrete             | byte           | 2009m1               | 2023m12   |
| *prazocurto_r*                                 | Short residual maturity                                                                        | indicator                     | discrete             | byte           | 2009m1               | 2023m12   |
| *tipogarantia*                                 | Type of collateral                                                                             | categorical                   | discrete             | byte           | 2009m1               | 2023m12   |
| *valor_reg*                                    | Regular credit - in euros                                                                      | euros                         | continuous           | double         | 2009m1               | 2023m12   |
| *valor_pot*                                    | Potential credit - in euros                                                                    | euros                         | continuous           | double         | 2009m1               | 2023m12   |
| *valor_vencido*                                | Overdue credit - in euros                                                                      | euros                         | continuous           | double         | 2009m1               | 2023m12   |
| *valor_abatv*                                  | Written-off credit - in euros                                                                  | euros                         | continuous           | double         | 2009m1               | 2023m12   |
| *valorg*                                       | Amount of collateral                                                                           | euros                         | continuous           | double         | 2009m1               | 2023m12   |


[Return](#table-of-contents)

## Bank-Firm Credit Outstanding

|Variable | Designation  | Scale of Measurement   | Data type              | Storage type           | Start                  | End                    |
| :---:                    | :---:                                                                                    | :---:  | :---:             | :---:           | :---:                  | :---:                    |
| *tina*                      | Anonymized tax identificaton number                                                            | code                   | discrete               | long                   | 2009m1                 | 2023m12               |
| *bina*                      | Creditor identification number                                                                 | int                    | discrete               | long                   | 2009m1                 | 2023m12               |
| *date*                      | Reporting month                                                                                | month                  | discrete               | int                    | 2009m1                 | 2023m12               |
| *valor_reg*                 | Regular credit - in euros                                                                      | euros                  | continuous             | double                 | 2009m1                 | 2023m12               |
| *valor_pot*                 | Potential credit - in euros                                                                    | euros                  | continuous             | double                 | 2009m1                 | 2023m12               |
| *valor_vencido*             | Overdue credit - in euros                                                                      | euros                  | continuous             | double                 | 2009m1                 | 2023m12               |
| *valor_abatv*               | Written-off credit - in euros                                                                  | euros                  | continuous             | double                 | 2009m1                 | 2023m12               |
| *valor_reg_sto*             | Regular credit: short original maturity - in euros                                             | euros                  | continuous             | double                 | 2009m1                 | 2023m12               |
| *valor_reg_str*             | Regular credit: short residual maturity - in euros                                             | euros                  | continuous             | double                 | 2009m1                 | 2023m12               |
| *valor_reg_secured*         | Secured regular credit - in euros                                                              | euros                  | continuous             | double                 | 2009m1                 | 2023m12               |
| *valor_pot_secured*         | Secured potential credit - in euros                                                            | euros                  | continuous             | double                 | 2009m1                 | 2023m12               |
| *valor_vencido_secured*     | Secured overdue credit - in euros                                                              | euros                  | continuous             | double                 | 2009m1                 | 2023m12               |
| *valor_abatv_secured*       | Secured written-off credit - in euros                                                          | euros                  | continuous             | double                 | 2009m1                 | 2023m12               |

[Return](#table-of-contents)


## Firm Credit Outstanding and Bank Relationship

|Variable | Designation  | Scale of Measurement   | Data type              | Storage type           | Start                  | End                    |
| :---:                    | :---:                                                                                    | :---:  | :---:             | :---:           | :---:                  | :---:                    |
| *tina*                      | Anonymized tax identificaton number                                                            | code                   | discrete               | long                   | 2009m1                 | 2023m12                |
| *date*                      | Reporting month                                                                                | month                  | discrete               | int                    | 2009m1                 | 2023m12                |
| *valor_reg*                 | Regular credit - in euros                                                                      | euros                  | continuous             | double                 | 2009m1                 | 2023m12                |
| *valor_pot*                 | Potential credit - in euros                                                                    | euros                  | continuous             | double                 | 2009m1                 | 2023m12                |
| *valor_vencido*             | Overdue credit - in euros                                                                      | euros                  | continuous             | double                 | 2009m1                 | 2023m12                |
| *valor_abatv*               | Written-off credit - in euros                                                                  | euros                  | continuous             | double                 | 2009m1                 | 2023m12                |
| *valor_reg_sto*             | Regular credit: short original maturity - in euros                                             | euros                  | continuous             | double                 | 2009m1                 | 2023m12                |
| *valor_reg_str*             | Regular credit: short residual maturity - in euros                                             | euros                  | continuous             | double                 | 2009m1                 | 2023m12                |
| *valor_reg_secured*         | Secured regular credit - in euros                                                              | euros                  | continuous             | double                 | 2009m1                 | 2023m12                |
| *valor_pot_secured*         | Secured potential credit - in euros                                                            | euros                  | continuous             | double                 | 2009m1                 | 2023m12                |
| *valor_vencido_secured*     | Secured overdue credit - in euros                                                              | euros                  | continuous             | double                 | 2009m1                 | 2023m12                |
| *valor_abatv_secured*       | Secured written-off credit - in euros                                                          | euros                  | continuous             | double                 | 2009m1                 | 2023m12                |
| *nb_relacao*                | Number of bank relationships                                                                   | number                 | discrete               | int                    | 2009m1                 | 2023m12                |
| *max_relacao*               | Largest bank relationship in share                                                             | share                  | continuous             | double                 | 2009m1                 | 2023m12                |
| *hhi_relacao*               | Concentration of bank relationships                                                            | index                  | continuous             | double                 | 2009m1                 | 2023m12                |


[Return](#table-of-contents)


## Legal Form
| Code |	Designação | Designation |
| :---: | :----- | :----- |
|	0	|	Todas as Naturezas	|	All Legal Forms	|
|	1	|	Pessoa Colectiva de Direito Público	|	Legal Person under Public Law 	|
|	2	|	Pessoa Colectiva Internacional	|	International Legal Person	|
|	3	|	Organismo da Administração Pública	|	Body of Public Administration	|
|	4	|	Associação de Regentes e Beneficiários	|	Regent and Beneficiary Association 	|
|	5	|	Entidade Pública Empresarial	|	Public Corporation	|
|	7	|	Empresa Municipal	|	Municipal Company	|
|	8	|	Empresa Intermunicipal	|	Intermunicipal Company	|
|	9	|	Empresa Regional	|	Regional Company	|
|	10	|	Empresa Metropolitana	|	Metropolitan Company	|
|	11	|	Fundação	|	Foundation	|
|	12	|	Entidade Empresarial Municipal	|	Municipal Business Entity	|
|	13	|	Entidade Empresarial Intermunicipal	|	Intermunicipal Business Entity	|
|	14	|	Entidade Empresarial Metropolitana	|	Metropolitan Business Entity	|
|	15	|	Sociedade Civil	|	Civil Society	|
|	16	|	Sociedade civil com personalidade jurídica	|	Civil Society with Legal Personality	|
|	17	|	Sociedade anónima europeia	|	European Public Limited Company	|
|	18	|	Sociedade em nome colectivo	|	General Partnership	|
|	19	|	Sociedade Anónima	|	Public Limited Liability Company	|
|	20	|	Sociedade em Comandita	|	Limited Partneship	|
|	21	|	Sociedade por Quotas	|	Private Limited Liability Company	|
|	22	|	Sociedade Unipessoal por Quotas	|	Sole quotaholder private limited company	|
|	23	|	Sociedade anónima desportiva	|	Public Limited Sports Company	|
|	24	|	Agrupamento Europeu de Interesse Económico Civil	|	European Economic Interest Grouping (civil)	|
|	25	|	Agrupamento Europeu de Interesse Económico	|	European Economic Interest Grouping	|
|	26	|	Agrupamento Complementar de Empresas	|	Business Group	|
|	28	|	Cooperativa de Responsabilidade Ilimitada	|	Unlimited Liability Cooperative Company	|
|	29	|	Cooperativa de Responsabilidade Limitada	|	Limited Liability Cooperative Company	|
|	30	|	Cooperativa em Comandita	|	Limited Partnership Cooperative Company	|
|	31	|	União de Cooperativas	|	Union of Cooperative	|
|	32	|	Federação de Cooperativas	|	Federation of Cooperative	|
|	33	|	Confederação de Cooperativas	|	Confederation of Cooperative	|
|	34	|	Mútua de Seguros	|	Mutual Insurance Associations	|
|	35	|	Pessoa Colectiva Religiosa	|	Religious Legal Person	|
|	36	|	Pessoa Jurídica Canónica	|	Canonical Juridical Person	|
|	37	|	Pessoa Colectiva Religiosa Não Católica	|	Non-Catholic Religious Legal Person	|
|	38	|	Pessoa Colectiva Estrangeira	|	Foreign Legal Person	|
|	39	|	Empresa Pública Estrangeira	|	Foreign Public Company	|
|	40	|	Associação Estrangeira	|	Foreign Association	|
|	41	|	Fundação Estrangeira	|	Foreign Foundation	|
|	42	|	Sociedade Civil Estrangeira	|	Foreign Civil Society	|
|	43	|	Sociedade Civil Sob Forma Comercial Estrangeira	|	Foreign Civil Society with a commercial form 	|
|	44	|	Sociedade Comercial Estrangeira	|	Foreign Commercial Society	|
|	45	|	Representação permanente	|	Permanent Representation	|
|	46	|	Empresário Individual	|	Sole Proprietorship	|
|	47	|	Comerciante Individual	|	Individual Merchant	|
|	48	|	Estabelecimento Individual de Responsabilidade Limitada	|	Sole trader entity with limited liability	|
|	49	|	Sociedade Irregular	|	Unregistered company	|
|	50	|	Representação de Pessoa Colectiva Internacional	|	Representative of International Legal Person	|
|	51	|	Entidade Equiparada a Pessoa Colectiva	|	Entity Considered Equivalent to Legal Person	|
|	52	|	Estado	|	State	|
|	53	|	Autarquia local	|	Local Authority	|
|	54	|	Outras pessoas colectivas de direito público	|	Other Legal Persons Governed by Public Law	|
|	55	|	Associação ou Fundação	|	Association or Foundation	|
|	56	|	Outras Associações	|	Other Associations	|
|	57	|	Não residentes, com estabelecimento estável	|	Non-Resident with Permanent Establishment	|
|	59	|	Outras Sociedades (IES)	|	Other corporations (IES)	|
|	60	|	Entidade Pública Municipal, Intermunicipal e Regional	|	Municipal, Intermunicipal and Regional public company	|
|	64	|	Não residentes, sem estabelecimento estável	|	Non-Resident without Permanent Establishment	|
|	65	|	Entidades que não exerçam, a título principal, actividade comercial industrial ou agrícola	|	Entities Whose Main Activity Is Not in Industrial or Agricultural Commercial Sector	|
|	68	|	Agrup. Complem. Empresas e Agrup. Europeu de Interesse Económico	|	Complementary group of companies and European economic interest group	|
|	70	|	Agrupamento Europeu de Interesse Económico Comercial	|	European Economic Interest Grouping	|
|	71	|	Cooperativa	|	Cooperative	|
|	72	|	Cooperativa de 2º grau	|	Second-level Cooperative	|
|	75	|	Pessoa Colectiva de Utilidade Pública	|	Public Utility Legal Person	|
|	76	|	Entidade Equiparada Estrangeira - Identificação	|	Foreign Equivalent Entity - Identification	|
|	77	|	Representação Permanente Não Sujeita a Registo	|	Permanent Representation Not Subject to Registration	|
|	78	|	Sucursal Financeira Exterior	|	Foreign Financial Branch	|
|	79	|	Trust	|	Trust	|
|	80	|	Pessoa colectiva em formação	|	Legal Person under Construction	|
|	81	|	Associação	|	Association	|
|	82	|	Associação de direito público	|	Association Governed by Public Law 	|
|	83	|	Associação de direito privado	|	Association Governed by Private Law 	|
|	84	|	Fundação de direito público	|	Foundation Governed by Public Law 	|
|	85	|	Fundação de direito privado	|	Foundation Governed by Private Law 	|
|	86	|	Fundos de Pensões	|	Pension Fund	|
|	87	|	Fundos de Investimento Mobiliário	|	Mutual Fund	|
|	88	|	Fundos de Investimento Imobiliário	|	Real Estate Investment Fund	|
|	89	|	Fundos de Poupança Reforma	|	Retirement Savings Fund	|
|	90	|	Fundos de Poupança Educação	|	Savings Education Fund	|
|	91	|	Fundos de Poupança Reforma/Educação	|	Savings-Retirement Education Fund	|
|	92	|	Fundos de Poupança Acções	|	Savings-shares Fund	|
|	93	|	Fundos de Capital de Risco	|	Venture Capital Funds	|
|	94	|	Fundos de Fundos	|	Funds of Funds	|
|	95	|	Não Residentes Sujeitos Retenção Fonte a Título Definitivo	|	Non-Resident Subject to Withholding Tax	|
|	96	|	Heranças Indivisas	|	Undivided Estates	|
|	97	|	Organizações Internacionais	|	International Organisations	|
|	98	|	Decreto Lei 408/87 de 31/12	|	Decree Law 408/87 of 31/12	|
|	99	|	Funcionários de Embaixadas e Consulados	|	Official of Embassies and Consulates 	|
|	100	|	Outros	|	Others	|
|	101	|	Não Residentes	|	Non-Resident	|
|	102	|	Fundos	|	Fund	|
|	103	|	Entidades Estrangeiras	|	Foreign Entity	|
|	104	|	Representações	|	Representative	|
|	105	|	Outras Sociedades	|	Other Corporations	|
|	997	|	Código inválido	|	Invalid Code	|
|	998	|	Desconhecido / Em atribuição	|	Unknown	|
|	4306	|	Organizacoes Internacionais	|	International Organizations	|
|	7192	|	Fundação	|	Foundation	|
|	7193	|	Fundação estrangeira - representação permanente	|	Foreign foundation - permanent representation	|
|	7194	|	Associação de direito privado e utilidade pública	|	Association of private law and public utility	|
|	7201	|	Pessoa coletiva religiosa (católica)	|	Religious public entity (Catholic)	|
|	7202	|	Pessoa jurídica canónica (Dec. Lei no. 19/2015)	|	Canonical legal entities (Decree Law No. 19/2015)	|

[Return](#table-of-contents)


## Economic Activities CAE3

| Code |	Designação | Designation |
| :---: | :----- | :----- |
|	1111	|	Cerealicultura (excepto arroz)	|	Growing of cereals (except rice)	|
|	1112	|	Cultura de leguminosas secas e sementes oleaginosas	|	Leguminous crops and oil seeds	|
|	1120	|	Cultura de arroz	|	Growing of rice	|
|	1130	|	Culturas de produtos hortícolas, raízes e tubérculos	|	Growing of vegetables and melons, roots and tubers	|
|	1140	|	Cultura de cana-de-açúcar	|	Growing of sugar cane	|
|	1150	|	Cultura de tabaco	|	Growing of tobacco	|
|	1160	|	Cultura de plantas têxteis	|	Growing of fibre crops	|
|	1191	|	Cultura de flores e de plantas ornamentais	|	Growing of flowers and ornamental plants	|
|	1192	|	Outras culturas temporárias, n.e.	|	Growing of other non-perennial crops, n.e.c.	|
|	1210	|	Viticultura	|	Growing of grapes	|
|	1220	|	Cultura de frutos tropicais e subtropicais	|	Growing of tropical and subtropical fruits	|
|	1230	|	Cultura de citrinos	|	Growing of citrus fruits	|
|	1240	|	Cultura de pomóideas e prunóideas	|	Growing of pome fruits and stone fruits	|
|	1251	|	Cultura de frutos de casca rija	|	Growing of nuts	|
|	1252	|	Cultura de outros frutos em árvores e arbustos	|	Growing of other tree and bush fruits 	|
|	1261	|	Olivicultura	|	Growing of olive	|
|	1262	|	Cultura de outros frutos oleaginosos	|	Growing of other oleaginous fruits	|
|	1270	|	Cultura de plantas destinadas à preparação de bebidas	|	Growing of beverage crops	|
|	1280	|	Cultura de especiarias, plantas aromáticas, medicinais e farmacêuticas	|	Growing of spices, aromatic, drug and pharmaceutical crops	|
|	1290	|	Outras culturas permanentes	|	Growing of other perennial crops	|
|	1300	|	Cultura de materiais de propagação vegetativa	|	Plant propagation	|
|	1410	|	Criação de bovinos para produção de leite	|	Raising of dairy cattle	|
|	1420	|	Criação de outros bovinos (excepto para produção de leite) e búfalos	|	Raising of other cattle and buffaloes	|
|	1430	|	Criação de equinos, asininos e muares	|	Raising of horses and other equines	|
|	1440	|	Criação de camelos e camelídeos	|	Raising of camels and camelids	|
|	1450	|	Criação de ovinos e caprinos	|	Raising of sheep and goats	|
|	1460	|	Suinicultura	|	Raising of swine/pigs	|
|	1470	|	Avicultura	|	Raising of poultry	|
|	1491	|	Apicultura	|	Beekeeping	|
|	1492	|	Cunicultura	|	Rabbit	|
|	1493	|	Criação de animais de companhia	|	Breeding company	|
|	1494	|	Outra produção animal, n.e.	|	Raising of other animals, n.e.c.	|
|	1500	|	Agricultura e produção animal combinadas	|	Mixed farming	|
|	1610	|	Actividades dos serviços relacionados com a agricultura	|	Support activities for crop production	|
|	1620	|	Actividades dos serviços relacionados com a produção animal, excepto serviços de veterinária	|	Support activities for animal production	|
|	1630	|	Preparação de produtos agrícolas para venda 	|	Post-harvest crop activities	|
|	1640	|	Preparação e tratamento de sementes para propagação	|	Seed processing for propagation	|
|	1701	|	Caça e repovoamento cinegético	|	Hunting and trapping	|
|	1702	|	Actividades dos serviços relacionados com a caça e repovoamento cinegético	|	Service activities related to hunting and trapping	|
|	2100	|	Silvicultura e outras actividades florestais	|	Silviculture and other forestry activities	|
|	2200	|	Exploração florestal	|	Logging	|
|	2300	|	Extracção de cortiça, resina e apanha de outros produtos florestais, excepto madeira	|	Gathering of wild growing non-wood products	|
|	2400	|	Actividades dos serviços relacionados com a silvicultura e exploração florestal	|	Support services to forestry	|
|	3111	|	Pesca marítima	|	Marine fishing	|
|	3112	|	Apanha de algas e de outros produtos do mar	|	Collecting seaweed and other sea products	|
|	3121	|	Pesca em águas interiores	|	Fishing in inland waters	|
|	3122	|	Apanha de produtos de águas interiores	|	Collecting inland water products	|
|	3210	|	Aquicultura em águas salgadas e salobras	|	Marine aquaculture	|
|	3220	|	Aquicultura em águas doces	|	Freshwater aquaculture	|
|	5100	|	Extracção de hulha (inclui antracite)	|	Mining of hard coal	|
|	5200	|	Extracção de lenhite	|	Mining of lignite	|
|	6100	|	Extracção de petróleo bruto	|	Extraction of crude petroleum	|
|	6200	|	Extracção de gás natural	|	Extraction of natural gas	|
|	6430	|	Trusts, fundos e  entidades financeiras similares	|	Trusts, funds and similar financial entities	|
|	7100	|	Extracção e preparação de minérios de ferro	|	Mining of iron ores	|
|	7210	|	Extracção e preparação de minérios de urânio e de tório	|	Mining of uranium and thorium ores	|
|	7290	|	Extracção e preparação de outros minérios metálicos não ferrosos	|	Mining of other non-ferrous metal ores	|
|	8111	|	Extracção de mármore e outras rochas carbonatadas	|	Quarrying of marble and other carbonated stones	|
|	8112	|	Extracção de granito ornamental e rochas similares	|	Quarrying of ornamental granite and similar stones	|
|	8113	|	Extracção de calcário e cré	|	Quarrying of limestone and chalk	|
|	8114	|	Extracção de gesso	|	Quarrying of gypsum	|
|	8115	|	Extracção de ardósia	|	Quarrying of slate	|
|	8121	|	Extracção de saibro, areia e pedra britada	|	Operation of gravel and sand pits	|
|	8122	|	Extracção de argilas e caulino	|	Mining of clays and kaolin	|
|	8910	|	Extracção de minerais para a indústria química e para a fabricação de adubos	|	Mining of chemical and fertiliser minerals	|
|	8920	|	Extracção da turfa	|	Extraction of peat	|
|	8931	|	Extracção de sal marinho	|	Extraction of sea salt	|
|	8932	|	Extracção de sal gema	|	Extraction of rock salt	|
|	8991	|	Extracção de feldspato	|	Quarrying of feldspar	|
|	8992	|	Extracção de outros minerais não metálicos, n.e.	|	Quarrying of other non-metallic mineral products, n.e.c.	|
|	9100	|	Actividades dos serviços relacionados com a extracção de petróleo e gás, excepto a prospecção	|	Support activities for petroleum and natural gas extraction	|
|	9900	|	Outras actividades dos serviços relacionados com as indústrias extractivas	|	Support activities for other mining and quarrying	|
|	10110	|	Abate de gado (produção de carne)	|	Processing and preserving of meat	|
|	10120	|	Abate de aves (produção de carne)	|	Processing and preserving of poultry meat	|
|	10130	|	Fabricação de produtos à base de carne	|	Production of meat and poultry meat products	|
|	10201	|	Preparação de produtos da pesca e da aquicultura	|	Preparation of fish and fish products	|
|	10202	|	Congelação de produtos da pesca e da aquicultura	|	Freezing of fish and fish products	|
|	10203	|	Conservação de produtos da pesca e da aquicultura em azeite e outros óleos vegetais e outros molhos	|	Preserving of fish and fish products in olive oil and other vegetable oil and other sauces	|
|	10204	|	Salga, secagem e outras actividades de transformação de produtos da pesca e aquicultura	|	Drying, salting and other fish processing and preserving	|
|	10310	|	Preparação e conservação de batatas	|	Processing and preserving of potatoes	|
|	10320	|	Fabricação de sumos de frutos e de produtos hortícolas	|	Manufacture of fruit and vegetable juice	|
|	10391	|	Congelação de frutos e de produtos hortícolas	|	Freezing of fruit and vegetables	|
|	10392	|	Secagem e desidratação de frutos e de produtos hortícolas	|	Drying and dehydration of fruit and vegetables	|
|	10393	|	Fabricação de doces, compotas, geleias e marmelada	|	Manufacture of jams, marmalades and table jellies	|
|	10394	|	Descasque e transformação de frutos de casca rija comestíveis	|	Peeling and processing of edible nuts	|
|	10395	|	Preparação e conservação de frutos e de produtos hortícolas por outros processos	|	Preparation and preserving of fruit and vegetables, n.e.c.	|
|	10411	|	Produção de óleos e gorduras animais brutos	|	Manufacture of crude animal oils and fats	|
|	10412	|	Produção de azeite	|	Production of olive oil	|
|	10413	|	Produção de óleos vegetais brutos (excepto azeite)	|	Production of crude vegetable oils (except olive oil)	|
|	10414	|	Refinação de azeite, óleos e gorduras	|	Manufacture of olive oil, refined oils and fats	|
|	10420	|	Fabricação de margarinas e de gorduras alimentares similares	|	Manufacture of margarine and similar edible fats	|
|	10510	|	Indústrias do leite e derivados	|	Operation of dairies and cheese making	|
|	10520	|	Fabricação de gelados e sorvetes	|	Manufacture of ice cream	|
|	10611	|	Moagem de cereais	|	Grain milling	|
|	10612	|	Descasque, branqueamento e outros tratamentos do arroz	|	Husking, whitening and other treatment of rice	|
|	10613	|	Transformação de cereais e leguminosas, n.e.	|	Manufacture of grain mill products, n.e.c.	|
|	10620	|	Fabricação de amidos, féculas e produtos afins	|	Manufacture of starches and starch products	|
|	10711	|	Panificação	|	Manufacture of bread	|
|	10712	|	Pastelaria	|	Manufacture of fresh pastry goods and cakes	|
|	10720	|	Fabricação de bolachas, biscoitos, tostas e pastelaria de conservação	|	Manufacture of rusks and biscuits	|
|	10730	|	Fabricação de massas alimentícias, cuscuz e similares	|	Manufacture of macaroni, noodles, couscous and similar farinaceous products	|
|	10810	|	Indústria do açúcar	|	Manufacture of sugar	|
|	10821	|	Fabricação de cacau e de chocolate	|	Manufacture of cocoa and chocolate	|
|	10822	|	Fabricação de produtos de confeitaria	|	Manufacture of sugar confectionery	|
|	10830	|	Indústria do café e do chá	|	Processing of tea and coffee	|
|	10840	|	Fabricação de condimentos e temperos	|	Manufacture of condiments and seasonings	|
|	10850	|	Fabricação de refeições e pratos pré-cozinhados	|	Manufacture of prepared meals and dishes	|
|	10860	|	Fabricação de alimentos homogeneizados e dietéticos	|	Manufacture of homogenised food preparations and dietetic food	|
|	10891	|	Fabricação de fermentos, leveduras e adjuvantes para panificação e pastelaria	|	Manufacture of starters, yeast and adjuvants for breadmaking and pastry	|
|	10892	|	Fabricação de caldos, sopas e sobremesas	|	Manufacture of broths, soups and desserts	|
|	10893	|	Fabricação de outros produtos alimentares diversos, n.e.	|	Manufacture of other miscellaneous food products n.e.c.	|
|	10911	|	Fabricação de pré-misturas	|	Manufacture of premixes	|
|	10912	|	Fabricação de alimentos para animais de criação (excepto para aquicultura)	|	Manufacture of prepared feeds for farm animals (except for aquaculture)	|
|	10913	|	Fabricação de alimentos para aquicultura	|	Manufacture of prepared feeds for aquaculture	|
|	10920	|	Fabricação de alimentos para animais de companhia	|	Manufacture of prepared pet foods	|
|	11011	|	Fabricação de aguardentes preparadas	|	Manufacture of prepared spirits	|
|	11012	|	Fabricação de aguardentes não preparadas	|	Manufacture of non-prepared spirits	|
|	11013	|	Produção de licores e de outras bebidas destiladas	|	Manufacture of liqueurs and other distilled alcoholic beverages	|
|	11021	|	Produção de vinhos comuns e licorosos	|	Manufacture of ordinary and liqueur wine	|
|	11022	|	Produção de vinhos espumantes e espumosos	|	Manufacture of sparkling wine	|
|	11030	|	Fabricação de cidra e outras bebidas fermentadas de frutos	|	Manufacture of cider and other fruit wines	|
|	11040	|	Fabricação de vermutes e de outras bebidas fermentadas não destiladas	|	Manufacture of other non-distilled fermented beverages	|
|	11050	|	Fabricação de cerveja	|	Manufacture of beer	|
|	11060	|	Fabricação de malte	|	Manufacture of malt	|
|	11071	|	Engarrafamento de águas minerais naturais e de nascente	|	Bottling of natural mineral and spring waters 	|
|	11072	|	Fabricação de refrigerantes e de outras bebidas não alcoólicas, n.e.	|	Production of soft drinks and other non-alcoholic flavoured and/or sweetened waters, n.e.c.	|
|	12000	|	Preparação de tabaco	|	Preparation of tobacco	|
|	13101	|	Preparação e fiação de fibras do tipo algodão	|	Preparation and spinning of cotton-type fibres	|
|	13102	|	Preparação e fiação de fibras do tipo lã	|	Preparation and spinning of woollen-type fibres	|
|	13103	|	Preparação e fiação da seda e preparação e texturização de filamentos sintéticos e artificiais	|	Throwing and preparation of silk, including from noils, and throwing and texturing of synthetic or artificial filament yarns	|
|	13104	|	Fabricação de linhas de costura	|	Manufacture of sewing threads	|
|	13105	|	Preparação e fiação de linho e de outras fibras têxteis	|	Preparation and spinning of flax-type fibres and other textile fibres	|
|	13201	|	Tecelagem de fio do tipo algodão	|	Cotton-type weaving	|
|	13202	|	Tecelagem de fio do tipo lã	|	Woollen-type weaving	|
|	13203	|	Tecelagem de fio do tipo seda e de outros têxteis	|	Silk-type and other textile weaving	|
|	13301	|	Branqueamento e tingimento	|	Bleaching and dyeing	|
|	13302	|	Estampagem	|	Printing services of textile articles	|
|	13303	|	Acabamento de fios,  tecidos e artigos têxteis, n.e.	|	Finishing of yarns, fabrics and textiles, n.e.c.	|
|	13910	|	Fabricação de tecidos de malha	|	Manufacture of knitted and crocheted fabrics	|
|	13920	|	Fabricação de artigos têxteis confeccionados, excepto vestuário	|	Manufacture of made-up textile articles, except apparel	|
|	13930	|	Fabricação de tapetes e carpetes	|	Manufacture of carpets and rugs	|
|	13941	|	Fabricação de cordoaria	|	Manufacture of cordage, rope and twine	|
|	13942	|	Fabricação de redes	|	Manufacture of nets	|
|	13950	|	Fabricação de não tecidos e respectivos artigos, excepto vestuário	|	Manufacture of non-wovens and articles made from non-wovens, except apparel	|
|	13961	|	Fabricação de passamanarias e sirgarias	|	Manufacture of ornamental trimmings and narrow fabrics	|
|	13962	|	Fabricação de têxteis para uso técnico e industrial, n.e.	|	Manufacture of other technical and industrial textiles, n.e.c.	|
|	13991	|	Fabricação de bordados	|	Manufacture of embroidery	|
|	13992	|	Fabricação de rendas	|	Manufacture of lace	|
|	13993	|	Fabricação de outros  têxteis diversos, n.e.	|	Manufacture of other miscellaneous textiles, n.e.c.	|
|	14110	|	Confecção de vestuário em couro	|	Manufacture of leather clothes	|
|	14120	|	Confecção de vestuário de trabalho	|	Manufacture of workwear	|
|	14131	|	Confecção de outro vestuário exterior em série	|	Manufacture of other ready-to-wear outerwear 	|
|	14132	|	Confecção de outro vestuário exterior por medida	|	Manufacture of other made-to-measure outerwear	|
|	14133	|	Actividades de acabamento de artigos de vestuário	|	Finishing activities on wear products	|
|	14140	|	Confecção de vestuário interior	|	Manufacture of underwear	|
|	14190	|	Confecção de outros artigos e acessórios de vestuário	|	Manufacture of other wearing apparel and accessories	|
|	14200	|	Fabricação de artigos de peles com pêlo	|	Manufacture of articles of fur	|
|	14310	|	Fabricação de meias e similares de malha	|	Manufacture of knitted and crocheted hosiery	|
|	14390	|	Fabricação de outro vestuário de malha	|	Manufacture of other knitted and crocheted apparel	|
|	15111	|	Curtimenta e acabamento de peles sem pêlo	|	Tanning and dressing of leather	|
|	15112	|	Fabricação de couro reconstituído	|	Manufacture of composition leather	|
|	15113	|	Curtimenta e acabamento de peles com pêlo	|	Tanning and dressing of fur	|
|	15120	|	Fabricação de artigos de viagem e de uso pessoal, de marroquinaria, de correeiro e de seleiro	|	Manufacture of luggage, handbags and the like, saddlery and harness	|
|	15201	|	Fabricação de calçado	|	Manufacture of footwear	|
|	15202	|	Fabricação de componentes para calçado	|	Manufacture of parts of footwear	|
|	16101	|	Serração de madeira	|	Sawmilling of wood	|
|	16102	|	Impregnação de madeira	|	Impregnation of wood	|
|	16211	|	Fabricação de painéis de partículas de madeira	|	Manufacture of wood particle boards	|
|	16212	|	Fabricação de painéis de fibras de madeira	|	Manufacture of wood fibre boards	|
|	16213	|	Fabricação de folheados, contraplacados, lamelados e de outros painéis	|	Manufacture of veneer sheets	|
|	16220	|	Parqueteria	|	Manufacture of assembled parquet floors	|
|	16230	|	Fabricação de outras obras de carpintaria para a construção	|	Manufacture of other builders' carpentry and joinery	|
|	16240	|	Fabricação de embalagens de madeira	|	Manufacture of wooden containers	|
|	16291	|	Fabricação de outras obras de madeira	|	Manufacture of other products of wood	|
|	16292	|	Fabricação de obras de cestaria e de espartaria	|	Manufacture of articles of straw and plaiting materials	|
|	16293	|	Indústria de preparação da cortiça	|	Cork industry	|
|	16294	|	Fabricação de rolhas de cortiça	|	Manufacture of cork	|
|	16295	|	Fabricação de outros produtos de cortiça	|	Manufacture of other articles of cork	|
|	17110	|	Fabricação de pasta	|	Manufacture of pulp	|
|	17120	|	Fabricação de papel e de cartão (excepto canelado)	|	Manufacture of paper and paperboard	|
|	17211	|	Fabricação de papel e de cartão canelados (inclui embalagens)	|	Manufacture of corrugated paper and paperboard 	|
|	17212	|	Fabricação de outras embalagens de papel e de cartão	|	Manufacture of other containers of paper and paperboard	|
|	17220	|	Fabricação de artigos de papel para uso doméstico e sanitário	|	Manufacture of household and sanitary goods and of toilet requisites	|
|	17230	|	Fabricação de artigos de papel para papelaria	|	Manufacture of paper stationery	|
|	17240	|	Fabricação de papel de parede	|	Manufacture of wallpaper	|
|	17290	|	Fabricação de outros artigos de pasta de papel, de papel e de cartão	|	Manufacture of other articles of paper and paperboard	|
|	18110	|	Impressão de jornais	|	Printing of newspapers	|
|	18120	|	Outra impressão	|	Other printing	|
|	18130	|	Actividades de preparação da impressão e de produtos media	|	Pre-press and pre-media services	|
|	18140	|	Encadernação  e actividades  relacionadas	|	Binding and related services	|
|	18200	|	Reprodução de suportes gravados	|	Reproduction of recorded media	|
|	19100	|	Fabricação de produtos de coqueria	|	Manufacture of coke oven products	|
|	19201	|	Fabricação de produtos petrolíferos refinados	|	Manufacture of refined petroleum products	|
|	19202	|	Fabricação de produtos petrolíferos a partir de resíduos	|	Manufacture of petroleum products from waste	|
|	19203	|	Fabricação de briquetes e aglomerados de hulha e lenhite	|	Manufacture of briquettes and pellets of coal and lignite	|
|	20110	|	Fabricação de gases industriais	|	Manufacture of industrial gases	|
|	20120	|	Fabricação de corantes e pigmentos	|	Manufacture of dyes and pigments	|
|	20130	|	Fabricação de outros produtos químicos inorgânicos de base	|	Manufacture of other inorganic basic chemicals	|
|	20141	|	Fabricação de resinosos e seus derivados	|	Manufacture of resin and its derivatives	|
|	20142	|	Fabricação de carvão (vegetal e animal) e produtos associados	|	Manufacture of coal (plant and animal) and related products	|
|	20143	|	Fabricação de álcool etílico de fermentação	|	Manufacture of ethyl alcohol fermentation	|
|	20144	|	Fabricação de outros produtos químicos orgânicos de base, n.e.	|	Manufacture of other organic basic chemicals, n.e.c.	|
|	20151	|	Fabricação de adubos químicos ou minerais e de compostos azotados	|	Manufacture of chemical or mineral fertilisers and nitrogen compounds	|
|	20152	|	Fabricação de adubos orgânicos e organo-minerais	|	Manufacture of organic and organic-mineral fertilisers	|
|	20160	|	Fabricação de matérias plásticas sob formas primárias	|	Manufacture of plastics in primary forms	|
|	20170	|	Fabricação de borracha sintética sob formas primárias	|	Manufacture of synthetic rubber in primary forms	|
|	20200	|	Fabricação de pesticidas e de outros produtos agroquímicos	|	Manufacture of pesticides and other agrochemical products	|
|	20301	|	Fabricação de tintas (excepto impressão), vernizes, mastiques e produtos similares	|	Manufacture of paints (except printing ink), varnishes, mastics and related products	|
|	20302	|	Fabricação de tintas de impressão	|	Manufacture of printing ink	|
|	20303	|	Fabricação de pigmentos preparados, composições vitrificáveis e afins	|	Manufacture of pigments, prepared vitrifiable and related	|
|	20411	|	Fabricação de sabões, detergentes e glicerina	|	Manufacture of soap, detergents and glycerol	|
|	20412	|	Fabricação de produtos de limpeza, polimento e protecção	|	Manufacture of cleaning and polishing preparations	|
|	20420	|	Fabricação de perfumes, de cosméticos e de produtos de higiene	|	Manufacture of perfumes and toilet preparations	|
|	20510	|	Fabricação de explosivos e artigos de pirotecnia	|	Manufacture of explosives	|
|	20520	|	Fabricação de colas	|	Manufacture of glues	|
|	20530	|	Fabricação de óleos essenciais	|	Manufacture of essential oils	|
|	20591	|	Fabricação de biodiesel	|	Manufacture of biodiesel	|
|	20592	|	Fabricação de produtos químicos auxiliares para uso industrial	|	Manufacture of chemical products for industrial use	|
|	20593	|	Fabricação de óleos e massas lubrificantes, com exclusão da efectuada nas refinarias	|	Manufacture of lubricating oils and greases, except that made in refineries	|
|	20594	|	Fabricação de outros produtos químicos diversos, n.e.	|	Manufacture of other miscellaneous chemical products, n.e.c.	|
|	20600	|	Fabricação de fibras sintéticas ou artificiais	|	Manufacture of man-made fibres	|
|	21100	|	Fabricação de produtos farmacêuticos de base	|	Manufacture of basic pharmaceutical products	|
|	21201	|	Fabricação de medicamentos	|	Manufacture of medicaments	|
|	21202	|	Fabricação de outras preparações e de artigos farmacêuticos	|	Manufacture of other pharmaceutical preparations and pharmaceuticals	|
|	22111	|	Fabricação de pneus e câmaras-de-ar	|	Manufacture of rubber tyres and tubes	|
|	22112	|	Reconstrução de pneus	|	Retreading and rebuilding of rubber tyres	|
|	22191	|	Fabricação de componentes de borracha para calçado	|	Manufacture of rubber components for footwear	|
|	22192	|	Fabricação de outros produtos de borracha, n.e.	|	Manufacture of other rubber products, n.e.c.	|
|	22210	|	Fabricação de chapas, folhas, tubos e perfis de plástico	|	Manufacture of plastic plates, sheets, tubes and profiles	|
|	22220	|	Fabricação de embalagens de plástico	|	Manufacture of plastic packing goods	|
|	22230	|	Fabricação de artigos de plástico para a construção	|	Manufacture of builder's ware of plastic	|
|	22291	|	Fabricação de componentes de plástico para calçado	|	Manufacture of plastic components for footwear	|
|	22292	|	Fabricação de outros artigos de plástico, n.e.	|	Manufacture of other plastic products, n.e.c.	|
|	23110	|	Fabricação de vidro plano	|	Manufacture of flat glass	|
|	23120	|	Moldagem e transformação de vidro plano	|	Shaping and processing of flat glass	|
|	23131	|	Fabricação de vidro de embalagem	|	Manufacture of hollow glass	|
|	23132	|	Cristalaria	|	Manufacture of crystal ware	|
|	23140	|	Fabricação de fibras de vidro	|	Manufacture of glass fibres	|
|	23190	|	Fabricação e transformação de outro vidro (inclui vidro técnico)	|	Manufacture and processing of other glass, including technical glassware	|
|	23200	|	Fabricação de produtos cerâmicos refractários	|	Manufacture of refractory products	|
|	23311	|	Fabricação de azulejos	|	Manufacture of ceramic tiles 	|
|	23312	|	Fabricação de ladrilhos, mosaicos e placas de cerâmica	|	Manufacture of floor flags, tiles and mosaic	|
|	23321	|	Fabricação de tijolos	|	Manufacture of bricks	|
|	23322	|	Fabricação de telhas	|	Manufacture of tiles 	|
|	23323	|	Fabricação de abobadilhas	|	Manufacture of support or filler tiles	|
|	23324	|	Fabricação de outros produtos cerâmicos para a construção	|	Manufacture of other clay building materials	|
|	23411	|	Olaria de barro	|	Pottery	|
|	23412	|	Fabricação de artigos de uso doméstico de faiança, porcelana e grés fino	|	Manufacture of household articles made of stone- or earthenware, porcelain and china	|
|	23413	|	Fabricação de artigos de ornamentação de faiança, porcelana e grés fino	|	Manufacture of ornamental articles made of stone- or earthenware, porcelain and china	|
|	23414	|	Actividades de decoração de artigos cerâmicos de uso doméstico e ornamental	|	Activities decoration of ceramic household and ornamental articles	|
|	23420	|	Fabricação de artigos cerâmicos para usos sanitários	|	Manufacture of ceramic sanitary fixtures	|
|	23430	|	Fabricação de isoladores e peças isolantes em cerâmica	|	Manufacture of ceramic insulators and insulating fittings	|
|	23440	|	Fabricação de outros produtos em cerâmica para usos técnicos	|	Manufacture of other technical ceramic products	|
|	23490	|	Fabricação de outros produtos cerâmicos não refractários	|	Manufacture of other ceramic products	|
|	23510	|	Fabricação de cimento	|	Manufacture of cement	|
|	23521	|	Fabricação de cal	|	Manufacture of lime 	|
|	23522	|	Fabricação de gesso	|	Manufacture of plaster	|
|	23610	|	Fabricação de produtos de betão para a construção	|	Manufacture of concrete products for construction purposes	|
|	23620	|	Fabricação de produtos de gesso para a construção	|	Manufacture of plaster products for construction purposes	|
|	23630	|	Fabricação de betão pronto	|	Manufacture of ready-mixed concrete	|
|	23640	|	Fabricação de argamassas	|	Manufacture of mortars	|
|	23650	|	Fabricação de produtos de fibrocimento	|	Manufacture of fibre cement	|
|	23690	|	Fabricação de outros produtos de betão, gesso e cimento	|	Manufacture of other articles of concrete, plaster and cement	|
|	23701	|	Fabricação de artigos de mármore e de rochas similares	|	Manufacture of articles of marble and similar stone	|
|	23702	|	Fabricação de artigos em ardósia (lousa)	|	Manufacture of articles of slate	|
|	23703	|	Fabricação de artigos de granito e de rochas, n.e.	|	Manufacture of articles of granite and stones, n.e.c.	|
|	23910	|	Fabricação de produtos abrasivos	|	Production of abrasive products	|
|	23991	|	Fabricação de misturas betuminosas	|	Manufacture of bituminous mixtures	|
|	23992	|	Fabricação de outros produtos minerais não metálicos diversos, n.e.	|	Manufacture of other non-metallic mineral products, n.e.c.	|
|	24100	|	Siderurgia e fabricação de ferro-ligas	|	Manufacture of basic iron and steel and of ferro-alloys	|
|	24200	|	Fabricação de tubos, condutas, perfis ocos e respectivos acessórios,  de aço	|	Manufacture of tubes, pipes, hollow profiles and related fittings, of steel	|
|	24310	|	Estiragem a frio	|	Cold drawing of bars	|
|	24320	|	Laminagem a frio de arco ou banda	|	Cold rolling of narrow strip	|
|	24330	|	Perfilagem a frio	|	Cold forming or folding	|
|	24340	|	Trefilagem a frio	|	Cold drawing of wire	|
|	24410	|	Obtenção e primeira transformação de metais preciosos	|	Precious metals production	|
|	24420	|	Obtenção e primeira transformação de alumínio	|	Aluminium production	|
|	24430	|	Obtenção e primeira transformação de chumbo, zinco e estanho	|	Lead, zinc and tin production	|
|	24440	|	Obtenção e primeira transformação de cobre	|	Copper production	|
|	24450	|	Obtenção e primeira transformação de outros metais não ferrosos	|	Other non-ferrous metal production	|
|	24460	|	Tratamento de combustível nuclear	|	Processing of nuclear fuel 	|
|	24510	|	Fundição de ferro fundido	|	Casting of iron	|
|	24520	|	Fundição de aço	|	Casting of steel	|
|	24530	|	Fundição de metais leves	|	Casting of light metals	|
|	24540	|	Fundição de outros metais não ferrosos	|	Casting of other non-ferrous metals	|
|	25110	|	Fabricação de estruturas de construções metálicas	|	Manufacture of metal structures and parts of structures	|
|	25120	|	Fabricação de portas, janelas e elementos similares em metal	|	Manufacture of doors and windows of metal	|
|	25210	|	Fabricação de caldeiras e radiadores para aquecimento central	|	Manufacture of central heating radiators and boilers	|
|	25290	|	Fabricação de outros reservatórios e recipientes metálicos	|	Manufacture of other tanks, reservoirs and containers of metal	|
|	25300	|	Fabricação de geradores de vapor (excepto caldeiras para aquecimento central)	|	Manufacture of steam generators, except central heating hot water boilers	|
|	25401	|	Fabricação de armas de caça, de desporto e defesa	|	Manufacture of hunting, sporting or protective firearms and ammunition	|
|	25402	|	Fabricação de armamento	|	Manufacture of armament	|
|	25501	|	Fabricação de produtos forjados, estampados e laminados	|	Forging, pressing, stamping and roll forming of metal	|
|	25502	|	Fabricação de produtos por pulverometalurgia	|	Powder metallurgy	|
|	25610	|	Tratamento e revestimento de metais	|	Treatment and coating of metals	|
|	25620	|	Actividades de mecânica geral	|	Machining	|
|	25710	|	Fabricação de cutelaria	|	Manufacture of cutlery	|
|	25720	|	Fabricação de fechaduras, dobradiças e de outras ferragens	|	Manufacture of locks and hinges	|
|	25731	|	Fabricação de ferramentas manuais	|	Manufacture of hand tools	|
|	25732	|	Fabricação de ferramentas mecânicas	|	Manufacture of mechanical tools	|
|	25733	|	Fabricação de peças sinterizadas	|	Manufacture of sintered parts	|
|	25734	|	Fabricação de moldes metálicos	|	Manufacture of metal moulds	|
|	25910	|	Fabricação de embalagens metálicas pesadas	|	Manufacture of steel drums and similar containers	|
|	25920	|	Fabricação de embalagens metálicas ligeiras	|	Manufacture of light metal packaging 	|
|	25931	|	Fabricação de produtos de arame	|	Manufacture of wire products	|
|	25932	|	Fabricação de molas	|	Manufacture of springs	|
|	25933	|	Fabricação de correntes metálicas	|	Manufacture of metal chains	|
|	25940	|	Fabricação de rebites, parafusos e porcas	|	Manufacture of fasteners and screw machine products	|
|	25991	|	Fabricação de louça metálica e artigos de uso doméstico	|	Manufacture of metal household articles	|
|	25992	|	Fabricação de outros produtos metálicos diversos,  n.e.	|	Manufacture of other fabricated miscellaneous metal products,  n.e.c.	|
|	26110	|	Fabricação de componentes electrónicos	|	Manufacture of electronic components	|
|	26120	|	Fabricação de placas de circuitos electrónicos	|	Manufacture of loaded electronic boards	|
|	26200	|	Fabricação de computadores e de equipamento periférico	|	Manufacture of computers and peripheral equipment	|
|	26300	|	Fabricação de aparelhos e equipamentos para comunicações	|	Manufacture of communication equipment	|
|	26400	|	Fabricação de receptores  de rádio e de televisão e bens de consumo similares	|	Manufacture of consumer electronics	|
|	26511	|	Fabricação de contadores de electricidade, gás, água e de outros líquidos	|	Manufacture of instruments for measuring electricity, gas  water and other fluid	|
|	26512	|	Fabricação de instrumentos e aparelhos de medida, verificação, navegação e outros fins, n.e.	|	Manufacture of instruments and appliances for measuring, checking, testing, navigating and other purposes, n.e.c.	|
|	26520	|	Fabricação de relógios e material de relojoaria	|	Manufacture of watches and clocks	|
|	26600	|	Fabricação de equipamentos de radiação, electromedicina e electroterapêutico	|	Manufacture of irradiation, electromedical and electrotherapeutic equipment	|
|	26701	|	Fabricação de instrumentos e equipamentos ópticos não oftálmicos	|	Manufacture of optical non-ophthalmic instruments 	|
|	26702	|	Fabricação de material fotográfico e cinematográfico	|	Manufacture of photographic and cinematographic equipment	|
|	26800	|	Fabricação de suportes de informação magnéticos e ópticos	|	Manufacture of magnetic and optical media	|
|	27110	|	Fabricação de motores, geradores e transformadores eléctricos	|	Manufacture of electric motors, generators and transformers	|
|	27121	|	Fabricação de material de distribuição e controlo para instalações eléctricas de alta tensão	|	Manufacture of electricity distribution and control apparatus for high-voltage electrical installations	|
|	27122	|	Fabricação de material de distribuição e controlo para instalações eléctricas de baixa tensão	|	Manufacture of electricity distribution and control apparatus for low-voltage electrical installations	|
|	27200	|	Fabricação de acumuladores e pilhas	|	Manufacture of batteries and accumulators	|
|	27310	|	Fabricação de cabos de fibra óptica	|	Manufacture of fibre optic cables	|
|	27320	|	Fabricação de outros fios e cabos eléctricos e electrónicos	|	Manufacture of other electronic and electric wires and cables	|
|	27330	|	Fabricação de dispositivos e acessórios para instalações eléctricas de baixa tensão	|	Manufacture of wiring devices	|
|	27400	|	Fabricação de lâmpadas eléctricas e de outro equipamento de iluminação	|	Manufacture of electric lighting equipment	|
|	27510	|	Fabricação de electrodomésticos	|	Manufacture of electric domestic appliances	|
|	27520	|	Fabricação de aparelhos não eléctricos para uso doméstico	|	Manufacture of non-electric domestic appliances	|
|	27900	|	Fabricação de outro equipamento eléctrico	|	Manufacture of other electrical equipment	|
|	28110	|	Fabricação de motores e turbinas, excepto motores para aeronaves, automóveis e motociclos	|	Manufacture of engines and turbines, except aircraft, vehicle and cycle engines	|
|	28120	|	Fabricação de equipamento hidráulico e pneumático	|	Manufacture of fluid power equipment	|
|	28130	|	Fabricação de outras bombas e compressores	|	Manufacture of other pumps and compressors	|
|	28140	|	Fabricação de  outras torneiras e válvulas	|	Manufacture of other taps and valves	|
|	28150	|	Fabricação de rolamentos, de engrenagens e de outros órgãos de transmissão	|	Manufacture of bearings, gears, gearing and driving elements	|
|	28210	|	Fabricação de fornos e queimadores	|	Manufacture of ovens, furnaces and furnace burners	|
|	28221	|	Fabricação de ascensores e monta cargas, escadas e passadeiras rolantes	|	Manufacture of lifts, escalators and moving walkways	|
|	28222	|	Fabricação de equipamentos de elevação e de movimentação, n.e.	|	Manufacture of lifting and handling equipment, n.e.c.	|
|	28230	|	Fabricação de máquinas e equipamento de escritório, excepto computadores e equipamento periférico	|	Manufacture of office machinery and equipment (except computers and peripheral equipment)	|
|	28240	|	Fabricação de máquinas-ferramentas portáteis com motor	|	Manufacture of power-driven hand tools	|
|	28250	|	Fabricação de equipamento não doméstico para refrigeração e ventilação	|	Manufacture of non-domestic cooling and ventilation equipment	|
|	28291	|	Fabricação de máquinas de acondicionamento e de embalagem	|	Manufacture of packing and wrapping machinery 	|
|	28292	|	Fabricação de balanças e de outro equipamento para pesagem	|	Manufacture of scales and other weighing machinery	|
|	28293	|	Fabricação de outras máquinas diversas de uso geral, n.e.	|	Manufacture of other general purpose machinery, n.e.c.	|
|	28300	|	Fabricação de máquinas e de tractores para a agricultura, pecuária e silvicultura	|	Manufacture of agricultural and forestry machinery	|
|	28410	|	Fabricação de máquinas-ferramentas para metais	|	Manufacture of metal forming machinery	|
|	28490	|	Fabricação de outras máquinas-ferramentas, n.e.	|	Manufacture of other machine tools	|
|	28910	|	Fabricação de máquinas para a metalurgia	|	Manufacture of machinery for metallurgy	|
|	28920	|	Fabricação de máquinas para as indústrias extractivas e para a construção	|	Manufacture of machinery for mining, quarrying and construction	|
|	28930	|	Fabricação de máquinas para as indústrias alimentares, das bebidas e do tabaco	|	Manufacture of machinery for food, beverage and tobacco processing	|
|	28940	|	Fabricação de máquinas para as indústrias têxtil, do vestuário e do couro	|	Manufacture of machinery for textile, apparel and leather production	|
|	28950	|	Fabricação de máquinas para as indústrias do papel e do cartão	|	Manufacture of machinery for paper and paperboard production	|
|	28960	|	Fabricação de máquinas para as indústrias do plástico e da borracha	|	Manufacture of plastics and rubber machinery	|
|	28991	|	Fabricação de máquinas para as indústrias de materiais de construção, cerâmica e vidro	|	Manufacture of machinery for construction, ceramics and glass	|
|	28992	|	Fabricação de outras máquinas diversas para uso específico, n.e.	|	Manufacture of other miscellaneous special purpose machinery, n.e.c.	|
|	29100	|	Fabricação de veículos automóveis	|	Manufacture of motor vehicles	|
|	29200	|	Fabricação de carroçarias, reboques e semi-reboques	|	Manufacture of bodies (coachwork) for motor vehicles	|
|	29310	|	Fabricação de equipamento eléctrico e electrónico para veículos automóveis	|	Manufacture of electrical and electronic equipment for motor vehicles	|
|	29320	|	Fabricação de outros componentes e acessórios para veículos automóveis	|	Manufacture of other parts and accessories for motor vehicles	|
|	30111	|	Construção de embarcações metálicas e estruturas flutuantes, excepto de recreio e desporto	|	Building of metal ships, except pleasure and sporting boats	|
|	30112	|	Construção de embarcações não metálicas, excepto de recreio e desporto	|	Building of non-metal ships, except pleasure and sporting boats	|
|	30120	|	Construção de embarcações de recreio e de desporto	|	Building of pleasure and sporting boats	|
|	30200	|	Fabricação de material circulante para caminhos-de-ferro	|	Manufacture of railway locomotives and rolling stock	|
|	30300	|	Fabricação de aeronaves, de veículos espaciais e equipamento relacionado	|	Manufacture of air and spacecraft and related machinery	|
|	30400	|	Fabricação de veículos militares de combate	|	Manufacture of military fighting vehicles	|
|	30910	|	Fabricação de motociclos	|	Manufacture of motorcycles	|
|	30920	|	Fabricação de bicicletas e veículos para inválidos	|	Manufacture of bicycles and invalid carriages	|
|	30990	|	Fabricação de outro equipamento de transporte, n.e.	|	Manufacture of other transport equipment n.e.c.	|
|	31010	|	Fabricação de mobiliário para escritório e comércio	|	Manufacture of office and shop furniture	|
|	31020	|	Fabricação de mobiliário de cozinha	|	Manufacture of kitchen furniture	|
|	31030	|	Fabricação de colchoaria	|	Manufacture of mattresses	|
|	31091	|	Fabricação de mobiliário de madeira para outros fins	|	Manufacture of wooden furniture for other purposes	|
|	31092	|	Fabricação de mobiliário metálico para outros fins	|	Manufacture of metal furniture for other purposes	|
|	31093	|	Fabricação de mobiliário de outros materiais para outros fins	|	Manufacture of furniture of other material for other purposes	|
|	31094	|	Actividades de acabamento de mobiliário	|	Completion and finishing of furniture	|
|	32110	|	Cunhagem de moedas	|	Striking of coins	|
|	32121	|	Fabricação de filigranas	|	Manufacture of filigree	|
|	32122	|	Fabricação de artigos de joalharia e de outros artigos de ourivesaria	|	Manufacture of jewellery and related articles, n.c.e	|
|	32123	|	Trabalho de diamantes e de outras pedras preciosas ou semi-preciosas para joalharia e uso industrial	|	Working of diamonds and of other precious or semi-precious stones for jewellery and industrial use	|
|	32130	|	Fabricação de bijutarias	|	Manufacture of imitation jewellery and related articles	|
|	32200	|	Fabricação de instrumentos musicais	|	Manufacture of musical instruments	|
|	32300	|	Fabricação de artigos de desporto	|	Manufacture of sports goods	|
|	32400	|	Fabricação de jogos e de brinquedos	|	Manufacture of games and toys	|
|	32501	|	Fabricação de material óptico oftálmico	|	Manufacture of optical ophthalmic instruments	|
|	32502	|	Fabricação de material ortopédico e próteses e de instrumentos médico-cirúrgicos	|	Manufacture of orthopaedic appliances and prosthesis and medical and surgical equipment	|
|	32910	|	Fabricação de vassouras, escovas e pincéis	|	Manufacture of brooms and brushes	|
|	32991	|	Fabricação de canetas, lápis e similares	|	Manufacture of pens, pencils and related articles	|
|	32992	|	Fabricação de fechos de correr, botões e similares	|	Manufacture of slide fasteners, buttons and related articles	|
|	32993	|	Fabricação de guarda-sóis e chapéus de chuva	|	Manufacture of parasols and umbrellas	|
|	32994	|	Fabricação de equipamento de protecção e segurança	|	Manufacture of equipment for safety and security	|
|	32995	|	Fabricação de caixões mortuários em madeira	|	Manufacture of wooden coffins	|
|	32996	|	Outras indústrias transformadoras diversas, n.e.	|	Other miscellaneous manufacturing activities, n.e.c.	|
|	33110	|	Reparação e manutenção  de produtos metálicos (excepto máquinas e equipamento)	|	Repair of fabricated metal products	|
|	33120	|	Reparação e  manutenção de máquinas e equipamentos	|	Repair of machinery	|
|	33130	|	Reparação e manutenção de equipamento electrónico e óptico	|	Repair of electronic and optical equipment	|
|	33140	|	Reparação e manutenção de equipamento eléctrico	|	Repair of electrical equipment	|
|	33150	|	Reparação e manutenção de embarcações	|	Repair and maintenance of ships and boats	|
|	33160	|	Reparação e manutenção de aeronaves e de veículos espaciais	|	Repair and maintenance of aircraft and spacecraft	|
|	33170	|	Reparação e manutenção de outro equipamento de transporte	|	Repair and maintenance of other transport equipment	|
|	33190	|	Reparação e manutenção de outro equipamento	|	Repair of other equipment	|
|	33200	|	Instalação de máquinas e de equipamentos industriais	|	Installation of industrial machinery and equipment	|
|	35111	|	Produção de electricidade de origem hídrica	|	Production of electricity from water	|
|	35112	|	Produção de electricidade de origem térmica	|	Production of electricity from thermal sources	|
|	35113	|	Produção de electricidade de origem eólica, geotérmica, solar e de origem, n.e.	|	Production of electricity from wind, geothermal, solar and origin nec	|
|	35120	|	Transporte de electricidade	|	Transmission of electricity	|
|	35130	|	Distribuição de electricidade	|	Distribution of electricity	|
|	35140	|	Comércio de electricidade	|	Trade of electricity	|
|	35210	|	Produção de gás	|	Manufacture of gas	|
|	35220	|	Distribuição de combustíveis gasosos por condutas	|	Distribution of gaseous fuels through mains	|
|	35230	|	Comércio de gás por condutas	|	Trade of gas through mains	|
|	35301	|	Produção e distribuição de vapor,  água quente e fria  e ar frio por conduta	|	Production and distribution of steam, hot and cold water and cold air by conduct	|
|	35302	|	Produção de gelo	|	Production of ice	|
|	36001	|	Captação e tratamento de água	|	Water collection and treatment	|
|	36002	|	Distribuição de água	|	Distribution of water	|
|	37001	|	Recolha e drenagem de águas residuais	|	Collection and drainage of sewage	|
|	37002	|	Tratamento de águas residuais	|	Wastewater	|
|	38111	|	Recolha de resíduos inertes	|	Collection of inert waste	|
|	38112	|	Recolha de outros resíduos não perigosos	|	Collection of other non-hazardous waste	|
|	38120	|	Recolha de resíduos perigosos	|	Collection of hazardous waste	|
|	38211	|	Tratamento e eliminação de resíduos inertes	|	Treatment and disposal of inert waste	|
|	38212	|	Tratamento e eliminação de outros resíduos não perigosos	|	Treatment and disposal of other non-hazardous waste	|
|	38220	|	Tratamento e eliminação de resíduos perigosos	|	Treatment and disposal of hazardous waste	|
|	38311	|	Desmantelamento de veículos automóveis, em fim de vida	|	Dismantling of vehicles at the end of life	|
|	38312	|	Desmantelamento de equipamentos eléctricos e electrónicos, em fim de vida	|	Dismantling of electrical and electronic equipment at the end of life	|
|	38313	|	Desmantelamento de outros equipamentos e bens, em fim de vida	|	Dismantling of equipment and other assets at the end of life	|
|	38321	|	Valorização de resíduos metálicos	|	Recovery of scrap metal	|
|	38322	|	Valorização de resíduos não metálicos	|	Recovery of non-metallic material	|
|	39000	|	Descontaminação e actividades similares	|	Remediation activities and other waste management services	|
|	41100	|	Promoção imobiliária (desenvolvimento de projectos de edifícios)	|	Development of building projects	|
|	41200	|	Construção de edifícios (residenciais e não residenciais)	|	Construction of residential and non-residential buildings	|
|	42110	|	Construção de estradas e pistas de aeroportos	|	Construction of roads and motorways	|
|	42120	|	Construção de vias férreas	|	Construction of railways and underground railways	|
|	42130	|	Construção de pontes e túneis	|	Construction of bridges and tunnels	|
|	42210	|	Construção de redes de transporte de águas, de esgotos e de outros fluídos	|	Construction of utility projects for fluids	|
|	42220	|	Construção de redes de transporte e distribuição de electricidade e redes de telecomunicações	|	Construction of utility projects for electricity and telecommunications	|
|	42910	|	Engenharia hidráulica	|	Construction of water projects	|
|	42990	|	Construção de outras obras de engenharia civil, n.e.	|	Construction of other civil engineering projects n.e.c.	|
|	43110	|	Demolição	|	Demolition	|
|	43120	|	Preparação dos locais de construção	|	Site preparation	|
|	43130	|	Perfurações e sondagens	|	Test drilling and boring	|
|	43210	|	Instalação eléctrica	|	Electrical installation	|
|	43221	|	Instalação de canalizações	|	Installation of plumbling 	|
|	43222	|	Instalação de climatização	|	Installation of conditioning air	|
|	43290	|	Outras instalações em construções	|	Other construction installation	|
|	43310	|	Estucagem	|	Plastering	|
|	43320	|	Montagem de trabalhos de carpintaria e de caixilharia	|	Joinery installation	|
|	43330	|	Revestimento de pavimentos e de paredes	|	Floor and wall covering	|
|	43340	|	Pintura e colocação de vidros	|	Painting and glazing	|
|	43390	|	Outras actividades de acabamento em edifícios	|	Other building completion and finishing	|
|	43910	|	Actividades de colocação de coberturas	|	Roofing activities	|
|	43991	|	Aluguer de equipamento de construção e de demolição, com operador	|	Renting of construction or demolition equipment with operator	|
|	43992	|	Outras actividades  especializadas de construção diversas, n.e.	|	Other miscellaneous specialised construction activities n.e.c.	|
|	45110	|	Comércio de veículos automóveis ligeiros	|	Sale of cars and light motor vehicles	|
|	45190	|	Comércio de outros veículos automóveis	|	Sale of other motor vehicles	|
|	45200	|	Manutenção e reparação de veículos automóveis	|	Maintenance and repair of motor vehicles	|
|	45310	|	Comércio por grosso de peças e acessórios para veículos automóveis	|	Wholesale trade of motor vehicle parts and accessories	|
|	45320	|	Comércio a retalho de peças e acessórios para veículos automóveis	|	Retail trade of motor vehicle parts and accessories	|
|	45401	|	Comércio por grosso e a retalho de motociclos, de suas peças e acessórios	|	Wholesale and retail of motorcycles and related parts and accessories	|
|	45402	|	Manutenção e reparação de motociclos, de suas peças e acessórios	|	Maintenance and repair of motorcycles and related parts and accessories	|
|	46110	|	Agentes do comércio por grosso de matérias-primas agrícolas e têxteis, animais vivos e produtos semi-acabados	|	Agents involved in the sale of agricultural raw materials, live animals, textile raw materials and semi-finished goods	|
|	46120	|	Agentes do comércio por grosso de combustíveis, minérios, metais e de produtos químicos para a indústria	|	Agents involved in the sale of fuels, ores, metals and industrial chemicals	|
|	46130	|	Agentes do comércio por grosso de madeira e materiais de construção	|	Agents involved in the sale of timber and building materials	|
|	46140	|	Agentes do comércio por grosso de máquinas, equipamento industrial, embarcações e aeronaves	|	Agents involved in the sale of machinery, industrial equipment, ships and aircraft	|
|	46150	|	Agentes do comércio por grosso de mobiliário, artigos para uso doméstico e ferragens	|	Agents involved in the sale of furniture, household goods, hardware and ironmongery	|
|	46160	|	Agentes do comércio por grosso de têxteis, vestuário, calçado e artigos de couro	|	Agents involved in the sale of textiles, clothing, fur, footwear and leather goods	|
|	46170	|	Agentes do comércio por grosso de produtos alimentares, bebidas e tabaco	|	Agents involved in the sale of food, beverages and tobacco	|
|	46180	|	Agentes especializados do comércio por grosso de outros produtos	|	Agents specialised in the sale of other particular products	|
|	46190	|	Agentes do comércio por grosso misto sem predominância	|	Agents involved in the sale of a variety of goods	|
|	46211	|	Comércio por grosso de alimentos para animais	|	Wholesale of animal feeds	|
|	46212	|	Comércio por grosso de tabaco em bruto	|	Wholesale of ummanufactured tobacco	|
|	46213	|	Comércio por grosso de cortiça em bruto	|	Wholesale of cork in the rough	|
|	46214	|	Comércio por grosso de cereais, sementes, leguminosas, oleaginosas e outras matérias-primas agrícolas	|	Wholesale of grain, seed, grain legume, oleaginous and other agricultural raw materials	|
|	46220	|	Comércio por grosso de flores e plantas	|	Wholesale of flowers and plants	|
|	46230	|	Comércio por grosso de animais vivos	|	Wholesale of live animals	|
|	46240	|	Comércio por grosso de peles e couro	|	Wholesale of hides, skins and leather	|
|	46311	|	Comércio por grosso de fruta e de produtos hortícolas, excepto batata	|	Wholesale of fruit and vegetables, except potatoes	|
|	46312	|	Comércio por grosso de batata	|	Wholesale of potatoes	|
|	46320	|	Comércio por grosso de carne e produtos à base de carne	|	Wholesale of meat and meat products	|
|	46331	|	Comércio por grosso de leite, seus derivados e ovos	|	Wholesale of dairy produce and eggs	|
|	46332	|	Comércio por grosso de azeite, óleos e gorduras alimentares	|	Wholesale of olive oil, edible oils and fats	|
|	46341	|	Comércio por grosso de bebidas alcoólicas	|	Wholesale of alcoholic beverages	|
|	46342	|	Comércio por grosso de bebidas não alcoólicas	|	Wholesale of non-alcoholic beverages	|
|	46350	|	Comércio por grosso de tabaco	|	Wholesale of tobacco products	|
|	46361	|	Comércio por grosso de açúcar	|	Wholesale of sugar	|
|	46362	|	Comércio por grosso de chocolate e de produtos de confeitaria	|	Wholesale of chocolate and sugar confectionery	|
|	46370	|	Comércio por grosso de café, chá, cacau e especiarias	|	Wholesale of coffee, tea, cocoa and spices	|
|	46381	|	Comércio por grosso de peixe, crustáceos e moluscos	|	Wholesale of fish, crustaceans and molluscs	|
|	46382	|	Comércio por grosso de outros produtos alimentares, n.e.	|	Wholesale of other food, n.e.c.	|
|	46390	|	Comércio por grosso não especializado de produtos alimentares, bebidas e tabaco	|	Non-specialised wholesale of food, beverages and tobacco	|
|	46410	|	Comércio por grosso de têxteis	|	Wholesale of textiles	|
|	46421	|	Comércio por grosso de vestuário e de acessórios	|	Wholesale of clothing and clothing accessories	|
|	46422	|	Comércio por grosso de calçado	|	Wholesale of footwear	|
|	46430	|	Comércio por grosso de electrodomésticos, aparelhos de rádio e de televisão	|	Wholesale of electrical household appliances	|
|	46441	|	Comércio por grosso de louças em cerâmica e em vidro	|	Wholesale of china and glassware 	|
|	46442	|	Comércio por grosso de produtos de limpeza	|	Wholesale of cleaning materials	|
|	46450	|	Comércio por grosso de perfumes e de produtos de higiene	|	Wholesale of perfume and cosmetics	|
|	46460	|	Comércio por grosso de produtos farmacêuticos	|	Wholesale of pharmaceutical goods	|
|	46470	|	Comércio por grosso de móveis para uso doméstico, carpetes,  tapetes  e artigos de iluminação	|	Wholesale of furniture, carpets and lighting equipment	|
|	46480	|	Comércio por grosso de relógios e de artigos de ourivesaria e joalharia	|	Wholesale of watches and jewellery	|
|	46491	|	Comércio por grosso de artigos de papelaria	|	Wholesale of stationery	|
|	46492	|	Comércio por grosso de livros, revistas e jornais	|	Wholesale of books, magazines and newspapers	|
|	46493	|	Comércio por grosso de brinquedos, jogos e artigos de desporto	|	Wholesale of toys, games and sports goods	|
|	46494	|	Outro comércio por grosso de bens de consumo, n.e.	|	Wholesale of other household goods, n.e.c.	|
|	46510	|	Comércio por grosso de computadores, equipamentos periféricos e programas informáticos	|	Wholesale of computers, computer peripheral equipment and software	|
|	46520	|	Comércio por grosso de  equipamentos  electrónicos,  de telecomunicações e suas partes	|	Wholesale of electronic and telecommunications equipment and parts	|
|	46610	|	Comércio por grosso de máquinas e equipamentos, agrícolas	|	Wholesale of agricultural machinery, equipment and supplies	|
|	46620	|	Comércio por grosso de máquinas-ferramentas	|	Wholesale of machine tools	|
|	46630	|	Comércio por grosso de máquinas para a indústria extractiva, construção e engenharia civil	|	Wholesale of mining, construction and civil engineering machinery	|
|	46640	|	Comércio por grosso de máquinas para a indústria têxtil, máquinas de costura e de tricotar	|	Wholesale of machinery for the textile industry and of sewing and knitting machines	|
|	46650	|	Comércio por grosso de mobiliário de escritório	|	Wholesale of office furniture	|
|	46660	|	Comércio por grosso de outras máquinas e material de escritório	|	Wholesale of other office machinery and equipment	|
|	46690	|	Comércio por grosso de outras máquinas e equipamentos	|	Wholesale of other machinery and equipment	|
|	46711	|	Comércio por grosso de produtos petrolíferos	|	Wholesale of petroleum products 	|
|	46712	|	Comércio por grosso de combustíveis sólidos, líquidos e gasosos, não derivados do petróleo	|	Wholesale of solid, liquid and gaseous fuels and products not related to petroleum	|
|	46720	|	Comércio por grosso de minérios e de metais	|	Wholesale of metals and metal ores	|
|	46731	|	Comércio por grosso de madeira em bruto e de produtos derivados	|	Wholesale of wood in the rough and related products	|
|	46732	|	Comércio por grosso de materiais de construção (excepto madeira) e equipamento sanitário	|	Wholesale of construction materials (except wood) and sanitary equipment	|
|	46740	|	Comércio por grosso de ferragens, ferramentas manuais e artigos para canalizações e aquecimento	|	Wholesale of hardware, plumbing and heating equipment and supplies	|
|	46750	|	Comércio por grosso de produtos químicos	|	Wholesale of chemical products	|
|	46761	|	Comércio por grosso de fibras têxteis naturais, artificiais e sintéticas	|	Wholesale of natural and man-made textile fibres	|
|	46762	|	Comércio por grosso de outros bens intermédios, n.e.	|	Wholesale of other intermediate products n.e.c.	|
|	46771	|	Comércio por grosso de sucatas e de desperdícios metálicos	|	Wholesale of metal waste and scrap 	|
|	46772	|	Comércio por grosso de desperdícios têxteis, de cartão e papéis velhos	|	Wholesale of textile, cardboard and paper waste	|
|	46773	|	Comércio por grosso de desperdícios de materiais, n.e.	|	Wholesale of material waste, n.e.c.	|
|	46900	|	Comércio por grosso não especializado	|	Non-specialised wholesale trade	|
|	47111	|	Comércio a retalho em supermercados e hipermercados	|	Retail sale in supermarkets and hypermarkets	|
|	47112	|	Comércio a retalho em outros estabelecimentos não especializados, com predominância de produtos alimentares, bebidas ou tabaco	|	Retail sale in others non-specialised stores with food, beverages or tobacco predominating	|
|	47191	|	Comércio a retalho não especializado, sem predominância de produtos alimentares, bebidas ou tabaco, em grandes armazéns e similares	|	Non-specialised retail sale in big stores and similar with food, beverages or tobacco not predominating  	|
|	47192	|	Comércio a retalho em  outros estabelecimentos não especializados, sem predominância de produtos alimentares, bebidas ou tabaco	|	Other retail sale in non-specialised stores	|
|	47210	|	Comércio a retalho de frutas e produtos hortícolas, em estabelecimentos especializados	|	Retail sale of fruit and vegetables in specialised stores	|
|	47220	|	Comércio a retalho de carne e produtos à base de carne, em estabelecimentos especializados	|	Retail sale of meat and meat products in specialised stores	|
|	47230	|	Comércio a retalho de peixe, crustáceos e moluscos, em estabelecimentos especializados	|	Retail sale of fish, crustaceans and molluscs in specialised stores	|
|	47240	|	Comércio a retalho de pão, de produtos de pastelaria e de confeitaria, em estabelecimentos especializados	|	Retail sale of bread, cakes, flour confectionery and sugar confectionery in specialised stores	|
|	47250	|	Comércio a retalho de bebidas, em estabelecimentos especializados	|	Retail sale of beverages in specialised stores	|
|	47260	|	Comércio a retalho de tabaco, em estabelecimentos especializados	|	Retail sale of tobacco products in specialised stores	|
|	47291	|	Comércio a retalho de leite e de derivados, em estabelecimentos especializados	|	Retail sale of dairy produce in specialised stores	|
|	47292	|	Comércio a retalho de produtos alimentares, naturais e dietéticos, em estabelecimentos especializados	|	Retail sale of food, natural and dietary in specialized stores	|
|	47293	|	Outro comércio a retalho de produtos alimentares, em estabelecimentos especializados, n.e.	|	Other retail sale of food in specialised stores, n.e.c.	|
|	47300	|	Comércio a retalho de combustível para veículos a motor, em estabelecimentos especializados	|	Retail sale of automotive fuel in specialised stores	|
|	47410	|	Comércio a retalho de computadores, unidades periféricas e programas informáticos, em estabelecimentos especializados	|	Retail sale of computers, peripheral units and software in specialised stores	|
|	47420	|	Comércio a retalho de equipamento de telecomunicações, em estabelecimentos especializados	|	Retail sale of telecommunications equipment in specialised stores	|
|	47430	|	Comércio a retalho de equipamento audiovisual, em estabelecimentos especializados	|	Retail sale of audio and video equipment in specialised stores	|
|	47510	|	Comércio a retalho de têxteis, em estabelecimentos especializados	|	Retail sale of textiles in specialised stores	|
|	47521	|	Comércio a retalho de ferragens e de vidro plano, em estabelecimentos especializados	|	Retail sale of hardware and flat glass in specialised stores	|
|	47522	|	Comércio a retalho de tintas, vernizes e produtos similares, em estabelecimentos especializados	|	Retail sale of paints, varnishes and similar products in specialised stores	|
|	47523	|	Comércio a retalho de material de bricolage, equipamento sanitário, ladrilhos e materiais similares, em estabelecimentos especializados	|	Retail sale of do-it-yourself material, sanitary equipment, floor tile and similar equipment in specialised stores	|
|	47530	|	Comércio a retalho de carpetes, tapetes, cortinados e  revestimentos  para paredes e pavimentos, em estabelecimentos especializados	|	Retail sale of carpets, rugs, wall and floor coverings in specialised stores	|
|	47540	|	Comércio a retalho de electrodomésticos, em estabelecimentos especializados	|	Retail sale of electrical household appliances in specialised stores	|
|	47591	|	Comércio a retalho de mobiliário e artigos de iluminação, em estabelecimentos especializados	|	Retail sale of furniture, lighting equipment and household articles in specialised stores	|
|	47592	|	Comércio a retalho de louças, cutelaria e de outros artigos similares para uso doméstico, em estabelecimentos especializados	|	Retail sale of tableware, cutlery and other similar household articles in specialised stores	|
|	47593	|	Comércio a retalho de outros artigos para o lar, n.e., em estabelecimentos especializados	|	Retail sale of other household articles in specialised stores, n.e.c.	|
|	47610	|	Comércio a retalho de livros, em estabelecimentos especializados	|	Retail sale of books in specialised stores	|
|	47620	|	Comércio a retalho de jornais, revistas e artigos de papelaria, em estabelecimentos especializados	|	Retail sale of newspapers and stationery in specialised stores	|
|	47630	|	Comércio a retalho de  discos, CD, DVD, cassetes e similares, em estabelecimentos especializados	|	Retail sale of music and video recordings in specialised stores	|
|	47640	|	Comércio a retalho de artigos de desporto, de campismo e lazer, em estabelecimentos especializados	|	Retail sale of sporting equipment in specialised stores	|
|	47650	|	Comércio a retalho de jogos e brinquedos, em estabelecimentos especializados	|	Retail sale of games and toys in specialised stores	|
|	47711	|	Comércio a retalho de vestuário para adultos, em estabelecimentos especializados	|	Retail sale of adults? clothing in specialised stores	|
|	47712	|	Comércio a retalho de vestuário para bebés e crianças, em estabelecimentos especializados	|	Retail sale of children?s and infants? clothing in specialised stores	|
|	47721	|	Comércio a retalho de calçado, em estabelecimentos especializados	|	Retail sale of footwear in specialised stores 	|
|	47722	|	Comércio a retalho de marroquinaria e artigos de viagem, em estabelecimentos especializados	|	Retail sale of handbags and luggage in specialised stores	|
|	47730	|	Comércio a retalho de produtos farmacêuticos, em estabelecimentos especializados	|	Dispensing chemist in specialised stores	|
|	47740	|	Comércio a retalho de produtos médicos e ortopédicos, em estabelecimentos especializados	|	Retail sale of medical and orthopaedic goods in specialised stores	|
|	47750	|	Comércio a retalho de produtos cosméticos e de higiene, em estabelecimentos especializados	|	Retail sale of cosmetic and toilet articles in specialised stores	|
|	47761	|	Comércio a retalho de flores, plantas, sementes e  fertilizantes, em estabelecimentos especializados	|	Retail sale of flowers, plants, seeds and fertilisers in specialised stores	|
|	47762	|	Comércio a retalho de animais de companhia e respectivos alimentos, em estabelecimentos especializados	|	Retail sale of pet animals and pet food in specialised stores	|
|	47770	|	Comércio a retalho de relógios e de artigos de ourivesaria e joalharia, em estabelecimentos especializados	|	Retail sale of watches and jewellery in specialised stores	|
|	47781	|	Comércio a retalho de máquinas e de outro material de escritório, em estabelecimentos especializados	|	Retail sale of office machinery and other equipment  in specialised stores	|
|	47782	|	Comércio a retalho de material óptico, fotográfico, cinematográfico e de instrumentos de precisão, em estabelecimentos especializados	|	Retail sale of photographic, optical, cinematographic and precision equipment in specialised stores	|
|	47783	|	Comércio a retalho de combustíveis para uso doméstico, em estabelecimentos especializados	|	Retail sale of household fuel oil, bottled gas, coal and wood in specialised stores	|
|	47784	|	Comércio a retalho de outros produtos novos, em estabelecimentos especializados, n.e.	|	Other retail sale in specialised stores, n.e.c.	|
|	47790	|	Comércio a retalho de artigos em segunda mão, em estabelecimentos especializados	|	Retail sale of second-hand goods in stores	|
|	47810	|	Comércio a retalho em bancas, feiras e unidades móveis de venda, de produtos alimentares, bebidas e tabaco	|	Retail sale via stalls and markets of food, beverages and tobacco products	|
|	47820	|	Comércio a retalho em bancas, feiras e unidades móveis de venda, de têxteis, vestuário, calçado, malas e similares	|	Retail sale via stalls and markets of textiles, clothing and footwear	|
|	47890	|	Comércio a retalho em bancas, feiras e unidades móveis de venda, de outros produtos	|	Retail sale via stalls and markets of other goods	|
|	47910	|	Comércio a retalho por correspondência ou via Internet	|	Retail sale via mail order houses or via Internet	|
|	47990	|	Comércio a retalho por outros métodos, não efectuado em estabelecimentos, bancas, feiras ou unidades móveis de venda	|	Other retail sale not in stores, stalls or markets	|
|	49100	|	Transporte interurbano  de passageiros por caminho-de-ferro	|	Passenger rail transport, interurban	|
|	49200	|	Transporte de mercadorias por caminho-de-ferro	|	Freight rail transport	|
|	49310	|	Transportes terrestres, urbanos e suburbanos, de passageiros	|	Urban and suburban passenger land transport	|
|	49320	|	Transporte ocasional de passageiros em veículos ligeiros	|	Taxi operation	|
|	49391	|	Transporte interurbano em autocarros	|	Inter-urban passenger transportation by bus	|
|	49392	|	Outros transportes terrestres de passageiros diversos, n.e	|	Other miscellaneous land passenger transport, n.e.c.	|
|	49410	|	Transportes rodoviários de mercadorias	|	Freight transport by road	|
|	49420	|	Actividades de mudanças, por via rodoviária	|	Removal services	|
|	49500	|	Transportes por oleodutos ou gasodutos 	|	Transport via pipeline	|
|	50101	|	Transportes marítimos não costeiros de passageiros	|	Sea passenger water transport 	|
|	50102	|	Transportes costeiros e locais de passageiros	|	Coastal and local passenger water transport	|
|	50200	|	Transportes marítimos de mercadorias 	|	Sea and coastal freight water transport	|
|	50300	|	Transportes de passageiros por vias navegáveis interiores	|	Inland passenger water transport	|
|	50400	|	Transportes de mercadorias por vias navegáveis interiores	|	Inland freight water transport	|
|	51100	|	Transportes aéreos de passageiros	|	Passenger air transport	|
|	51210	|	Transportes aéreos de mercadorias	|	Freight air transport	|
|	51220	|	Transportes espaciais	|	Space transport	|
|	52101	|	Armazenagem frigorífica	|	Storage of frozen goods	|
|	52102	|	Armazenagem não frigorífica	|	Storage of non-frozen goods	|
|	52211	|	Gestão de infra-estruturas dos transportes terrestres	|	Management of the infraestructure for land transportation	|
|	52212	|	Assistência a veículos na estrada	|	Assistance activities to vehicles on the road	|
|	52213	|	Outras actividades auxiliares dos transportes terrestres	|	Other supporting land transport activities	|
|	52220	|	Actividades auxiliares dos transportes por água	|	Service activities incidental to water transportation	|
|	52230	|	Actividades auxiliares dos transportes aéreos	|	Service activities incidental to air transportation	|
|	52240	|	Manuseamento de carga	|	Cargo handling	|
|	52291	|	Organização do transporte	|	Transport organisation	|
|	52292	|	Agentes aduaneiros e similares de apoio ao transporte	|	Activities of customs clearance agents and similars	|
|	53100	|	Actividades postais sujeitas a obrigações do serviço universal	|	Postal activities under universal service obligation	|
|	53200	|	Outras actividades postais e de courier	|	Other postal and courier activities	|
|	55111	|	Hotéis com restaurante	|	Hotels with restaurant  	|
|	55112	|	Pensões com restaurante	|	Guest houses with restaurant	|
|	55113	|	Estalagens com restaurante	|	Inns with restaurant	|
|	55114	|	Pousadas com restaurante	|	Lodging-houses with restaurant	|
|	55115	|	Motéis com restaurante	|	Motels with restaurant	|
|	55116	|	Hotéis-Apartamentos com restaurante	|	Apartment-hotels with restaurant	|
|	55117	|	Aldeamentos turísticos com restaurante	|	Holiday villages with restaurant	|
|	55118	|	Apartamentos turísticos com restaurante	|	Holiday flats with restaurant	|
|	55119	|	Outros estabelecimentos hoteleiros com restaurante	|	Hotel and similar establishments with restaurant, n.e.c.	|
|	55121	|	Hotéis sem restaurante	|	Hotels without restaurant	|
|	55122	|	Pensões sem restaurante	|	Guest houses without restaurant	|
|	55123	|	Apartamentos turísticos sem restaurante	|	Holiday flats without restaurant	|
|	55124	|	Outros estabelecimentos hoteleiros sem restaurante	|	Hotel and similar establishments without restaurant, n.e.c.	|
|	55201	|	Alojamento mobilado para turistas	|	Letting services of short-stay furnished accommodation	|
|	55202	|	Turismo no espaço rural	|	Short-stay lodging in farmhouses 	|
|	55203	|	Colónias e campos de férias 	|	Holiday camps 	|
|	55204	|	Outros locais de alojamento de curta duração	|	Other short-stay lodging, n.e.c.	|
|	55300	|	Parques de campismo e de caravanismo	|	Camping grounds, recreational vehicle parks and trailer parks	|
|	55900	|	Outros locais de alojamento	|	Other accommodation	|
|	56101	|	Restaurantes tipo tradicional	|	Traditional restaurants 	|
|	56102	|	Restaurantes com lugares ao balcão	|	Snack-bars restaurants	|
|	56103	|	Restaurantes sem serviço de mesa	|	Self-service restaurants 	|
|	56104	|	Restaurantes típicos	|	Typical restaurants 	|
|	56105	|	Restaurantes com espaço de dança	|	Restaurants with dance floor 	|
|	56106	|	Confecção de refeições prontas a levar para casa	|	Confection of ready meals for take-away	|
|	56107	|	Restaurantes, n.e. (inclui actividades de restauração em meios móveis)	|	Restaurants and mobile food service activities n.e.c.	|
|	56210	|	Fornecimento de refeições para eventos 	|	Event catering activities	|
|	56290	|	Outras actividades de serviço  de refeições	|	Other food service activities	|
|	56301	|	Cafés	|	Cafés	|
|	56302	|	Bares	|	Bars	|
|	56303	|	Pastelarias e casas de chá	|	Pastries and tea houses	|
|	56304	|	Outros estabelecimentos de bebidas sem espectáculo	|	Other beverage establishments without entertain