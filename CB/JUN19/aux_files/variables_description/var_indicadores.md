<meta charset="utf-8"/>
# Central Balance Sheet Database
# Economic and Financial Indicators File

[1. Variables Description](#variables-description)

[2. Time Series](#time-series)


## Variables Description

| Name | Description | Unit of measurement | Start Time | End time | Changes in classification | Accounting Plan | Indicator components	| Formula	| Comments |
| :--------: | :-------------: | :-------: | :-----: | :-----: | :-----: | :-----: | :---: | :-------: | :------------------------------------------------: |
| ano | Year of reference | years | 2006 | 2017 | no | . | . | . |  |
| **Identifiers** |
| tina | Anonymized Tax Identification Number | code | 2006 | 2017 | no | . | . | . |  |
| **Indicators** |
| VF06027 | Gross operating margin rate | ratio | 2006 | 2010 | no | POC | (N) Gross margin (D) Operating revenues | VF05926/VF05899 | CASE WHEN [VF05899]<=0 OR ABS([VF05926] / [VF05899])>100 THEN NULL ELSE CASE WHEN [VF05926] =0 THEN 0 ELSE ([VF05926]/[VF05899]) END END |
| VF06028 | Days in receivables (number of days) | ratio | 2006 | 2010 | no | POC | (N) Clients x 365 (D) Turnover | (VF05702x365)/VF05900 | CASE WHEN [VF05900] =0 ABS(ROUND(([VF05702]) x 365 / [VF05900],0))>1825 THEN NULL ELSE CASE WHEN [VF05702] =0 OR [VF05702] = 0 THEN 0 ELSE ROUND(([VF05702]) x 365 / [VF05900],0) END END |
| VF06032 | Days in accounts payable (number of days) | ratio | 2006 | 2010 | no | POC | (N) Suppliers x 365 (D) (Purchases + Supplies and external services ) | (VF06394 x 365)/(VF05866+VF03020) | CASE WHEN ([VF05866]=0) AND ([VF03020]=0) OR ABS(([VF06394]) x 365 / ([VF05866]+[VF03020]))>1825 THEN NULL ELSE CASE WHEN [VF06394] =0 THEN 0 ELSE ROUND(([VF06394]) x 365 / ([VF05866]+[VF03020]),0) END END |
| VF06036 | Inventories turnover (times) | ratio | 2006 | 2010 | no | POC | (N) Turnover (D) Inventories (including Payments on Account from customers) | VF05900/(VF05752+(VF05752(N-1))x 2)  | CASE WHEN ([VF05752]+[VF05752(N-1)]) x 2=0 OR [VF05900] =0 OR ([VF05752]+[VF05752(N-1)]) =0 OR [VF05752] =0 OR [VF05752(N-1)] =0 OR ABS([VF05900] / ([VF05752]+[VF05752(N-1)]) x 2)>100 THEN NULL ELSE ([VF05900]/([VF05752]+ [VF05752(N-1)]) x 2) END |
| VF06037 | Working capital turnover (times) | ratio | 2006 | 2010 | no | POC | (N) Turnover (D) Surplus(+)/Deficit(-) in working capital | VF05900/VF05852 | CASE WHEN [VF05852]<=0 OR ABS([VF05900] / [VF05852])>100 THEN NULL ELSE CASE WHEN [VF05900] =0 THEN 0 ELSE [VF05900] / [VF05852] END END |
| VF06038 | Growth rate of turnover | ratio | 2006 | 2010 | no | POC | (N) Variation in turnover (D) Turnover (homologous year) | VF05902/VF05901 | CASE WHEN [VF05901] =0 OR ABS([VF05902] / [VF05901])>100 THEN NULL ELSE CASE WHEN [VF05902] =0 OR [VF05901]=0 THEN 0 ELSE [VF05902] / [VF05901] END END |
| VF06039 | Growth rate of gross value added (GVA) | ratio | 2006 | 2010 | no | POC | (N) Variation in GVA (D) GVA (homologous year) |  (VF05929)-(VF05929(N-1)) / ABS(VF05929(N-1)) | CASE WHEN [VF05679] =0 AND [VF06011] =0 AND [VF06012] =0 AND ([VF03319]=0) OR [VF05929(N-1)] =0 OR ABS([VF05929] - [VF05929(N-1)]) / ABS([VF05929(N-1)])>100 THEN NULL ELSE ([VF05929] - [VF05929(N-1)]) / ABS([VF05929(N-1)]) END |
| VF06041 | Investment rate | ratio | 2006 | 2010 | no | POC | (N) Investment in Fixed Assets and Variation in Surplus(+)/Deficit(-) in working capital (D) Total income | VF05734/VF05941 | CASE WHEN [VF05679] =0 AND [VF06011] =0 AND [VF06012] =0 AND ([VF03319]=0) OR [VF05941]<=0 OR ABS([VF05734] / [VF05941])>100 OR [VF05734] =0 THEN NULL ELSE [VF05734] / [VF05941] END |
| VF06043 | Coverage rate of investment by self-financing | ratio | 2006 | 2010 | no | POC | (N) Self-financing (D) Investment in Fixed Assets and Variation in Surplus(+)/Deficit(-) in working capital | VF05942/VF05734 | CASE WHEN [VF05679] =0 AND [VF06011] =0 AND [VF06012] =0 AND ([VF03319]=0) OR ([VF05852]-[VF05852(N-1)])<0 OR [VF05734]<=0 OR ABS([VF05942]/[VF05734])>100 THEN NULL ELSE CASE WHEN [VF05942] =0 THEN 0 ELSE [VF05942]/[VF05734] END END |
| VF06045 | Capital ratio | ratio | 2006 | 2010 | no | POC | (N) Equity (excluding Capital Subscribers) (D) (Assets -Debts from Capital Subscribers) | VF05774/(VF05682-VF06395) | CASE WHEN ([VF05682]-[VF06395])=0 OR ABS([VF05774] / ([VF05682]-[VF06395]))>100 THEN NULL ELSE CASE WHEN [VF05774] =0 THEN 0 ELSE [VF05774] / ([VF05682]-[VF06395]) END END |
| VF06050 | Coverage of fixed assets | ratio | 2006 | 2010 | no | POC | (N) Own funds and External stable funds (D) Total gross fixed assets | VF05767/VF06106 | CASE WHEN [VF06106]<=0 OR ABS([VF05767] / [VF06106])>100 THEN NULL ELSE CASE WHEN [VF05767] =0 THEN 0 ELSE [VF05767] / [VF06106] END END |
| VF06052 | Coverage of medium and long term investment | ratio | 2006 | 2010 | no | POC | (N) Own funds and External stable funds (D) Total gross fixed assets and Surplus(+)/Deficit(-) in working capital | VF05767/VF05731 | CASE WHEN [VF05731]=0 OR [VF05852]<=0 OR ABS([VF05767] / [VF05731])>100 THEN NULL ELSE CASE WHEN [VF05767] =0 THEN 0 ELSE [VF05767] / [VF05731] END END |
| VF06054 | Debt to equity ratio | ratio | 2006 | 2010 | no | POC | (N) External stable funds and Negative treasury (D) Own funds (Equity and Accumulated Amortizations and Adjustments/Provisions) | VF05805/VF05770 | CASE WHEN [VF05770]<=0 OR ABS([VF05805] / [VF05770])>100 THEN NULL ELSE CASE WHEN [VF05805] =0 THEN 0 ELSE [VF05805] / [VF05770] END END |
| VF06056 | Current ratio | ratio | 2006 | 2010 | no | POC | (N) Current assets (D) Short-term debt | VF05692/VF05837 | CASE WHEN [VF05837] =0 OR ABS([VF05692] / [VF05837])>100 THEN NULL ELSE CASE WHEN [VF05692] =0 OR [VF05837]=0 THEN 0 ELSE [VF05692] / [VF05837] END END |
| VF06057 | Quick ratio | ratio | 2006 | 2010 | no | POC | (N) Current Assets (excluding Inventories) (D) Short-term debt | VF05694/VF05837 | CASE WHEN [VF05837] =0 OR ABS([VF05694] / [VF05837])>100 THEN NULL ELSE CASE WHEN [VF05694] =0 OR [VF05837]=0 THEN 0 ELSE [VF05694] / [VF05837] END END |
| VF06058 | Return on assets | ratio | 2006 | 2010 | no | POC | (N) Earning before Interest and Tax - EBIT (D) (Assets - Dívidas de Subscritores de Capital) | VF05925/(VF05682-VF06395) | CASE WHEN ([VF05682]-[VF06395])=0 OR ABS([VF05925] / ([VF05682]-[VF06395]))>100 THEN NULL ELSE CASE WHEN [VF05925] =0 THEN 0 ELSE [VF05925] / ([VF05682]-[VF06395]) END END |
| VF06060 | Asset turnover (times) | ratio | 2006 | 2010 | no | POC | (N) Turnover (D) (Assets -Dívidas de Subscritores de Capital) | VF05900/(VF05682-VF06395) | CASE WHEN ([VF05682]-[VF06395])=0 OR ABS([VF05900] / ([VF05682]-[VF06395]))>100 THEN NULL ELSE CASE WHEN [VF05900] =0 THEN 0 ELSE [VF05900] / ([VF05682]-[VF06395]) END END |
| VF06062 | Return on sales | ratio | 2006 | 2010 | no | POC | (N) Earning before Interest and Tax - EBIT (D) Turnover | VF05925/VF05900 | CASE WHEN [VF05900] =0 OR ABS([VF05925] / [VF05900])>100 THEN NULL ELSE CASE WHEN [VF05925] =0 OR [VF05900]=0 THEN 0 ELSE [VF05925]/[VF05900] END END |
| VF06066 | Gross economic profitability | ratio | 2006 | 2010 | no | POC | (N) Gross economic result (excluding Supplementary revenues and Other operating costs/revenues) (D) Tangible Fixed Assets and Surplus/deficit in Working Capital and Fixed Assets in Progress and Payments on Account for Fixed Assets | VF05928/(VF05733+VF06393) | CASE WHEN ([VF05733]+[VF06393])<=0 OR ABS([VF05928] / ([VF05733]+[VF06393]))>100 THEN NULL ELSE CASE WHEN [VF05928] =0 THEN 0 ELSE [VF05928] /([VF05733]+[VF06393]) END END |
| VF06067 | Gross value added rate (GVA) | ratio | 2006 | 2010 | no | POC | (N) GVA (D) Operating Net Income | VF05929/VF05899 | CASE WHEN [VF05899]<=0 OR ABS([VF05929] / [VF05899])>100 THEN NULL ELSE CASE WHEN [VF05929] =0 THEN 0 ELSE [VF05929] / [VF05899] END END |
| VF06071 | Return on equity | ratio | 2006 | 2010 | no | POC | (N) Net income (D) Equity (excluding Capital Subscribers) | VF05794/VF05774 | CASE WHEN [VF05774]<=0 OR ABS([VF05794] / [VF05774])>100 THEN NULL ELSE CASE WHEN [VF05794] =0 THEN 0 ELSE [VF05794] / [VF05774] END END |
| VF06079 | Compound leverage factor | ratio | 2006 | 2010 | no | POC | Interest burden (QS) x Leverage ratio | VF06080 x VF06082 | CASE WHEN ABS([VF06080])>100 OR ABS([VF06082])>100 OR [VF06080] =0 OR [VF06082] =0 OR ABS(CASE WHEN [VF06080] =0 THEN 0 ELSE [VF06080] END)* CASE WHEN [VF06082] =0 THEN 0 ELSE [VF06082] END >100 THEN NULL ELSE CASE WHEN [VF06080] =0 THEN 0 ELSE [VF06080]* CASE WHEN [VF06082] =0 THEN 0 ELSE [VF06082] END END END |
| VF06080 | Interest burden (QS) | ratio | 2006 | 2010 | no | POC | (N) Ordinary profit or loss (D) Earning before Interest and Tax - EBIT | VF05936/VF05925 | CASE WHEN ([VF05936]<=0 AND [VF05925]<0 ) OR [VF05925] =0 OR ABS([VF05936] / [VF05925])>100 THEN NULL ELSE CASE WHEN [VF05936] =0 THEN 0 ELSE [VF05936] / [VF05925] END END |
| VF06082 | Leverage ratio | ratio | 2006 | 2010 | no | POC | (N) (Assets -Debts from Capital Subscribers) (D) Equity (excluding Capital Subscribers) | (VF05682-VF06395)/VF05774 | CASE WHEN [VF05774]<=0 OR ABS(([VF05682]-[VF06395]) / [VF05774])>100 THEN NULL ELSE CASE WHEN ([VF05682]-[VF06395]) =0 THEN 0 ELSE ([VF05682]-[VF06395]) / [VF05774] END END |
| VF06083 | Extraordinary income factor | ratio | 2006 | 2010 | no | POC | (N) Earnings before Tax - EBT (D) Ordinary profit or loss | VF05938/VF05936 | CASE WHEN ([VF05938]<=0 AND [VF05936]<0 ) OR [VF05936] =0 OR ABS([VF05938] / [VF05936])>100 THEN NULL ELSE CASE WHEN [VF05938] =0 THEN 0 ELSE [VF05938] / [VF05936] END END |
| VF06085 | Tax burden (QS) | ratio | 2006 | 2010 | no | POC | (N) Net income (D) Earnings before Tax - EBT | VF05794/VF05938 | CASE WHEN [VF05938] =0 OR ([VF05794]<=0 AND [VF05938]<0 ) THEN NULL ELSE CASE WHEN [VF05794] =0 THEN 0 ELSE [VF05794] / [VF05938] END END |
| VF06087 | Income distribution - Employees | ratio | 2006 | 2010 | no | POC | (N) Income distribution - Employees (D) Total income | VF06107/VF05941 | CASE WHEN [VF05941]<=0 OR ABS([VF06107] / [VF05941])>100 THEN NULL ELSE CASE WHEN [VF06107] =0 THEN 0 ELSE [VF06107] / [VF05941] END END |
| VF06089 | Income distribution - Banks and other funders | ratio | 2006 | 2010 | no | POC | (N) Costs  - Interest expenses (D) Total income | VF03964/VF05941 | CASE WHEN [VF05941]<=0 OR ABS([VF03964] / [VF05941])>100 THEN NULL ELSE CASE WHEN [VF03964] =0 THEN 0 ELSE [VF03964] / [VF05941] END END |
| VF06091 | Income distribution - State | ratio | 2006 | 2010 | no | POC | (N) Income distribution -State (D) Total income | VF06108/VF05941 | CASE WHEN [VF05941]<=0 OR ABS([VF06108] / [VF05941])>100 THEN NULL ELSE CASE WHEN [VF06108] =0 THEN 0 ELSE [VF06108] / [VF05941] END END |
| VF06093 | Income distribution - Enterprise (self-financing) | ratio | 2006 | 2010 | no | POC | (N) Self-financing (D) Total income | VF05942/VF05941 | CASE WHEN [VF05941]<=0 OR ABS([VF05942] / [VF05941])>100 THEN NULL ELSE CASE WHEN [VF05942] =0 THEN 0 ELSE [VF05942] / [VF05941] END END |
| VF06095 | Income distribution - Other | ratio | 2006 | 2010 | no | POC | (N) Non-allocable income (D) Total income | VF06109/VF05941 | CASE WHEN [VF05941]<=0 OR ABS([VF06109] / [VF05941])>100 THEN NULL ELSE CASE WHEN [VF06109] =0 THEN 0 ELSE [VF06109] / [VF05941] END END |
| VF06097 | Coefficient GVA / Property, plant and equipment (euros) | ratio | 2006 | 2010 | no | POC | (N) GVA (D) (Tangible Fixed Assets+ Fixed Assets in Progress and Advances for Fixed Assets) | VF05929/(VF05743+VF06393) | CASE WHEN ([VF05743]+[VF06393])<=0 OR ABS([VF05929]/([VF05743]+[VF06393]))>100 THEN NULL ELSE CASE WHEN [VF05929] =0 THEN 0 ELSE [VF05929] / ([VF05743]+[VF06393]) END END |
| VF06099 | Coefficient GVA / Employee costs (euros) | ratio | 2006 | 2010 | no | POC | (N) GVA (D) Employee expenses  | VF05929/VF05873 | CASE WHEN [VF05873]=0 OR ABS([VF05929] / [VF05873])>100 THEN NULL ELSE CASE WHEN [VF05929] =0 OR [VF05873]=0 THEN 0 ELSE [VF05929] / [VF05873] END END |
| VF06104 | Coefficient capital / Employee costs (euros) | ratio | 2006 | 2010 | no | POC | (N) (Tangible fixed assets+ Fixed Assets in Progress and Payments on Account for Fixed Assets) (D) Employee expenses | (VF05743+VF06393)/VF05873 | CASE WHEN [VF05873]=0 OR ABS(([VF05743]+[VF06393]) / [VF05873])>100 THEN NULL ELSE CASE WHEN ([VF05743]+[VF06393]) =0 THEN 0 ELSE ([VF05743]+[VF06393]) / [VF05873] END END |
| VF16318 | Current ratio | ratio | 2010 | 2017 | no | SNC | (N) Current assets (D) Current liabilities | VF16019/VF16079 | CASE WHEN [VF16079]<=0 OR ABS([VF16019]/[VF16079])>100 THEN NULL ELSE CASE WHEN [VF16019] =0 THEN 0 ELSE ([VF16019]/[VF16079]) END END |
| VF16319 | Quick ratio | ratio | 2010 | 2017 | no | SNC | (N) (Current assets - Inventories and biological assets) (D) Current liabilities | (VF16019-VF16022)/VF16079 | CASE WHEN [VF16079]<=0 OR ABS(([VF16019]-[VF16022])/[VF16079])>100 THEN NULL ELSE CASE WHEN ([VF16019]-[VF16022]) =0 THEN 0 ELSE (([VF16019]-[VF16022])/[VF16079]) END END |
| VF16320 | Capital ratio (QS) | ratio | 2010 | 2017 | no | SNC | (N) Equity (D) Total Assets | VF16051/VF15991 | CASE WHEN [VF15991]<=0 OR ABS([VF16051]/[VF15991])>100 THEN NULL ELSE CASE WHEN [VF16051] =0 THEN 0 ELSE ([VF16051]/[VF15991]) END END |
| VF16323 | Assets to equity ratio  | ratio | 2010 | 2017 | no | SNC | (N) Total Assets (D) Equity | VF15991/VF16051 | CASE WHEN [VF16051]<=0 OR ABS([VF15991]/[VF16051])>100 THEN NULL ELSE CASE WHEN [VF15991]=0 THEN 0 ELSE ([VF15991]/[VF16051]) END END |
| VF16324 | Solvency ratio (QS) | ratio | 2010 | 2017 | no | SNC | (N) Equity (D) Liabilities | VF16051/VF16070 | CASE WHEN [VF16070]<=0 OR ABS([VF16051]/[VF16070])>100 THEN NULL ELSE CASE WHEN [VF16051] =0 THEN 0 ELSE ([VF16051]/[VF16070]) END END |
| VF16326 | Non-current assets coverage ratio | ratio | 2010 | 2017 | no | SNC | (N) Equity + Current liabilities (D) Non-current assets | (VF16051+VF16071)/VF15994 | CASE WHEN [VF15994]<=0 OR ABS(([VF16051]+[VF16071])/[VF15994])>100 THEN NULL ELSE CASE WHEN ([VF16051]+[VF16071]) =0 THEN 0 ELSE (([VF16051]+[VF16071])/[VF15994]) END END |
| VF16331 | Obtained funding over total liabilities (QS) | ratio | 2010 | 2017 | no | SNC | (N) Obtained funding (D) Liabilities | VF16091/VF16070 | CASE WHEN [VF16070]<=0 OR ABS([VF16091]/[VF16070])>100 THEN NULL ELSE CASE WHEN [VF16091] =0 THEN 0 ELSE ([VF16091]/[VF16070]) END END |
| VF16338 | Cost of obtained funding | ratio | 2010 | 2017 | no | SNC | (N) Interest expenses from obtained funding (D) Obtained funding | VF16185/VF16091 | CASE WHEN [VF16091]<=0 OR [VF16185]<=0 OR ABS([VF16185]/[VF16091])>1 THEN NULL ELSE ([VF16185]/[VF16091]) x 100 END |
| VF16340 | Financial Cost Effect | ratio | 2010 | 2017 | no | SNC | (N) Earnings before Tax - EBT (D) Earning before Interest and Tax - EBIT | VF16217/VF16216 | CASE WHEN [VF16216]<=0 OR ABS([VF16217]/[VF16216])>100 THEN NULL ELSE CASE WHEN [VF16217] =0 THEN 0 ELSE ([VF16217]/[VF16216]) END END |
| VF16345 | Operating effect | ratio | 2010 | 2017 | no | SNC | (N) Operating net income (D) Total Assets | VF16213/VF15991 | CASE WHEN [VF16421]=0 OR [VF16422]=0 OR [VF15991]=0 THEN NULL ELSE ([VF16213]/[VF15991]) END |
| VF16346 | Other financial income effect | ratio | 2010 | 2017 | no | SNC | (N) Earning before Interest and Tax - EBIT (D) Operating net income | VF16216/VF16213 | CASE WHEN [VF16421]=0 OR [VF16422]=0 OR [VF16213]=0 THEN NULL ELSE ([VF16216]/[VF16213]) END |
| VF16348 | Compound leverage factor - QS | ratio | 2010 | 2017 | no | SNC | Assets to equity ratio x Interest burden | VF16340 x VF16323 | CASE WHEN [VF16421]=0 OR [VF16422]=0 THEN NULL ELSE [VF16340]x[VF16323] END |
| VF16350 | Tax burden | ratio | 2010 | 2017 | no | SNC | (N) Net income (D) Earnings before Tax - EBT | VF16218/VF16217 | CASE WHEN [VF16421]=0 OR [VF16422]=0 THEN NULL ELSE CASE WHEN [VF16218] =0 OR [VF16217]=0 THEN 0 ELSE ([VF16218]/[VF16217]) END END |
| VF16351 | Return on sales | ratio | 2010 | 2017 | no | SNC | (N) Operating net income (D) Turnover | VF16213/VF16132 | CASE WHEN [VF16132]<=0 OR ABS([VF16213]/[VF16132])>100 THEN NULL ELSE CASE WHEN [VF16213] =0 THEN 0 ELSE ([VF16213]/[VF16132]) END END |
| VF16353 | Return on assets | ratio | 2010 | 2017 | no | SNC | (N) Earnings before Interest, Taxes, Depreciation and Amortization - EBITDA (D) Total Assets | VF16215/VF15991 | CASE WHEN [VF15991]<=0 OR ABS([VF16215]/[VF15991])>100 THEN NULL ELSE CASE WHEN [VF16215] =0 THEN 0 ELSE ([VF16215]/[VF15991]) END END |
| VF16355 | GVA over output - QS | ratio | 2010 | 2017 | no | SNC | (N) GVA (D) Output | VF16205/VF16198 | CASE WHEN [VF16198]<=0 OR ABS([VF16205]/[VF16198])>100 THEN NULL ELSE CASE WHEN [VF16205] =0 THEN 0 ELSE ([VF16205]/[VF16198]) END END |
| VF16357 | EBITDA over Turnover | ratio | 2010 | 2017 | no | SNC | (N) Earnings before Interest, Taxes, Depreciation and Amortization - EBITDA (D) Turnover | VF16215/VF16132 | CASE WHEN [VF16132]<=0 OR ABS([VF16215]/[VF16132])>100 THEN NULL ELSE CASE WHEN [VF16215] =0 THEN 0 ELSE ([VF16215]/[VF16132]) END END |
| VF16358 | Degree of combined leverage | ratio | 2010 | 2017 | no | SNC | (N) Turnover - Costs of goods sold and material consumed - Supplies and external services  (D) Earnings before Tax - EBT | (VF16132-VF16156-VF16157)/VF16217 | CASE WHEN [VF16217]<=0 OR ([VF16132]-[VF16156]-[VF16157])<0 OR ABS(([VF16132]-[VF16156]-[VF16157])/[VF16217])>100 THEN NULL ELSE CASE WHEN ([VF16132]-[VF16156]-[VF16157]) =0 THEN 0 ELSE ([VF16132]-[VF16156]-[VF16157])/[VF16217] END END |
| VF16359 | Degree of operating leverage | ratio | 2010 | 2017 | no | SNC | (N) Turnover - Costs of goods sold and material consumed - Supplies and external services  (D) Operating net income | (VF16132-VF16156-VF16157)/VF16213 | CASE WHEN [VF16423]=0 THEN NULL ELSE CASE WHEN ([VF16132]-[VF16156]-[VF16157]) =0 OR [VF16213]=0 THEN 0 ELSE (([VF16132]-[VF16156]-[VF16157])/[VF16213]) END END |
| VF16360 | Degree of other financial income leverage | ratio | 2010 | 2017 | no | SNC | (N) Operating net income (D) Earning before Interest and Tax - EBIT | VF16213/VF16216 | CASE WHEN [VF16423]=0 OR [VF16216]=0 THEN NULL ELSE ([VF16213]/[VF16216]) END |
| VF16361 | Degree of financial leverage | ratio | 2010 | 2017 | no | SNC | (N) Earning before Interest and Tax - EBIT (D) Earnings before Tax - EBT | VF16216/VF16217 | CASE WHEN [VF16423]=0 OR [VF16217]=0 THEN NULL ELSE ([VF16216]/[VF16217]) END |
| VF16362 | Days sales outstanding (days) | ratio | 2010 | 2017 | no | SNC | (N) Customers x 365 (D) Turnover + Estimate of value added tax received on turnover (relative to residents) | VF16362==(VF16031 x 365)/((VF16132-VF16135) x (1+IVA)+VF16135) | CASE WHEN (([VF16132]-[VF16135]) x (1+[IVA])+[VF16135])=0 OR [VF16132]<=0 OR ABS([VF16031]x 365/(([VF16132]-[VF16135]) x (1+[IVA])+[VF16135]))>1825 THEN NULL ELSE CASE WHEN [VF16031] =0 THEN 0 ELSE [VF16031] x 365/(([VF16132]-[VF16135]) x (1+[IVA])+[VF16135]) END END |
| VF16363 | Days sales outstanding concerning non-residents (days) | ratio | 2010 | 2017 | no | SNC | (N) Non-resident customers x 365 (D) Turnover concerning non-residents | (VF16109 x 365)/VF16135 | CASE WHEN [VF16135]<=0 OR ABS([VF16109] x 365/[VF16135])>1825 THEN NULL ELSE CASE WHEN [VF16109] =0 THEN 0 ELSE ([VF16109] x 365/[VF16135]) END END |
| VF16364 | Days payable outstanding (days) | ratio | 2010 | 2017 | no | SNC | (N) Suppliers x 365 (D) (Purchases + Supplies and external services + Estimate of value added tax on purchases and supplies and external services (relative to residents) | (VF16083x365)/((VF16155+VF16157-VF16159) x  (1+IVA)+VF16159) | CASE WHEN ([VF16155]+[VF16157]-[VF16159]) x (1+[IVA])+[VF16159])=0 OR ([VF16155]+[VF16157])<=0 OR ABS([VF16083]x365/(([VF16155]+[VF16157]-[VF16159])x(1+[IVA])+[VF16159]))>1825 THEN NULL ELSE CASE WHEN [VF16083] =0 THEN 0 ELSE [VF16083]x 365 /(([VF16155]+[VF16157]-[VF16159])x(1+[IVA])+[VF16159]) END END \] |
| VF16365 | Days payable outstanding concerning non-residents (days) | ratio | 2010 | 2017 | no | SNC | (N) Non-resident suppliers x 365 (D) Purchases of goods and services abroad  | (VF16110 x 365)/VF16159 | CASE WHEN [VF16159]<=0 OR ABS([VF16110] x 365 /[VF16159])>1825 THEN NULL ELSE CASE WHEN [VF16110] =0 THEN 0 ELSE ([VF16110] x 365 /[VF16159]) END END |
| VF16366 | Days sales of inventory (days) | ratio | 2010 | 2017 | no | SNC | (N) Inventories and biological assets (D) Purchases | (VF16022 x 365)/VF16155 | CASE WHEN [VF16155]<=0 OR ABS([VF16022] x 365 /[VF16155])>1825 OR [VF16022]<0 THEN NULL ELSE CASE WHEN [VF16022] =0 THEN 0 ELSE ([VF16022] x 365 /[VF16155]) END END |
| VF16367 | Asset turnover (times) - QS | ratio | 2010 | 2017 | no | SNC | (N) Turnover (D) Total assets | VF16132/VF15991 | CASE WHEN [VF15991]<=0 OR ABS([VF16132]/[VF15991])>100 THEN NULL ELSE CASE WHEN [VF16132] =0 THEN 0 ELSE ([VF16132]/[VF15991]) END END |
| VF16369 | Net working capital requirements over turnover | ratio | 2010 | 2017 | no | SNC | (N) Net working capital Requirements (+) / Resources (-) (D) Turnover | VF16130/VF16132 | CASE WHEN [VF16132]<=0 OR ABS([VF16130]/[VF16132])>100 THEN NULL ELSE CASE WHEN [VF16130] =0 THEN 0 ELSE ([VF16130]/[VF16132]) END END |
| VF16370 | Coefficient GVA over fixed non-financial assets | ratio | 2010 | 2017 | no | SNC | (N) GVA (D) Tangible and intangible assets | VF16205/VF15995 | CASE WHEN [VF15995]<=0 OR ABS([VF16205]/[VF15995])>100 THEN NULL ELSE CASE WHEN [VF16205] =0 THEN 0 ELSE ([VF16205]/[VF15995]) END END |
| VF16371 | Coefficient GVA over employee costs | ratio | 2010 | 2017 | no | SNC | (N) GVA (D) Employee expenses | VF16205/VF16160 | CASE WHEN [VF16160]<=0 OR ABS([VF16205]/[VF16160])>100 THEN NULL ELSE CASE WHEN [VF16205] =0 THEN 0 ELSE ([VF16205]/[VF16160]) END END |
| VF16373 | Coefficient Fixed non-financial assets over employee expenses | ratio | 2010 | 2017 | no | SNC | (N) Tangible and intangible assets (D) Employee expenses | VF15995/VF16160 | CASE WHEN [VF16160]<=0 OR [VF15995]<0 OR ABS([VF15995]/[VF16160])>100 THEN NULL ELSE CASE WHEN [VF15995] =0 THEN 0 ELSE ([VF15995]/[VF16160]) END END |
| VF16374 | Suppliers - QS | ratio | 2010 | 2017 | no | SNC | (N) Costs of goods sold and material consumed + Supplies and external services (D) Total net income | (VF16156+VF16157)/VF16152 | CASE WHEN [VF16432]=0 THEN NULL ELSE CASE WHEN ([VF16156]+[VF16157]) =0 OR [VF16152]=0 THEN 0 ELSE (([VF16156]+[VF16157])/[VF16152]) END END |
| VF16375 | Employees - QS | ratio | 2010 | 2017 | no | SNC | (N) Employee expenses (D) Total net income | VF16160/VF16152 | CASE WHEN [VF16432]=0 THEN NULL ELSE CASE WHEN [VF16160] =0 OR [VF16152]=0 THEN 0 ELSE ([VF16160]/[VF16152]) END END |
| VF16376 | Banks and other sources of funding - QS | ratio | 2010 | 2017 | no | SNC | (N) Interest expenses from obtained funding (D) Total net income | VF16185/VF16152 | CASE WHEN [VF16432]=0 THEN NULL ELSE CASE WHEN [VF16185] =0 OR [VF16152]=0 THEN 0 ELSE ([VF16185]/[VF16152]) END END |
| VF16377 | State - QS | ratio | 2010 | 2017 | no | SNC | (N) Income tax + Taxes (D) Total net income | (VF16177+VF16191)/VF16152 | CASE WHEN [VF16432]=0 THEN NULL ELSE CASE WHEN ([VF16177]+[VF16191]) =0 OR [VF16152]=0 THEN 0 ELSE (([VF16177]+[VF16191])/[VF16152]) END END |
| VF16378 | Enterprise - self-financing - QS | ratio | 2010 | 2017 | no | SNC | (N) Self-financing (D) Total net income | VF16220/VF16152 | CASE WHEN [VF16432]=0 THEN NULL ELSE CASE WHEN [VF16220] =0 OR [VF16152]=0 THEN 0 ELSE ([VF16220]/[VF16152]) END END |
| VF16379 | Others - QS | ratio | 2010 | 2017 | no | SNC | (N) (Other expenses+ Interest expenses - Interest expenses from obtained funding - Taxes) (D) Total net income | 1-((VF16156+VF16157)/VF16152)-(VF16160/VF16152)-(VF16185/VF16152)-((VF16177+VF16191)/VF16152)-(VF16220/VF16152)) | CASE WHEN [VF16432]=0 OR [VF16152]= 0 THEN NULL ELSE 1-(([VF16156]+[VF16157])/[VF16152])-([VF16160]/[VF16152])-([VF16185]/[VF16152])-(([VF16177]+[VF16191])/[VF16152])-([VF16220]/[VF16152]) END |
| VF16426 | Interest expenses / EBITDA | ratio | 2010 | 2017 | no | SNC | (N) Interest expenses from obtained funding (D) (N) Earnings before Interest, Taxes, Depreciation and Amortization - EBITDA | VF16185/VF16215 | CASE WHEN [VF16215]<=0 OR ABS([VF16185]/[VF16215])>100 THEN NULL ELSE CASE WHEN [VF16185] =0 THEN 0 ELSE ([VF16185]/[VF16215]) END END |
| VF17747 | Asset turnover ratio | ratio | 2010 | 2017 | no | SNC | (N) Turnover (D) Total Assets | VF16132/VF15991 | CASE WHEN [VF15991] <= 0 OR ABS([VF16132]/[VF15991])>100 THEN NULL ELSE CASE WHEN [VF16132] = 0 THEN 0 ELSE ([VF16132]/[VF15991]) END END |
| VF17749 | Profit or loss of the year before taxes (EBT) / Equity | ratio | 2010 | 2017 | no | SNC | (N) Earnings before Tax - EBT (D) Equity | VF16217/VF16051 | CASE WHEN [VF16051] <= 0 OR ABS([VF16217]/[VF16051])>100 THEN NULL ELSE CASE WHEN [VF16217] = 0 THEN 0 ELSE ([VF16217]/[VF16051]) END END |
| VF17750 | Gross value added / Net turnover | ratio | 2010 | 2017 | no | SNC | (N) GVA (D) Turnover | VF16205/VF16132 | CASE WHEN [VF16132] <= 0 OR ABS([VF16205]/[VF16132])>100 THEN NULL ELSE CASE WHEN [VF16205] = 0 THEN 0 ELSE ([VF16205]/[VF16132]) END END |
| VF17752 | Profit or loss of the year before taxes (EBT) / Net turnover | ratio | 2010 | 2017 | no | SNC | (N) Earnings before Tax - EBT (D) Turnover | VF16217/VF16132 | CASE WHEN [VF16132] <= 0 OR ABS([VF16217]/[VF16132])>100 THEN NULL ELSE CASE WHEN [VF16217] = 0 THEN 0 ELSE ([VF16217]/[VF16132]) END END |
| VF17753 | Equity / Total assets | ratio | 2010 | 2017 | no | SNC | (N) Equity (D) Total Assets | VF16051/VF15991 | CASE WHEN [VF15991] <= 0 OR ABS([VF16051]/[VF15991])>100 THEN NULL ELSE CASE WHEN [VF16051] = 0 THEN 0 ELSE ([VF16051]/[VF15991]) END END |
| VF17754 | Trade payables / Total assets | ratio | 2010 | 2017 | no | SNC | (N) Suppliers (D) Total Assets | VF16083/VF15991 | CASE WHEN [VF15991] <= 0 OR ABS([VF16083]/[VF15991])>100 THEN NULL ELSE CASE WHEN [VF16083] = 0 THEN 0 ELSE ([VF16083]/[VF15991]) END END |
| VF17755 | Total income / Net turnover | ratio | 2010 | 2017 | no | SNC | (N) Total income (D) Turnover | VF16152/VF16132 | CASE WHEN [VF16132] <= 0 OR ABS([VF16152]/[VF16132])>100 THEN NULL ELSE CASE WHEN [VF16152] = 0 THEN 0 ELSE ([VF16152]/[VF16132]) END END |
| VF17756 | Total expenses / Net turnover | ratio | 2010 | 2017 | no | SNC | (N) Total expenses (D) Turnover | VF16193/VF16132 | CASE WHEN [VF16132] <= 0 OR ABS([VF16193]/[VF16132])>100 THEN NULL ELSE CASE WHEN [VF16193] = 0 THEN 0 ELSE ([VF16193]/[VF16132]) END END |
| VF17757 | Financial fixed assets / Total assets | ratio | 2010 | 2017 | no | SNC | (N) Financial investments (D) Total Assets | VF16015/VF15991 | CASE WHEN [VF15991] <= 0 OR [VF16015] < 0 OR ABS([VF16015]/[VF15991])>100 THEN NULL ELSE CASE WHEN [VF16015] = 0 THEN 0 ELSE ([VF16015]/[VF15991]) END END |
| VF17758 | Trade receivables / Total assets | ratio | 2010 | 2017 | no | SNC | (N) Clients (D) Total Assets | VF16031/VF15991 | CASE WHEN [VF15991] <= 0 OR ABS([VF16031]/[VF15991])>100 THEN NULL ELSE CASE WHEN [VF16031] = 0 THEN 0 ELSE ([VF16031]/[VF15991]) END END |
| VF17759 | Other financial assets and cash and bank / Total assets | ratio | 2010 | 2017 | no | SNC | (N) (Cash and bank deposits + Other financial instruments) (D) Total Assets | (VF16036+VF16039)/VF15991 | CASE WHEN [VF15991] <= 0 OR ([VF16036] + [VF16039]) < 0 OR ABS(([VF16036]+[VF16039])/[VF15991]) > 100 THEN NULL ELSE CASE WHEN ([VF16036] + [VF16039]) = 0 THEN 0 ELSE (([VF16036]+[VF16039])/[VF15991]) END END |



