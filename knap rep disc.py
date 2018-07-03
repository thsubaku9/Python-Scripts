wt=input("Enter the weights ").strip()
wt=wt.split(' ')
wt=list(map(int,wt))
vl=input("Enter the values ").strip()
vl=vl.split(' ')
vl=list(map(int,vl))
wLimit=int(input("Enter the weight limit").strip())
#got the values
rng=len(vl)
res=[0]*(wLimit+1)
#extracted params

for w in range(1,wLimit+1):
    for Ki in range(0,rng):
        if(wt[Ki]<=w):
            vlTemp=res[w-wt[Ki]]+vl[Ki]
        if(vlTemp>res[w]):
            res[w]=vlTemp
#DP array
#create a set array/2D that stores elements accessed to make selected elements easier            
            

print("Required value for the given weight with repetitions is ",res[wLimit])
    
        

