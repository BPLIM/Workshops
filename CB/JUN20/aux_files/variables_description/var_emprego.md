<meta charset="utf-8"/>
# Central Balance Sheet Database
# Employment Information File

[1. Variables Description](#variables-description)

[2. Time Series](#time-series)


## Variables Description

| Name | Description | Unit of measurement | Start Time | End time | Changes in classification | Accounting Plan | Accounting Regime | Comments |
| -------- | ------------- | ------- | ----- | ----- | ----- | ----- | --- | ------- |
| ano | Year of reference | years | 2006 | 2018 | no | . | . |  |
| **Identifiers** |
| tina | Anonymized Tax Identification Number | code | 2006 | 2018 | no | . | na |  |
| **Total Number of Employees** |
| VF03319 | Number of (paid and unpaid) employees | number of people | 2006 | 2010 | no | POC | na | [Q05-0507-Nota7-A0419]+[Q05-0507-Nota7-A1508] |
| VF15532 | Number of (paid and unpaid) employees | number of people | 2010 | 2018 | no | SNC | N,S,M | Q05A-05291A-A6012-1-soma |
| VF03321 | Number of paid employees | number of people | 2006 | 2010 | no | POC | na | [Q05-0507-Nota7-A1509]+[Q05-0507-Nota7-A0422] |
| VF15534 | Number of paid employees | number of people | 2010 | 2018 | no | SNC | N,S,M | Q05A-05291A-A6013-1 |
| VF04902 | Number of unpaid employees | number of people | 2006 | 2010 | no | POC | na | Q05-0507-Nota7-A1508 |
| VF15536 | Number of unpaid employees | number of people | 2010 | 2018 | no | SNC | N,S,M | Q05A-05291A-A6014-1 |
| **Employment by Gender** |
| VF15546 | Number of (paid and unpaid) male employees | number of people | 2010 | 2018 | no | SNC | N,S,M | Q05A-05291A-A6019-1 |
| VF15548 | Number of (paid and unpaid) female employees | number of people | 2010 | 2018 | no | SNC | N,S,M | Q05A-05291A-A6020-1 |
| **Employment by Contract Type** |
| VF03325 | Service providers | number of people | 2006 | 2010 | no | POC | na | Q05-0507-Nota7-A0423 |
| VF15551 | Service providers | number of people | 2010 | 2018 | no | SNC | N,S,M | Q05A-05291A-A6022-1 |
| VF03322 | Number of paid apprentices | number of people | 2006 | 2010 | no | POC | na | Q05-0507-Nota7-A0420 |
| VF03323 | Number of paid homeworkers | number of people | 2006 | 2010 | no | POC | na | Q05-0507-Nota7-A0421 |
| **Research and Development Employment** |
| VF03326 | Number of employees allocated to research and development  | number of people | 2006 | 2010 | no | POC | na | Q05-0507-Nota7-A0424 |
| VF15550 | Number of employees allocated to research and development  | number of people | 2010 | 2018 | no | SNC | N,S,M | Q05A-05291A-A6021-1 |
| **Employment by Working Time Arrangement** |
| VF03320 | Number of (paid and unpaid) full-time employees | number of people | 2006 | 2010 | no | POC | na | Q05-0507-Nota7-A0418 |
| VF04904 | Number of (paid and unpaid) part-time employees | number of people | 2006 | 2010 | no | POC | na | Q05-0507-Nota7-A1510 |
| VF04903 | Number of paid full-time employees | number of people | 2006 | 2010 | no | POC | na | Q05-0507-Nota7-A1509 |
| VF03324 | Number of paid part-time employees | number of people | 2006 | 2010 | no | POC | na | Q05-0507-Nota7-A0422 |
| VF15538 | Number of (paid and unpaid) full-time employees | number of people | 2010 | 2018 | no | SNC | N,S,M | Q05A-05291A-A6015-1 |
| VF15542 | Number of (paid and unpaid) part-time employees | number of people | 2010 | 2018 | no | SNC | N,S,M | Q05A-05291A-A6017-1 |
| VF15540 | Number of paid full-time employees | number of people | 2010 | 2018 | no | SNC | N,S,M | Q05A-05291A-A6016-1 |
| VF15544 | Number of paid part-time employees | number of people | 2010 | 2018 | no | SNC | N,S,M | Q05A-05291A-A6018-1 |
| **Temporary Agency Employment** |
| VF03327 | Temporary Agency Employment | number of people | 2006 | 2010 | no | POC | na | Q05-0507-Nota7-A0425 |
| VF15553 | Temporary Agency Employment | number of people | 2010 | 2018 | no | SNC | N,S,M | Q05A-05291A-A6023-1 |
| **Total Hours Worked** |
| VF03328 | Number of hours worked by paid and unpaid employees | number of hours | 2006 | 2010 | no | POC | na | Q05-0507-Nota7-A0426 |
| VF15533 | Number of hours worked by paid and unpaid employees | number of hours | 2010 | 2018 | no | SNC | N,S,M | Q05A-05291A-A6012-2-soma |
| VF03330 | Number of hours worked by paid employees | number of hours | 2006 | 2010 | no | POC | na | Q05-0507-Nota7-A0428 |
| VF15535 | Number of hours worked by paid employees | number of hours | 2010 | 2018 | no | SNC | N,S,M | Q05A-05291A-A6013-2 |
| VF04905 | Number of hours worked by unpaid employees | number of hours | 2006 | 2010 | no | POC | na | Q05-0507-Nota7-A1511 |
| VF15537 | Number of hours worked by unpaid employees | number of hours | 2010 | 2018 | no | SNC | N,S,M | Q05A-05291A-A6014-2 |
| VF05990 | Total Hours Worked | number of hours | 2006 | 2010 | no | POC | na | [Q05-0507-Nota7-A0426] |
| **Hours Worked by Working Time Arrangement** |
| VF03329 | Number of hours worked by paid and unpaid full-time employees | number of hours | 2006 | 2010 | no | POC | na | Q05-0507-Nota7-A0427 |
| VF15539 | Number of hours worked by paid and unpaid full-time employees | number of hours | 2010 | 2018 | no | SNC | N,S,M | Q05A-05291A-A6015-2 |
| VF04906 | Number of hours worked by paid full-time employees | number of hours | 2006 | 2010 | no | POC | na | Q05-0507-Nota7-A1512 |
| VF15541 | Number of hours worked by paid full-time employees | number of hours | 2010 | 2018 | no | SNC | N,S,M | Q05A-05291A-A6016-2 |
| VF04907 | Number of hours worked by paid and unpaid part-time employees | number of hours | 2006 | 2010 | no | POC | na | Q05-0507-Nota7-A1513 |
| VF15543 | Number of hours worked by paid and unpaid part-time employees | number of hours | 2010 | 2018 | no | SNC | N,S,M | Q05A-05291A-A6017-2 |
| VF03331 | Number of hours worked by paid part-time employees | number of hours | 2006 | 2010 | no | POC | na | Q05-0507-Nota7-A0429 |
| VF15545 | Number of hours worked by paid part-time employees | number of hours | 2010 | 2018 | no | SNC | N,S,M | Q05A-05291A-A6018-2 |
| **Hours Worked by Gender** |
| VF15547 | Number of hours worked by male employees | number of hours | 2010 | 2018 | no | SNC | N,S,M | Q05A-05291A-A6019-2 |
| VF15549 | Number of hours worked by female employees | number of hours | 2010 | 2018 | no | SNC | N,S,M | Q05A-05291A-A6020-2 |
| **Hours worked by Contract Type** |
| VF03332 | Number of hours worked by service providers | number of hours | 2006 | 2010 | no | POC | na | Q05-0507-Nota7-A0430 |
| VF15552 | Number of hours worked by service providers | number of hours | 2010 | 2018 | no | SNC | N,S,M | Q05A-05291A-A6022-2 |
|  |  |  |  |  |  |  |  |  |  |  |  |
| VF04036 | Corporate bodies Remunerations | euros | 2006 | 2010 | no | POC | na | Q06-A0641 |
| VF04037 | Salaries | euros | 2006 | 2010 | no | POC | na | Q06-A0642 |
| VF04038 | Pensions | euros | 2006 | 2010 | no | POC | na | Q06-A0643 |
| VF04039 | Retirement benefits and pension premiums | euros | 2006 | 2010 | no | POC | na | Q06-A0644 |
| VF04040 | Social security expenses | euros | 2006 | 2010 | no | POC | na | Q06-A0645 |
| VF04041 | Insurance schemes for accidents at work and occupational diseases | euros | 2006 | 2010 | no | POC | na | Q06-A0646 |
| VF04042 | Expenses with social actions | euros | 2006 | 2010 | no | POC | na | Q06-A0647 |
| VF04043 | Other employee expenses | euros | 2006 | 2010 | no | POC | na | Q06-A0648 |
| VF15555 | Salaries of corporate bodies | euros | 2010 | 2018 | no | SNC | N,S,M | Q05A-05292A-A6025 |
| VF15556 | Salaries of corporate bodies- of which participation in profits | euros | 2010 | 2018 | no | SNC | N,S,M | Q05A-05292A-A6026 |
| VF15557 | Salaries | euros | 2010 | 2018 | no | SNC | N,S,M | Q05A-05292A-A6027 |
| VF15558 | Salaries - of which participation in the profits | euros | 2010 | 2018 | no | SNC | N,S,M | Q05A-05292A-A6028 |
| VF15559 | Post-employment benefits | euros | 2010 | 2018 | no | SNC | N,S,M | Q05A-05292A-A6029-soma |
| VF15560 | Pension premiums | euros | 2010 | 2018 | no | SNC | N,S,M | Q05A-05292A-A6030 |
| VF15561 | Other benefits | euros | 2010 | 2018 | no | SNC | N,S,M | Q05A-05292A-A6031 |
| VF15562 | Post-employment benefits- Other benefits: of which defined contribution pension plans - corporate bodies | euros | 2010 | 2018 | no | SNC | N,S,M | Q05A-05292A-A6032 |
| VF15563 | Post-employment benefits- Other benefits: of which defined contribution pension plans - other | euros | 2010 | 2018 | no | SNC | N,S,M | Q05A-05292A-A6033 |
| VF15564 | Compensations/indemnities | euros | 2010 | 2018 | no | SNC | N,S,M | Q05A-05292A-A6034 |
| VF15565 | Social security expenses | euros | 2010 | 2018 | no | SNC | N,S,M | Q05A-05292A-A6035 |
| VF15566 | Insurance schemes for accidents at work and occupational diseases | euros | 2010 | 2018 | no | SNC | N,S,M | Q05A-05292A-A6036 |
| VF15567 | Expenses with social actions | euros | 2010 | 2018 | no | SNC | N,S,M | Q05A-05292A-A6037 |
| VF15568 | Other employee expenses | euros | 2010 | 2018 | no | SNC | N,S,M | Q05A-05292A-A6038 |
| VF15569 | Training expenses | euros | 2010 | 2018 | no | SNC | N,S,M | Q05A-05292A-A6039 |
| VF15570 | Other expenses- Expenses with uniforms | euros | 2010 | 2018 | no | SNC | N,S,M | Q05A-05292A-A6040 |
| VF18834 | Expenses with defined pension plans | euros | 2010 | 2018 | no | SNC | N,S,M | Q05A-05292A-A6137 |


|Legend |     |
| :----: | :--------: |
| na | Not Applicable |
| POC | Official Chart of Accounts |
| SNC	| Accounting Standards System |
| N	| International Accounting Standards |
| S	| Accounting and Financial Reporting Standards and Accounting and Financial Reporting Standards for Small-Sized Entities |
| M	| Accounting and Financial Reporting Standards for Micro-Entities |



## Time Series

|     |   2006 | 2007 | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018 |
| :---: |  :---: | :---: |  :---: |  :---: |  :---: |  :---: |  :---: |  :---: |  :---: |  :---: |  :---: | :---: | :---: |
| ano | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| tina | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF03319 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF03320 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF03321 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF03322 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF03323 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF03324 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF03325 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF03326 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF03327 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF04902 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF04903 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF04904 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF05990 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF15532 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15534 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15536 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15538 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15540 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15542 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15544 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15546 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15548 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15550 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15551 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15553 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF03328 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF03329 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF03330 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF03331 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF03332 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF04905 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF04906 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF04907 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF05990 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF15533 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15535 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15537 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15539 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15541 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15543 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15545 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15547 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15549 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15552 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF04036 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF04037 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF04038 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF04039 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF04040 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF04041 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF04042 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF04043 | [✓] | [✓] | [✓] | [✓] | [✓] | [x] | [x] | [x] | [x] | [x] | [x] | [x] | [x] |
| VF15555 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15556 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15557 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15558 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15559 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15560 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15561 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15562 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15563 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15564 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15565 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15566 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15567 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15568 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15569 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF15570 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |
| VF18834 | [x] | [x] | [x] | [x] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] | [✓] |


| Legend |   |
| :---: | :---------: |
| [✓] | Variable available in year t |
| [x] | Variable not available in year t |







