<meta charset="utf-8"/>
# Monetary Financial Institutions Balance Sheet Database
## Codebook
`extraction`: June 2021

```s/


    di _new _new "BBS Panel - Asset Side Variables - December 2020
    quietly use "Z:\data\Products\BBS\2021_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2020_JUN21_ASSET_V01.dta", clear
    quietly keep if year(dofm(date))== 2020 & month(dofm(date))==12
    codebook, all

    di _new _new "BBS Panel - Liability Side Variables - December  2020
    quietly use "Z:\data\Products\BBS\2021_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2020_JUN21_LIAB_V01.dta", clear
    quietly keep if year(dofm(date))== 2020 & month(dofm(date))==12
    codebook, all


```
