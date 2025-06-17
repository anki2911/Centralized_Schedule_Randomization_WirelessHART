import matplotlib.pyplot as plt
from random import randint
import numpy as np

#Let's generate some random X, Y data X = [ [frst group],[second group] ...]
X = []
Y = []
color = []
marker = []
for i in range(4):
    X.append([])
    Y.append([])
    color.append([])
    marker.append([])
    for j in range(400):
        X[i].append(j/100+1)

f = open("Results/KL_3.txt","r") 
i = 0
j = 0
d = 0
for lines in f:
    lines = lines.strip("\n")
    #lines = lines.split()
    for words in lines:
        words = lines.split()
    if words[0] == "%":
        i = i + 1
        d = d + 0.25
        if i == 4:
            i = 0
            d = 0.0
    else:
        Y[i].append(float(words[0]))
        color[i].append(d)
        print float(words[0])
    
print len(X[0])
print len(Y[0])
#X = [ [randint(0,50) for i in range(0,5)] for i in range(0,24)]
#Y = [ [randint(0,50) for i in range(0,5)] for i in range(0,24)]
labels = []
for i in range(4):
    p = i+1
    labels.append(str(p)+"0 flows")


fig = plt.figure()
ax = fig.add_subplot(111)
for x,y,lab in zip(X,Y,labels):
    ax.scatter(x,y,s=80,alpha=0.9,label=lab)
plt.gray()
plt.xlim([0, 5])
plt.ylim([0, 0.6])   
plt.xticks(np.arange(0, 5, 1.0),fontsize='large', fontweight='bold')
plt.yticks(np.arange(0, 0.6, 0.1),fontsize='large', fontweight='bold') 
plt.title('Graph A',fontsize='large', fontweight='bold')
plt.ylabel('K-L Divergence',fontsize='large', fontweight='bold',labelpad=20)
plt.xlabel('number of channels',fontsize='large', fontweight='bold',labelpad=20)
           
#Now this is actually the code that you need, an easy fix your colors just cut and paste not you need ax.
colormap = plt.cm.gist_ncar #nipy_spectral, Set1,Paired  
colorst = [colormap(i) for i in np.linspace(0, 0.8,len(ax.collections))]       
for t,j1 in enumerate(ax.collections):
    j1.set_color(colorst[t])


ax.legend(fontsize='large')
plt.grid()
plt.show()
