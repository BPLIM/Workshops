<meta charset="utf-8"/>
# Central Balance Sheet Harmonized Panel Data
## Codebook
`extraction`: June 2020

## **Corporate Actions - Harmonized Panel**

```
    di _new _new "AMARC - 2006-2018"
    quietly use "S:/data/Products/CB/2020_06/CB_Panel/Output/Data/Firms/CBHP_I_YFRM_20062018_JUN20_AMARC_V01.dta", clear
    label language en
    codebook, all mv
```







