import sqlite3
import sys

total_cnt = 0
var1 = 0.0
var2 = 0.0
conn = sqlite3.connect('sparse.db')

curs = conn.cursor()
curs1 = conn.cursor()
curs2 = conn.cursor()

with conn:

	curs.executescript("""
        DROP TABLE IF EXISTS count_tab;
        CREATE TABLE count_tab(SysName TEXT,Count INTEGER);
        """);

	curs.execute("SELECT SysName, COUNT(SysName) FROM syscall GROUP BY SysName;")
	rows = curs.fetchall()

	for row in rows:
	    curs.executescript("INSERT INTO count_tab VALUES('%s','%s');"%(row[0], row[1]))
	curs.execute("SELECT * FROM count_tab")
	rows = curs.fetchall()

	for row in rows:
	    t = str(row[1])
	    total_cnt = total_cnt + row[1]
	    
	print "Total no. of system calls called : %s"%total_cnt

