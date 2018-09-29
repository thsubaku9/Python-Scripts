import queue

fl=open('graph.txt','r')
lines=fl.read()
lines=lines.split('\n')
n=len(lines)
adjMat=list()
visited=[0]*n
parent=[-1]*n
distance=[-1]*n
for i in range(0,n):
    adjMat+=[[]]

for i in range(0,n):
    adjMat[i]+=[0]*n    

for itr in range(0,n):
    me=lines[itr].split(' ')
    for je in me:
        parse=je.strip()
        tr=je.split(sep='-')
        adjMat[itr][int(je[0])-1]=int(tr[1])
    
q=queue.Queue(n)

startNode=int(input("Enter starting node: "))
startNode-=1
q.queue.append(startNode)

visited[startNode]=1
parent[startNode]=startNode
distance[startNode]=0
while(q.empty()==False):
    currentNode=q.queue.pop()
    for v in range(0,n):
        if(adjMat[currentNode][v]>0):
            if(visited[v]==0):
                parent[v]=currentNode
                visited[v]=1
                distance[v]=distance[currentNode]+adjMat[currentNode][v]
                q.queue.append(v)
            elif(visited[v]==1 and distance[v]>distance[currentNode]+adjMat[currentNode][v]):
                distance[v]=distance[currentNode]+adjMat[currentNode][v]
                parent[v]=currentNode
                
print("\nDisplaying paths:\n")
for i in range(0,n):
    print(i)
    j=i
    totDist=0
    while(parent[j]!=startNode):
        print("<-"+str(j+1))
        j=parent[j]
    print("<-"+(startNode+1))
    print("\nDistance to "+str(i+1)+" : "+str(distance[i])+"\n")
    
    
