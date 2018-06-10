
def exc(a,i,j):
    a[i],a[j]=a[j],a[i]

def shift(a,ln):
    for i in range(ln,1,-1):
        j=i//2
        if(a[i]>a[j]):
            exc(a,i,j)

def heap(a):
    ln=len(a)-1
    for i in range(1,ln//2):
        exc(a,i,ln)
        ln=ln-1
        comp(a,ln-1,ln)

    print(a)


def comp(a,j,ln):
    parent=j//2
    child=parent*2
    while(child<ln):
        if(a[child]>a[child+1]):
            child+=1
        if(a[parent]<a[child]):
            if(child<ln):
                exc(a,parent,child)             
        child=parent
        parent/=2
        
    
        

        
        
        
    
    
            

            
    
