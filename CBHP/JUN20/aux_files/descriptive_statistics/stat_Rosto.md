<meta charset="utf-8"/>
# Central Balance Sheet Harmonized Panel Data
## Descriptive statistics
`extraction`: June 2020

## **General Information - Harmonized Panel**

```
    di _new _new "Rosto - 2006-2018"
    quietly use "S:/data/Products/CB/2020_06/CB_Panel/Output/Data/Firms/CBHP_I_YFRM_20062018_JUN20_ROSTO_V01.dta", clear
    sum, separator(1000)

    di "Descriptive Statistics by Year"
    bysort ano: sum, separator(1000)
```







