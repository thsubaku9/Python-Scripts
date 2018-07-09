#discrete knapsack without rep

n=int(input("Number of elements\t"))
eVals=input("Elements values\t").strip().split()
eVals=list(map(int,eVals))
eWt=input("Elements weight\t").strip().split()
eWt=list(map(int,eWt))
wMax=int(input("Weight constraint\t"))

#all details present now

optvl=[0]*(wMax+1)
eleP=dict()

#hash for mapping selected elements for that optimal weight
for itr in range(0,wMax+1):
    eleP[itr]=[]

#iterate for each weight, through each element
#select the element whose weight<=iterated weight and the element has not been visited
    
for wt in range(1,wMax+1):
    vCheck=0
    for ele in range(0,n):
        if(eWt[ele]<=wt):
            if(ele not in eleP[wt-eWt[ele]]):
                if(eVals[ele]+optvl[wt-eWt[ele]]>vCheck):
                    vCheck=eVals[ele]+optvl[wt-eWt[ele]]
                    ms=eleP[wt-eWt[ele]]+[ele]
    if(vCheck>optvl[wt]):
        optvl[wt]=vCheck
        eleP[wt]=ms

        
print("Optimal score",optvl[-1])
print("Optimal selection for optimal score",eleP[wMax].sort())
