# MA(1)-process
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data_len = 100
mean = -2.0
theta = -0.8
std = 2.0
ma = pd.DataFrame(np.random.normal(mean,std,data_len),columns={"white-noise"})

ma["y"] = mean
ma["y"] = ma["y"].astype("float32")
for i in range(data_len-1):
    ma.at[i+1,"y"] = ma.at[i+1,"white-noise"] + theta*ma.at[i,"white-noise"]

print(ma)

plt.figure(facecolor="white")
plt.plot(ma["y"])
plt.title("$ \\theta $ = "+str(theta)+" , $\mu$ = "+str(mean)+" , $\sigma$ = "+str(std))
plt.show()