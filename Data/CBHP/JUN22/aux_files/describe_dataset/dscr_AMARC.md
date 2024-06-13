<meta charset="utf-8"/>
# Central Balance Sheet Harmonized Panel Data
## File Description
`extraction`: June 2022

## **Corporate Actions - Harmonized Panel**

```
    di _new _new "AMARC - 2006-2020"
    quietly use "S:/data/Products/CB/2022_06/CB_Panel/Output/Data/Firms/CBHP_I_YFRM_20062020_JUN22_AMARC_V01.dta", clear
    drop nipc*
    label language en
    describe
```
