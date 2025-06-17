# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
#np.random.seed(19680801)




fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#n = 10
xs = []
ys = []
zs = []
for i in range(4):
    str1 = "../Codes/New_Multi_" + str(i+1)
    for j in range(4):
        str2 = str1 + "/D" + str(j+1) + "1/R1/"
        for k in range(100):
            str3 = str2 + "entropy_out_1_" + str(k+1) + ".txt"
            f = open(str3,"r")
            l = float(f.read())
            xs.append(i+1)
            ys.append(int(j+1)*10)
            zs.append(l)
            
# For each set of style and range settings, plot n random points in the box
# defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
#for c, m, zlow, zhigh in [('r', 'o', 1,4),('r', 'o', 10,40)]:
    #xs = [1,2,3,4,5,6,7,8,9,10]
    #ys = [1,2,3,4,5,6,7,8,9,10]
    #zs = [1,2,3,4,5,6,7,8,9,10]
#    ax.scatter(xs, ys, zs, c=c, marker=m)
ax.scatter3D(xs,ys,zs, c=zs, cmap='Reds');
ax.set_xlabel('Number of channels')
ax.set_ylabel('Number of flows')
ax.set_zlabel('schedule entropy')

plt.show()


