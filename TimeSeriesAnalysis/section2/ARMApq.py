import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm

# ARMA(p,q) model
# return : data of MA model
# p(int),q(int) : model dimension
# l(int) : lenght of data
# paramsp(int) : parameters of model [constant ,param1,param2 ...]
# paramsq(int) : parameters of model [param1,param2 ...]
def ARMA(p,q,l,paramsp,paramsq):

    if(p!=len(paramsp)-1):
        print("Incorrect argument")
    elif(q!=len(paramsq)):
        print("Incorrect argument")
    else :
        wn = np.random.normal(0.0,1.0,l)
        result=[]
        for i in range(l):
            if(i>=p):
                y = paramsp[0]+wn[i]
                for j in range(p):
                    y+=paramsp[j+1]*result[i-j-1]
                for j in range(q):
                    y+= paramsq[j]*wn[i-j-1]
                result.append(y)
            else :
                result.append(paramsp[0])
        return result

p = 2
q = 2
r = ARMA(p,q,100,[0,0.7,0.3],[0.2,0.4])
# print(r)
plt.figure(facecolor="white")
plt.plot(r)
plt.title("ARMA("+str(p)+","+str(q)+")")
plt.show()