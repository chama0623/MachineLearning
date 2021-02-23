import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("../Data/msci_day.xls")
df["Date"] = pd.to_datetime(df["Date"],format="%Y-%m-%d")

# 問題(1)
col = df.columns[1:]
data_num = len(col)-1
fig = plt.figure(facecolor="white")
for i in range(data_num):
    plt.subplot(data_num,1,i+1)
    plt.plot(df["Date"],df[col[i]])
    plt.ylabel(col[i])
fig.subplots_adjust(hspace=0.6, wspace=0.2)
plt.show()

# 直交化インパルス応答関数
import statsmodels.api as sm
from statsmodels.tsa.api import VAR
# VARモデルで近似
df_var = df.drop(columns={"Date"})
model = VAR(df_var.dropna())
results = model.fit(maxlags=15, ic='aic')

# グレンジャー因果性の検定
for i in range(data_num):
    for j in range(data_num):
        print(col[i]+"->"+col[j])
        # col[i]->col[j]のグレンジャー因果性検定
        test_results = results.test_causality(causing=i, caused=j)
        pvalue = test_results.pvalue
        print(test_results)
        print(pvalue)

# インパルス応答関数をプロット
irf = results.irf(10)
irf.plot(orth=False)
plt.show()

# 分散分解
# プロット
FEVD = results.fevd(10)
FEVD.plot()
plt.show()
# 標準出力
print(FEVD.summary())