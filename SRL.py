__author__ = 'Kienka Cromwell KIO'
import  math as mt

def checkEqual2(iterator):
    return len(set(iterator)) <= 1

def partition_component(nloop,coefficient):
    #Component of Z
    z=0.0
    for i in range(nloop):
        #print i
        z = z+(i*coefficient)
    return z
def changer(elementList):
    if checkEqual2(elementList):
        if elementList[0]==0:
            elementList[0]=1
            return elementList
        if elementList[0]==1:
            print "I am One"
        else:
            print "I am in Two"
    else:
        if elementList[0]==1:
            elementList[0]=2
        return elementList


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


#For Computing the Z,

Z=mt.exp(X1+X2+X3+X4+X5+X6+X7+X8+X9+X10+X11+X12)
Z2=mt.exp(X1+X2+X3+X4+X5+X6+X7+X8+X9+X10*X11*X12)
print mt.log(Z)
print Z,mt.log(Z2)

#Finding the probability of the model
#Gibbs sampling of a network

ls=changer([0,0,0])
print ls
ls=changer(ls)
print ls





#Sample Generation given the P(X)

#Learn the Structure and Parameter from the sample and compare with that of the Graph

#Inference on the learnt network


