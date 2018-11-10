# encoding: utf-8
from pylab import *
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import csv
t_range=78
x = []
y = []
x_ref =[]
y_ref = []
r_dist = []
e_ang = []
r_ang =[]
vx=[0,t_range,-1,15]
vy=[0,t_range,-1,15]
v_ang=[0,t_range,-180,180]

xt =[7.17,7.17]
xdt=[10.9,10.9]
yt =[0 ,5]
yat =[0 ,-180]
time =[]
with open('ControlTriangulo.txt','r') as csvfile:
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

t_ang1=6.49
t_ang2=35.33
t_ang3=56.51
t_dis1=29.08
t_dis2=51.49
t_dis3=73.23
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
plt.subplot(3,1,2)
plt.plot(time,x, label=u'')
plt.plot(time,x_ref, label='',linestyle="--",linewidth= 2.5,color = "green")
plt.legend((u'Posición observada', u'Valor de referencia'),
           shadow=True, loc='upper right', handlelength=1.5, fontsize=10,prop=fontP)
plt.plot([t_ang1,t_ang1],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_ang2,t_ang2],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_ang3,t_ang3],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_dis1,t_dis1],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_dis2,t_dis2],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_dis3,t_dis3],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.xticks([0,t_ang1,t_dis1,t_ang2,t_dis2,t_ang3,t_dis3,t_range],['$0$','$t_{\psi 1}=%.2f$ '%(t_ang1),'$t_{d1}=%.2f$ '%(t_dis1),'                $t_{\psi 2}=%.2f$ '%(t_ang2),'$t_{d2}=%.2f$ ' %(t_dis2) ,'                $t_{\psi 3}=%.2f$ '%(t_ang3),'$t_{d3}=%.2f$ ' %(t_dis3) ,'$%d$' %t_range])

plt.axis(vx)



plt.legend()
plt.xlabel(' \n tiempo ($s$)')
plt.ylabel('x ($m$)')


ann = plt.annotate("$wpx_{ref1}$",
                  xy=(10, 10), xycoords='data',
                  xytext=(8, 13), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )
ann = plt.annotate("$wpx_{ref2}$",
                  xy=(46, 10), xycoords='data',
                  xytext=(42, 13), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate("$wpx_{ref3}$",
                  xy=(61, 0), xycoords='data',
                  xytext=(59, 5), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )
#
plt.annotate('', xy=(t_ang1, -4.5),xytext=(t_dis1,-4.5), arrowprops=dict(arrowstyle='<->',facecolor='red'),annotation_clip=False)  
plt.annotate('$Ts_{wp1}=%.2f$' %(t_dis1-t_ang1),xy=((t_dis1+t_ang1)/2-3,-6.5), annotation_clip=False)

plt.annotate('', xy=(t_ang2, -4.5),xytext=(t_dis2,-4.5), arrowprops=dict(arrowstyle='<->',facecolor='red'),annotation_clip=False)  
plt.annotate('$Ts_{wp2}=%.2f$' %(t_dis2-t_ang2),xy=((t_dis2+t_ang2)/2-3,-6.5), annotation_clip=False)

plt.annotate('', xy=(t_ang3, -4.5),xytext=(t_dis3,-4.5), arrowprops=dict(arrowstyle='<->',facecolor='red'),annotation_clip=False)  
plt.annotate('$Ts_{wp3}=%.2f$' %(t_dis3-t_ang3),xy=((t_dis3+t_ang3)/2-3,-6.5), annotation_clip=False)


#yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
plt.subplot(3,1,3)
plt.plot(time,y, label=u'')
plt.plot(time,y_ref, label='',linestyle="--",linewidth= 2.5,color = "green")
plt.legend((u'Posición observada', u'Valor de referencia'),
           shadow=True, loc='upper right', handlelength=1.5, fontsize=10,prop=fontP)
plt.plot([t_ang1,t_ang1],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_ang2,t_ang2],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_ang3,t_ang3],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_dis1,t_dis1],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_dis2,t_dis2],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_dis3,t_dis3],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.axis(vy)
plt.xticks([0,t_ang1,t_dis1,t_ang2,t_dis2,t_ang3,t_dis3,t_range],['$0$','$t_{\psi 1}=%.2f$ '%(t_ang1),'$t_{d1}=%.2f$ '%(t_dis1),'                $t_{\psi 2}=%.2f$ '%(t_ang2),'$t_{d2}=%.2f$ ' %(t_dis2) ,'                $t_{\psi 3}=%.2f$ '%(t_ang3),'$t_{d3}=%.2f$ ' %(t_dis3) ,'$%d$' %t_range])
plt.legend()
plt.xlabel(' \n tiempo ($s$)')
plt.ylabel('y ($m$)')


