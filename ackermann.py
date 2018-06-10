###Ackermann Function

def mn(m,n):
    if m==0:
        return n+1
    else:
        if m>0 and n==0:            
            mn(m-1,1)
        elif m>0 and n>0 :
            mn(m-1,mn(m,n-1))

            
