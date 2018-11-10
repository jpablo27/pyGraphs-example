# encoding: utf-8
import matplotlib.pyplot as plt
import csv
import re
from pylab import *

t = []
y = []
r_dist = []
e_ang = []
r_ang =[]
v=[0,13,0,30]
v_ang=[0,10,-45,180]

xt =[5.24,5.24]
xdt=[35.82,35.82]
yt =[0 ,20]
yat =[-45 ,270]

with open('G90p.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        t.append(float(row[0]))
        e_ang.append(float(row[1]))
        r_ang.append(float(row[2]))

fig = plt.figure(figsize=(12,7),dpi=100)

plt.plot(t,e_ang, label=u'Ángulo observado')
plt.plot(t,r_ang, label=u'Ángulo de referencia',color = "green", linewidth= 2.5, linestyle="--")
plt.plot(xt,yat,color = "red", linewidth= 2.5, linestyle="--")
plt.legend()
plt.xlabel('tiempo ($s$)')
plt.ylabel(u'$\psi$ ($^{o}$)')
plt.axis(v_ang)
plt.title('   \n   ')
plt.xticks([0,5.24,10],['$0$','$t_{s}=5.24$','$10$'])
plt.yticks([-45,0,90,180],['$-45$','$0$','$\psi_{ref}=90$','$180$'])
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 20}

matplotlib.rc('font', **font)
plt.subplots_adjust(left=0.15,right=0.96)

plt.savefig('destination_path.eps', format='eps', dpi=1000)

plt.show()
