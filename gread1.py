import sys
import sqlite3
import pylab as p

fig = p.figure()

conn = sqlite3.connect('sparse.db')
curs = conn.cursor()
cnt = 0
bytes = 0
y=[]
group_labels=[]
i=0

with conn:
    curs.execute("select * from read_tab;")
    rows=curs.fetchall()
    for row in rows:
	i=i+1
	section = i
	
	y.append(float(row[1]))
	group_labels.append(i)
	    

    N = len(y)
    ind = range(N)
    ax = fig.add_subplot(1,1,1)
    ax.bar(ind, y, facecolor='cyan',align='center',ecolor='cyan')
	    
	    
	   
    #Create a y label
    ax.set_ylabel('No of Byte read')
    ax.set_xlabel('Calls')
    # Create a title, in italics
    ax.set_title('Analysis of No.of Byte read by Each read System Call',fontstyle='oblique',color='indigo',size='18')
       
    ax.set_xticks(ind)
    ax.set_xticklabels(group_labels)
    #fig.autofmt_xdate()
	    
    p.savefig('Graphs/readgr.png',facecolor='Lightgrey',edgecolor='Gray')
   # p.show()
	
