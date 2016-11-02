from mpl_toolkits.mplot3d import axes3d
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

fin = open("coord.txt","r")

x,y,z = list(), list(), list()

for line in fin:
    _x,_y,_z = map(float, line.split())
    x.append(_x)
    y.append(_y)
    z.append(_z)

ax.plot(x, y, z, zdir='z', label='zs=0, zdir=z')
ax.set_xlim3d(-5000  ,20000)
ax.set_ylim3d(-10000 ,10000)
ax.set_zlim3d(-10000 ,50000)
#plt.ylim(-100000000000 ,10000000000000 )
#plt.xlim(-100000000000 ,10000000000000 )
#ax.view_init(90, -90)
plt.show()

