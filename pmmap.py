import sqlite3
import sys

string={}
prot1={}
flag=1
status={}
string1=" PROT_READ|PROT_WRITE"
string2=" PROT_READ"
string3=" PROT_READ|PROT_EXEC"
string4="-1"
countr=0

conn = sqlite3.connect('sparse.db')

curs = conn.cursor()

with conn:

	curs.executescript("""
		DROP TABLE IF EXISTS mmap_tab;
		CREATE TABLE mmap_tab(Time INTEGER,Bytes TEXT,Protection TEXT,Satus TEXT,Mapd_Location TEXT);
		""");

	curs.execute("SELECT Pid,SysName,arg,Error,StartTime,ret FROM syscall WHERE SysName LIKE 'mmap';")
	rows = curs.fetchall()

	for row in rows:
		temp = row[2].split(",")
	        nbytes = temp[1]
		prot=temp[2]
		
		if((temp[2]==string1)):
			prot1="Read - Write Protection"
		elif((temp[2]==string2)):
			prot1="Read Only Protection"
		elif((temp[2]==string3)):
			prot1="Read - Execute Protection"
		
		if(row[5]==string4):
			status="Failed"
		else:
			maploc=row[5]
			status="Successful"

		curs.executescript("INSERT INTO mmap_tab VALUES('%s','%s','%s','%s','%s');"%(row[4],nbytes,prot1,status,maploc))

	'''		
	curs.execute("SELECT * FROM mmap_tab;")
	rows = curs.fetchall()
	print "\n SYSNAME      TIME       LENGTH       PROTECTION                         STATUS           MAPPED LOCATION\n"

	for row in rows:
		print ("\n %s           %s           %s        %s                        %s             %s          " %(row[0],row[1],row[2],row[3],row[4],row[5]))
	'''
