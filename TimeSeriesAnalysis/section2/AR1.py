# AR(1)-process
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data_len = 100
c = 2.0
phi = 0.8
mean=0.0
std = 1.0
ma = pd.DataFrame(np.random.normal(mean,std,data_len),columns={"white-noise"})

ma["y"] = c
ma["y"] = ma["y"].astype("float32")
for i in range(data_len-1):
    ma.at[i+1,"y"] = c + ma.at[i+1,"white-noise"] + phi*ma.at[i,"y"]

print(ma)

plt.figure(facecolor="white")
plt.plot(ma["y"])
plt.title("$ \\phi $ = "+str(phi)+" , $c$ = "+str(c)+" , $\sigma$ = "+str(std))
plt.show()