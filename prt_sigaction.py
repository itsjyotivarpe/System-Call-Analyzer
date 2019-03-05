import sqlite3
import sys

action={}
signal1={}
temp={}
string1="SIG_DFL"
string2="SIG_IGN"
string4="-1"


conn = sqlite3.connect('sparse.db')

curs = conn.cursor()

with conn:

	curs.executescript("""
        DROP TABLE IF EXISTS rt_sigaction_tab;
        CREATE TABLE rt_sigaction_tab(SysName TEXT,Time TEXT,Action TEXT,Status TEXT);
        """);
	
	curs.execute("SELECT SysName,arg,StartTime,ret FROM syscall WHERE SysName LIKE 'rt_sigaction';")
	rows = curs.fetchall()
	if(None in rows):
		print " No Syscall called rt_sigaction present!!"
	else:

		for row in rows:
			
			temp=row[1].split("{")
			tmp = temp[0].split(",")
			signal1=tmp[0]
			if(temp[0]=="SIGRTMIN, "):
				action=" Adjusting Real Time min"

			elif(temp[0]=="SIGRT_1, "):
				action="Real Time Signal 1"

			else:
				arg1=temp[1]
				temp1=arg1.split(",")
				print temp1[0]

				if((temp1[0]==string1)):
					action=" Default Action"

				elif((temp1[0]==string2)):
					action=" Ignore Signal"

				else:
					action="Null"

				
		
			if(row[3]==string4):
	
				status="Failed"
			else:
		
				status="Successful"

			
	
			curs.executescript("""	INSERT INTO rt_sigaction_tab VALUES('%s','%s','%s','%s');"""%(signal1,row[2],action,status))

	
	
		
