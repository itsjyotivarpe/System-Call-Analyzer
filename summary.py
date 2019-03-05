import sqlite3
import sys



conn = sqlite3.connect('sparse.db')

curs = conn.cursor()
curs1 = conn.cursor()
curs2 = conn.cursor()
total_time = 0.0
total_time1 = 0.0

tt = 0

with conn:

	
	curs.executescript("""
        DROP TABLE IF EXISTS error_tab;
        CREATE TABLE error_tab(SysName TEXT,Error INTEGER);
        """);
	curs.execute("SELECT SysName, COUNT(SysName) FROM syscall WHERE ret LIKE '-1' GROUP BY SysName;")
	
	rows = curs.fetchall()
	for row in rows:
	    
	    curs.executescript("""INSERT INTO error_tab VALUES('%s','%s');"""%(row[0], row[1]))
	curs.executescript("""
        DROP TABLE IF EXISTS time_tab;
        CREATE TABLE time_tab(SysName TEXT,Time INTEGER);
        """);
	curs.execute("SELECT sum(time), SysName FROM syscall GROUP BY SysName")
	
	rows = curs.fetchall()
	for row in rows:
	    
	    curs.executescript("""INSERT INTO time_tab VALUES('%s','%s');"""%(row[1], row[0]))
	
	curs.executescript("""
        DROP TABLE IF EXISTS summary_tab;
        CREATE TABLE summary_tab(SysName TEXT,Count INTEGER, Error INTEGER, Error_per INTEGER, Time INTEGER, Time_per INTEGER);
        """);
	curs.execute("SELECT sum(time), SysName FROM syscall GROUP BY SysName")
	
	rows = curs.fetchall()
	for row in rows:
	    
	    curs.executescript("""INSERT INTO summary_tab(SysName, Time) VALUES('%s', '%s');"""%(row[1], row[0]))
	
	    
	    
	curs.execute("SELECT * FROM time_tab")
	rows = curs.fetchall()
	for row in rows:
	    t = str(row[1])
	    
	    curs.executescript("""UPDATE summary_tab SET Time='%s' WHERE SysName='%s';"""%(row[1], row[0]))
	    
	    
	    total_time = total_time + row[1]
	    
	
	curs.execute("SELECT * FROM time_tab")
	rows = curs.fetchall()
	
	for row in rows:
	    var1 = row[1]/total_time
	    var2 = var1*100
	    curs.executescript("""UPDATE summary_tab SET Time_per='%s' WHERE SysName='%s';"""%(var2, row[0]))
	    
	curs.execute("SELECT SysName, COUNT(SysName) FROM syscall WHERE ret LIKE '-1' GROUP BY SysName;")
	
	rows = curs.fetchall()
	for row in rows:
	    
	    curs.executescript("""UPDATE summary_tab SET Error='%s' WHERE SysName='%s';"""%(row[1], row[0]))
	curs.execute("SELECT * FROM error_tab")
	rows = curs.fetchall()
	for row in rows:
	    t = str(row[1])
	    
	   
	    
	    total_time1 = total_time1 + row[1]
	    
	
	curs1.execute("SELECT * FROM error_tab")
	rows = curs1.fetchall()
	
	for row in rows:
	    
	    var1 = row[1]/total_time1
	    
	    var2 = var1*100
	    
	    curs.executescript("""UPDATE summary_tab SET Error_per='%s' WHERE SysName='%s';"""%(var2, row[0]))
	curs2.execute("select SysName, COUNT(SysName) from syscall GROUP BY SysName;")
	rows = curs2.fetchall()
	for row in rows:
	    curs.executescript("""UPDATE summary_tab SET Count='%s' WHERE SysName='%s';"""%(row[1], row[0]))

	
	
	
	
