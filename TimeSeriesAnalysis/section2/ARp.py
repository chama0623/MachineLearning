import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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

p = 1
r = AR(p,100,[-2.0,-0.8])
# print(r)
plt.figure(facecolor="white")
plt.plot(r)
plt.title("AR("+str(p)+")")
plt.show()