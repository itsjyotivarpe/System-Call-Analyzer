import sqlite3
import sys

string={}
prot1={}
flag=1
status={}
string1=" R_OK"
string2=" X_OK"
string3=" W_OK"
string4="-1"

countr=0

conn = sqlite3.connect('sparse.db')

curs1 = conn.cursor()
curs = conn.cursor()

with conn:

	curs1.executescript("""
		DROP TABLE IF EXISTS access_tab;
		CREATE TABLE access_tab(Time TEXT,Path TEXT,Permission TEXT,Status TEXT);
		""");

	curs.execute("SELECT SysName,arg,StartTime,ret FROM syscall WHERE SysName LIKE 'access';")
	rows = curs.fetchall()

	for row in rows:		
		temp = row[1].split(",")
	        path1 = temp[0]
		'''
		if("/lib"in path1):
			print "library"
			Line="
		''' 
		permission1 =temp[1]
				
		if((temp[1]==string1)):
			prot1="Read"
			
		elif((temp[1]==string2)):
			prot1="Execute"
			
		elif((temp[1]==string3)):
			prot1="Write"
			
		if(row[3]==string4):
			status="Failed"
		else:
			status="Successful"

		curs1.executescript("INSERT INTO access_tab VALUES('%s','%s','%s','%s');"%(row[2],path1,prot1,status))
