import math
import matplotlib.pyplot as pl
import matplotlib as mpl
import numpy

def gam(x,n):
	return (math.exp(-x)*math.pow(x,n))

fig=pl.figure()
fig.patch.set_facecolor('pink')
X=numpy.arange(0,30.5,0.5)
Y=[]
y=[]

for n in range(0,9,1):
    for i in X:
        y+=[gam(i,n)]
    Y+=[y]
    y=[]

#sets created

colr=['#FF0000','#F0F000','#00FF00','#00F0F0','#0000FF','#F000F0','#F0FFF0','#B0FFE0','#D0EEF0','#0FFFF0']

for k in range(0,len(Y)):
    cl=colr[k]
    pl.plot(list(X),Y[k],cl)

pl.show()    
    
