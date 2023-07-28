<meta charset="utf-8"/>
# Harmonized Central Credit Responsibility Database (HCRC)
## Summary Statistics
`Extraction Date`: June 2023

```s/

    di _new _new "HCRC Credit Exposure File - 2009 - December"
    quietly use "Z:/data/Products/HCRC/2023_06/HCRC_Annual/Output/Data/Firms/2009/HCRC_C_MFRMEXP_2009_JUN23_BAL_V01.dta", clear
    sum valor_reg, separator(1000)
    sum valor_pot, separator(1000)
    sum valor_vencido, separator(1000)
    sum valor_abatv, separator(1000)

    di _new _new "HCRC Credit Exposure File - 2010 - December"
    quietly use "Z:/data/Products/HCRC/2023_06/HCRC_Annual/Output/Data/Firms/2010/HCRC_C_MFRMEXP_2010_JUN23_BAL_V01.dta", clear
    sum valor_reg, separator(1000)
    sum valor_pot, separator(1000)
    sum valor_vencido, separator(1000)
    sum valor_abatv, separator(1000)

    di _new _new "HCRC Credit Exposure File - 2011 - December"
    quietly use "Z:/data/Products/HCRC/2023_06/HCRC_Annual/Output/Data/Firms/2011/HCRC_C_MFRMEXP_2011_JUN23_BAL_V01.dta", clear
    sum valor_reg, separator(1000)
    sum valor_pot, separator(1000)
    sum valor_vencido, separator(1000)
    sum valor_abatv, separator(1000)

    di _new _new "HCRC Credit Exposure File - 2012 - December"
    quietly use "Z:/data/Products/HCRC/2023_06/HCRC_Annual/Output/Data/Firms/2012/HCRC_C_MFRMEXP_2012_JUN23_BAL_V01.dta", clear
    sum valor_reg, separator(1000)
    sum valor_pot, separator(1000)
    sum valor_vencido, separator(1000)
    sum valor_abatv, separator(1000)

    di _new _new "HCRC Credit Exposure File - 2013 - December"
    quietly use "Z:/data/Products/HCRC/2023_06/HCRC_Annual/Output/Data/Firms/2013/HCRC_C_MFRMEXP_2013_JUN23_BAL_V01.dta", clear
    sum valor_reg, separator(1000)
    sum valor_pot, separator(1000)
    sum valor_vencido, separator(1000)
    sum valor_abatv, separator(1000)

    di _new _new "HCRC Credit Exposure File - 2014 - December"
    quietly use "Z:/data/Products/HCRC/2023_06/HCRC_Annual/Output/Data/Firms/2014/HCRC_C_MFRMEXP_2014_JUN23_BAL_V01.dta", clear
    sum valor_reg, separator(1000)
    sum valor_pot, separator(1000)
    sum valor_vencido, separator(1000)
    sum valor_abatv, separator(1000)

    di _new _new "HCRC Credit Exposure File - 2015 - December"
    quietly use "Z:/data/Products/HCRC/2023_06/HCRC_Annual/Output/Data/Firms/2015/HCRC_C_MFRMEXP_2015_JUN23_BAL_V01.dta", clear
    sum valor_reg, separator(1000)
    sum valor_pot, separator(1000)
    sum valor_vencido, separator(1000)
    sum valor_abatv, separator(1000)

    di _new _new "HCRC Credit Exposure File - 2016 - December"
    quietly use "Z:/data/Products/HCRC/2023_06/HCRC_Annual/Output/Data/Firms/2016/HCRC_C_MFRMEXP_2016_JUN23_BAL_V01.dta", clear
    sum valor_reg, separator(1000)
    sum valor_pot, separator(1000)
    sum valor_vencido, separator(1000)
    sum valor_abatv, separator(1000)

    di _new _new "HCRC Credit Exposure File - 2017 - December"
    quietly use "Z:/data/Products/HCRC/2023_06/HCRC_Annual/Output/Data/Firms/2017/HCRC_C_MFRMEXP_2017_JUN23_BAL_V01.dta", clear
    sum valor_reg, separator(1000)
    sum valor_pot, separator(1000)
    sum valor_vencido, separator(1000)
    sum valor_abatv, separator(1000)

    di _new _new "HCRC Credit Exposure File - 2018 - December"
    quietly use "Z:/data/Products/HCRC/2023_06/HCRC_Annual/Output/Data/Firms/2018/HCRC_C_MFRMEXP_2018_JUN23_BAL_V01.dta", clear
    sum valor_reg, separator(1000)
    sum valor_pot, separator(1000)
    sum valor_vencido, separator(1000)
    sum valor_abatv, separator(1000)

    di _new _new "HCRC Credit Exposure File - 2019 - December"
    quietly use "Z:/data/Products/HCRC/2023_06/HCRC_Annual/Output/Data/Firms/2019/HCRC_C_MFRMEXP_2019_JUN23_BAL_V01.dta", clear
    sum valor_reg, separator(1000)
    sum valor_pot, separator(1000)
    sum valor_vencido, separator(1000)
    sum valor_abatv, separator(1000)


    di _new _new "HCRC Credit Exposure File - 2020 - December"
    quietly use "Z:/data/Products/HCRC/2023_06/HCRC_Annual/Output/Data/Firms/2020/HCRC_C_MFRMEXP_2020_JUN23_BAL_V01.dta", clear
    sum valor_reg, separator(1000)
    sum valor_pot, separator(1000)
    sum valor_vencido, separator(1000)
    sum valor_abatv, separator(1000)

    di _new _new "HCRC Credit Exposure File - 2021 - December"
    quietly use "Z:/data/Products/HCRC/2023_06/HCRC_Annual/Output/Data/Firms/2021/HCRC_C_MFRMEXP_2021_JUN23_BAL_V01.dta", clear
    sum valor_reg, separator(1000)
    sum valor_pot, separator(1000)
    sum valor_vencido, separator(1000)
    sum valor_abatv, separator(1000)

    di _new _new "HCRC Credit Exposure File - 2022 - December"
    quietly use "Z:/data/Products/HCRC/2023_06/HCRC_Annual/Output/Data/Firms/2022/HCRC_C_MFRMEXP_2022_JUN23_BAL_V01.dta", clear
    sum valor_reg, separator(1000)
    sum valor_pot, separator(1000)
    sum valor_vencido, separator(1000)
    sum valor_abatv, separator(1000)
```
