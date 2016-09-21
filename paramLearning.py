__author__ = 'Kienka Cromwll KIO'

import pandas as pd
import math as mt
import numpy as np
import random as rd


def partition_component(nloop,coefficient):
    #Component of Z
    z=0.0
    for i in range(nloop):
        #print i
        z = z+(i*coefficient)
    return z

#Computing the Partition function in the dataset


#These Variable has domain D1 {0,1,2}
X1=partition_component(3,1)
print X1
X2=partition_component(3,2)
X3=partition_component(3,2)
X4=partition_component(3,2)
X5=partition_component(3,1)
X6=partition_component(3,3)


#These Variable has domain D1 {0,1}
X7=partition_component(2,3)
X8=partition_component(2,4)
X9=partition_component(2,3)
X10=partition_component(2,1)
X11=partition_component(2,1)
X12=partition_component(2,1)

#For Computing the Z
Z=mt.exp(X1+X2+X3+X4+X5+X6+X7+X8+X9+X10+X11+X12)


df=pd.read_csv('C:/Users/Gabrielahrlr/Desktop/sm291.csv')
cntdf=[]
sample_size=len(df)
sample_row= list(df.iloc[1])
for i in range(len(df.X1)):
    f_1=[df.iloc[i][0],df.iloc[i][1],df.iloc[i][3]]
    f_2=[df.iloc[i][1],df.iloc[i][2],df.iloc[i][9]]
    f_3=[df.iloc[i][8],df.iloc[i][10]]
    f_4=[df.iloc[i][2],df.iloc[i][7],df.iloc[i][8]]
    f_5=[df.iloc[i][6],df.iloc[i][7],df.iloc[i][8]]
    f_6=[df.iloc[i][6],df.iloc[i][11]]
    f_7=[df.iloc[i][5],df.iloc[i][6],df.iloc[i][7]]
    f_8=[df.iloc[i][3],df.iloc[i][5],df.iloc[i][7]]
    f_9=[df.iloc[i][4],df.iloc[i][5]]

    #parameter Estimation time using log likelihood
    loglikelihood=((float(len(df[(df.X1==f_1[0])&(df.X2==f_1[1]) &(df.X4==f_1[2])]))*sum(f_1))+ \
    (float(len(df[(df.X2==f_2[0])&(df.X3==f_2[1]) &(df.X10==f_2[2])]))*sum(f_2))+ \
    (float(len(df[(df.X9==f_3[0])&(df.X11==f_3[1])]))*sum(f_3))+ \
    (float(len(df[(df.X3==f_4[0])&(df.X8==f_4[1]) &(df.X9==f_4[2])]))*sum(f_4))+ \
    (float(len(df[(df.X7==f_5[0])&(df.X8==f_5[1]) &(df.X9==f_5[2])]))*sum(f_5))+ \
    (float(len(df[(df.X7==f_6[0])&(df.X12==f_6[1])]))*sum(f_6))+ \
    (float(len(df[(df.X6==f_7[0])&(df.X7==f_7[1]) &(df.X8==f_7[2])]))*sum(f_7))+ \
    (float(len(df[(df.X4==f_8[0])&(df.X6==f_8[1]) &(df.X8==f_8[2])]))*sum(f_8))+ \
    (float(len(df[(df.X5==f_9[0])&(df.X6==f_9[1])]))*sum(f_9)))- (sample_size*mt.log(Z))




    #display the likelihood
    cntdf.append(loglikelihood)

df['log(P)']=pd.Series(cntdf)

print df.head()
print 'Expected Value: ', df['log(P)'].mean()/mt.log(Z)






print f_1

print sample_size
print f_2
cnt = 0
#print list(f3().iloc[1])
#print list(f3()[(f3().X9==0) & (f3().X11==1 )]['F1'])[0]
#Get the file
#df=pd.DataFrame()
#factorCounter()
#There should be a dataset
#Also there should be a return of the dataframe and also the counts on each row...
