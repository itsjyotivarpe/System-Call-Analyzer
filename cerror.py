import sqlite3
import sys
tt = 0


conn = sqlite3.connect('sparse.db')

curs = conn.cursor()

with conn:

	curs.executescript("""
        DROP TABLE IF EXISTS error_tab;
        CREATE TABLE error_tab(SysName TEXT,Error INTEGER);
        """);

	curs.execute("SELECT SysName, COUNT(SysName) FROM syscall WHERE ret LIKE '-1' GROUP BY SysName;")
	rows = curs.fetchall()

	for row in rows:
	    curs.executescript("""INSERT INTO error_tab VALUES('%s','%s');"""%(row[0], row[1]))
	curs.execute("SELECT MAX(Error), SysName FROM error_tab")
	rows = curs.fetchall()

	for row in rows:
	    print "Maximum Errors %s was occured in %s system call"%((row[0]),(row[1]))
	
	curs.execute("SELECT MIN(Error), SysName FROM error_tab")
	rows = curs.fetchall()

	for row in rows:
	    print "Minimum Errors %s was occured in %s system call"%((row[0]),(row[1]))
	
	curs.execute("SELECT * from error_tab;")
	rows = curs.fetchall()
	for row in rows:
	    tt = tt + row[1]
	    
	print "Total Errors : %s "%tt

