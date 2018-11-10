# encoding: utf-8
import matplotlib.pyplot as plt
import csv
import re
from pylab import *

x = []
y = []
r_dist = []
e_ang = []
r_ang =[]
v=[0,25,0,20]
v_ang=[0,25,-180,180]

xt =[7.17,7.17]
xdt=[19.07,19.07]
yt =[0 ,15]
yat =[0 ,-180]
fig = plt.figure(figsize=(12,7),dpi=100)

with open('OnlyD10.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0]))
        y.append(float(row[1]))
        r_dist.append(float(row[2]))
        e_ang.append(float(row[3]))
        r_ang.append(float(row[4]))

plt.subplot(2,1,1)
plt.plot(x,y, label='Distancia observada')
plt.plot(x,r_dist, label='Distancia de referencia',color = "green", linewidth= 2.5, linestyle="--")
#plt.plot(xt,yt,color = "red", linewidth= 2.5, linestyle="--")
plt.plot(xdt,yt,color = "red", linewidth= 2.5, linestyle="--")
plt.axis(v)
#plt.title('Control de desplazamiento hacia un  waypoint. \n  Prueba de 5m')
#plt.annotate('$t_{2}=14.7$', xy=(14.0, -2.5),annotation_clip=False)
#plt.annotate('$t_{1}=7.17$', xy=(6.0, -2.5),annotation_clip=False)
plt.xticks([0,19.07,25],['$0$','$t_{1}=19.07$','$25$'])

######### annotating the x axis   #########
#plt.annotate('', xy=(7.17, -0.5),xytext=(14.7,-0.5), arrowprops=dict(arrowstyle='<->',facecolor='red'),annotation_clip=False)  

#plt.annotate('$\Delta_{t}=7.53$',xy=(10,-2.0), annotation_clip=False)

plt.legend()
plt.xlabel(' tiempo ($s$)')
plt.ylabel('$d$($m$)')

plt.subplots_adjust(hspace=0.4)
#

plt.subplot(2,1,2)
plt.plot(x,e_ang, label=u'Ángulo observado')
plt.plot(x,r_ang, label=u'Ángulo de referencia ',color = "green", linewidth= 2.5, linestyle="--")
#plt.plot(xt,yat,color = "red", linewidth= 2.5, linestyle="--")
plt.legend()
plt.xlabel('tiempo ($s$)')
plt.ylabel('$\psi$  ($^{o}$)')
plt.axis(v_ang)
plt.title('   \n   ')
#plt.annotate('$t_{1}=7.17$', xy=(6.5, -220),annotation_clip=False)
plt.xticks([0,7.17,25],['$0$','','$25$'])
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 18}

matplotlib.rc('font', **font)
plt.savefig('destination_path.eps', format='eps', dpi=1000)

plt.show()
