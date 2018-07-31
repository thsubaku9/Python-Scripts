#Finding the least time to travel distance D with energy limit
H=int(input('Enter the E limit'))
D=int(input('Enter D to cover'))
vel=input('velocity selections')
vel=vel.split()
vel=list(map(int,vel))
enl=input('energy consumption')
enl=enl.split()
enl=list(map(int,enl))


resDPt=[None]*(D+1)
resDPe=[None]*(D+1)
resDPt[0]=0
resDPe[0]=0

'''
i-> checking dp over the distance sequentially
c2->selection of v,E pair
i2->traversing distance sequentially with seleceted pairing
'''
for i in range(1,D+1):
    testab=0
    eestab=0
    for c2 in range(0,len(vel)):
        for i2 in range(1,i+1):
            tReq=i2/vel[c2]
            tprev=resDPt[i-i2]
            eReq=tReq*(enl[c2])+resDPe[i-i2]        
            if(eReq<H):
                testab=tReq+tprev
                eestab=eReq
                if(resDPt[i]==None):
                    resDPt[i]=testab
                    resDPe[i]=eestab
                elif(resDPt[i]>testab):
                    resDPt[i]=testab
                    resDPe[i]=eestab
                
print("Necessary time to travel distance "+ str(D)+" is "+str(resDPt[D])+" Required energy: "+str(resDPe[D]))
            

