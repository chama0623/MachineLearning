# かばん検定
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.stats.diagnostic import acorr_ljungbox

# ホワイトノイズの場合
# 相関関係はないため,帰無仮説は棄却されない = 有意水準5%とすると,P値が0.05を下回らない
data_len = 100 # データ長
mean=2.0 # 平均
std = 1.0 # 標準偏差

y = np.random.normal(mean,std,data_len)
result = acorr_ljungbox(y,lags = 5,return_df=True)
print("result (white noise)")
print(result)

plt.figure(facecolor="white")
plt.plot(y)
plt.title("white noise")

# MA(3) modelの場合
# y(t) = 1+e(t)+0.5+e(t-3)
# ラグが2次以下では有意な差がないが3次以上になると有意に差が現れる.

data_len = 100
data = np.zeros(data_len)
err = np.random.standard_normal(data_len)
for i in range(data_len):
    if i-3 < 0:
        data[i] = 1 + err[i]
    else:
        data[i] = 1 + err[i] + 0.5 * err[i-3]

result = acorr_ljungbox(data,lags = 5,return_df=True)

print("\nresult (MA(3) model)")
print(result)

plt.figure(figsize=(10,6))
plt.plot(data,lw = 1.5)
plt.title('MA(3) model')
plt.show()