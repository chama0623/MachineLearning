import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# MA(q) model
# return : data of MA model
# q(int) : model dimension
# l(int) : lenght of data
# params(int) : parameters of model [constant ,param1,param2 ...]
def MA(q,l,params):

    if(q!=len(params)-1):
        print("Incorrect argument")
    else :
        wn = np.random.normal(0.0,1.0,l)
        result=[]
        for i in range(l):
            if(i>=q):
                y = params[0]+wn[i]
                for j in range(q):
                    y+=params[j+1]*wn[i-j-1]
                result.append(y)
            else :
                result.append(params[0])
        return result

q = 2
r = MA(q,100,[0,0.7,0.3])
# print(r)
plt.figure(facecolor="white")
plt.plot(r)
plt.title("MA("+str(q)+")")
plt.show()