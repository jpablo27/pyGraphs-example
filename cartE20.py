from pylab import *
import matplotlib.pyplot as plt
import numpy as np
import csv



v=[-2,4,-2.5,25]

y = []
x = []
#Open the T1.txt file with the drone trajectory 
with open('T1_20.txt','r') as csvfile:
	plots = csv.reader(csvfile, delimiter=',')
	for row in plots:
		x.append(float(row[0]))
		y.append(float(row[1]))

x_ref =[0,0]
y_ref =[0,20]

x_wps =[0,0]
y_wps =[0,20]

colors = ['g','y']
labs = ['$inicio$','$wp_1$']
color=['m']

fig = plt.figure(figsize=(12,7),dpi=100)
ax = fig.add_subplot(111)

plt.plot(x_ref,y_ref,color = "red", linewidth= 2.5, linestyle="-",label='Trayectoria deseada')
plt.plot(x, y, color="blue", linewidth=2.5, linestyle="--",label='Trayectoria observada')
plt.scatter(x_wps,y_wps,s=100,c=colors,alpha=1.0)

for i, txt in enumerate(labs):
	ax.annotate(txt, (x_wps[i]+0.25,y_wps[i]+0.25), fontsize=22)

plt.xlabel('x ($m$)')
plt.ylabel('y ($m$)')
plt.axis(v)
plt.legend()


left,right = ax.get_xlim()
low,high = ax.get_ylim()
arrow( left, 0, right -left, 0, length_includes_head = True, head_width = 0.15 )
arrow( 0, low, 0, high-low, length_includes_head = True, head_width = 0.15 ) 

grid()
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 20}

matplotlib.rc('font', **font)

plt.savefig('destination_path.eps', format='eps', dpi=1000)
plt.show()