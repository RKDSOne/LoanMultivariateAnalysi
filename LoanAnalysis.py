import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from pandas.tools.plotting import autocorrelation_plot
import statsmodels.api as sm
import statsmodels.formula.api as smf


matplotlib.style.use('ggplot')

data = pd.read_csv("LoanStats3a.csv",skiprows=1)
print data.head()


#del data["id"]
# df = df.drop(['x','y'], axis=1)


datav1 = pd.concat([data.annual_inc,data.int_rate,data.home_ownership], axis =1 )





# int_rate is a string with a % symbol
datav1["int_rate"] = datav1["int_rate"].map(lambda x : str(x))
datav1["int_rate"] = datav1["int_rate"].map(lambda x : x.rstrip("%"))
datav1["int_rate"] = datav1["int_rate"].map(lambda x : float(x))

print datav1.head()

# Plot 
print type(datav1.annual_inc[0])
print type(datav1.int_rate[0])

datav1.plot(kind = "scatter", x ="annual_inc", y = "int_rate")
#plt.show()
print datav1.head()
"""
X = datav1["annual_inc"]
y = datav1["int_rate"]

X = sm.add_constant(X)
est = sm.OLS(y, X).fit()
"""

est = smf.ols(formula='int_rate ~ annual_inc *C(home_ownership)', data=datav1).fit()

print est.summary()


# int_rate  = B * annual_inc + b0