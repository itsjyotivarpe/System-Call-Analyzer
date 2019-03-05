import sqlite3
import sys

total_time = 0.0
var1 = 0.0
var2 = 0.0
conn = sqlite3.connect('sparse.db')

curs = conn.cursor()

with conn:

	curs.executescript("""
        DROP TABLE IF EXISTS errorper_tab;
        CREATE TABLE errorper_tab(SysName TEXT,Error_per INTEGER);
        """);

	curs.execute("SELECT * FROM error_tab")
	rows = curs.fetchall()

	for row in rows:
	    total_time = total_time + row[1]
	    
	curs.execute("SELECT * FROM error_tab")
	rows = curs.fetchall()
	
	for row in rows:
	    var1 = row[1]/total_time
	    var2 = var1*100
	    curs.executescript("""INSERT INTO errorper_tab VALUES('%s','%f');"""%(row[0], var2))
	curs.execute("SELECT MAX(Error_per), SysName FROM errorper_tab")
	rows = curs.fetchall()

	for row in rows:
	    print "Maximum %s percentage of errors was occured in %s System call"%(row[0],row[1])
	curs.execute("SELECT MIN(Error_per), SysName FROM errorper_tab")
	rows = curs.fetchall()
	for row in rows:
	    print "Minimum %s percentage of errors was occured in %s System call"%(row[0],row[1])
	
	
	
	
	
	
	
	
	
	
	
	
