# encoding: utf-8
from pylab import *
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import csv
t_range=101
x = []
y = []
x_ref =[]
y_ref = []
r_dist = []
e_ang = []
r_ang =[]
vx=[0,t_range,-1,4]
vy=[0,t_range,-1,10]
v_ang=[0,t_range,0,180]

xt =[7.17,7.17]
xdt=[10.9,10.9]
yt =[0 ,5]
yat =[0 ,-180]
time =[]
with open('expRRT.txt','r') as csvfile:
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
fontP.set_size(9)   

t_ang1=2.86
t_ang2=16.33
t_ang3=27.36
t_ang4=35.44
t_ang5=50.95
t_ang6=56.83
t_ang7=70.42
t_ang8=82.33
t_ang9=91.01

t_obs=19.8

t_dis1=6.71
t_dis2=19.91
t_dis3=39.16
t_dis4=59.6
t_dis5=72.8
t_dis6=85.6
t_dis7=94.8

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
plt.subplot(3,1,2)
plt.plot(time,x, label=u'')
plt.plot(time,x_ref, label='',linestyle="--",linewidth= 2.5,color = "green")
plt.legend((u'Posición observada', u'Valor de referencia'),
           shadow=True, loc='upper right', handlelength=1.5, fontsize=10,prop=fontP)
plt.plot([t_ang1,t_ang1],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang2,t_ang2],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang3,t_ang3],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang4,t_ang4],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang5,t_ang5],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang6,t_ang6],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang7,t_ang7],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang8,t_ang8],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang9,t_ang9],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)


plt.plot([t_dis1,t_dis1],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")
plt.plot([t_dis2,t_dis2],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")
plt.plot([t_dis3,t_dis3],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")
plt.plot([t_dis4,t_dis4],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")
plt.plot([t_dis5,t_dis5],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")
plt.plot([t_dis6,t_dis6],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")
plt.plot([t_dis7,t_dis7],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")

plt.xticks([t_dis1,t_dis2,t_dis3,t_dis4,t_dis5,t_dis6,t_dis7],
  ['$t_{d1}=%.2f$' %t_dis1,
  '$t_{d2}=%.2f$' %t_dis2,
  '$t_{d3}=%.2f$' %t_dis3,
  '$t_{d4}=%.2f$' %t_dis4,
  '$t_{d5}=%.2f$' %t_dis5,
  '$t_{d6}=%.2f$' %t_dis6,
  '$t_{d7}=%.2f$' %t_dis7])
plt.xticks(fontsize=10)
plt.axis(vx)



plt.legend()
plt.xlabel(' \n tiempo ($s$)')
plt.ylabel('x ($m$)')


ann = plt.annotate("$wpx_{ref1}$",
                  xy=(12, 0), xycoords='data',
                  xytext=(10, 2), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )
ann = plt.annotate("$wpx_{ref2}$",
                  xy=(24, 0), xycoords='data',
                  xytext=(22, 2), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate("$wpx_{ref3}$",
                  xy=(42, 1.5), xycoords='data',
                  xytext=(40, 3), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate("$wpx_{ref4}$",
                  xy=(64, 2.7), xycoords='data',
                  xytext=(62, 1.2), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )
ann = plt.annotate("$wpx_{ref5}$",
                  xy=(77, 1.65), xycoords='data',
                  xytext=(75, 3.1), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate("$wpx_{ref6}$",
                  xy=(90, 0.56), xycoords='data',
                  xytext=(88, -0.5), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )
ann = plt.annotate("$wpx_{ref7}$",
                  xy=(99, 0), xycoords='data',
                  xytext=(97, 1), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )
#


#yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
plt.subplot(3,1,3)
plt.plot(time,y, label=u'')
plt.plot(time,y_ref, label='',linestyle="--",linewidth= 2.5,color = "green")
plt.legend((u'Posición observada', u'Valor de referencia'),
           shadow=True, loc='lower right', handlelength=1.5, fontsize=10,prop=fontP)
plt.plot([t_ang1,t_ang1],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang2,t_ang2],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang3,t_ang3],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang4,t_ang4],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang5,t_ang5],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang6,t_ang6],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang7,t_ang7],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang8,t_ang8],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang9,t_ang9],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)

plt.plot([t_dis1,t_dis1],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")
plt.plot([t_dis2,t_dis2],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")
plt.plot([t_dis3,t_dis3],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")
plt.plot([t_dis4,t_dis4],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")
plt.plot([t_dis5,t_dis5],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")
plt.plot([t_dis6,t_dis6],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")
plt.plot([t_dis7,t_dis7],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")

plt.axis(vy)
plt.legend()
plt.xlabel(' \n tiempo ($s$)')
plt.ylabel('y ($m$)')
plt.xticks([t_dis1,t_dis2,t_dis3,t_dis4,t_dis5,t_dis6,t_dis7],
  ['$t_{d1}=%.2f$' %t_dis1,
  '$t_{d2}=%.2f$' %t_dis2,
  '$t_{d3}=%.2f$' %t_dis3,
  '$t_{d4}=%.2f$' %t_dis4,
  '$t_{d5}=%.2f$' %t_dis5,
  '$t_{d6}=%.2f$' %t_dis6,
  '$t_{d7}=%.2f$' %t_dis7])
plt.xticks(fontsize=10)

#plt.xticks([0,t_ang1,t_dis1,t_ang2,t_dis2,t_ang3,t_dis3,t_ang4,t_dis4,t_range],['$0$','$t_{\psi 1}=%.2f$ '%(t_ang1),'$t_{d1}=%.2f$ '%(t_dis1),'                $t_{\psi 2}=%.2f$ '%(t_ang2),'$t_{d2}=%.2f$ ' %(t_dis2) ,'                $t_{\psi 3}=%.2f$ '%(t_ang3),'$t_{d3}=%.2f$ ' %(t_dis3) , '                $t_{\psi 4}=%.2f$ '%(t_ang4),'$t_{d4}=%.2f$ ' %(t_dis4) ,'$%d$' %t_range])

ann = plt.annotate("$wpy_{ref1}$",
                  xy=(12, 2), xycoords='data',
                  xytext=(10, 5), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )
ann = plt.annotate("$wpy_{ref2}$",
                  xy=(24, 3.5), xycoords='data',
                  xytext=(22, 6.5), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate("$wpy_{ref3}$",
                  xy=(42, 4.1), xycoords='data',
                  xytext=(40, 7.1), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate("$wpy_{ref4}$",
                  xy=(64, 5), xycoords='data',
                  xytext=(62, 2), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )
ann = plt.annotate("$wpy_{ref5}$",
                  xy=(77, 6), xycoords='data',
                  xytext=(75, 3), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate("$wpy_{ref6}$",
                  xy=(90, 7.2), xycoords='data',
                  xytext=(88, 4.2), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )
ann = plt.annotate("$wpy_{ref7}$",
                  xy=(99, 7.9), xycoords='data',
                  xytext=(97, 5), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )
#



#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

plt.subplot(3,1,1)
plt.plot(time,e_ang, label=u'')
plt.plot(time,r_ang, label=u'',linestyle="--",linewidth= 2.5,color = "green")
plt.legend((u'Ángulo observado', u'Ángulo de referencia'),
           shadow=True, loc='lower right', handlelength=1.5, fontsize=1,prop=fontP)
plt.plot([t_ang1,t_ang1],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_ang2,t_ang2],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_ang3,t_ang3],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_ang4,t_ang4],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_ang5,t_ang5],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_ang6,t_ang6],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_ang7,t_ang7],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_ang8,t_ang8],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_ang9,t_ang9],[-180,180],color = "red", linewidth= 1.0, linestyle="--")

plt.plot([t_dis1,t_dis1],[-180,180],color = "blue", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_dis2,t_dis2],[-180,180],color = "blue", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_dis3,t_dis3],[-180,180],color = "blue", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_dis4,t_dis4],[-180,180],color = "blue", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_dis5,t_dis5],[-180,180],color = "blue", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_dis6,t_dis6],[-180,180],color = "blue", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_dis7,t_dis7],[-180,180],color = "blue", linewidth= 1.0, linestyle="--", alpha=0.4)


