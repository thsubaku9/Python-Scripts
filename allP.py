import numpy as np

def recursionPath(adjMat,visited,tempSeq,resSeq,lastNode,n,cursor):
    if(tempSeq[-1]==lastNode):
        resSeq+=[tuple(tempSeq)]
        return
    
    for i in range(0,n):
        if(visited[0][i]==1):
            continue
        elif(visited[0][i]==0 and adjMat[cursor-1][i]==1):
            tempSeq.append(i)
            visited[0][i]=1
            recursionPath(adjMat,visited,tempSeq,resSeq,lastNode,n,cursor+1)
            tempSeq.pop()
            visited[0][i]=0
        else:
            continue
    

#getting initial data
fileName=input('enter the file name\t')+'.txt'
rw=''
with open(fileName,'r') as a:
	rw+=a.read()
rw=rw.split('\n')
n=len(rw)
adjMat=np.zeros((n,n),int)
visited=np.zeros((1,n),int)

startNode=int(input("Enter starting point"))-1
endNode=int(input("Enter last point"))-1

tempSeq=list()
tempSeq.append(startNode)               
resultSeq=[]

visited[0][startNode]=1
#reducing to int
j=[]
for i in rw:
	k=i.split(' ')
	artemp=[]
	for kk in k:
		artemp+=[int(kk)-1]
	j+=[artemp]

#modifying AdjMat
for x1 in range(0,n):
    for x2 in j[x1]:
        adjMat[x1][x2]=1

#memory efficiency
del j,rw;

recursionPath(adjMat,visited,tempSeq,resultSeq,endNode,n,1)
