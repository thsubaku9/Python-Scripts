mx=0
pt=0

def maxArea(ar):
    global mx
    global pt
    for i in range(0,len(ar)):
        lf=i
        rg=i
        cbuild=ar[i]        
        for j in range(i,-1,-1):
            if(ar[j]>=cbuild):
                lf=j
            else:
                break
        for j in range(i,len(ar)):
            if(ar[j]>=cbuild):
                rg=j
            else:
                break
        chk=cbuild*(rg-lf+1)
        global mx
        if(chk>mx):
            pt=i
            mx=chk

ar=input('Enter the height of respective histograms').strip()
ar=ar.split(' ')
ar=list(map(int,ar))
maxArea(ar)
print("Maximum area is ",mx," around the point ",pt)
