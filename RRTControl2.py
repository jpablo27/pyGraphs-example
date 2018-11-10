# encoding: utf-8
from pylab import *
from matplotlib.font_manager import FontProperties
import matplotlib.pyplot as plt
import csv
t_range=92
x = []
y = []
x_ref =[]
y_ref = []
r_dist = []
e_ang = []
r_ang =[]
vx=[0,t_range,-3,1]
vy=[0,t_range,-1,20]
v_ang=[0,t_range,20,180]

xt =[7.17,7.17]
xdt=[10.9,10.9]
yt =[0 ,5]
yat =[0 ,-180]
time =[]
with open('expRRT2.txt','r') as csvfile:
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

t_ang1=0
t_ang2=7.46
t_ang3=15.66
t_ang4=23.97
t_ang5=35.58
t_ang6=41.88
t_ang7=55.21
t_ang8=64.97
t_ang9=75.6
t_ang10=84.11
t_ang11=49.7
t_ang12=30.2


t_dis1=2.75
t_dis2=10.9
t_dis3=19.33
t_dis4=27.7
t_dis5=46.7
t_dis6=58.6
t_dis7=68.15
t_dis8=79.36
t_dis9=87.82

#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
plt.subplot(3,1,2)
plt.plot(time,x, label=u'')
plt.plot(time,x_ref, label='',linestyle="--",linewidth= 2.5,color = "green")
plt.legend((u'Posición observada', u'Valor de referencia'),
           shadow=True, loc='lower right', handlelength=1.5, fontsize=10,prop=fontP)
plt.plot([t_ang1,t_ang1],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang2,t_ang2],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang3,t_ang3],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang5,t_ang5],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang6,t_ang6],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang7,t_ang7],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang8,t_ang8],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang9,t_ang9],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang10,t_ang10],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang11,t_ang11],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang12,t_ang12],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)



