# encoding: utf-8
from pylab import *
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import csv
t_range=51
x = []
y = []
x_ref =[]
y_ref = []
r_dist = []
e_ang = []
r_ang =[]
vx=[0,t_range,-3,3]
vy=[0,t_range,-1,15]
v_ang=[0,t_range,-180,180]

xt =[7.17,7.17]
xdt=[10.9,10.9]
yt =[0 ,5]
yat =[0 ,-180]
time =[]
with open('IV10.txt','r') as csvfile:
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
#plt.plot(xt,yt,color = "red", linewidth= 2.5, linestyle="--")
#plt.plot(xdt,yt,color = "red", linewidth= 2.5, linestyle="--")
plt.axis(vx)
plt.plot([23.19,23.19],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([46.01,46.01],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([7.43,7.43],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([30.89,30.89],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.xticks([0,7.43,23.19,30.89,46.01,t_range],['$0$','$t_{\psi 1}=7.43$','$t_{d1}=23.19$','$t_{\psi 2}=30.89$','$t_{d2}=46.01$','$51$'],fontsize = 15)

plt.legend()
plt.xlabel('  tiempo ($s$)')
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
                  xy=(25, 0), xycoords='data',
                  xytext=(24, 2), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )
plt.annotate('', xy=(7.43, -4.25),xytext=(23.19,-4.25), arrowprops=dict(arrowstyle='<->',facecolor='red'),annotation_clip=False)  
plt.annotate('$Ts_{wp1}=15.76$',xy=(11,-5.0), annotation_clip=False,fontsize = 15)

plt.annotate('', xy=(30.89, -4.25),xytext=(46.01,-4.25), arrowprops=dict(arrowstyle='<->',facecolor='red'),annotation_clip=False)  
plt.annotate('$Ts_{wp2}=15.12$',xy=(35,-5.0), annotation_clip=False,fontsize = 15)

#yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
plt.subplot(3,1,3)
plt.plot(time,y, label=u'')
plt.plot(time,y_ref, label='',linestyle="--",linewidth= 2.5,color = "green")
plt.legend((u'Posición observada', u'Valor de referencia'),
           shadow=True, loc='upper right', handlelength=1.5, fontsize=10,prop=fontP)
plt.plot([23.19,23.19],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([46.01,46.01],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([7.43,7.43],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([30.89,30.89],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.axis(vy)
plt.xticks([0,7.43,23.19,30.89,46.01,t_range],['$0$','$t_{\psi 1}=7.43$','$t_{d1}=23.19$','$t_{\psi 2}=30.89$','$t_{d2}=46.01$','$51$'],fontsize = 15)
plt.legend()
plt.xlabel('  tiempo ($s$)')
plt.ylabel('y ($m$)')


ann = plt.annotate("$wpy_{ref1}$",
                  xy=(4, 10), xycoords='data',
                  xytext=(3, 6), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )
ann = plt.annotate("$wpy_{ref2}$",
                  xy=(26, 0), xycoords='data',
                  xytext=(25, 2), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

plt.annotate('', xy=(7.43, -4.2),xytext=(23.19,-4.2), arrowprops=dict(arrowstyle='<->',facecolor='red'),annotation_clip=False)  
plt.annotate('$Ts_{wp1}=15.76$',xy=(11,-6.5), annotation_clip=False,fontsize = 15)

plt.annotate('', xy=(30.89, -4.2),xytext=(46.01,-4.2), arrowprops=dict(arrowstyle='<->',facecolor='red'),annotation_clip=False)  
plt.annotate('$Ts_{wp2}=15.12$',xy=(35,-6.5), annotation_clip=False,fontsize = 15)

#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

plt.subplot(3,1,1)
plt.plot(time,e_ang, label=u'')
plt.plot(time,r_ang, label=u'',linestyle="--",linewidth= 2.5,color = "green")
plt.legend((u'Ángulo observado', u'Ángulo de referencia'),
           shadow=True, loc='center right', handlelength=1.5, fontsize=10,prop=fontP)
plt.plot([7.43,7.43],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([30.89,30.89],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([23.19,23.19],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([46.01,46.01],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.legend()
plt.xlabel('\ntiempo ($s$)')
plt.ylabel(u'$\psi$ ($^{o}$)')
plt.axis(v_ang)
plt.title('   \n   ')
plt.xticks([0,7.43,23.19,30.89,46.01,t_range],['$0$','$t_{\psi 1}=7.43$','$t_{d1}=23.19$','$t_{\psi 2}=30.89$','$t_{d2}=46.01$','$51$'],fontsize = 15)
plt.yticks(fontsize = 10)

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
                  xy=(26, 100), xycoords='data',
                  xytext=(25, 150), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

plt.annotate('', xy=(0, -260),xytext=(7.43,-260), arrowprops=dict(arrowstyle='<->',facecolor='red'),annotation_clip=False)  
plt.annotate('$Ts_{\psi 1}=7.43$',xy=(1,-310), annotation_clip=False,fontsize = 15)

plt.annotate('', xy=(23.19, -260),xytext=(30.89,-260), arrowprops=dict(arrowstyle='<->',facecolor='red'),annotation_clip=False)  
plt.annotate('$Ts_{\psi 2}=7.7$',xy=(24.5,-310), annotation_clip=False,fontsize = 15)

plt.subplots_adjust(hspace=0.60)
plt.subplots_adjust(left=0.07,right=0.97)
plt.savefig('destination_path.eps', format='eps', dpi=1000)

plt.show()