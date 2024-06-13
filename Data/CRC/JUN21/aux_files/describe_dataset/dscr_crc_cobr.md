<meta charset="utf-8"/>
# Central Credit Responsibility Database
## Dataset description
`extraction`: April 2019

```stc_2

    di _new _new "CCR Firm Level - 1980 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/1980/External/CRC_A_MFRM_1980_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 1981 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/1981/External/CRC_A_MFRM_1981_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 1982 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/1982/External/CRC_A_MFRM_1982_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 1983 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/1983/External/CRC_A_MFRM_1983_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 1984 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/1984/External/CRC_A_MFRM_1984_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 1985 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/1985/External/CRC_A_MFRM_1985_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 1986 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/1986/External/CRC_A_MFRM_1986_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 1987 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/1987/External/CRC_A_MFRM_1987_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 1988 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/1988/External/CRC_A_MFRM_1988_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 1989 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/1989/External/CRC_A_MFRM_1989_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 1990 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/1990/External/CRC_A_MFRM_1990_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 1991 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/1991/External/CRC_A_MFRM_1991_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 1992 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/1992/External/CRC_A_MFRM_1992_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 1993 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/1993/External/CRC_A_MFRM_1993_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 1994 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/1994/External/CRC_A_MFRM_1994_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 1995 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/1995/External/CRC_A_MFRM_1995_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 1996 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/1996/External/CRC_A_MFRM_1996_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 1997 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/1997/External/CRC_A_MFRM_1997_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 1998 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/1998/External/CRC_A_MFRM_1998_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 1999 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/1999/External/CRC_A_MFRM_1999_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 2000 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/2000/External/CRC_A_MFRM_2000_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 2001 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/2001/External/CRC_A_MFRM_2001_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 2002 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/2002/External/CRC_A_MFRM_2002_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 2003 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/2003/External/CRC_A_MFRM_2003_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 2004 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/2004/External/CRC_A_MFRM_2004_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 2005 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/2005/External/CRC_A_MFRM_2005_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 2006 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/2006/External/CRC_A_MFRM_2006_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 2007 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/2007/External/CRC_A_MFRM_2007_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 2008 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/2008/External/CRC_A_MFRM_2008_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 2009 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/2009/External/CRC_A_MFRM_2009_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 2010 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/2010/External/CRC_A_MFRM_2010_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 2011 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/2011/External/CRC_A_MFRM_2011_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 2012 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/2012/External/CRC_A_MFRM_2012_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 2013 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/2013/External/CRC_A_MFRM_2013_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 2014 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/2014/External/CRC_A_MFRM_2014_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 2015 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/2015/External/CRC_A_MFRM_2015_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 2016 - December"
    quietly use "Z:/data/Products/CRC/2017_04/CRC_Annual/Output/Data/Firms/2016/External/CRC_A_MFRM_2016_APR17_COBR_V01.dta", clear
    quietly rename TINA tina
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 2017 - December"
    quietly use "Z:/data/Products/CRC/2018_04/CRC_Annual/Output/Data/Firms/2017/External/CRC_A_MFRM_2017_APR18_COBR_V01.dta", clear
    quietly drop if valor_global==.
    describe

    di _new _new "CCR Firm Level - 2018 - August"
    quietly use "Z:/data/Products/CRC/2019_04/CRC_Annual/Output/Data/Firms/2018/External/CRC_A_MFRM_2018_APR19_COBR_V01.dta", clear
    quietly drop if valor_global==.
    describe

```
