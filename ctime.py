import sqlite3
import sys
tt = 0.0



conn = sqlite3.connect('sparse.db')

curs = conn.cursor()

with conn:

	curs.executescript("""
        DROP TABLE IF EXISTS time_tab;
        CREATE TABLE time_tab(SysName TEXT,Time INTEGER);
        """);

	curs.execute("SELECT sum(time), SysName FROM syscall GROUP BY sysname")
	rows = curs.fetchall()

	for row in rows:
	    curs.executescript("""INSERT INTO time_tab VALUES('%s','%s');"""%(row[1], row[0]))
    
	curs.execute("SELECT MAX(Time), SysName FROM time_tab")
	rows = curs.fetchall()

	for row in rows:
	    print "Maximum Time %s usec was consumed by %s system call"%((row[0]),(row[1]))
	
	curs.execute("SELECT MIN(Time), SysName FROM time_tab")
	rows = curs.fetchall()

	for row in rows:
	    print "Minimum Time %s usec was consumed by %s system call"%((row[0]),(row[1]))
	
	curs.execute("SELECT * from time_tab;")
	rows = curs.fetchall()
	for row in rows:
	    tt = tt + row[1]
	    
	print "Total Time : %s "%tt