plt.legend()
plt.xlabel('\n tiempo ($s$)')
plt.ylabel(u'$\psi $($^{o}$)')
plt.axis(v_ang)
plt.title('   \n   ')
plt.xticks([t_ang1,t_ang2,t_ang3,t_ang4,t_ang5,t_ang6,t_ang7,t_ang8,t_ang9,t_range],['$t_{\psi 1}=%.2f$ '%(t_ang1),r'$t_{\alpha_1}=%.2f$'%(t_ang2),r'$t_{\alpha_2}=%.2f$ '%(t_ang3),'              $t_{\psi 2}=%.2f$ '%(t_ang4),r'$t_{\alpha_3}=%.2f$          '%(t_ang5),'             $t_{\psi 3}=%.2f$ '%(t_ang6),'$t_{\psi 4}=%.2f$ '%(t_ang7),'$t_{\psi 5}=%.2f$ '%(t_ang8),'$t_{\psi 6}=%.2f$ '%(t_ang9),'$%d$' %t_range])
##plt.yticks(fontsize=8)
plt.xticks(fontsize=10)



ann = plt.annotate("$\psi_{ref1}$",
                  xy=(12, 86), xycoords='data',
                  xytext=(10, 136), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )
ann = plt.annotate(r"$\alpha_{1}$",
                  xy=(24, 96), xycoords='data',
                  xytext=(22, 146), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate(r"$\alpha_{2}$",
                  xy=(29.64, 78.75), xycoords='data',
                  xytext=(27, 28.75), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate("$\psi_{re2}$",
                  xy=(42, 124), xycoords='data',
                  xytext=(40, 74), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )
ann = plt.annotate(r"$\alpha_{3}$",
                  xy=(52, 12), xycoords='data',
                  xytext=(50, 100), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate("$\psi_{ref3}$",
                  xy=(64, 108), xycoords='data',
                  xytext=(62, 58), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )
ann = plt.annotate("$\psi_{ref4}$",
                  xy=(76, 31), xycoords='data',
                  xytext=(74, 81), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate("$\psi_{ref5}$",
                  xy=(88, 135), xycoords='data',
                  xytext=(86, 85), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate("$\psi_{ref6}$",
                  xy=(99, 135), xycoords='data',
                  xytext=(97, 85), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )



plt.subplots_adjust(hspace=0.60)
plt.subplots_adjust(left=0.07,right=0.97)
plt.savefig('destination_path.eps', format='eps', dpi=1000)
plt.show()