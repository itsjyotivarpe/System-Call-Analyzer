import sqlite3
import sys


child_pid={}
status={}
string1="CLD_EXITED"
string2="CLD_KILLED"
string3="CLD_DUMPED"
string4="CLD_TRAPPED"
string5="CLD_CONTINUED"

code={}

conn = sqlite3.connect('sparse.db')

curs = conn.cursor()


with conn:

	curs.executescript("""
        DROP TABLE IF EXISTS sigchld;
        CREATE TABLE sigchld(Pid TEXT,Signame TEXT,Code TEXT,Status TEXT,Child TEXT);
        """);
	

	#3198  17:12:08.177944 --- SIGCHLD {si_signo=SIGCHLD, si_code=CLD_EXITED, si_pid=3199, si_status=1, si_utime=0, si_stime=0} ---
	curs.execute("SELECT Pid,Signame,arg FROM signals WHERE Signame LIKE 'SIGCHLD';")
	rows = curs.fetchall()
	
	for row in rows:
		print row[0]
		#print row[2]
		temp = row[2].split(",")
		temp1= temp[0].split("=")
		#print temp1[1]
		temp2= temp[1].split("=")
		#print temp2[1]
		temp3=temp[2].split("=")
		#print temp3[1]
		child_pid=temp3[1]
		print child_pid
		temp4=temp[3].split("=")
		#print temp4[1]
		status=temp4[1]
		print status
				
				
		if((temp2[1]==string1)):
			code="child   called  has exited "
			
		elif((temp2[1]==string2)):
			code="child  killed  by  signal"
			
		elif((temp2[1]==string3)):
			code="child killed by signal and  dumped  core"

		elif((temp2[1]==string4)):
			code="traced child has trapped"
			
		elif((temp2[1]==string5)):
			code="child continued by SIGCONT"
		'''		
		else:

			print "np"
		'''
		#Pid TEXT,Signame TEXT,Code TEXT,Status TEXT,Child TEXT);
	        curs.executescript("INSERT INTO sigchld VALUES('%s','%s','%s','%s','%s');" %(row[0], row[1], code, status, child_pid))
	'''		
	curs.execute("SELECT * FROM sigchld;")
	rows = curs.fetchall()
	print "\n PID         SigName              Code                             Status                     Child             \n"
	for row in rows:  
		print ("\n %s          %s            %s                              %s                         %s                    " %(row[0],row[1],row[2],row[3],row[4]))
	'''
