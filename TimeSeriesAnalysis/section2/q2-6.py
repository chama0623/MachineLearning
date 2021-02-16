# ARMAモデルの推定
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
import pmdarima as pm
from statsmodels.stats.diagnostic import acorr_ljungbox
import warnings
warnings.simplefilter('ignore')

df = pd.read_excel("../Data/arma.xls")

# 原系列,自己相関,偏自己相関のプロット
lag = 20
for i in range(3):
    name = "y"+str(i+1)
    print("-"*8+name+"-"*8)

    acf = sm.tsa.stattools.acf(df[name],nlags=lag)
    pacf = sm.tsa.stattools.pacf(df[name],nlags=lag)
    
    print("lag  ACF    PACF")
    for j in range(lag+1):
        print("%d  %.4lf  %.4lf"%(j,acf[j],pacf[j]))
    print("")

    # plot
    fig = plt.figure(facecolor="white")
    ax_plot = plt.subplot(3,1,1)
    ax_acf = plt.subplot(3,1,2)
    ax_pacf = plt.subplot(3,1,3)
    ax_plot.plot(df["date"],df[name])
    ax_plot.set_title(name)
    # plot autocorrelation
    sm.graphics.tsa.plot_acf(df[name], ax=ax_acf,lags=lag)

    # plot partial autocorrelation
    sm.graphics.tsa.plot_pacf(df[name],ax=ax_pacf, lags=lag)
    fig.subplots_adjust(hspace=0.6, wspace=0.2)

    # modeling
    model = pm.auto_arima(df[name], start_p=0, start_q=0,
                      test='adf',       # use adftest to find optimal 'd'
                      max_p=4, max_q=4, # maximum p and q
                      m=12,              # frequency of series
                      d=None,           # let model determine 'd'
                      seasonal=False,   # No Seasonality
                      start_P=0, 
                      D=0, 
                      trace=True,
                      error_action='ignore',  
                      suppress_warnings=True, 
                      stepwise=True,
                      n_jobs=-1)
    print(model.summary())
    model.plot_diagnostics(figsize=(7,7))

    plt.figure(facecolor="white")
    x = np.arange(len(df[name]))
    plt.plot(df["date"],df[name])
    fitted, confint = model.predict(n_periods=len(df[name]), return_conf_int=True)
    plt.plot(x,fitted)
    plt.show()

"""
y1
AR(6),MA(4),ARMA(4,4)
y2
AR(4),MA(3),ARMA(2,2)
y3
AR(3),MA(4),ARMA(2,2)
"""