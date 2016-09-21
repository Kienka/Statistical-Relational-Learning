__author__ = 'Kienka Cromwell KIO'

#For sampling.
import pandas as pd
import math as mt
import numpy as np
import random as rd
def f1():
    ls1=[]
    size= 3*3*3

    for x in range(3):
        for y in range(3):
            #for z in range(3):
                ls1.append([x,y,mt.exp(x+y)])

    df1=pd.DataFrame(data=ls1,columns=['X1','X2','F1'])
    return df1
def f3():
    ls1=[]
    size= 3*3*3

    for x in range(3):
        for y in range(3):
            #for z in range(3):
                ls1.append([x,y,mt.exp(x+y)])

    df1=pd.DataFrame(data=ls1,columns=['X1','X4','F1'])
    return df1
def f2():
    ls1=[]
    size= 3*3*3

    for x in range(3):
        for y in range(3):
            #for z in range(3):
                ls1.append([x,y,mt.exp(x+y)])

    df1=pd.DataFrame(data=ls1,columns=['X2','X4','F1'])
    return df1
def f4():
    ls1=[]
    for x in range(3):
        for y in range(3):
            #for z in range(2):
                ls1.append([x,y,mt.exp(x+y)])

    df1=pd.DataFrame(data=ls1,columns=['X2','X3','F1'])
    return df1
def f5():
    ls1=[]
    for x in range(3):
        for y in range(2):
            #for z in range(2):
                ls1.append([x,y,mt.exp(x+y)])

    df1=pd.DataFrame(data=ls1,columns=['X2','X10','F1'])
    return df1
def f6():
    ls1=[]
    for x in range(3):
        for y in range(2):
            #for z in range(2):
                ls1.append([x,y,mt.exp(x+y)])

    df1=pd.DataFrame(data=ls1,columns=['X3','X10','F1'])
    return df1


def f8():
    ls1=[]
    for x in range(3):
        for y in range(2):
            #for z in range(2):
                ls1.append([x,y,mt.exp(x+y)])

    df1=pd.DataFrame(data=ls1,columns=['X3','X8','F1'])
    return df1

def f9():
    ls1=[]
    for x in range(3):
        for y in range(2):
            #for z in range(2):
                ls1.append([x,y,mt.exp(x+y)])

    df1=pd.DataFrame(data=ls1,columns=['X3','X9','F1'])
    return df1

def f10():
    ls1=[]
    for x in range(2):
        for y in range(2):
            #for z in range(2):
                ls1.append([x,y,mt.exp(x+y)])

    df1=pd.DataFrame(data=ls1,columns=['X8','X9','F1'])
    return df1

def f7():
    ls1=[]
    for x in range(2):
        for y in range(2):

            ls1.append([x,y,mt.exp(x+y)])

    df1=pd.DataFrame(data=ls1,columns=['X9','X11','F1'])
    return df1
def f11():
    ls1=[]
    for x in range(2):
        for y in range(2):
            #for z in range(2):
                ls1.append([x,y,mt.exp(x+y)])

    df1=pd.DataFrame(data=ls1,columns=['X7','X8','F1'])
    return df1
def f12():
    ls1=[]
    for x in range(2):
        for y in range(2):
            #for z in range(2):
                ls1.append([x,y,mt.exp(x+y)])

    df1=pd.DataFrame(data=ls1,columns=['X7','X9','F1'])
    return df1

def f13():
    ls1=[]
    for x in range(2):
        for y in range(2):

            ls1.append([x,y,mt.exp(x+y)])

    df1=pd.DataFrame(data=ls1,columns=['X7','X12','F1'])
    return df1
def f14():
    ls1=[]
    for x in range(3):
        for y in range(2):
            #for z in range(2):
                ls1.append([x,y,mt.exp(x+y)])

    df1=pd.DataFrame(data=ls1,columns=['X6','X7','F1'])
    return df1
def f15():
    ls1=[]
    for x in range(3):
        for y in range(2):
            #for z in range(2):
                ls1.append([x,y,mt.exp(x+y)])

    df1=pd.DataFrame(data=ls1,columns=['X6','X8','F1'])
    return df1

def f16():
    ls1=[]
    for x in range(3):
        for y in range(3):
            #for z in range(2):
                ls1.append([x,y,mt.exp(x+y)])

    df1=pd.DataFrame(data=ls1,columns=['X4','X6','F1'])
    return df1
