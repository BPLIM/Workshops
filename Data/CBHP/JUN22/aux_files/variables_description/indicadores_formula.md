<meta charset="utf-8"/>
# Variables in Central Balance Sheet Harmonized Panel Data

## Economic and Financial Indicators

| Indicator | Descrição | Description | Formula |  | Detailed Formula |
| :---: | :----------- | :------------- | :--------------------- | :--------------------- | :--------------------- |
| R001 | Liquidez geral  | Current ratio  | (N) Current assets (D) Current liabilities | B029/B089 | CASE WHEN [B089]<=0 OR ABS([B029]/[B089])>100 THEN NULL ELSE CASE WHEN [B029] =0 THEN 0 ELSE ([B029]/[B089]) END END |"
| R002 | Liquidez reduzida  | Quick ratio  | (N) (Current assets - Inventories and biological assets) (D) Current liabilities | (B029-B032)/B089 | CASE WHEN [B089]<=0 OR ABS(([B029]-[B032])/[B089])>100 THEN NULL ELSE CASE WHEN ([B029]-[B032]) =0 THEN 0 ELSE (([B029]-[B032])/[B089]) END END |"
| R003 | Autonomia financeira | Capital ratio | (N) Equity (D) Total Assets | B061/B001 | CASE WHEN [B001]<=0 OR ABS([B061]/[B001])>100 THEN NULL ELSE CASE WHEN [B061] =0 THEN 0 ELSE ([B061]/[B001]) END END |"
| R006 | Taxa de endividamento  | Assets to equity ratio  | (N) Total Assets (D) Equity | B001/B061 | CASE WHEN [B061]<=0 OR ABS([B001]/[B061])>100 THEN NULL ELSE CASE WHEN [B001]=0 THEN 0 ELSE ([B001]/[B061]) END END |"
| R007 | Solvabilidade | Solvency ratio | (N) Equity (D) Liabilities | B061/B080 | CASE WHEN [B080]<=0 OR ABS([B061]/[B080])>100 THEN NULL ELSE CASE WHEN [B061] =0 THEN 0 ELSE ([B061]/[B080]) END END |"
| R009 | Cobertura dos activos não correntes  | Non-current assets coverage ratio  | (N) Equity + Current liabilities (D) Non-current assets | (B061+B081)/B004 | CASE WHEN [B004]<=0 OR ABS(([B061]+[B081])/[B004])>100 THEN NULL ELSE CASE WHEN ([B061]+[B081]) =0 THEN 0 ELSE (([B061]+[B081])/[B004]) END END |"
| R023 | Efeito dos juros suportados  | Financial Cost Effect  | (N) Earnings before Tax - EBT (D) Earning before Interest and Tax - EBIT | D086/D085 | CASE WHEN [D085]<=0 OR ABS([D086]/[D085])>100 THEN NULL ELSE CASE WHEN [D086] =0 THEN 0 ELSE ([D086]/[D085]) END END |"
| R034 | Rendibilidade económica das vendas  (RE /VN) | Return on sales  | (N) Operating net income (D) Turnover | D082/D001 | CASE WHEN [D001]<=0 OR ABS([D082]/[D001])>100 THEN NULL ELSE CASE WHEN [D082] =0 THEN 0 ELSE ([D082]/[D001]) END END |"
| R036 | Rendibilidade do activo | Return on assets  | (N) Earnings before Interest, Taxes, Depreciation and Amortization - EBITDA (D) Total Assets | D084/B001 | CASE WHEN [B001]<=0 OR ABS([D084]/[B001])>100 THEN NULL ELSE CASE WHEN [D084] =0 THEN 0 ELSE ([D084]/[B001]) END END |"
| R040 | EBITDA / Volume de negócios | EBITDA over Turnover  | (N) Earnings before Interest, Taxes, Depreciation and Amortization - EBITDA (D) Turnover | D084/D001 | CASE WHEN [D001]<=0 OR ABS([D084]/[D001])>100 THEN NULL ELSE CASE WHEN [D084] =0 THEN 0 ELSE ([D084]/[D001]) END END |"
| R041 | Grau de alavancagem combinada | Degree of combined leverage | (N) Turnover - Costs of goods sold and material consumed - Supplies and external services (D) Earnings before Tax - EBT | (D001-D025-D026)/D086 | CASE WHEN [D086]<=0 OR ([D001]-[D025]-[D026])<0 OR ABS(([D001]-[D025]-[D026])/[D086])>100 THEN NULL ELSE CASE WHEN ([D001]-[D025]-[D026]) =0 THEN 0 ELSE ([D001]-[D025]-[D026])/[D086] END END |"
| R050 | Rotação do activo (nº vezes) | Asset turnover (times) | (N) Turnover (D) Total assets | D001/B001 | CASE WHEN [B001]<=0 OR ABS([D001]/[B001])>100 THEN NULL ELSE CASE WHEN [D001] =0 THEN 0 ELSE ([D001]/[B001]) END END |"
| R056 | Coeficiente Capital/Gastos com o pessoal (euros) | Coefficient Fixed non-financial assets over employee expenses | (N) Tangible and intangible assets (D) Employee expenses | B005/D029 | CASE WHEN [D029]<=0 OR [B005]<0 OR ABS([B005]/[D029])>100 THEN NULL ELSE CASE WHEN [B005] =0 THEN 0 ELSE ([B005]/[D029]) END END |"
| R150 | Volume de negócios / Total do ativo  | Asset turnover ratio  | (N) Turnover (D) Total Assets | D001/B001 | CASE WHEN [B001] <= 0 OR ABS([D001]/[B001])>100 THEN NULL ELSE CASE WHEN [D001] = 0 THEN 0 ELSE ([D001]/[B001]) END END |"
| R152 | Resultado antes de impostos  / Capital próprio  | Profit or loss of the year before taxes (EBT) / Equity  | (N) Earnings before Tax - EBT (D) Equity | D086/B061 | CASE WHEN [B061] <= 0 OR ABS([D086]/[B061])>100 THEN NULL ELSE CASE WHEN [D086] = 0 THEN 0 ELSE ([D086]/[B061]) END END |"
| R155 | Resultado antes de impostos  / Volume de negócios  | Profit or loss of the year before taxes (EBT) / Net turnover  | (N) Earnings before Tax - EBT (D) Turnover | D086/D001 | CASE WHEN [D001] <= 0 OR ABS([D086]/[D001])>100 THEN NULL ELSE CASE WHEN [D086] = 0 THEN 0 ELSE ([D086]/[D001]) END END |"
| R156 | Capital próprio / Total do ativo  | Equity / Total assets  | (N) Equity (D) Total Assets | B061/B001 | CASE WHEN [B001] <= 0 OR ABS([B061]/[B001])>100 THEN NULL ELSE CASE WHEN [B061] = 0 THEN 0 ELSE ([B061]/[B001]) END END |"
| R157 | Fornecedores / Total do ativo  | Trade payables / Total assets  | (N) Suppliers (D) Total Assets | B093/B001 | CASE WHEN [B001] <= 0 OR ABS([B093]/[B001])>100 THEN NULL ELSE CASE WHEN [B093] = 0 THEN 0 ELSE ([B093]/[B001]) END END |"
| R158 | Total de rendimentos / Volume de negócios  | Total income / Net turnover  | (N) Total income (D) Turnover | D021/D001 | CASE WHEN [D001] <= 0 OR ABS([D021]/[D001])>100 THEN NULL ELSE CASE WHEN [D021] = 0 THEN 0 ELSE ([D021]/[D001]) END END |"
| R159 | Total de gastos / Volume de negócios  | Total expenses / Net turnover  | (N) Total expenses (D) Turnover | D062/D001 | CASE WHEN [D001] <= 0 OR ABS([D062]/[D001])>100 THEN NULL ELSE CASE WHEN [D062] = 0 THEN 0 ELSE ([D062]/[D001]) END END |"
| R160 | Investimentos financeiros / Total do ativo  | Financial fixed assets / Total assets  | (N) Financial investments (D) Total Assets | B025/B001 | CASE WHEN [B001] <= 0 OR [B025] < 0 OR ABS([B025]/[B001])>100 THEN NULL ELSE CASE WHEN [B025] = 0 THEN 0 ELSE ([B025]/[B001]) END END |"
| R161 | Clientes  / Total do ativo  | Trade receivables / Total assets  | (N) Clients (D) Total Assets | B041/B001 | CASE WHEN [B001] <= 0 OR ABS([B041]/[B001])>100 THEN NULL ELSE CASE WHEN [B041] = 0 THEN 0 ELSE ([B041]/[B001]) END END |"







