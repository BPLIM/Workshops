<meta charset="utf-8"/>
# Monetary Financial Institutions Balance Sheet Database
## Descriptive statistics
`extraction`: June 2023



```s/

    di _new _new "BBS Panel - Asset Side Variables - December 1997
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_ASSET_V01.dta", clear
    quietly keep if year(dofm(date))== 1997 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Liability Side Variables - December 1997
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_LIAB_V01.dta", clear
    quietly keep if year(dofm(date))== 1997 & month(dofm(date))==12
    sum, separator(1000)


    di _new _new "BBS Panel - Asset Side Variables - December 1998
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_ASSET_V01.dta", clear
    quietly keep if year(dofm(date))== 1998 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Liability Side Variables - December 1998
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_LIAB_V01.dta", clear
    quietly keep if year(dofm(date))== 1998 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Asset Side Variables - December 1999
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_ASSET_V01.dta", clear
    quietly keep if year(dofm(date))== 1999 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Liability Side Variables - December 1999
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_LIAB_V01.dta", clear
    quietly keep if year(dofm(date))== 1999 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Asset Side Variables - December 2000
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_ASSET_V01.dta", clear
    quietly keep if year(dofm(date))== 2000 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Liability Side Variables - December 2000
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_LIAB_V01.dta", clear
    quietly keep if year(dofm(date))== 2000 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Asset Side Variables - December 2001
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_ASSET_V01.dta", clear
    quietly keep if year(dofm(date))== 2001 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Liability Side Variables - December 2001
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_LIAB_V01.dta", clear
    quietly keep if year(dofm(date))== 2001 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Asset Side Variables - December 2002
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_ASSET_V01.dta", clear
    quietly keep if year(dofm(date))== 2002 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Liability Side Variables - December 2002
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_LIAB_V01.dta", clear
    quietly keep if year(dofm(date))== 2002 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Asset Side Variables - December 2003
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_ASSET_V01.dta", clear
    quietly keep if year(dofm(date))== 2003 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Liability Side Variables - December 2003
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_LIAB_V01.dta", clear
    quietly keep if year(dofm(date))== 2003 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Asset Side Variables - December 2004
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_ASSET_V01.dta", clear
    quietly keep if year(dofm(date))== 2004 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Liability Side Variables - December 2004
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_LIAB_V01.dta", clear
    quietly keep if year(dofm(date))== 2004 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Asset Side Variables - December 2005
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_ASSET_V01.dta", clear
    quietly keep if year(dofm(date))== 2005 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Liability Side Variables - December 2005
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_LIAB_V01.dta", clear
    quietly keep if year(dofm(date))== 2005 & month(dofm(date))==12
    sum, separator(1000)


    di _new _new "BBS Panel - Asset Side Variables - December 2006
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_ASSET_V01.dta", clear
    quietly keep if year(dofm(date))== 2006 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Liability Side Variables - December 2006
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_LIAB_V01.dta", clear
    quietly keep if year(dofm(date))== 2006 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Asset Side Variables - December 2007
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_ASSET_V01.dta", clear
    quietly keep if year(dofm(date))== 2007 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Liability Side Variables - December 2007
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_LIAB_V01.dta", clear
    quietly keep if year(dofm(date))== 2007 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Asset Side Variables - December 2008
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_ASSET_V01.dta", clear
    quietly keep if year(dofm(date))== 2008 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Liability Side Variables - December 2008
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_LIAB_V01.dta", clear
    quietly keep if year(dofm(date))== 2008 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Asset Side Variables - December 2009
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_ASSET_V01.dta", clear
    quietly keep if year(dofm(date))== 2009 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Liability Side Variables - December 2009
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_LIAB_V01.dta", clear
    quietly keep if year(dofm(date))== 2009 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Asset Side Variables - December 2010
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_ASSET_V01.dta", clear
    quietly keep if year(dofm(date))== 2010 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Liability Side Variables - December 2010
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_LIAB_V01.dta", clear
    quietly keep if year(dofm(date))== 2010 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Asset Side Variables - December 2011
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_ASSET_V01.dta", clear
    quietly keep if year(dofm(date))== 2011 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Liability Side Variables - December 2011
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_LIAB_V01.dta", clear
    quietly keep if year(dofm(date))== 2011 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Asset Side Variables - December 2012
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_ASSET_V01.dta", clear
    quietly keep if year(dofm(date))== 2012 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Liability Side Variables - December 2012
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_LIAB_V01.dta", clear
    quietly keep if year(dofm(date))== 2012 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Asset Side Variables - December 2013
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_ASSET_V01.dta", clear
    quietly keep if year(dofm(date))== 2013 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Liability Side Variables - December 2013
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_LIAB_V01.dta", clear
    quietly keep if year(dofm(date))== 2013 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Asset Side Variables - December 2014
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_ASSET_V01.dta", clear
    quietly keep if year(dofm(date))== 2014 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Liability Side Variables - December 2014
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_LIAB_V01.dta", clear
    quietly keep if year(dofm(date))== 2014 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Asset Side Variables - December 2015
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_ASSET_V01.dta", clear
    quietly keep if year(dofm(date))== 2015 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Liability Side Variables - December 2015
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_LIAB_V01.dta", clear
    quietly keep if year(dofm(date))== 2015 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Asset Side Variables - December 2016
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_ASSET_V01.dta", clear
    quietly keep if year(dofm(date))== 2016 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Liability Side Variables - December 2016
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_LIAB_V01.dta", clear
    quietly keep if year(dofm(date))== 2016 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Asset Side Variables - December 2017
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_ASSET_V01.dta", clear
    quietly keep if year(dofm(date))== 2017 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Liability Side Variables - December 2017
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_LIAB_V01.dta", clear
    quietly keep if year(dofm(date))== 2017 & month(dofm(date))==12
    sum, separator(1000)


    di _new _new "BBS Panel - Asset Side Variables - December 2018
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_ASSET_V01.dta", clear
    quietly keep if year(dofm(date))== 2018 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Liability Side Variables - December 2018
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_LIAB_V01.dta", clear
    quietly keep if year(dofm(date))== 2018 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Asset Side Variables - December 2019
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_ASSET_V01.dta", clear
    quietly keep if year(dofm(date))== 2019 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Liability Side Variables - December 2019
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_LIAB_V01.dta", clear
    quietly keep if year(dofm(date))== 2019 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Asset Side Variables - December 2020
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_ASSET_V01.dta", clear
    quietly keep if year(dofm(date))== 2020 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Liability Side Variables - December 2020
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_LIAB_V01.dta", clear
    quietly keep if year(dofm(date))== 2020 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Liability Side Variables - December 2021
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_LIAB_V01.dta", clear
    quietly keep if year(dofm(date))== 2021 & month(dofm(date))==12
    sum, separator(1000)

    di _new _new "BBS Panel - Liability Side Variables - December 2022
    quietly use "Z:\data\Products\BBS\2023_06\BBS_Panel\Output\Data\BBS_P_MBNK_SEP1997DEC2022_JUN23_LIAB_V01.dta", clear
    quietly keep if year(dofm(date))== 2022 & month(dofm(date))==12
    sum, separator(1000)

```
