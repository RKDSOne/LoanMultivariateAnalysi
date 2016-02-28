import matplotlib.pyplot as plt 
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData.dropna(inplace=True)

plt.figure()
loansData.boxplot(column="Amount.Funded.By.Investors")
plt.savefig("boxplotAmountFunded.png")

plt.figure()
loansData.boxplot(column="Amount.Requested")
plt.savefig("boxplotAmountRequested.png")

plt.figure()
loansData.hist(column="Amount.Funded.By.Investors")
plt.savefig("histogramAmountFunded.png")

plt.figure()
loansData.hist(column="Amount.Requested")
plt.savefig("histogramAmountRequested.png")


plt.figure()
stats.probplot(loansData["Amount.Funded.By.Investors"],dist="norm", plot=plt)
plt.savefig("QQplotAmountFunded.png")

plt.figure()
stats.probplot(loansData["Amount.Requested"],dist="norm", plot=plt)
plt.savefig("QQplotAmountRequested.png")