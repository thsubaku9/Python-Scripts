#merge sort

def mgsrt(a):
    left=[]
    right=[]
    for i in range(0,int(len(a)/2)):
        left+=[a[i]]
    for j in range(int(len(a)/2),len(a)):
        right+=[a[j]]

    if(len(left)>1):
        left=mgsrt(left)
    if(len(right)>1):
        right=mgsrt(right)
    ptrl=0
    ptrr=0
    res=[]
    for i in range(0,len(left)):
        if(left[ptrl]<right[ptrr]):
            res+=[left[ptrl]]
            ptrl+=1
        elif(left[ptrl]>=right[ptrr]):
            res+=[right[ptrr]]
            ptrr+=1
    for z in range(ptrl,len(left)):
        res+=[left[z]]
    for z in range(ptrr,len(right)):
        res+=[right[z]]
    return res

n=input("Enter size of array")
a=[]
for i in range(0,int(n)):
    B=input("Enter Number")
    a+=[B]
print(a)
a=mgsrt(a)
print(a)

        
            
        
    

    
        
