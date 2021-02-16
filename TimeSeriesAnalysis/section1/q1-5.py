# 時系列データのプロットとカバン検定
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.stats.diagnostic import acorr_ljungbox
import statsmodels.api as sm

df = pd.read_excel("../Data/economicdata.xls")
df = df.rename(columns={"Unnamed: 0":"date"})

# 問題(1)
fig = plt.figure(figsize=(10,8),facecolor="white")
plt.subplot(3,2,1)
plt.plot(df["date"],df["topix"])
plt.title("東証株価指数(TOPIX)")
plt.subplot(3,2,2)
plt.plot(df["date"],df["exrate"])
plt.title("実効為替レート")
plt.subplot(3,2,3)
plt.plot(df["date"],df["indprod"])
plt.title("季調済み鉱工業生産指数")
plt.subplot(3,2,4)
plt.plot(df["date"],df["cpi"])
plt.title("消費者物価指数(CPI)")
plt.subplot(3,2,5)
plt.plot(df["date"],df["saunemp"])
plt.title("季調済み失業率")
plt.subplot(3,2,6)
plt.plot(df["date"],df["intrate"])
plt.title("コールレート")
fig.subplots_adjust(hspace=0.6, wspace=0.2)
plt.show()

# 問題(2)
# 差分過程を計算
diff_topix = df["topix"].diff(1)
diff_exrate = df["exrate"].diff(1)
diff_indprod = df["indprod"].diff(1)

fig = plt.figure(figsize=(10,8),facecolor="white")
plt.subplot(3,1,1)
plt.plot(df["date"][1:],diff_topix[1:])
plt.title("TOPIX(差分)")
plt.subplot(3,1,2)
plt.plot(df["date"][1:],diff_exrate[1:])
plt.title("実効為替レート(差分)")
plt.subplot(3,1,3)
plt.plot(df["date"][1:],diff_indprod[1:])
plt.title("季調済み鉱工業生産指数(差分)")
fig.subplots_adjust(hspace=0.6, wspace=0.2)
plt.show()

# 問題(4)
lbvalues, pvalues = acorr_ljungbox(diff_indprod[1:], lags=20)
lag = 1
print("Lag     Q        p-value")
for lb, p in zip(lbvalues, pvalues):
    print("%2d   %lf   %lf" %(lag,round(lb,4),round(p,10)))
    lag += 1

fig = sm.graphics.tsa.plot_acf(diff_indprod[1:], lags=20)
plt.show()