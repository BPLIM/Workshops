<meta charset="utf-8"/>
# Fast and Exceptional Enterprise Survey
## Descriptive Statistics
`extraction`: SEP22

```
    di _new _new "Edition 15 (2020)"
    quietly use "S:/data/Products/COVID/2020_07/Output/Data/152020/IREE_I_WFRM_152020_JUL20_V01.dta", clear
    drop nipc
    label language en
    sum, separator(1000)

    di _new _new "Edition 16 (2020)"
    quietly use "S:/data/Products/COVID/2020_07/Output/Data/162020/IREE_I_WFRM_162020_JUL20_V01.dta", clear
    drop nipc
    label language en
    sum, separator(1000)

    di _new _new "Edition 17 (2020)"
    quietly use "S:/data/Products/COVID/2020_07/Output/Data/172020/IREE_I_WFRM_172020_JUL20_V01.dta", clear
    drop nipc
    label language en
    sum, separator(1000)

    di _new _new "Edition 18 (2020)"
    quietly use "S:/data/Products/COVID/2020_07/Output/Data/182020/IREE_I_WFRM_182020_JUL20_V01.dta", clear
    drop nipc
    label language en
    sum, separator(1000)

    di _new _new "Edition 19 (2020)"
    quietly use "S:/data/Products/COVID/2020_07/Output/Data/192020/IREE_I_WFRM_192020_JUL20_V01.dta", clear
    drop nipc
    label language en
    sum, separator(1000)

    di _new _new "Edition 20 (2020)"
    quietly use "S:/data/Products/COVID/2020_07/Output/Data/202020/IREE_I_WFRM_202020_JUL20_V01.dta", clear
    drop nipc
    label language en
    sum, separator(1000)

    di _new _new "Edition 21 (2020)"
    quietly use "S:/data/Products/COVID/2020_07/Output/Data/212020/IREE_I_WFRM_212020_JUL20_V01.dta", clear
    drop nipc
    label language en
    sum, separator(1000)

    di _new _new "Edition 22 (2020)"
    quietly use "S:/data/Products/COVID/2020_07/Output/Data/222020/IREE_I_WFRM_222020_JUL20_V01.dta", clear
    drop nipc
    label language en
    sum, separator(1000)

    di _new _new "Edition 23 (2020)"
    quietly use "S:/data/Products/COVID/2020_07/Output/Data/232020/IREE_I_WFRM_232020_JUL20_V01.dta", clear
    drop nipc
    label language en
    sum, separator(1000)

    di _new _new "Edition 24 (2020)"
    quietly use "S:/data/Products/COVID/2020_11/Output/Data/242020/IREE_I_WFRM_242020_NOV20_V01.dta", clear
    drop nipc
    label language en
    sum, separator(1000)

    di _new _new "Edition 01 (2021)"
    quietly use "S:/data/Products/COVID/2021_04/Output/Data/012021/IREE_I_WFRM_012021_APR21_V01.dta", clear
    drop nipc
    label language en
    sum, separator(1000)

    di _new _new "Edition 01 (2022)"
    quietly use "S:/data/Products/COVID/2022_09/Output/Data/012022/IREE_I_WFRM_012022_SEP22_V01.dta", clear
    drop nipc
    label language en
    sum, separator(1000)
```
