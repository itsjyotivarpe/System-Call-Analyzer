import sqlite3
import sys


child_pid={}
status={}
string1=" O_CLOEXEC"
string2=" O_NONBLOCK"
string3="CLD_DUMPED"
string4="-1"
string5="CLD_CONTINUED"
strings="pipe2"
rd={}
wr={}

code={}

conn = sqlite3.connect('sparse.db')

curs = conn.cursor()


with conn:

	curs.executescript("""
        DROP TABLE IF EXISTS pipe_tab;
        CREATE TABLE pipe_tab(SysName TEXT,Time TEXT,Read_End TEXT,Write_End TEXT,Status TEXT,Flag TEXT,Description TEXT);
        """);
	
	
	curs.execute("SELECT SysName,arg,StartTime,ret FROM syscall WHERE SysName LIKE 'pipe' OR SysName LIKE 'pipe2';")
	rows = curs.fetchall()
	cnt=1
	for row in rows:
		
		temp1= row[1].split("[")
		
		temp11= temp1[1].split(",")

		rd=temp11[0]
		
		temp12= temp11[1].split("]")

		temp13= temp12[0].split(" ")
		
		wr=temp13[1]
		
		if (row[0]== strings):
			flag=temp11[2]
			
			if(flag==string1):
				Flag="  O_CLOEXEC"
				desc="Avoids additonal operations  to set the FD_CLOEXEC  flags"
			else:
				Flag=" O_NONBLOCK "
				desc="  Saves extra call to fcntl system call"
		else:
			flag="null"

		if( rd== '0'):
			read= "Stdin"
		elif(rd=='1'):
			read= "Stdout"
		elif(rd=='2'):
			read= "Stderr"
		else:
			read= "Application File.Check open Statistics"
			
		if( wr== '0'):
			write= "Stdin"
		elif(wr=='1'):
			write= "Stdout"
		elif(wr=='2'):
			write= "Stderr"
		else:
			write= "Application File.Check Open Statistics"

		if(row[3]== string4):
			status="Failed"
		else:
			status="Successful"
		
		curs.executescript("INSERT INTO pipe_tab VALUES('%s','%s','%s','%s','%s','%s','%s');"%(row[0],row[2],read,write,status,Flag,desc))
	
	
