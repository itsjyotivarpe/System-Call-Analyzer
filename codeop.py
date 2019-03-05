import sqlite3
import sys



conn = sqlite3.connect('sparse1.db')
total_time = 0.0
tt = 0
curs = conn.cursor()

with conn:

	curs.executescript("""
        DROP TABLE IF EXISTS time_tab;
        CREATE TABLE time_tab(SysName TEXT,Time INTEGER);
        """);
	curs.executescript("""
        DROP TABLE IF EXISTS timeper_tab;
        CREATE TABLE timeper_tab(SysName TEXT,Time_per INTEGER);
        """);
	
	curs.execute("SELECT sum(time), SysName FROM syscall GROUP BY SysName")
	rows = curs.fetchall()
	for row in rows:

	    curs.executescript("""INSERT INTO time_tab VALUES('%s','%f');"""%(row[1], row[0]))
	curs.execute("SELECT * FROM time_tab")
	print "System call           Time"
	rows = curs.fetchall()
	for row in rows:
	    t = str(row[1])
	    print str(row[0])+" :          "+t
	   
	    
	    total_time = total_time + row[1]
	    
	print "Total Time : %s"%total_time
	
	
