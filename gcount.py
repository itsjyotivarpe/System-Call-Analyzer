import sys
import sqlite3
import pylab as p

s3=[]
fig = p.figure()
conn = sqlite3.connect('sparse.db')

curs = conn.cursor()
curs1 = conn.cursor()
cnt = 0
bytes = 0
y=[]
group_labels=[]
i=0

with conn:
    curs.execute("select * from count_tab;")
    rows=curs.fetchall()
    
    for row in rows:
		
	i=i+1
	y.append(float(row[1]))
	group_labels.append(str(row[0]))
	#s1 = row[0]
	#s2 = str (row[1])
	#s = s1 + ' : ' + s2 
	#s3.append(str(s))

    N = len(y)
    ind = range(N)

    ax = fig.add_subplot(1,1,1)

    ax.bar(ind, y, facecolor='blue',align='center',ecolor='blue')
	    
    #Create a y label
    ax.set_ylabel('No of times SystemCall Called')
    # Create a title, in italics
    ax.set_title('Graph for No of times SystemCall Called',fontstyle='italic',color='indigo',size='18')
	 
    # This sets the ticks on the x axis to be exactly where we put
    # the center of the bars.
    ax.set_xticks(ind)
    ax.set_xticklabels(group_labels)
    fig.autofmt_xdate(rotation=90)
	    
    # Shink current axis by 20%
    #box = ax.get_position()
    #ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

    # Put a legend to the right of the current axis
	    
    #ax.legend(s3,loc='center left', bbox_to_anchor=(1, 0.5))
    p.savefig('Graphs/countgr.png',facecolor='Lightgrey',edgecolor='Gray')
    #p.show()