def f17():
    ls1=[]
    for x in range(3):
        for y in range(2):
            #for z in range(2):
                ls1.append([x,y,mt.exp(x+y)])

    df1=pd.DataFrame(data=ls1,columns=['X4','X8','F1'])
    return df1

def f18():
    ls1=[]
    for x in range(3):
        for y in range(3):

            ls1.append([x,y,mt.exp(x+y)])

    df1=pd.DataFrame(data=ls1,columns=['X5','X6','F1'])
    return df1

def decider(valueIndex,sequence):
    value_size1=3
    value_size2=2
    newval=0
    rand1=rd.uniform(0.0, 1.0)
    print rand1

    meta_info={'X1':{'size':value_size1,'factor':[f1(),f3()]},
           'X2':{'size':value_size1,'factor':[f1(),f2(),f4(),f5()]},
           'X3':{'size':value_size1,'factor':[f4(),f6(),f8(),f9()]},
           'X4':{'size':value_size1,'factor':[f2(),f3(),f16(),f17()]},
           'X5':{'size':value_size1,'factor':[f18()]},
           'X6':{'size':value_size1,'factor':[f14(),f15(),f18()]},
           'X7':{'size':value_size2,'factor':[f11(),f12(),f13(),f14()]},
           'X8':{'size':value_size2,'factor':[f8(),f10(),f11(),f15(),f17()]},
           'X9':{'size':value_size2,'factor':[f7(),f9(),f10(),f12()]},
           'X10':{'size':value_size2,'factor':[f5(),f6()]},
           'X11':{'size':value_size2,'factor':[f7()]},
           'X12':{'size':value_size2,'factor':[f13()]}
           }
    #FOR X1, remember the sequence indexes INDEX 1
    if valueIndex==0:

        sumlist=[]
        df= meta_info['X1']['factor'][0]
        df2= meta_info['X1']['factor'][1]
        for i in range(value_size1):
            num=list( df[(df.X1==i) & (df.X2==sequence[1])]['F1'])[0]*list( df2[(df2.X1==i) & (df2.X4==sequence[3])]['F1'])[0]
            sumlist.append(num)
            #sumlist.append(list( df[(df.X1==i) & (df.X2==sequence[1])]['F1'])[0])
        sum1=sum(sumlist)
        norm=[(x / sum1) for x in sumlist]
        print norm
        if rand1<norm[0]:
            newval=0
        if rand1>=norm[0]and rand1<(norm[0]+norm[1]):
            newval=1
        if rand1>=(norm[0]+norm[1]):
            newval=2

    #For X5,
    if valueIndex==4:
        max1=1
        sumlist=[]
        df= meta_info['X5']['factor'][0]
        for i in range(value_size1):
           sumlist.append(list( df[(df.X5==i) & (df.X6==sequence[5]) ]['F1'])[0])
        sum1=sum(sumlist)
        norm=[(x / sum1) for x in sumlist]
        print norm
        if rand1<norm[0]:
            newval=0
        if rand1>=norm[0]and rand1<(norm[0]+norm[1]):
            newval=1
        if rand1>=(norm[0]+norm[1]):
            newval=2


    #FOR X10, remember the sequence indexes INDEX 1
    if valueIndex==9:
        sumlist=[]

        df= meta_info['X10']['factor'][0]
        df2= meta_info['X10']['factor'][1]
        for i in range(value_size2):
            num=list( df[(df.X10==i) & (df.X2==sequence[1])]['F1'])[0]*list( df2[(df2.X10==i) & (df2.X3==sequence[2])]['F1'])[0]
            sumlist.append(num)
            #sumlist.append(list( df[(df.X10==i) & (df.X2==sequence[1]) & (df.X3==sequence[2]) ]['F1'])[0])
        sum1=sum(sumlist)
        norm=[(x / sum1) for x in sumlist]
        print norm
        if rand1<norm[0]:
            newval=0
        else:
            newval=1


    if valueIndex==10:
        max1=1
        sumlist=[]
        df= meta_info['X11']['factor'][0]
        for i in range(value_size2):
            sumlist.append(list( df[(df.X11==i) & (df.X9==sequence[8])  ]['F1'])[0])
        sum1=sum(sumlist)
        norm=[(x / sum1) for x in sumlist]
        print norm
        if rand1<norm[0]:
            newval=0
        else:
            newval=1



    if valueIndex==11:
        max1=1
        sumlist=[]
        df= meta_info['X12']['factor'][0]
        for i in range(value_size2):
            sumlist.append(list( df[(df.X12==i) & (df.X7==sequence[6])  ]['F1'])[0])
        sum1=sum(sumlist)
        norm=[(x / sum1) for x in sumlist]
        print norm
        if rand1<norm[0]:
            newval=0
        else:
            newval=1

    if valueIndex==1:
        max1=0.0
        num=0.0
        sumlist=[]
        df= meta_info['X2']['factor'][0]
        df2= meta_info['X2']['factor'][1]
        df3= meta_info['X2']['factor'][2]
        df4= meta_info['X2']['factor'][3]
        for i in range(value_size1):
            num=list( df[(df.X2==i) & (df.X1==sequence[0])]['F1'])[0]\
                *list( df2[(df2.X2==i) & (df2.X4==sequence[3])]['F1'])[0]\
                *list( df3[(df3.X2==i) & (df3.X3==sequence[2])]['F1'])[0]\
                *list( df4[(df4.X2==i) & (df4.X10==sequence[9])]['F1'])[0]
            sumlist.append(num)
        sum1=sum(sumlist)
        norm=[(x / sum1) for x in sumlist]
        print norm
        if rand1<norm[0]:
            newval=0
        if rand1>=norm[0]and rand1<(norm[0]+norm[1]):
            newval=1
        if rand1>=(norm[0]+norm[1]):
            newval=2


    if valueIndex==2:
        max1=0.0
        sumlist=[]
        num=0.0
        df= meta_info['X3']['factor'][0]
        df2= meta_info['X3']['factor'][1]
        df3= meta_info['X3']['factor'][2]
        df4= meta_info['X3']['factor'][3]
        for i in range(value_size1):
            #num=list( df[(df.X3==i) & (df.X2==sequence[1]) &(df.X10==sequence[9]) ]['F1'])[0]*list( df2[(df2.X3==i) & (df2.X8==sequence[7]) &(df2.X9==sequence[8]) ]['F1'])[0]
            #sumlist.append(num)
            num=list( df[(df.X3==i) & (df.X2==sequence[1])]['F1'])[0]\
                    *list( df2[(df2.X3==i) & (df2.X10==sequence[9])]['F1'])[0]\
                    *list( df3[(df3.X3==i) & (df3.X8==sequence[7])]['F1'])[0]\
                    *list( df4[(df4.X3==i) & (df4.X9==sequence[8])]['F1'])[0]
            sumlist.append(num)
        sum1=sum(sumlist)
        norm=[(x / sum1) for x in sumlist]
        print norm
        if rand1<norm[0]:
            newval=0
        if rand1>=norm[0]and rand1<(norm[0]+norm[1]):
            newval=1
        if rand1>=(norm[0]+norm[1]):
            newval=2

    if valueIndex==3:
        max1=0.0
        num=0.0
        sumlist=[]
        df= meta_info['X4']['factor'][0]
        df2= meta_info['X4']['factor'][1]
        df3= meta_info['X4']['factor'][2]
        df4= meta_info['X4']['factor'][3]
        for i in range(value_size1):
            num=list( df[(df.X4==i) & (df.X2==sequence[1])]['F1'])[0]\
                    *list( df2[(df2.X4==i) & (df2.X1==sequence[0])]['F1'])[0]\
                    *list( df3[(df3.X4==i) & (df3.X6==sequence[5])]['F1'])[0]\
                    *list( df4[(df4.X4==i) & (df4.X8==sequence[7])]['F1'])[0]
            sumlist.append(num)
        sum1=sum(sumlist)
        norm=[(x / sum1) for x in sumlist]
        print norm
        if rand1<norm[0]:
            newval=0
        if rand1>=norm[0]and rand1<(norm[0]+norm[1]):
            newval=1
        if rand1>=(norm[0]+norm[1]):
            newval=2


    if valueIndex==5:
        max1=0.0
        num=0.0
        sumlist=[]
        df= meta_info['X6']['factor'][0]
        df2= meta_info['X6']['factor'][1]
        df3= meta_info['X6']['factor'][2]
        #df4= meta_info['X6']['factor'][3]
        for i in range(value_size1):
            num=list( df[(df.X6==i) & (df.X7==sequence[6])]['F1'])[0]\
                    *list( df2[(df2.X6==i) & (df2.X8==sequence[7])]['F1'])[0]\
                    *list( df3[(df3.X6==i) & (df3.X5==sequence[5])]['F1'])[0]

            sumlist.append(num)
        sum1=sum(sumlist)
        norm=[(x / sum1) for x in sumlist]
        print norm
        if rand1<norm[0]:
            newval=0
        if rand1>=norm[0]and rand1<(norm[0]+norm[1]):
            newval=1
        if rand1>=(norm[0]+norm[1]):
            newval=2

    if valueIndex==6:
        max1=0.0
        num=0.0
        sumlist=[]
        df= meta_info['X7']['factor'][0]
        df2= meta_info['X7']['factor'][1]
        df3= meta_info['X7']['factor'][2]
        df4= meta_info['X7']['factor'][3]
        for i in range(value_size2):
            num=list( df[(df.X7==i) & (df.X8==sequence[7])]['F1'])[0]\
                    *list( df2[(df2.X7==i) & (df2.X9==sequence[8])]['F1'])[0]\
                    *list( df3[(df3.X7==i) & (df3.X12==sequence[11])]['F1'])[0]\
                    *list( df4[(df4.X7==i) & (df4.X6==sequence[5])]['F1'])[0]
            sumlist.append(num)
        sum1=sum(sumlist)
        norm=[(x / sum1) for x in sumlist]
        print norm
        if rand1<norm[0]:
            newval=0

        else:
            newval=1

    if valueIndex==8:
        max1=0.0
        num=0.0
        sumlist=[]
        df= meta_info['X9']['factor'][0]
        df2= meta_info['X9']['factor'][1]
        df3= meta_info['X9']['factor'][2]
        df4= meta_info['X9']['factor'][3]

        for i in range(value_size2):
            num=list( df[(df.X9==i) & (df.X11==sequence[10])]['F1'])[0]\
                    *list( df2[(df2.X9==i) & (df2.X3==sequence[2])]['F1'])[0]\
                    *list( df3[(df3.X9==i) & (df3.X8==sequence[7])]['F1'])[0]\
                    *list( df4[(df4.X9==i) & (df4.X7==sequence[6])]['F1'])[0]

            sumlist.append(num)

        sum1=sum(sumlist)
        norm=[(x / sum1) for x in sumlist]
        print norm
        if rand1<norm[0]:
            newval=0

        else:
            newval=1

    if valueIndex==7:
        max1=0.0
        num=0.0
        sumlist=[]
        df= meta_info['X8']['factor'][0]
        df2= meta_info['X8']['factor'][1]
        df3= meta_info['X8']['factor'][2]
        df4= meta_info['X8']['factor'][3]
        df5= meta_info['X8']['factor'][4]

        for i in range(value_size2):
            num=list( df[(df.X8==i) & (df.X3==sequence[2])]['F1'])[0]\
                    *list( df2[(df2.X8==i) & (df2.X9==sequence[8])]['F1'])[0]\
                    *list( df3[(df3.X8==i) & (df3.X7==sequence[6])]['F1'])[0]\
                    *list( df4[(df4.X8==i) & (df4.X6==sequence[5])]['F1'])[0]\
                    *list( df5[(df5.X8==i) & (df5.X4==sequence[3])]['F1'])[0]

            sumlist.append(num)
        sum1=sum(sumlist)
        norm=[(x / sum1) for x in sumlist]
        print norm
        if rand1<norm[0]:
            newval=0

        else:
            newval=1
    #mylist=[]
    mylist=sequence[:]
    mylist[valueIndex]=newval

    return mylist


        #if meta_info['X1']['factor'][0]=='f1':
            #print 'Blah Blah'

#Functionsssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss





#f1()
#Gener
sequence=[0,0,0,0,0,0,0,0,0,0,0,0]
data=[]
data2=[]
#print decider(8,sequence)
data.append(sequence)
data2.append(sequence)
#print data
d=0
for i in range(6000):

    #sequence=decider(rd.randint(0,11),sequence)
    if d>11:
       d=0
    sequence=decider(d,sequence)
    d=d+1
    if i%13==0:
        data2.append(sequence)
    #print sequence
    data.append(sequence)

fd=pd.DataFrame(data=data,columns=['X1','X2','X3','X4','X5','X6','X7','X8','X9','X10','X11','X12'])
print fd

fd1=pd.DataFrame(data=data2,columns=['X1','X2','X3','X4','X5','X6','X7','X8','X9','X10','X11','X12'])
#print fd1
fd.to_csv('C:/Users/Gabrielahrlr/Desktop/sm297.csv', index=False)
fd1.to_csv('C:/Users/Gabrielahrlr/Desktop/sm298.csv', index=False)
#print f1().columns.values