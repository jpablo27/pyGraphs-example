# encoding: utf-8
from pylab import *
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import csv

x = []
y = []
x_ref =[]
y_ref = []
r_dist = []
e_ang = []
r_ang =[]
vx=[0,34,-3,3]
vy=[0,34,-1,6]
v_ang=[0,34,-180,180]

xt =[7.17,7.17]
xdt=[10.9,10.9]
yt =[0 ,5]
yat =[0 ,-180]
time =[]
with open('IV5.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=",")
    for row in plots:
    	time.append(float(row[0]))
        x.append(float(row[1]))
        x_ref.append(float(row[2]))
        y.append(float(row[3]))
        y_ref.append(float(row[4]))
        e_ang.append(float(row[5]))
        r_ang.append(float(row[6]))

fig = plt.figure(figsize=(12,7),dpi=100)

fontP = FontProperties()
fontP.set_size('small')     
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
plt.subplot(3,1,2)
plt.plot(time,x, label=u'')
plt.plot(time,x_ref, label='',linestyle="--",linewidth= 2.5,color = "green")
plt.legend((u'Posición observada', u'Valor de referencia'),
           shadow=True, loc='upper right', handlelength=1.5, fontsize=10,prop=fontP)
plt.axis(vx)
plt.plot([14.59,14.59],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([29.33,29.33],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([7.54,7.54],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([22.47,22.47],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.xticks([0,7.54,14.59,22.47,29.33,34],['$0$','$t_{\psi 1}=7.54$','$t_{d1}=14.59$','$t_{\psi 2}=22.47$','$t_{d2}=29.33$','$34$'],fontsize = 15)

plt.legend()
plt.xlabel(' tiempo ($s$)')
plt.ylabel('x ($m$)')


ann = plt.annotate("$wpx_{ref1}$",
                  xy=(4, 0), xycoords='data',
                  xytext=(3, 2), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )
ann = plt.annotate("$wpx_{ref2}$",
                  xy=(17, 0), xycoords='data',
                  xytext=(16, 2), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )
plt.annotate('', xy=(7.54, -4.25),xytext=(14.59,-4.25), arrowprops=dict(arrowstyle='<->',facecolor='red'),annotation_clip=False)  
plt.annotate('$Ts_{wp1}=7.05$',xy=(9,-5.), annotation_clip=False,fontsize = 15)

plt.annotate('', xy=(22.47, -4.25),xytext=(29.33,-4.25), arrowprops=dict(arrowstyle='<->',facecolor='red'),annotation_clip=False)  
plt.annotate('$Ts_{wp2}=6.86$',xy=(24.0,-5.0), annotation_clip=False,fontsize = 15)
#
#yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
plt.subplot(3,1,3)
plt.plot(time,y, label=u'')
plt.plot(time,y_ref, label='',linestyle="--",linewidth= 2.5,color = "green")
plt.legend((u'Posición observada', u'Valor de referencia'),
           shadow=True, loc='upper right', handlelength=1.5, fontsize=10,prop=fontP)
plt.plot([14.59,14.59],vy[2:4],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([29.33,29.33],vy[2:4],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([7.54,7.54],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([22.47,22.47],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.axis(vy)
plt.xticks([0,7.54,14.59,22.47,29.33,34],['$0$','$t_{\psi 1}=7.54$','$t_{d1}=14.59$','$t_{\psi 2}=22.47$','$t_{d2}=29.33$','$34$'],fontsize = 15)
plt.legend()
plt.xlabel(' tiempo ($s$)')
plt.ylabel('y ($m$)')


ann = plt.annotate("$wpy_{ref1}$",
                  xy=(4, 5), xycoords='data',
                  xytext=(3, 3), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )
ann = plt.annotate("$wpy_{ref2}$",
                  xy=(17, 0), xycoords='data',
                  xytext=(16, 2), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

plt.annotate('', xy=(7.54, -2.5),xytext=(14.59,-2.5), arrowprops=dict(arrowstyle='<->',facecolor='red'),annotation_clip=False)  
plt.annotate('$Ts_{wp1}=7.05$',xy=(9,-3.5), annotation_clip=False,fontsize = 15)

plt.annotate('', xy=(22.47, -2.5),xytext=(29.33,-2.5), arrowprops=dict(arrowstyle='<->',facecolor='red'),annotation_clip=False)  
plt.annotate('$Ts_{wp2}=6.86$',xy=(24.0,-3.5), annotation_clip=False,fontsize = 15)

#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa



plt.subplot(3,1,1)
plt.plot(time,e_ang)
plt.plot(time,r_ang, linestyle="--",linewidth= 2.5,color = "green")
plt.legend((u'Ángulo observado', u'Ángulo de referencia'),
           shadow=True, loc='upper right', handlelength=1.5, fontsize=10,prop=fontP)

plt.plot([7.54,7.54],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([22.47,22.47],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([14.59,14.59],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([29.33,29.33],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.legend()
plt.xlabel('\ntiempo ($s$) ')
plt.ylabel(u'$\psi$ ($^{o}$)')
plt.axis(v_ang)
plt.yticks(fontsize = 10)
plt.xticks([0,7.54,14.59,22.47,29.33,34],['$0$','$t_{\psi 1}=7.54$','$t_{d1}=14.59$','$t_{\psi 2}=22.47$','$t_{d2}=29.33$','$34$'],fontsize = 15)

ann = plt.annotate("$\psi_{ref1}$",
                  xy=(1, -90), xycoords='data',
                  xytext=(2.5, 0), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate("$\psi_{ref2}$",
                  xy=(15, 100), xycoords='data',
                  xytext=(13, 150), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

plt.annotate('', xy=(0, -260),xytext=(7.54,-260), arrowprops=dict(arrowstyle='<->',facecolor='red'),annotation_clip=False)  
plt.annotate('$Ts_{\psi 1}=7.54$',xy=(3.,-310), annotation_clip=False,fontsize = 15)

plt.annotate('', xy=(14.59, -260),xytext=(22.47,-260), arrowprops=dict(arrowstyle='<->',facecolor='red'),annotation_clip=False)  
plt.annotate('$Ts_{\psi 2}=7.97$',xy=(17.0,-310), annotation_clip=False,fontsize = 15)

plt.subplots_adjust(hspace=0.60)

plt.subplots_adjust(left=0.07,right=0.97)

plt.savefig('destination_path.eps', format='eps', dpi=1000)


plt.show()