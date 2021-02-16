import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm

# AR(p) model
# return : data of AR model
# p(int) : model dimension
# l(int) : lenght of data
# params(int) : parameters of model [constant ,param1,param2 ...]
def AR(p,l,params):

    if(p!=len(params)-1):
        print("Incorrect argument")
    else :
        wn = np.random.normal(0.0,1.0,l)
        result=[]
        for i in range(l):
            if(i>=p):
                y = params[0]+wn[i]
                for j in range(p):
                    y+=params[j+1]*result[i-j-1]
                result.append(y)
            else :
                result.append(params[0])
        return result

# AR(4)
p = 4
r = AR(p,100,[0,0.1,0.1,0.3,0.3])

lag=10
# plot
fig = plt.figure(facecolor="white")
ax_plot = plt.subplot(3,1,1)
ax_acf = plt.subplot(3,1,2)
ax_pacf = plt.subplot(3,1,3)
ax_plot.plot(r)
ax_plot.set_title("AR("+str(p)+")")
# plot autocorrelation
sm.graphics.tsa.plot_acf(r, ax=ax_acf,lags=lag)
# plot partial autocorrelation
sm.graphics.tsa.plot_pacf(r,ax=ax_pacf, lags=lag)
fig.subplots_adjust(hspace=0.6, wspace=0.2)
plt.show()