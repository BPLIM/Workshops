<meta charset="utf-8"/>
# Variables in the Historical Series of the Portuguese Banking Sector Database
## Codebook
`extraction`: October 2021


## **Balance Sheet: Yearly**

```s/
di _new _new "SLB - Balance Sheet Variables - 1990"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 1990
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 1991"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 1991
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 1992"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 1992
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 1993"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 1993
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 1994"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 1994
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 1995"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 1995
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 1996"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 1996
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 1997"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 1997
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 1998"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 1998
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 1999"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 1999
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 2000"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 2000
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 2001"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 2001
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 2002"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 2002
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 2003"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 2003
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 2004"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 2004
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 2005"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 2005
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 2006"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 2006
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 2007"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 2007
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 2008"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 2008
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 2009"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 2009
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 2010"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 2010
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 2011"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 2011
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 2012"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 2012
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 2013"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 2013
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 2014"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 2014
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 2015"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 2015
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 2016"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 2016
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 2017"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 2017
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 2018"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 2018
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 2019"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 2019
codebook, all mv

di _new _new "SLB - Balance Sheet Variables - 2020"
quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_YBNK_19902020_OCT21_QA1_V01.dta", clear
quietly keep if year== 2020
codebook, all mv
```


## **Balance Sheet: Quarterly**

```s/
    di _new _new "SLB - Balance Sheet Variables - 2001"
    quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_QBNK_20012020_OCT21_QA1_V01.dta", clear
    quietly keep if year(dofq(date))== 2001
    codebook, all mv

    di _new _new "SLB - Balance Sheet Variables - 2002"
    quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_QBNK_20012020_OCT21_QA1_V01.dta", clear
    quietly keep if year(dofq(date))== 2002
    codebook, all mv

    di _new _new "SLB - Balance Sheet Variables - 2003"
    quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_QBNK_20012020_OCT21_QA1_V01.dta", clear
    quietly keep if year(dofq(date))== 2003
    codebook, all mv

    di _new _new "SLB - Balance Sheet Variables - 2004"
    quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_QBNK_20012020_OCT21_QA1_V01.dta", clear
    quietly keep if year(dofq(date))== 2004
    codebook, all mv

    di _new _new "SLB - Balance Sheet Variables - 2005"
    quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_QBNK_20012020_OCT21_QA1_V01.dta", clear
    quietly keep if year(dofq(date))== 2005
    codebook, all mv

    di _new _new "SLB - Balance Sheet Variables - 2006"
    quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_QBNK_20012020_OCT21_QA1_V01.dta", clear
    quietly keep if year(dofq(date))== 2006
    codebook, all mv

    di _new _new "SLB - Balance Sheet Variables - 2007"
    quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_QBNK_20012020_OCT21_QA1_V01.dta", clear
    quietly keep if year(dofq(date))== 2007
    codebook, all mv

    di _new _new "SLB - Balance Sheet Variables - 2008"
    quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_QBNK_20012020_OCT21_QA1_V01.dta", clear
    quietly keep if year(dofq(date))== 2008
    codebook, all mv

    di _new _new "SLB - Balance Sheet Variables - 2009"
    quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_QBNK_20012020_OCT21_QA1_V01.dta", clear
    quietly keep if year(dofq(date))== 2009
    codebook, all mv

    di _new _new "SLB - Balance Sheet Variables - 2010"
    quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_QBNK_20012020_OCT21_QA1_V01.dta", clear
    quietly keep if year(dofq(date))== 2010
    codebook, all mv

    di _new _new "SLB - Balance Sheet Variables - 2011"
    quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_QBNK_20012020_OCT21_QA1_V01.dta", clear
    quietly keep if year(dofq(date))== 2011
    codebook, all mv

    di _new _new "SLB - Balance Sheet Variables - 2012"
    quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_QBNK_20012020_OCT21_QA1_V01.dta", clear
    quietly keep if year(dofq(date))== 2012
    codebook, all mv

    di _new _new "SLB - Balance Sheet Variables - 2013"
    quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_QBNK_20012020_OCT21_QA1_V01.dta", clear
    quietly keep if year(dofq(date))== 2013
    codebook, all mv

    di _new _new "SLB - Balance Sheet Variables - 2014"
    quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_QBNK_20012020_OCT21_QA1_V01.dta", clear
    quietly keep if year(dofq(date))== 2014
    codebook, all mv

    di _new _new "SLB - Balance Sheet Variables - 2015"
    quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_QBNK_20012020_OCT21_QA1_V01.dta", clear
    quietly keep if year(dofq(date))== 2015
    codebook, all mv

    di _new _new "SLB - Balance Sheet Variables - 2016"
    quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_QBNK_20012020_OCT21_QA1_V01.dta", clear
    quietly keep if year(dofq(date))== 2016
    codebook, all mv

    di _new _new "SLB - Balance Sheet Variables - 2017"
    quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_QBNK_20012020_OCT21_QA1_V01.dta", clear
    quietly keep if year(dofq(date))== 2017
    codebook, all mv

    di _new _new "SLB - Balance Sheet Variables - 2018"
    quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_QBNK_20012020_OCT21_QA1_V01.dta", clear
    quietly keep if year(dofq(date))== 2018
    codebook, all mv

    di _new _new "SLB - Balance Sheet Variables - 2019"
    quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_QBNK_20012020_OCT21_QA1_V01.dta", clear
    quietly keep if year(dofq(date))== 2019
    codebook, all mv

    di _new _new "SLB - Balance Sheet Variables - 2020"
    quietly use "Z:/data/Products/SLB/2021_10/Output/Data/SLB_C_QBNK_20012020_OCT21_QA1_V01.dta", clear
    quietly keep if year(dofq(date))== 2020
    codebook, all mv
```
