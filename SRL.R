#SRL Project
library(gRbase)

#Loading all the cliques to form a matrix
G = ug(~X1:X2:X4 + X2:X3:X10 + X9:X11 + X3:X8:X9 + X7:X8:X9 + X7:X12 + X6:X7:X8 + X4:X6:X8 + X5:X6)

#Viewing the Adjacency Matrix
as(G, "matrix")

#View the plots in the graph
library(Rgraphviz)
nAttrs<-list()
nAttrs$color <- c(X3 = "red", X6 = "red", X7 = "red", X10 = "red", X12 = "red")
plot(G,nodeAttrs = nAttrs)

#Checking if the graph is complete and printing the maximum cliques in the dataset
library(RBGL)
is.complete(G)
str(maxClique(G))

#Loading sample for structure learning constraint base (independence)
library(bnlearn)
D2<-read.csv("C:/Users/Gabrielahrlr/Desktop/Campar-Kio/SM20.csv")
D2$X1=as.factor(D2$X1)
D2$X2=as.factor(D2$X2)
D2$X3=as.factor(D2$X3)
D2$X4=as.factor(D2$X4)
D2$X5=as.factor(D2$X5)
D2$X6=as.factor(D2$X6)
D2$X7=as.factor(D2$X7)
D2$X8=as.factor(D2$X8)
D2$X9=as.factor(D2$X9)
D2$X10=as.factor(D2$X10)
D2$X11=as.factor(D2$X11)
D2$X12=as.factor(D2$X12)
str(D2)
#Distribution
counts <- table(D2$X1)
barplot(counts / sum(counts), main="Importance Sampling for X1", xlab="Discrete Values") 


res = gs(D2,undirected=T,alpha=0.05,test="mc-x2",debug=T)
#arc.strength(res,)
res
plot(res)

#################################################
D <- read.csv("C:/Users/Gabrielahrlr/Desktop/sm291.csv")
D$X1=as.factor(D$X1)
D$X2=as.factor(D$X2)
D$X3=as.factor(D$X3)
D$X4=as.factor(D$X4)
D$X5=as.factor(D$X5)
D$X6=as.factor(D$X6)
D$X7=as.factor(D$X7)
D$X8=as.factor(D$X8)
D$X9=as.factor(D$X9)
D$X10=as.factor(D$X10)
D$X11=as.factor(D$X11)
D$X12=as.factor(D$X12)
str(D)

counts <- table(D$X1)
barplot(counts / sum(counts), main="Gibbs Sampling for X1", xlab="Discrete Values") 

library(MASS)
#Independence Test for D2
tbl= table(D2$X1,D2$X2)
tbl
chisq.test(tbl)
#library(gRim)
tbl= table(D$X1,D$X2)
tbl
chisq.test(tbl)

ci.test(D2,test = "mc-x2")


#Changing to all variables to discrete or factors
res = gs(D,undirected=T,alpha=0.05,test="mc-x2",debug=T)
res
plot(res,nodeAttrs = nAttrs)

#Using another structure learning Algorithm
## heauristics
res2 = mmpc(D,alpha=0.05,test="mc-x2",debug=T)
res2
plot(res2)

#Score base learning
res3 = tabu(D,undirected=T,alpha=0.05,test="mc-x2")
res3
plot(res3)

res4 = iamb(D,undirected=T,alpha=0.05,test="mc-x2")
res4
plot(res4)


#Using Decison trees to learn the structures

#Parameter Learning
