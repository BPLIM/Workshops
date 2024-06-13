<meta charset="utf-8"/>
# Monetary Financial Institutions Balance Sheet Database
## Codebook
`extraction`: June 2023

```s/


    di _new _new "BBS Panel - Asset Side Variables - December 2022
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_ASSET_V01.dta", clear
    quietly keep if year(dofm(date))== 2022 & month(dofm(date))==12
    codebook, all

    di _new _new "BBS Panel - Liability Side Variables - December  2022
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_LIAB_V01.dta", clear
    quietly keep if year(dofm(date))== 2022 & month(dofm(date))==12
    codebook, all


```
