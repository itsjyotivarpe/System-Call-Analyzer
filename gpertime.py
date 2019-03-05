from pylab import *
import matplotlib.pyplot as plt
import sqlite3
import numpy as np
from matplotlib import font_manager as fm
params = {'legend.fontsize':10,'legend.linwidth':1}
plt.rcParams.update(params)
s3=[]
fracs=[]
conn = sqlite3.connect('sparse.db')
curs = conn.cursor()

curs.execute("select * from timeper_tab;")
rows = curs.fetchall()

#fracs = [row[1] for row in rows]
labels = [row[0] for row in rows]


for row in rows:
	no=row[1]
	if no<1:
		no=no+15
		fracs.append(float(no))	
	else:
		fracs.append(float(no))	

	s1 = row[0]
	s2 = str (row[1])
	s = s1 + ' : ' + s2 + ' % '
	s3.append(str(s))
fig = plt.gcf()
fig.set_size_inches(12,6)
	
fig=plt.pie(fracs)
for p1, l1 in zip(fig[0], labels):
    r = p1.r
    dr = r*0.1
    t1, t2 = p1.theta1, p1.theta2
    theta = (t1+t2)/2.

    xc, yc = r/2.*cos(theta/180.*pi), r/2.*sin(theta/180.*pi)
    x1, y1 = (r+dr)*cos(theta/180.*pi), (r+dr)*sin(theta/180.*pi)
    if x1 > 0 :
        x1 = r+2*dr
        ha, va = "center", "center"
        tt = -180
        cstyle="angle,angleA=0,angleB=%f"%(theta,)
    else:
        x1 = -(r+2*dr)
        ha, va = "center", "center"
        tt = 0
        cstyle="angle,angleA=0,angleB=%f"%(theta,)

    annotate(l1,
             (xc, yc), xycoords="data",
             xytext=(x1, y1), textcoords="data", ha=ha, va=va,
             arrowprops=dict(arrowstyle="-", connectionstyle=cstyle, patchB=p1))

ax = plt.subplot(111)
ax.set_title('Percentage Time Taken by Each System Call In Microsecond',fontstyle='italic',color='indigo',size='21')
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.80, box.height])


ax.legend(s3,loc='center left', bbox_to_anchor=(1.1, 0.5))
plt.savefig('Graphs/pertimegr.png',facecolor='Lightgrey',edgecolor='Gray')	
#plt.show()
