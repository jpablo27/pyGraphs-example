# encoding: utf-8
from pylab import *
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import csv
t_range=84
x = []
y = []
x_ref =[]
y_ref = []
r_dist = []
e_ang = []
r_ang =[]
vx=[0,t_range,-3,3]
vy=[0,t_range,-1,25]
v_ang=[0,t_range,-180,180]

xt =[7.17,7.17]
xdt=[10.9,10.9]
yt =[0 ,5]
yat =[0 ,-180]
time =[]
with open('IV20.txt','r') as csvfile:
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

t_ang1=7.37
t_ang2=47.19
t_dis1=39.58
t_dis2=79.06       
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
plt.subplot(3,1,2)
plt.plot(time,x, label=u'')
plt.plot(time,x_ref, label='',linestyle="--",linewidth= 2.5,color = "green")
plt.legend((u'Posición observada', u'Valor de referencia'),
           shadow=True, loc='upper right', handlelength=1.5, fontsize=10,prop=fontP)
#plt.plot(xt,yt,color = "red", linewidth= 2.5, linestyle="--")
#plt.plot(xdt,yt,color = "red", linewidth= 2.5, linestyle="--")
plt.axis(vx)
plt.plot([t_ang1,t_ang1],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_ang2,t_ang2],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_dis1,t_dis1],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_dis2,t_dis2],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.xticks([0,t_ang1,t_dis1,t_ang2,t_dis2,t_range],['$0$','$t_{\psi 1}=%.2f$ '%(t_ang1),'$t_{d1}=%.2f$ '%(t_dis1),'$t_{\psi 2}=%.2f$ '%(t_ang2),'$t_{d2}=%.2f$ ' %(t_dis2) ,'$%d$' %t_range])

######### annotating the x axis   #########
#plt.annotate('', xy=(7.17, -0.5),xytext=(14.7,-0.5), arrowprops=dict(arrowstyle='<->',facecolor='red'),annotation_clip=False)  

#plt.annotate('$\Delta_{t}=7.53$',xy=(10,-2.0), annotation_clip=False)

plt.legend()
plt.xlabel(' tiempo ($s$)')
plt.ylabel('x ($m$)')

plt.subplots_adjust(hspace=0.4)

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
                  xy=(47, 0), xycoords='data',
                  xytext=(43, 2), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

plt.annotate('', xy=(t_ang1, -4.25),xytext=(t_dis1,-4.25), arrowprops=dict(arrowstyle='<->',facecolor='red'),annotation_clip=False)  
plt.annotate('$Ts_{wp1}=%.2f$' %(t_dis1-t_ang1),xy=((t_dis1+t_ang1)/2,-5.0), annotation_clip=False)

plt.annotate('', xy=(t_ang2, -4.25),xytext=(t_dis2,-4.25), arrowprops=dict(arrowstyle='<->',facecolor='red'),annotation_clip=False)  
plt.annotate('$Ts_{wp2}=%.2f$' %(t_dis2-t_ang2),xy=((t_dis2+t_ang2)/2,-5.0), annotation_clip=False)



#yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
plt.subplot(3,1,3)
plt.plot(time,y, label=u'')
plt.plot(time,y_ref, label='',linestyle="--",linewidth= 2.5,color = "green")
plt.legend((u'Posición observada', u'Valor de referencia'),
           shadow=True, loc='upper right', handlelength=1.5, fontsize=10,prop=fontP)
plt.plot([t_ang1,t_ang1],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_ang2,t_ang2],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_dis1,t_dis1],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_dis2,t_dis2],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.axis(vy)
plt.xticks([0,t_ang1,t_dis1,t_ang2,t_dis2,t_range],['$0$','$t_{\psi 1}=%.2f$ '%(t_ang1),'$t_{d1}=%.2f$ '%(t_dis1),'$t_{\psi 2}=%.2f$ '%(t_ang2),'$t_{d2}=%.2f$ ' %(t_dis2) ,'$%d$' %t_range])
plt.legend()
plt.xlabel(' tiempo ($s$)')
plt.ylabel('y ($m$)')

plt.subplots_adjust(hspace=0.4)

ann = plt.annotate("$wpy_{ref1}$",
                  xy=(4, 20), xycoords='data',
                  xytext=(3, 11), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )
ann = plt.annotate("$wpy_{ref2}$",
                  xy=(46, 0), xycoords='data',
                  xytext=(42, 5), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

plt.annotate('', xy=(t_ang1, -6.5),xytext=(t_dis1,-6.5), arrowprops=dict(arrowstyle='<->',facecolor='red'),annotation_clip=False)  
plt.annotate('$Ts_{wp1}=%.2f$' %(t_dis1-t_ang1),xy=((t_dis1+t_ang1)/2,-9.5), annotation_clip=False)

plt.annotate('', xy=(t_ang2, -6.5),xytext=(t_dis2,-6.5), arrowprops=dict(arrowstyle='<->',facecolor='red'),annotation_clip=False)  
plt.annotate('$Ts_{wp2}=%.2f$' %(t_dis2-t_ang2),xy=((t_dis2+t_ang2)/2,-9.5), annotation_clip=False)

#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

plt.subplot(3,1,1)
plt.plot(time,e_ang, label=u'')
plt.plot(time,r_ang, label=u'',linestyle="--",linewidth= 2.5,color = "green")
plt.legend((u'Ángulo observado', u'Ángulo de referencia'),
           shadow=True, loc='center right', handlelength=1.5, fontsize=10,prop=fontP)
plt.plot([t_ang1,t_ang1],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_ang2,t_ang2],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_dis1,t_dis1],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_dis2,t_dis2],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.legend()
plt.xlabel('\n tiempo ($s$)')
plt.ylabel(u'$\psi $($^{o}$)')
plt.axis(v_ang)
plt.title('   \n   ')
plt.xticks([0,t_ang1,t_dis1,t_ang2,t_dis2,t_range],['$0$','$t_{\psi 1}=%.2f$ '%(t_ang1),'$t_{d1}=%.2f$ '%(t_dis1),'$t_{\psi 2}=%.2f$ '%(t_ang2),'$t_{d2}=%.2f$ ' %(t_dis2) ,'$%d$' %t_range])
plt.yticks(fontsize = 10)

ann = plt.annotate("$\psi_{ref1}$",
                  xy=(1, -90), xycoords='data',
                  xytext=(5, 100), textcoords='data',
                  size=20, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate("$\psi_{ref2}$",
                  xy=(45, 100), xycoords='data',
                  xytext=(43, 150), textcoords='data',
                  size=20, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

plt.annotate('', xy=(0, -260),xytext=(t_ang1,-260), arrowprops=dict(arrowstyle='<->',facecolor='red'),annotation_clip=False)  
plt.annotate('$Ts_{\psi 1}=%.2f$' %(t_ang1),xy=(t_ang1/2-3.5,-310), annotation_clip=False)

plt.annotate('', xy=(t_dis1, -260),xytext=(t_ang2,-260), arrowprops=dict(arrowstyle='<->',facecolor='red'),annotation_clip=False)  
plt.annotate('$Ts_{\psi 2}=%.2f$' %(t_ang2-t_dis1),xy=((t_ang2+t_dis1)/2-3.5,-310), annotation_clip=False)


plt.subplots_adjust(hspace=0.60)
plt.subplots_adjust(left=0.07,right=0.97)

plt.savefig('destination_path.eps', format='eps', dpi=1000)
plt.show()