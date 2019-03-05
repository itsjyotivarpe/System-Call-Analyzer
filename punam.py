import sys
import sqlite3

sysname = ''
nodename = ''
release = ''
version = '' 
machine = ''
domainname = ''
name = ''
node = ''

conn = sqlite3.connect('sparse.db')

curs = conn.cursor()
curs1 = conn.cursor()
curs2 = conn.cursor()


with conn:

	curs.executescript("""
		DROP TABLE IF EXISTS uname_tab;
		CREATE TABLE uname_tab(System_Name TEXT ,Node_Name TEXT);
		""");


	
	curs.execute("SELECT arg FROM syscall WHERE SysName = 'uname';")
        rows = curs.fetchall()
	
	for row in rows:
		
		temp = row[0].split("\"")
		#print temp[0]
		#print temp[1]
		#print temp[2]
		#print temp[3]

		name=str(temp[1])
		node=str(temp[3])
		
		#print name
		#print node
	curs.execute("INSERT INTO uname_tab VALUES('%s','%s');"%(name,node))

	curs.execute("SELECT * FROM uname_tab;")
	rows = curs.fetchall()
	print "\n SYSNAME        NODE            \n"
	for row in rows:  
		print ("\n %s          %s              " %(row[0],row[1]))

