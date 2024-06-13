<meta charset="utf-8"/>
# Central Credit Responsibility Database
## Summary Statistics
`extraction`: April 2019

```stc_2

    di _new _new "CCR Exposure Level - 2009 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/2009/CRC_A_MFRMEXP_2009_APR17_COLL_V01.dta", clear
    sum valorg, separator(1000)

    di _new _new "CCR Exposure Level - 2010 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/2010/CRC_A_MFRMEXP_2010_APR17_COLL_V01.dta", clear
    sum valorg, separator(1000)

    di _new _new "CCR Exposure Level - 2011 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/2011/CRC_A_MFRMEXP_2011_APR17_COLL_V01.dta", clear
    sum valorg, separator(1000)

    di _new _new "CCR Exposure Level - 2012 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/2012/CRC_A_MFRMEXP_2012_APR17_COLL_V01.dta", clear
    sum valorg, separator(1000)

    di _new _new "CCR Exposure Level - 2013 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/2013/CRC_A_MFRMEXP_2013_APR17_COLL_V01.dta", clear
    sum valorg, separator(1000)

    di _new _new "CCR Exposure Level - 2014 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/2014/CRC_A_MFRMEXP_2014_APR17_COLL_V01.dta", clear
    sum valorg, separator(1000)

    di _new _new "CCR Exposure Level - 2015 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/2015/CRC_A_MFRMEXP_2015_APR17_COLL_V01.dta", clear
    sum valorg, separator(1000)

    di _new _new "CCR Exposure Level - 2016 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/2016/CRC_A_MFRMEXP_2016_APR17_COLL_V01.dta", clear
    sum valorg, separator(1000)

    di _new _new "CCR Exposure Level - 2017 - December"
    quietly use "Z:/data/Products/CRC/2018_04/CRC_Annual/Output/Data/Firms/2017/CRC_A_MFRMEXP_2017_APR18_COLL_V01.dta", clear
    sum valorg, separator(1000)

    di _new _new "CCR Exposure Level - 2018 - December"
    quietly use "Z:/data/Products/CRC/2019_04/CRC_Annual/Output/Data/Firms/2018/CRC_A_MFRMEXP_2018_APR19_COLL_V01.dta", clear
    sum valorg, separator(1000)

```
