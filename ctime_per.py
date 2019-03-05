import sqlite3
import sys

conn = sqlite3.connect('sparse.db')
total_time = 0.0
tt = 0
curs = conn.cursor()

with conn:
	
	curs.executescript("""
        DROP TABLE IF EXISTS timeper_tab;
        CREATE TABLE timeper_tab(SysName TEXT,Time_per INTEGER);
        """);	
	curs.execute("SELECT * FROM time_tab")
	rows = curs.fetchall()

	for row in rows:
	    total_time = total_time + row[1]
	    
	print "Total Time : %s"%total_time

	curs.execute("SELECT * FROM time_tab")
	rows = curs.fetchall()
	
	for row in rows:
	    var1 = row[1]/total_time
	    var2 = var1*100
	    curs.executescript("""INSERT INTO timeper_tab VALUES('%s','%f');"""%(row[0], var2))
    
	curs.execute("SELECT MAX(Time_per), SysName FROM timeper_tab")
	rows = curs.fetchall()

	for row in rows:
	    print "Maximum %s percentage of time %s System call was called"%(row[0],row[1])
	curs.execute("SELECT MIN(Time_per), SysName FROM timeper_tab")
	rows = curs.fetchall()
	for row in rows:
	    print "Minimum %s percentage of time %s System call was called"%(row[0],row[1])
	