| Legend |     |
| :----: | :--------: |
| POC | Official Chart of Accounts |
| SNC	| Accounting Standards System |
| (N) | Numerator |
| (D) | Denominator |

## Time Series

|     |   2006 | 2007 | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 |
| :---: |  :---: | :---: |  :---: |  :---: |  :---: |  :---: |  :---: |  :---: |  :---: |  :---: |  :---: | :---: |
| ano | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| tina | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF06027 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06028 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06032 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06036 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06037 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06038 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06039 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06041 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06043 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06045 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06052 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06050 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06054 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06056 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06057 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06058 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06060 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06062 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06066 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06067 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06071 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06079 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06080 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06082 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06083 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06085 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06087 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06089 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06091 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06093 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06095 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06097 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06099 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF06104 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF16318 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16319 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16320 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16323 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16324 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16331 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16326 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16338 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16340 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16345 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16346 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16348 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16350 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16351 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16353 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16355 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16357 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16358 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16359 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16360 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16361 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16362 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16363 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16364 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16365 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16366 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16367 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16369 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16370 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16371 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16373 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16374 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16375 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16377 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16376 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16378 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16379 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF16426 | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF17747 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF17749 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF17750 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF17752 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF17753 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF17754 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF17755 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF17756 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF17757 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF17758 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF17759 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |


| Legend |   |
| :---: | :---------: |
| [✓] | Variable available in year t |
| [x] | Variable not available in year t |







