import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('DATA-Table.csv')


def bondlength_o1o3 (a, b, c, o1, o3):
    #build the metric tensor
    G = np.matrix([[a*a, 0, 0],[0, b*b, 0],[0, 0, c*c]])  
    # find the difference between the two vectors
    diffv = np.subtract(o3, o1)
    # calculate the square of the length of the two vectors
    bonddis_squared = diffv*G*diffv.T
    # calculate the length of the two vectors (aka bondlength)
    bonddis = float(np.sqrt(bonddis_squared))
    # print out a float 
    return float(bonddis)
    

#------------------------------------------
#------------------------------------------
bondlist = pd.DataFrame(columns=['o1o3'])

for i in data.index:
    a=b=c=data.ix[i,'a']
    o1 = ([[data.ix[i,'O1-x'],data.ix[i,'O1-y'],data.ix[i,'O1-z']]])
    o3 = ([[data.ix[i,'O3-x'],data.ix[i,'O3-y'],data.ix[i,'O3-z']]])
    bonddis = bondlength_o1o3(a,b,c,o1,o3)
   # print bonddis
    bondlist.loc[i] = [bonddis]

bondlist.to_csv('./bondlengths_O1O3.csv', sep=',')




#a = b = c = 12.7723
#o1 = np.matrix([[0.77896, 0.81568, 0.63424]])
#o3 = np.matrix([[0.46611, 0.68601, 0.42207]])
#bondlength_o1o3(a,b,c,o1,o3)



