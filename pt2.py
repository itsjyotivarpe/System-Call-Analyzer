import sqlite3
import sys

countr=0

conn = sqlite3.connect('sparse.db')

curs = conn.cursor()
curs1 = conn.cursor()



with conn:

	
	curs.executescript("""
        DROP TABLE IF EXISTS proctree;
        CREATE TABLE proctree(Parent TEXT,Child TEXT);
        """);

	curs.executescript("""
        DROP TABLE IF EXISTS temp1;
        CREATE TABLE temp1(Parent TEXT,Child TEXT);
        """);

	curs.execute("SELECT Pid,SysName,ret FROM syscall;")
	rows = curs.fetchall()
	for row in rows:
		if(row[1]=='execve'):
			#print "execve"
			curs.executescript("""INSERT INTO proctree VALUES('%s','%s');"""%(row[0], 'NULL'))
			
		if(row[1]=='clone'):
			#print "clone"
			pid= str (row[0])
			retval= str (row[2])
			#print pid
			#print retval
			curs.execute("SELECT Parent,Child FROM proctree;")
			rows=curs.fetchall()
			for row in rows:
				
				if(row[0]==pid):
					pid2=row[0]
					curs1.execute("SELECT * FROM temp1 WHERE Parent ='%s' ;"%(pid))
					rows=curs1.fetchone()
					print rows
					if(rows==None):
						curs.executescript("""INSERT INTO temp1 VALUES('%s','%s');"""%(row[0], retval))
			

					#for row in rows:
					

	curs.execute("SELECT * FROM temp1")
	rows = curs.fetchall()
	print('\nParent       Child\n')
	for row in rows:
	    print str(row[0])+"     "+str(row[1])

	    
	
