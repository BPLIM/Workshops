#%%
from linearmodels.datasets import jobtraining
from linearmodels import RandomEffects
from linearmodels import PanelOLS
import statistics
import statsmodels.formula.api as smf
import seaborn as sns
from statsmodels.sandbox.regression.predstd import wls_prediction_std
import matplotlib.pyplot as plt
import statsmodels.api as sm
import sys
sys.version
import os
import pandas as pd
from patsy import dmatrices

import numpy as np
from sklearn.linear_model import LinearRegression
os.chdir("/Users/miguelportela/Dropbox/3.aulas/2019/doutoramento/extensions_painel_data/7.empirics")

print(os.getcwd())

## REGRESSION EXAMPLE
# %%
df = pd.read_stata('data/nlsw88.dta')
df["wage"].mean()

def linear_regression(df, dep_col, indep_cols):
  lf = LinearRegression(normalize=True)
  lf.fit(df[indep_cols.split(' ')], df[dep_col])

  return lf

lr = linear_regression(df, 'wage', 'hours')

print(lr.coef_)

w1 = pd.read_stata('http://qcpages.qc.cuny.edu/~rvesselinov/statadata/WAGE1.DTA')

w1.to_stata('data/wage1.dta')

# %%

y=df.wage
X=df.age
X = sm.add_constant(X)
model = sm.OLS(y, X)
results = model.fit()
print(results.summary())

# %%
# matplotlib histogram
plt.hist(df['wage'], color='blue', edgecolor='black',
         bins=int(180/5))


# %%
# Density Plot and Histogram of all arrival delays
sns.distplot(df['wage'], hist=True, kde=True,
             bins=int(180/5), color='darkblue',
             hist_kws={'edgecolor': 'black'},
             kde_kws={'linewidth': 4})


# %%
# DESCRIPTIVES

print(df.mean())
print(df.std())
print(df.describe())

# %%
plt.hist(w1['wage'])
ln_wage = np.log(w1['wage'])
sns.kdeplot(ln_wage)

# %%
X = w1[['educ', 'female', 'married']]
X = sm.add_constant(X)
m3 = sm.OLS(ln_wage, X).fit()
print(m3.summary())


# %%
from linearmodels.datasets import jobtraining
data = jobtraining.load()
year = pd.Categorical(data.year)
data = data.set_index(['fcode', 'year'])
data['year'] = year

exog_vars = ['grant', 'employ']
exog = sm.add_constant(data[exog_vars])
mod = RandomEffects(data.clscrap, exog)
re_res = mod.fit()
print(re_res)

# %%
data.to_stata('jobtraining.dta')


# %%
data_w=pd.read_stata('data/lfp.dta')
data_w.describe()
mod = sm.Probit.from_formula('lfp ~ kids + lhinc + C(id)', data_w)

# %%