plt.plot([t_dis1,t_dis1],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")
plt.plot([t_dis2,t_dis2],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")
plt.plot([t_dis3,t_dis3],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")
plt.plot([t_dis4,t_dis4],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")
plt.plot([t_dis5,t_dis5],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")
plt.plot([t_dis6,t_dis6],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")
plt.plot([t_dis7,t_dis7],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")
plt.plot([t_dis8,t_dis8],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")
plt.plot([t_dis9,t_dis9],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")


plt.xticks([t_dis1,t_dis2,t_dis3,t_dis4,t_dis5,t_dis6,t_dis7,t_dis8,t_dis9],
  ['$t_{d1}=%.2f$' %t_dis1,
  '$t_{d2}$''$=%.2f$' %t_dis2,
  '$t_{d3}=%.2f$' %t_dis3,
  '$t_{d4}=%.2f$' %t_dis4,
  '$t_{d5}=%.2f$' %t_dis5,
  '$t_{d6}=%.2f$' %t_dis6,
  '$t_{d7}=%.2f$' %t_dis7,
  '$t_{d7}=%.2f$' %t_dis8,
  '$t_{d7}=%.2f$' %t_dis9])
plt.xticks(fontsize=10)
plt.axis(vx)



plt.legend()
plt.xlabel(' \n tiempo ($s$)')
plt.ylabel('x ($m$)')




ann = plt.annotate("$wpx_{ref1}$",
                  xy=(6, 0), xycoords='data',
                  xytext=(4, -1.5), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )
ann = plt.annotate("$wpx_{ref2}$",
                  xy=(14, 0), xycoords='data',
                  xytext=(12, -1.5), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate("$wpx_{ref3}$",
                  xy=(22, 0), xycoords='data',
                  xytext=(20, -1.5), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate("$wpx_{ref4}$",
                  xy=(31, 0), xycoords='data',
                  xytext=(29, -1.5), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )


ann = plt.annotate("$wpx_{ref5}$",
                  xy=(53, -2), xycoords='data',
                  xytext=(51, 0), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )
ann = plt.annotate("$wpx_{ref6}$",
                  xy=(61, -1), xycoords='data',
                  xytext=(59, 0), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate("$wpx_{ref7}$",
                  xy=(71, 0), xycoords='data',
                  xytext=(69, -2), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate("$wpx_{ref8}$",
                  xy=(82, 0), xycoords='data',
                  xytext=(80, -1), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )


ann = plt.annotate("$wpx_{ref9}$",
                  xy=(89, 0), xycoords='data',
                  xytext=(87, -1), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=0.2",
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
plt.plot([t_ang5,t_ang5],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang6,t_ang6],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang7,t_ang7],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang8,t_ang8],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang9,t_ang9],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang10,t_ang10],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang11,t_ang11],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_ang12,t_ang12],[-180,180],color = "red", linewidth= 1.0, linestyle="--", alpha=0.4)



plt.plot([t_dis1,t_dis1],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")
plt.plot([t_dis2,t_dis2],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")
plt.plot([t_dis3,t_dis3],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")
plt.plot([t_dis4,t_dis4],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")
plt.plot([t_dis5,t_dis5],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")
plt.plot([t_dis6,t_dis6],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")
plt.plot([t_dis7,t_dis7],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")
plt.plot([t_dis8,t_dis8],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")
plt.plot([t_dis9,t_dis9],[-180,180],color = "blue", linewidth= 1.0, linestyle="--")
plt.axis(vy)
plt.legend()
plt.xlabel(' \n tiempo ($s$)')
plt.ylabel('y ($m$)')
plt.xticks([t_dis1,t_dis2,t_dis3,t_dis4,t_dis5,t_dis6,t_dis7,t_dis8,t_dis9],
  ['$t_{d1}=%.2f$' %t_dis1,
  '$t_{d2}$''$=%.2f$' %t_dis2,
  '$t_{d3}=%.2f$' %t_dis3,
  '$t_{d4}=%.2f$' %t_dis4,
  '$t_{d5}=%.2f$' %t_dis5,
  '$t_{d6}=%.2f$' %t_dis6,
  '$t_{d7}=%.2f$' %t_dis7,
  '$t_{d7}=%.2f$' %t_dis8,
  '$t_{d7}=%.2f$' %t_dis9])
plt.xticks(fontsize=10)

#plt.xticks([0,t_ang1,t_dis1,t_ang2,t_dis2,t_ang3,t_dis3,t_ang4,t_dis4,t_range],['$0$','$t_{\psi 1}=%.2f$ '%(t_ang1),'$t_{d1}=%.2f$ '%(t_dis1),'                $t_{\psi 2}=%.2f$ '%(t_ang2),'$t_{d2}=%.2f$ ' %(t_dis2) ,'                $t_{\psi 3}=%.2f$ '%(t_ang3),'$t_{d3}=%.2f$ ' %(t_dis3) , '                $t_{\psi 4}=%.2f$ '%(t_ang4),'$t_{d4}=%.2f$ ' %(t_dis4) ,'$%d$' %t_range])




ann = plt.annotate("$wpy_{ref1}$",
                  xy=(6, 2), xycoords='data',
                  xytext=(4, 10), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )
ann = plt.annotate("$wpy_{ref2}$",
                  xy=(14, 3.8), xycoords='data',
                  xytext=(12, 12), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate("$wpy_{ref3}$",
                  xy=(22, 5.93), xycoords='data',
                  xytext=(20, 12), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate("$wpy_{ref4}$",
                  xy=(31, 7.6), xycoords='data',
                  xytext=(29, 14), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )


ann = plt.annotate("$wpy_{ref5}$",
                  xy=(50.51, 8), xycoords='data',
                  xytext=(48, 15), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )
ann = plt.annotate("$wpy_{ref6}$",
                  xy=(61, 10.6), xycoords='data',
                  xytext=(59, 16), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate("$wpy_{ref7}$",
                  xy=(71, 11.7), xycoords='data',
                  xytext=(69, 16), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate("$wpy_{ref8}$",
                  xy=(82, 13.6), xycoords='data',
                  xytext=(80, 18), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )


ann = plt.annotate("$wpy_{ref9}$",
                  xy=(89, 15.85), xycoords='data',
                  xytext=(87, 10), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )



#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

plt.subplot(3,1,1)
plt.plot(time,e_ang, label=u'')
plt.plot(time,r_ang, label=u'',linestyle="--",linewidth= 2.5,color = "green")
plt.legend((u'Ángulo observado', u'Ángulo de referencia'),
           shadow=True, loc='upper right', handlelength=1.5, fontsize=1,prop=fontP)
plt.plot([t_ang1,t_ang1],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_ang2,t_ang2],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_ang3,t_ang3],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_ang5,t_ang5],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_ang6,t_ang6],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_ang7,t_ang7],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_ang8,t_ang8],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_ang9,t_ang9],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_ang10,t_ang10],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_ang11,t_ang11],[-180,180],color = "red", linewidth= 1.0, linestyle="--")
plt.plot([t_ang12,t_ang12],[-180,180],color = "red", linewidth= 1.0, linestyle="--")


plt.plot([t_dis1,t_dis1],[-180,180],color = "blue", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_dis2,t_dis2],[-180,180],color = "blue", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_dis3,t_dis3],[-180,180],color = "blue", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_dis4,t_dis4],[-180,180],color = "blue", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_dis5,t_dis5],[-180,180],color = "blue", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_dis6,t_dis6],[-180,180],color = "blue", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_dis7,t_dis7],[-180,180],color = "blue", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_dis8,t_dis8],[-180,180],color = "blue", linewidth= 1.0, linestyle="--", alpha=0.4)
plt.plot([t_dis9,t_dis9],[-180,180],color = "blue", linewidth= 1.0, linestyle="--", alpha=0.4)


plt.legend()
plt.xlabel('\n tiempo ($s$)')
plt.ylabel(u'$\psi $($^{o}$)')
plt.axis(v_ang)
plt.title('   \n   ')
plt.xticks([t_ang1,t_ang2,t_ang3,t_ang12,t_ang5,t_ang6,t_ang11,t_ang7,t_ang8,t_ang9,t_ang10,t_range],['$t_{\psi 1}=%.2f$ '%(t_ang1),r'$t_{\psi 2}=%.2f$'%(t_ang2),r'$t_{\psi 3}=%.2f$ '%(t_ang3),r'$t_{\alpha 1}=%.2f$              '%(t_ang12),r'$t_{\alpha 2}=%.2f$'%(t_ang5),r'$t_{\psi 4}=%.2f$ '%(t_ang6),r'$t_{\alpha 3}=%.2f$ '%(t_ang11),r'        $t_{\psi 5}=%.2f$ '%(t_ang7),'$t_{\psi 6}=%.2f$ '%(t_ang8),'$t_{\psi 7}=%.2f$ '%(t_ang9),'$t_{\psi 8}=%.2f$'%(t_ang10),'$%d$' %t_range])
##plt.yticks(fontsize=8)
plt.xticks(fontsize=10)



ann = plt.annotate("$\psi_{ref1}$",
                  xy=(6, 86), xycoords='data',
                  xytext=(4, 136), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )
ann = plt.annotate("$\psi_{ref2}$",
                  xy=(14, 86), xycoords='data',
                  xytext=(12, 136), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate("$\psi_{ref3}$",
                  xy=(22, 86), xycoords='data',
                  xytext=(20, 136), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate(r"$\alpha_{1}$",
                  xy=(31, 86), xycoords='data',
                  xytext=(29, 136), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )


ann = plt.annotate(r"$\alpha_{2}$",
                  xy=(36, 50), xycoords='data',
                  xytext=(34, 136), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )


ann = plt.annotate("$\psi_{ref4}$",
                  xy=(40, 140), xycoords='data',
                  xytext=(42, 70), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate(r"$\alpha_{3}$",
                  xy=(50.51, 140), xycoords='data',
                  xytext=(48, 70), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )
ann = plt.annotate("$\psi_{ref5}$",
                  xy=(61, 75), xycoords='data',
                  xytext=(59, 125), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate("$\psi_{ref6}$",
                  xy=(71, 50), xycoords='data',
                  xytext=(69, 100), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=-0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )

ann = plt.annotate("$\psi_{ref7}$",
                  xy=(82, 87), xycoords='data',
                  xytext=(80, 37), textcoords='data',
                  size=15, va="center", ha="center",
                  arrowprops=dict(arrowstyle="-|>",
                                  connectionstyle="arc3,rad=0.2",
                                  relpos=(0., 0.),
                                  fc="w"), 
                  )


ann = plt.annotate("$\psi_{ref8}$",
                  xy=(89, 87), xycoords='data',
                  xytext=(87, 37), textcoords='data',
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