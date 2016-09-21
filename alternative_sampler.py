__author__ = 'Kienka Cromwell KIO'

import pandas as pd
from copy import deepcopy
import random as rd

def sampler(previousSample, index):
    mylist=previousSample[:]
    value_size1=[0,1,2]
    value_size2=[0,1]
    holder=[]
    newlist=[]


    if index<6:
        for i in value_size1:
            mylist[index]=i
            newlist=deepcopy(mylist)
            holder.append(newlist)



    if index>5:
        for i in value_size2:
            mylist[index]=i
            newlist=deepcopy(mylist)
            holder.append(newlist)

    return holder
d=0
data=[]
data2=[]
sequence=[0,2,1,0,0,0,1,0,0,1,0,1]
for i in range(230):
    #decider=rd.randint(0,9)
    #if decider==1:
     #   d=rd.randint(0,5)
    #if decider>=2:
      #  d=rd.randint(6,11)
    print i,' == I am the boss'
    if d>11:
       d=0
    data= data + sampler(sequence,d)

    sequence=data[-1]

    d=d+1

fd=pd.DataFrame(data=data,columns=['X1','X2','X3','X4','X5','X6','X7','X8','X9','X10','X11','X12'])
print fd

fd.to_csv('C:/Users/Gabrielahrlr/Desktop/sm241.csv', index=False)