ann = plt.annotate("$wpy_{ref1}$",
                  xy=(10, 10), xycoords='data',
                  xytext=(8, 13), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )
ann = plt.annotate("$wpy_{ref2}$",
                  xy=(46, 0), xycoords='data',
                  xytext=(40, 5), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate("$wpy_{ref3}$",
                  xy=(61, 0), xycoords='data',
                  xytext=(59, 5), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

plt.annotate('', xy=(t_ang1, -4.5),xytext=(t_dis1,-4.5), arrowprops=dict(arrowstyle='<->',facecolor='red'),annotation_clip=False)  
plt.annotate('$Ts_{wp1}=%.2f$' %(t_dis1-t_ang1),xy=((t_dis1+t_ang1)/2-4,-6.5), annotation_clip=False)

plt.annotate('', xy=(t_ang2, -4.5),xytext=(t_dis2,-4.5), arrowprops=dict(arrowstyle='<->',facecolor='red'),annotation_clip=False)  
plt.annotate('$Ts_{wp2}=%.2f$' %(t_dis2-t_ang2),xy=((t_dis2+t_ang2)/2-4,-6.5), annotation_clip=False)

plt.annotate('', xy=(t_ang3, -4.5),xytext=(t_dis3,-4.5), arrowprops=dict(arrowstyle='<->',facecolor='red'),annotation_clip=False)  
plt.annotate('$Ts_{wp3}=%.2f$' %(t_dis3-t_ang3),xy=((t_dis3+t_ang3)/2-4,-6.5), annotation_clip=False)

#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

plt.subplot(3,1,1)
plt.plot(time,e_ang, label=u'')
plt.plot(time,r_ang, label=u'',linestyle="--",linewidth= 2.5,color = "green")
plt.legend((u'Ángulo observado', u'Ángulo de referencia'),
           shadow=True, loc='upper right', handlelength=1.5, fontsize=1,prop=fontP)
plt.plot([t_ang1,t_ang1],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_ang2,t_ang2],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_ang3,t_ang3],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_dis1,t_dis1],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_dis2,t_dis2],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_dis3,t_dis3],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.legend()
plt.xlabel('\n tiempo ($s$)')
plt.ylabel(u'$\psi $($^{o}$)')
plt.axis(v_ang)
plt.title('   \n   ')
plt.xticks([0,t_ang1,t_dis1,t_ang2,t_dis2,t_ang3,t_dis3,t_range],['$0$','$t_{\psi 1}=%.2f$ '%(t_ang1),'$t_{d1}=%.2f$ '%(t_dis1),'                $t_{\psi 2}=%.2f$ '%(t_ang2),'$t_{d2}=%.2f$ ' %(t_dis2) ,'                $t_{\psi 3}=%.2f$ '%(t_ang3),'$t_{d3}=%.2f$ ' %(t_dis3) ,'$%d$' %t_range])
plt.yticks(fontsize=8)
ann = plt.annotate("$\psi_{ref1}$",
                  xy=(13, -176), xycoords='data',
                  xytext=(11, 0), textcoords='data',
                  size=20, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate("$\psi_{ref2}$",
                  xy=(45, 44), xycoords='data',
                  xytext=(43, -100), textcoords='data',
                  size=20, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate("$\psi_{ref3}$",
                  xy=(65, -90), xycoords='data',
                  xytext=(58, 50), textcoords='data',
                  size=20, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

plt.annotate('', xy=(0, -260),xytext=(t_ang1,-260), arrowprops=dict(arrowstyle='<->',facecolor='red'),annotation_clip=False)  
plt.annotate('$Ts_{\psi 1}=%.2f$' %(t_ang1),xy=(t_ang1/2-1.5,-310), annotation_clip=False)

plt.annotate('', xy=(t_dis1, -260),xytext=(t_ang2,-260), arrowprops=dict(arrowstyle='<->',facecolor='red'),annotation_clip=False)  
plt.annotate('$Ts_{\psi 2}=%.2f$' %(t_ang2-t_dis1),xy=((t_ang2+t_dis1)/2-1.5,-310), annotation_clip=False)


plt.annotate('', xy=(t_dis2, -260),xytext=(t_ang3,-260), arrowprops=dict(arrowstyle='<->',facecolor='red'),annotation_clip=False)  
plt.annotate('$Ts_{\psi 3}=%.2f$' %(t_ang3-t_dis2),xy=((t_ang3+t_dis2)/2-1.5,-310), annotation_clip=False)
plt.subplots_adjust(hspace=0.60)
plt.subplots_adjust(left=0.07,right=0.97)
plt.savefig('destination_path.eps', format='eps', dpi=1000)
plt.show()