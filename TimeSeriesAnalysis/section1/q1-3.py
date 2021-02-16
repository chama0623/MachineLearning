# generate white noise
import numpy as np
import matplotlib.pyplot as plt

data_len = 100 # データ長
mean=2.0 # 平均
std = 1.0 # 標準偏差

y = np.random.normal(mean,std,data_len)

plt.figure(facecolor="white")
plt.plot(y)
plt.show()