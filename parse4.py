#2148  00:32:52.015035 recvfrom(3, "\1\0\37\0\0\0\0\0\255\0\0\0\1\0\240\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0", 4096, 0, NULL, NULL) = 32 <0.000027>


#Program For Parsing

import sys
import getopt
import re
import traceback
import logging
import sqlite3

#temp2 = 0
gno  = 0
wr = 0

conn = sqlite3.connect('sparse.db')

curs = conn.cursor()
curs.executescript("""
        DROP TABLE IF EXISTS syscall;
        CREATE TABLE syscall(Pid TEXT, StartTime TEXT, SysName TEXT, arg TEXT, ret TEXT, time INTEGER, Error TEXT, Desc TEXT);
        """);
#curs.execute("CREATE TABLE syscall(Pid TEXT, StartTime TEXT, SysName TEXT, arg TEXT, ret TEXT, time INTEGER, Error TEXT, Desc TEXT);");#

curs3 = conn.cursor()
#curs3.executescript("CREATE TABLE sysdisp(Pid TEXT, StartTime TEXT, SysName TEXT, ret TEXT, time INTEGER, Status TEXT);");
curs3.executescript("""
        DROP TABLE IF EXISTS sysdisp;
        CREATE TABLE sysdisp(Pid TEXT, StartTime TEXT, SysName TEXT, ret TEXT, time INTEGER, Status TEXT);
        """);

curs1 = conn.cursor()
#curs1.executescript("CREATE TABLE unfinished(Pid TEXT, StartTime TEXT, SysName TEXT, arg TEXT);");
curs1.executescript("""
        DROP TABLE IF EXISTS unfinished;
        CREATE TABLE unfinished(Pid TEXT, SysName TEXT, totl INTEGER, idle INTEGER);
        """);


curs2 = conn.cursor()
#curs2.executescript("CREATE TABLE resumed(Pid TEXT, SysName TEXT, totl INTEGER, idle INTEGER);");
curs2.executescript("""
        DROP TABLE IF EXISTS resumed;
        CREATE TABLE resumed(Pid TEXT, SysName TEXT, totl INTEGER, idle INTEGER);
        """);
curs5 = conn.cursor()
curs5.executescript("""
        DROP TABLE IF EXISTS sigsegv;
        CREATE TABLE sigsegv(Pid TEXT, StartTime TEXT, SigName TEXT, No INTEGER, WR INTEGER);
        """);

curs4 = conn.cursor()
curs.executescript("""
        DROP TABLE IF EXISTS signals;
        CREATE TABLE signals(Pid TEXT, StartTime TEXT, SigName TEXT, arg TEXT);
        """);
gno = 0

def autoDetectFormat():

	with open("sample.txt") as f:

		for line in f:
    			result = detectLineFormat(line)
    
	with conn:

	    # Completed System Calls
		
		print("\n\t\t Complete System Calls...\n")
		print('\n Pid        SyscallName        RetVaL        Timespent      Error         Description \n')

		curs.execute("SELECT * from syscall")
		rows = curs.fetchall()

		for row in rows:
			print(' %s %15s %15s %10s %15s %15s' %(row[0],row[2],row[4],row[5],row[6],row[7]))	

	    # Resumed System Calls

		print("\n\t\t Resumed System Calls...\n")
		print('\n Pid        SyscallName        Total Time        Idel Time \n')

		curs2.execute("SELECT * from resumed")
		rows = curs2.fetchall()

		for row in rows:
			print(' %s %15s %15s %15s' %(row[0],row[1],row[2],row[3]))	

	    # Incomplete System Calls

		print("\n\t\t Incomplete System Calls...\n")
		print('\n Pid        SyscallName \n')

		curs1.execute("SELECT * from unfinished")
		rows = curs1.fetchall()

		for row in rows:
			print(' %s %15s %15s %15s' %(row[0],row[1],row[2],row[3]))	
		


		print("\n\t\t Signals...\n")
		print('\n Pid        Signal                Args      \n')

		curs1.execute("SELECT * from signals ")
		rows = curs1.fetchall()

		for row in rows:
			print(' %s %15s %15s' %(row[0],row[2],row[3]))	
def detectLineFormat(line):

    
	result2=regexp2.search(line)
	result17=regexp17.search(line)
	result15=regexp15.search(line)
	result16=regexp16.search(line)
	result13=regexp13.search(line)
	result14=regexp14.search(line)	
	
	result0=regexp0.search(line)
	result1=regexp1.search(line)
	#result2=regexp2.search(line)
	
	result3=regexp3.search(line)
	result4=regexp4.search(line)
	result5=regexp5.search(line)
	result6=regexp6.search(line)
	result7=regexp7.search(line)
	result8=regexp8.search(line)
	result9=regexp9.search(line)
	result10=regexp10.search(line)
	result18=regexp18.search(line)
	result19=regexp19.search(line)
	#result11=regexp11.search(line)
	#result12=regexp12.search(line)
	#result15=regexp15.search(line)
	#result16=regexp16.search(line)
	global gno
	global wr
		    		
	
	if result1:
	    gno = gno + 1
	    
            Line1["Pid"] = result1.group(1)
            Line1["StartTime"] = result1.group(2)
            Line1["Syscall"]= result1.group(3)
            if Line1["Syscall"]=='read' or Line1["Syscall"]=='write':
                wr = wr + 1
	    Line1["Args"] = result1.group(4)
	    Line1["Ret"] = result1.group(5)
	    Line1["Error"] = 'null'
	    Line1["Desc"] = 'null'
	    Line1["TimeSpent"] = result1.group(6)
	    Line1["Status"] = 'Success'

	    curs2.executescript("""
	    	INSERT INTO sysdisp VALUES('%s','%s','%s','%s','%s','%s');
		"""%(Line1["Pid"], Line1["StartTime"], Line1["Syscall"], Line1["Ret"], Line1["TimeSpent"], Line1["Status"]))

	    curs.executescript("""
	    	INSERT INTO syscall VALUES('%s','%s','%s','%s','%s','%s','%s','%s');
		"""%(Line1["Pid"], Line1["StartTime"], Line1["Syscall"], Line1["Args"], Line1["Ret"], Line1["TimeSpent"], Line1["Error"], Line1["Desc"]))

	    print(' %s     %s     %s          %s     %s     %s' %(Line1["Pid"],Line1["Syscall"],Line1["Ret"],Line1["TimeSpent"],Line1["Error"],Line1["Desc"]))
	    Line1["Args"] = 'null'
	
	elif result13:
	    gno = gno + 1

	    print("13!!!")

	    Line13["Pid"] = result13.group(1)
            Line13["StartTime"] = result13.group(2)
            Line13["Syscall"]= result13.group(3)
            if Line13["Syscall"]=='read' or Line13["Syscall"]=='write':
                wr = wr + 1
            
	    Line13["Args"] = result13.group(4)
	    Line13["Ret"] = result13.group(5)
	    Line13["Error"] = 'null'
	    Line13["Desc"] = 'null'
	    Line13["TimeSpent"] = result13.group(6)
	    Line13["Status"] = 'Success'

	    curs2.executescript("""
	    	INSERT INTO sysdisp VALUES('%s','%s','%s','%s','%s','%s');
		"""%(Line13["Pid"], Line13["StartTime"], Line13["Syscall"], Line13["Ret"], Line13["TimeSpent"], Line13["Status"]))

	    curs.executescript("""
	    	INSERT INTO syscall VALUES('%s','%s','%s','%s','%s','%s','%s','%s');
		"""%(Line13["Pid"], Line13["StartTime"], Line13["Syscall"], Line13["Args"], Line13["Ret"], Line13["TimeSpent"], Line13["Error"], Line13["Desc"]))

	    print(' %s     %s     %s          %s     %s     %s' %(Line13["Pid"],Line13["Syscall"],Line13["Ret"],Line13["TimeSpent"],Line13["Error"],Line13["Desc"]))
	  #  print Line13["Args"]
	    Line13["Args"] = 'null'

	elif result15:
	    gno = gno + 1

	    print("15!!!")

	    Line15["Pid"] = result15.group(1)
            Line15["StartTime"] = result15.group(2)
            Line15["Syscall"]= result15.group(3)
            if Line15["Syscall"]=='read' or Line15["Syscall"]=='write':
                wr = wr + 1
            
	    Line15["Args"] = result15.group(4)
	    Line15["Ret"] = result15.group(5)
	    Line15["Error"] = 'null'
	    Line15["Desc"] = 'null'
	    Line15["TimeSpent"] = result15.group(6)
	    Line15["Status"] = 'Success'

	    curs2.executescript("""
	    	INSERT INTO sysdisp VALUES('%s','%s','%s','%s','%s','%s');
		"""%(Line15["Pid"], Line15["StartTime"], Line15["Syscall"], Line15["Ret"], Line15["TimeSpent"], Line15["Status"]))

	    curs.executescript("""
	    	INSERT INTO syscall VALUES('%s','%s','%s','%s','%s','%s','%s','%s');
		"""%(Line15["Pid"], Line15["StartTime"], Line15["Syscall"], Line15["Args"], Line15["Ret"], Line15["TimeSpent"], Line15["Error"], Line15["Desc"]))

	    print(' %s     %s     %s          %s     %s     %s' %(Line15["Pid"],Line15["Syscall"],Line15["Ret"],Line15["TimeSpent"],Line15["Error"],Line15["Desc"]))
	   
	    Line13["Args"] = 'null'
	
	
	elif result16:
	    gno = gno + 1

	    print("16!!!")

	    Line16["Pid"] = result16.group(1)
            Line16["StartTime"] = result16.group(2)
            Line16["Syscall"]= result16.group(3)
            if Line16["Syscall"]=='read' or Line16["Syscall"]=='write':
                wr = wr + 1
            
	    Line16["Args"] = result16.group(4)
	    Line16["Ret"] = result16.group(5)
	    Line16["Error"] = 'null'
	    Line16["Desc"] = 'null'
	    Line16["TimeSpent"] = result16.group(6)
	    Line16["Status"] = 'Success'

	    curs2.executescript("""
	    	INSERT INTO sysdisp VALUES('%s','%s','%s','%s','%s','%s');
		"""%(Line16["Pid"], Line16["StartTime"], Line16["Syscall"], Line16["Ret"], Line16["TimeSpent"], Line16["Status"]))

	    curs.executescript("""
	    	INSERT INTO syscall VALUES('%s','%s','%s','%s','%s','%s','%s','%s');
		"""%(Line16["Pid"], Line16["StartTime"], Line16["Syscall"], Line16["Args"], Line16["Ret"], Line16["TimeSpent"], Line16["Error"], Line16["Desc"]))

	    print(' %s     %s     %s          %s     %s     %s' %(Line16["Pid"],Line16["Syscall"],Line16["Ret"],Line16["TimeSpent"],Line16["Error"],Line16["Desc"]))
	   # print Line13["Args"]
	    Line16["Args"] = 'null'

	elif result17:
	    gno = gno + 1

	    print("17!!!")

	    Line17["Pid"] = result17.group(1)
            Line17["StartTime"] = result17.group(2)
            Line17["Syscall"]= result17.group(3)
            if Line17["Syscall"]=='read' or Line17["Syscall"]=='write':
                wr = wr + 1
            
	    Line17["Args"] = result17.group(4)
	    Line17["Ret"] = result17.group(5)
	    Line17["Error"] = 'null'
	    Line17["Desc"] = 'null'
	    Line17["TimeSpent"] = result17.group(6)
	    Line17["Status"] = 'Success'

	    curs2.executescript("""
	    	INSERT INTO sysdisp VALUES('%s','%s','%s','%s','%s','%s');
		"""%(Line17["Pid"], Line17["StartTime"], Line17["Syscall"], Line17["Ret"], Line17["TimeSpent"], Line17["Status"]))

	    curs.executescript("""
	    	INSERT INTO syscall VALUES('%s','%s','%s','%s','%s','%s','%s','%s');
		"""%(Line17["Pid"], Line17["StartTime"], Line17["Syscall"], Line17["Args"], Line17["Ret"], Line17["TimeSpent"], Line17["Error"], Line17["Desc"]))

	    print(' %s     %s     %s          %s     %s     %s' %(Line17["Pid"],Line17["Syscall"],Line17["Ret"],Line17["TimeSpent"],Line17["Error"],Line17["Desc"]))
	   # print Line13["Args"]
	    Line17["Args"] = 'null'

	
	elif result0:
	    gno = gno + 1

	    print("End of File !!!")

		   	
	elif result2:
	    gno = gno + 1

	    print "2"
	    Line2["Pid"] = result2.group(1)
            Line2["StartTime"] = result2.group(2)
            Line2["Syscall"]= result2.group(3)
            if Line2["Syscall"]=='read' or Line2["Syscall"]=='write':
                wr = wr + 1
            
	    Line2["Args"] = result2.group(4)
	    Line2["Ret"] = result2.group(5)
	    Line2["Error"] = result2.group(6)
	    Line2["Desc"] = result2.group(7)
	    Line2["TimeSpent"] = result2.group(8)
	    Line2["Status"] = 'Fail'

	    curs2.executescript("""
	    	INSERT INTO sysdisp VALUES('%s','%s','%s','%s','%s','%s');
		"""%(Line2["Pid"], Line2["StartTime"], Line2["Syscall"], Line2["Ret"], Line2["TimeSpent"], Line2["Status"]))

	    curs.executescript("""
	    	INSERT INTO syscall VALUES('%s','%s','%s','%s','%s','%s','%s','%s');
		"""%(Line2["Pid"], Line2["StartTime"], Line2["Syscall"], Line2["Args"], Line2["Ret"], Line2["TimeSpent"], Line2["Error"], Line2["Desc"]))
	    print(' %s     %s     %s          %s     %s     %s' %(Line2["Pid"],Line2["Syscall"],Line2["Ret"],Line2["TimeSpent"],Line2["Error"],Line2["Desc"]))
	elif result14:
	    gno = gno + 1

            print "14"	
	    Line14["Pid"] = result14.group(1)
            Line14["StartTime"] = result14.group(2)
            Line14["Syscall"]= result14.group(3)
            if Line14["Syscall"]=='read' or Line14["Syscall"]=='write':
                wr = wr + 1
            
	    Line14["Args"] = result14.group(4)
	    Line14["Ret"] = result14.group(5)
	    Line14["Error"] = result14.group(6)
	    Line14["Desc"] = result14.group(7)
	    Line14["TimeSpent"] = result14.group(8)
	    Line14["Status"] = 'Fail'

	    curs2.executescript("""
	    	INSERT INTO sysdisp VALUES('%s','%s','%s','%s','%s','%s');
		"""%(Line14["Pid"], Line14["StartTime"], Line14["Syscall"], Line14["Ret"], Line14["TimeSpent"], Line14["Status"]))

	    curs.executescript("""
	    	INSERT INTO syscall VALUES('%s','%s','%s','%s','%s','%s','%s','%s');
		"""%(Line14["Pid"], Line14["StartTime"], Line14["Syscall"], Line14["Args"], Line14["Ret"], Line14["TimeSpent"], Line14["Error"], Line14["Desc"]))
	    print(' %s     %s     %s          %s     %s     %s' %(Line14["Pid"],Line14["Syscall"],Line14["Ret"],Line14["TimeSpent"],Line14["Error"],Line14["Desc"]))

	elif result8:
	    gno = gno + 1

	    print "8"
	    Line8["Pid"] = result8.group(1)
            Line8["StartTime"] = result8.group(2)
            Line8["Syscall"]= result8.group(3)
            if Line8["Syscall"]=='read' or Line8["Syscall"]=='write':
                wr = wr + 1
            
	    Line8["Args"] = result8.group(4)
	    Line8["Ret"] = result8.group(5)
	    Line8["Error"] = "null"
	    Line8["Desc"] = result8.group(6)
	    Line8["TimeSpent"] = result8.group(7)
	    Line8["Status"] = 'Success'

	    curs2.executescript("""
	    	INSERT INTO sysdisp VALUES('%s','%s','%s','%s','%s','%s');
		"""%(Line8["Pid"], Line8["StartTime"], Line8["Syscall"], Line8["Ret"], Line8["TimeSpent"], Line8["Status"]))

	    curs.executescript("""
	    	INSERT INTO syscall VALUES('%s','%s','%s','%s','%s','%s','%s','%s');
		"""%(Line8["Pid"], Line8["StartTime"], Line8["Syscall"], Line8["Args"], Line8["Ret"], Line8["TimeSpent"], Line8["Error"], Line8["Desc"]))
	    print(' %s     %s     %s          %s     %s     %s' %(Line8["Pid"],Line8["Syscall"],Line8["Ret"],Line8["TimeSpent"],Line8["Error"],Line8["Desc"]))

	elif result10:
	    gno = gno + 1

	    print "3"
	    Line10["Pid"] = result10.group(1)
            Line10["StartTime"] = result10.group(2)
            Line10["Syscall"]= result10.group(3)
            if Line10["Syscall"]=='read' or Line10["Syscall"]=='write':
                wr = wr + 1
            
	    Line10["Args"] = result10.group(4)
	    Line10["Ret"] = result10.group(5)
	    Line10["Error"] = "null"
	    Line10["Desc"] = result10.group(6)
	    Line10["TimeSpent"] = result10.group(7)
	    Line10["Status"] = 'Success'

	    curs2.executescript("""
	    	INSERT INTO sysdisp VALUES('%s','%s','%s','%s','%s','%s');
		"""%(Line10["Pid"], Line10["StartTime"], Line10["Syscall"], Line10["Ret"], Line10["TimeSpent"], Line10["Status"]))

	    curs.executescript("""
	    	INSERT INTO syscall VALUES('%s','%s','%s','%s','%s','%s','%s','%s');
		"""%(Line10["Pid"], Line10["StartTime"], Line10["Syscall"], Line10["Args"], Line10["Ret"], Line10["TimeSpent"], Line10["Error"], Line10["Desc"]))
	    print(' %s     %s     %s          %s     %s     %s' %(Line10["Pid"],Line10["Syscall"],Line10["Ret"],Line10["TimeSpent"],Line10["Error"],Line10["Desc"]))

        elif result3:
	    gno = gno + 1

	    print "3"
            Line3["Pid"] = result3.group(1)
            Line3["StartTime"] = result3.group(2)
            Line3["Syscall"]= result3.group(3)
            if Line3["Syscall"]=='read' or Line3["Syscall"]=='write':
                wr = wr + 1
            
	    Line3["Args"] = result3.group(4)
	    Line3["Ret"] = result3.group(5)
	    Line3["Error"] = 'null'
	    Line3["Desc"] = 'null'
	    Line3["TimeSpent"] = result3.group(6)
	    Line3["Status"] = 'Success'

	    curs2.executescript("""
	    	INSERT INTO sysdisp VALUES('%s','%s','%s','%s','%s','%s');
		"""%(Line3["Pid"], Line3["StartTime"], Line3["Syscall"], Line3["Ret"], Line3["TimeSpent"], Line3["Status"]))
	
	    curs.executescript("""
	    	INSERT INTO syscall VALUES('%s','%s','%s','%s','%s','%s','%s','%s');
		"""%(Line3["Pid"], Line3["StartTime"], Line3["Syscall"], Line3["Args"], Line3["Ret"], Line3["TimeSpent"], Line3["Error"], Line3["Desc"]))
	    print(' %s     %s     %s          %s     %s     %s' %(Line3["Pid"],Line3["Syscall"],Line3["Ret"],Line3["TimeSpent"],Line3["Error"],Line3["Desc"]))
  
	elif result4:
	    gno = gno + 1

	    print("\nExit from Strace")

	elif result9:
	    gno = gno + 1

	    print "9"
	    Lines["Pid"] = result9.group(1)
            Lines["StartTime"] = result9.group(2)
            Lines["Signame"]= result9.group(3)
	    Lines["Args"] = result9.group(4)

	    curs1.executescript("""
	    	INSERT INTO signals VALUES('%s','%s','%s','%s');
		"""%(Lines["Pid"], Lines["StartTime"], Lines["Signame"], Lines["Args"]))
	    print(' %s     %s' %(Lines["Pid"],Lines["Signame"]))


	elif result5:
	    gno = gno + 1

	    print "5"
	    Line5["Pid"] = result5.group(1)
            Line5["StartTime"] = result5.group(2)
            Line5["Syscall"]= result5.group(3)
            if Line5["Syscall"]=='read' or Line5["Syscall"]=='write':
                wr = wr + 1
            
	    Line5["Args"] = 'null'

	    curs1.executescript("""
	    	INSERT INTO unfinished VALUES('%s','%s','%s','%s');
		"""%(Line5["Pid"], Line5["StartTime"], Line5["Syscall"], Line5["Args"]))
	    print(' %s     %s' %(Line5["Pid"],Line5["Syscall"]))

	elif result6:
	    gno = gno + 1

	    print "6"
	    Line6["Pid"] = result6.group(1)
            Line6["StartTime"] = result6.group(2)
            Line6["Syscall"]= result6.group(3)
            if Line6["Syscall"]=='read' or Line6["Syscall"]=='write':
                wr = wr + 1
            
	    Line6["Args"] = result6.group(4)
	    
	    curs1.executescript("""
	    	INSERT INTO unfinished VALUES('%s','%s','%s','%s');
		"""%(Line6["Pid"], Line6["StartTime"], Line6["Syscall"], Line6["Args"]))
	    print(' %s     %s' %(Line6["Pid"],Line6["Syscall"]))

	elif result7:
	    gno = gno + 1

	    print "7"
	    pid1 = result7.group(1)

	    curs1.execute("SELECT * from unfinished where Pid=:PID", {"PID": pid1})
	    temp = curs1.fetchone()

	# inserting in Complete System Calls Table

	    Line71["Pid"] = temp[0]
	    Line71["StartTime"] = temp[1]
	    Line71["Syscall"]= temp[2]
            if Line71["Syscall"]=='read' or Line71["Syscall"]=='write':
                wr = wr + 1
	    
	    Line71["Args"] = temp[3]
	    Line71["Ret"] = result7.group(4)
	    Line71["Error"] = 'null'
	    Line71["Desc"] = 'null'
	    Line71["TimeSpent"] = result7.group(5)
	    Line71["Status"] = 'Success'

	    curs2.executescript("""
	    	INSERT INTO sysdisp VALUES('%s','%s','%s','%s','%s','%s');
		"""%(Line71["Pid"], Line71["StartTime"], Line71["Syscall"], Line71["Ret"], Line71["TimeSpent"], Line71["Status"]))

	    curs.executescript("""
	    	INSERT INTO syscall VALUES('%s','%s','%s','%s','%s','%s','%s','%s');
		"""%(Line71["Pid"], Line71["StartTime"], Line71["Syscall"], Line71["Args"], Line71["Ret"], Line71["TimeSpent"], Line71["Error"], Line71["Desc"]))

	  #  print(' %s     %s     %s          %s     %s     %s' %(Line71["Pid"],Line71["Syscall"],Line71["Ret"],Line71["TimeSpent"],Line71["Error"],Line71["Desc"]))

	# insrting in Resumed System Calls Table

	    Line72["Pid"] = temp[0]
	    Line72["Syscall"] = temp[2]

	    lst = temp[1].split(".")
	    lststrt = int(lst[1])

	    znd = result7.group(2).split(".")
	    zndstrt = int(znd[1])

	    timespent1 = result7.group(5).split(".")
	    timespent = int(timespent1[0])

	    totl = zndstrt + timespent - lststrt	#2nd start + timespent - 1st start
	    idle = zndstrt - lststrt		#2nd start - 1st start

	    Line72["totl"] = totl
	    Line72["idle"] = idle

	    curs2.executescript("""
	    	INSERT INTO resumed VALUES('%s','%s','%s','%s');
		"""%(Line72["Pid"], Line72["Syscall"], Line72["totl"], Line72["idle"]))

	    curs1.execute("DELETE from unfinished where Pid=:PID", {"PID": pid1})

	elif result18:
	    gno = gno + 1
	    Line18["Pid"] = result18.group(1)
            Line18["StartTime"] = result18.group(2)
            Line18["Syscall"]= "SIGSEGV"
	    Line18["Args"] = "Segmentation fault"
	    Line18["No"] = gno
	    Line18["WR"] = wr
	    #Line18["Ret"] = result18.group(5)
	    #Line18["Error"] = 'null'
	    #Line18["Desc"] = 'null'
	    #Line18["TimeSpent"] = result18.group(6)
	    #Line18["Status"] = 'Success'

	    curs2.executescript("""
	    	INSERT INTO signals VALUES('%s','%s','%s','%s');
		"""%(Line18["Pid"], Line18["StartTime"], Line18["Syscall"], Line18["Args"]))
	
	    curs.executescript("""
	    	INSERT INTO sigsegv VALUES('%s','%s','%s','%s','%s');
		"""%(Line18["Pid"], Line18["StartTime"], Line18["Syscall"], Line18["No"], Line18["WR"]))

	    print "18"

	elif result19:
	    gno = gno + 1

	    print "Killed by Sigsegv"

	
	 


	else:
	    gno = gno + 1
	
        #4013  01:51:44.687319 <... wait4 resumed> [{WIFEXITED(s) && WEXITSTATUS(s) == 1}], 0, NULL) = 4014 <0.402551>
    	    print "no option"
	    temp1 = line.split(" ",1)    #(4013),  (01:51:44.687319 <... wait4 resumed> [{WIFEXITED(s) && WEXITSTATUS(s) == 1}], 0, NULL) = 4014 <0.402551>)

	    Line81["Pid"] = temp1[0]
	    pid2 = temp1[0]
	    print temp1[1]
	    temp2 = temp1[1].split(" ",5)    #( ), (01:51:44.687319), (<...), (wait4), (resumed>), ([{WIFEXITED(s) && WEXITSTATUS(s) == 1}], 0, NULL) = 4014      
	    Line81["StartTime"] = temp2[1]
	    #print temp2
	    starttime = temp2[1]
	    if(temp2[4]=="resumed>"):
	        Line81["Syscall"] = str(temp2[3])
            if Line81["Syscall"]=='read' or Line81["Syscall"]=='write':
                wr = wr + 1
	            
            sysname = str(temp2[3])
            temp1 = temp2[5].rsplit(" ",3)     #([{WIFEXITED(s) && WEXITSTATUS(s) == 1}], 0, NULL)), (=), (4014) ,(<0.402551>)
            timespent2 = temp1[3].split(">")    #(<0.402551), ()
            timespent1 = timespent2[0].split("<")   #(), (0.402551)
            Line81["TimeSpent"] = timespent1[1]
            timespented = timespent1[1]
            Line81["Desc"] = 'null'
            Line81["Error"] = 'null'
            Line81["Ret"] = temp1[2]	# 4014
            temp2=temp1[0].rsplit(")", 1)
            pid2 = Line81["Pid"]
	    curs1.execute("SELECT arg from unfinished where Pid=:PID", {"PID": pid2})
            temp3 = curs1.fetchone()
	    print temp3
            if (temp3[0]==None):
		        Line81["Args"] = temp2[0]
		        
            else:
			
		        argument1 = str(temp3[0])
		        argument = argument1+" "+temp2[0]
		        Line81["Args"] = argument

	    Line81["Status"] = 'Success'

	    curs2.executescript("""
	    	INSERT INTO sysdisp VALUES('%s','%s','%s','%s','%s','%s');
		"""%(Line81["Pid"], Line81["StartTime"], Line81["Syscall"], Line81["Ret"], Line81["TimeSpent"], Line81["Status"]))

		    
	    curs.executescript("""
	    	INSERT INTO syscall VALUES('%s','%s','%s','%s','%s','%s','%s','%s');
		"""%(Line81["Pid"], Line81["StartTime"], Line81["Syscall"], Line81["Args"], Line81["Ret"], Line81["TimeSpent"], Line81["Error"], Line81["Desc"]))

	    print(' %s     %s     %s          %s     %s     %s' %(Line81["Pid"],Line81["Syscall"],Line81["Ret"],Line81["TimeSpent"],Line81["Error"],Line81["Desc"]))

	# insrting in Resumed System Calls Table

            Line82["Pid"] = pid2
            Line82["Syscall"] = sysname
            curs1.execute("SELECT StartTime from unfinished where Pid=:PID", {"PID": pid2})
            starttemp = curs1.fetchone()
            
            lst = starttemp[0].split(".")
            lststrt = int(lst[1])
            znd = starttime.split(".")
            zndstrt = int(znd[1])
            timespent1 = timespented.split(".")
            timespent = int(timespent1[1])
            totl = zndstrt + timespent - lststrt	#2nd start + timespent - 1st start
            idle = zndstrt - lststrt		#2nd start - 1st start
            
            Line82["totl"] = totl
            Line82["idle"] = idle
            
            curs2.executescript("""INSERT INTO resumed VALUES('%s','%s','%s','%s');"""%(Line82["Pid"], Line82["Syscall"], Line82["totl"], Line82["idle"]))
            curs1.execute("DELETE from unfinished where Pid=:PID", {"PID": pid2})

	return

#4013  01:51:44.687319 <... wait4 resumed> [{WIFEXITED(s) && WEXITSTATUS(s) == 1}], 0, NULL) = 4014 <0.402551>

Line1={}
Line11={}
Line2={}
Line8={}
Line3={}
Line5={}
Line6={}
Line71={}
Line72={}
Line81={}
Line82={}
Line9={}
Line10={}
Line11={}
Line12={}
Line13={}
Line14={}
Line15={}
Line16={}
Line17={}
Lines={}
Lines1={}
Line18={}
Line19={}


    
	# +++ exited with 0 +++       
pat0 = r"\+\+\+ exited with \d+ \+\+\+"

	#PID TIME SYSNAME( ARG ) = DECIMAL DIGIT <TIMESPENT>
pat1 = r"(\d+)[ ]+(\d+:\d+:\d+\.\d+)[ ]+([a-zA-Z\_0-9]+)\((.*?)\)[ ]+=[ ]+(\-?\d+?)[ ]+\<(\d+\.\d+)\>"

	#PID TIME SYSNAME( ARG ) = DECIMAL DIGIT ERROR DESC <TIMESPENT>
pat2 = r"(\d+)[ ]+(\d+:\d+:\d+\.\d+)[ ]+([a-zA-Z\_0-9]+)\((\.|.*?)\)[ ]+=[ ]+(\-?\d+?)[ ]+([\|\_\,0-9a-zA-Z]+)[ ]+\((.*)\)[ ]+\<(\d+\.\d+)\>"

	#2148  00:32:52.019873 recvfrom(3, 0x7f308a01d074, 4096, 0, 0, 0) = -1 EAGAIN (Resource temporarily unavailable) <0.000024>
pat14 = r"(\d+)[ ]+(\d+:\d+:\d+\.\d+)[ ]+([a-zA-Z\_0-9]+)\(((\d*\,|0[xX][a-fA-F\d]+\,)*?)\)[ ]+=[ ]+(\-?\d+?)[ ]+([\|\_\,0-9a-zA-Z]+)[ ]+\((.*)\)[ ]+\<(\d+\.\d+)\>"

	#2148  00:32:52.015538 poll([{fd=3, events=POLLIN}], 1, -1) = 1 ([{fd=3, revents=POLLIN}]) <0.000030>
	#PID TIME SYSNAME( ARG ) = DECIMAL DIGIT (DESC) <TIMESPENT>
pat10 = r"(\d+)[ ]+(\d+:\d+:\d+\.\d+)[ ]+([a-zA-Z\_0-9]+)\((.*?)\)[ ]+=[ ]+(\-?\d+?)[ ]+\((.*?)\)[ ]+\<(\d+\.\d+)\>"

	#2145  00:32:51.944877 fcntl(255, F_GETFL) = 0x8000 (flags O_RDONLY|O_LARGEFILE) <0.000014>
	#PID TIME SYSNAME( ARG ) = HEX DESC <TIMESPENT>
pat8 = r"(\d+)[ ]+(\d+:\d+:\d+\.\d+)[ ]+([a-zA-Z\_0-9]+)\((.*?)\)[ ]+=[ ]+(-?0[xX][a-fA-F\d]+)[ ]+\((.*)\)[ ]+\<(\d+\.\d+)\>"

	#PID TIME SYSNAME( ARG ) = HEX <TIMESPENT>
pat3 = r"(\d+)[ ]+(\d+:\d+:\d+\.\d+)[ ]+([a-zA-Z\_0-9]+)\((.*?)\)[ ]+=[ ]+(-?0[xX][a-fA-F\d]+)[ ]+\<(\d+\.\d+)\>"

	#PID TIME SYSNAME( ARG ) = ?
pat4 = r"(\d+)[ ]+(\d+:\d+:\d+\.\d+)[ ]+([a-zA-Z\_0-9]+)\((.*?)\)[ ]+=[ ]+(\?)"

	#PID TIME SYSNAME ( <unfinished ...>
pat5 = r"(\d+)[ ]+(\d+:\d+:\d+\.\d+)[ ]+([a-zA-Z\_0-9]+)\(( <unfinished \.\.\.>)"

	#PID TIME SYSNAME ( arg <unfinished ...>
pat6 = r"(\d+)[ ]+(\d+:\d+:\d+\.\d+)[ ]+([a-zA-Z\_0-9]+)\((.*?) (\<unfinished \.\.\.>)"

#3199  17:12:08.176776 <... read resumed> "ASCII text\n", 128) = 11 <0.011279>
#2148  00:32:51.980068 <... rt_sigprocmask resumed> NULL, 8) = 0 <0.000040>
	#PID TIME <... sysname rsumed> ) = HEX <TIMESPENT>
pat7 = r"(\d+)[ ]+(\d+:\d+:\d+\.\d+)[ ]+<\.\.\. ([a-zA-Z\_0-9]+) resumed> (.*?)\)[ ]+=[ ]+(\-?\d+?)[ ]+\<(\d+\.\d+)\>"

	#PID TIME <... sysname rsumed> ARG ) = HEX <TIMESPENT>
#4013  01:51:44.687319 <... wait4 resumed> [{WIFEXITED(s) && WEXITSTATUS(s) == 1}], 0, NULL) = 4014 <0.402551>

	#PID TIME --- Signal {ARG} ---

	#3997  01:46:09.581243 --- SIGCHLD (Child exited) @ 0 (0) ---
#2145  00:32:51.955525 --- SIGCHLD {si_signo=SIGCHLD, si_code=CLD_EXITED, si_pid=2146, si_status=0, si_utime=0, si_stime=0} ---
pat9 = r"(\d+)[ ]+(\d+:\d+:\d+\.\d+)[ ]+\-\-\- ([a-zA-Z\_0-9]+)[ ]\{(.*?)\} \-\-\-"

#pat12=r"(\d+)[ ]+(\d+:\d+:\d+\.\d+)[ ]+\-\-\- (.*?) \-\-\-"

#2148  00:32:52.015434 writev(3, [{"\24\0\6\0\1\0\240\0\373\1\0\0\37\0\0\0\0\0\0\0\0 \0\0", 24}, {NULL, 0}, {"", 0}], 3) = 24 <0.000028>
#pat11 = r"(\d+)[ ]+(\d+:\d+:\d+\.\d+)[ ]+([a-zA-Z\_0-9]+)\((.|\{|\}|\[|\]|\,)*?\)[ ]+=[ ]+(\-?\d+?)[ ]+\<(\d+\.\d+)\>"

#5602  19:08:21.489760 read(4, "\20'\0\0\0\0\0\0\300\2\0\0\0\0\0\0\0\0\0\0\0\0\0\0\20\0\0\0\0\0\0\0"..., 4096) = 3640 <0.000019>
pat16 = r'(\d+)[ ]+(\d+:\d+:\d+\.\d+)[ ]+([a-zA-Z\_0-9]+)(\(\d+,[ ]"(.*?)"...,[ ]\d+\))[ ]+=[ ]+(\-?\d+?)[ ]+\<(\d+\.\d+)\>'

#2145  00:32:51.948298 rt_sigaction(SIGCHLD, {0x4411c0, [], SA_RESTORER|SA_RESTART, 0x39560359a0},  <unfinished ...>


#4002  01:46:09.651226 read(4, "\177ELF\1\1\1\0\0\0\0\0\0\0\0\0\3\0\3\0\1\0\0\0\320!\0\0004\0\0\0"..., 52) = 52 <0.000007>
pat13= r"(\d+)[ ]+(\d+:\d+:\d+\.\d+)[ ]+([a-zA-Z\_0-9]+)\((#?.*)\)[ ]+=[ ]+(\-?\d+?)[ ]+\<(\d+\.\d+)\>"

#2148  00:32:52.015035 recvfrom(3, "\1\0\37\0\0\0\0\0\255\0\0\0\1\0\240\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0", 4096, 0, NULL, NULL) = 32 <0.000027>
pat15 = r'(\d+)[ ]+(\d+:\d+:\d+\.\d+)[ ]+([a-zA-Z\_0-9]+)(\(\d+,[ ]"(.*?)"(.*?)\))[ ]+=[ ]+(\-?\d+?)[ ]+\<(\d+\.\d+)\>'

#  00:32:51.941543 open("/usr/lib/locale/locale-archive", O_RDONLY|O_CLOEXEC) = 3 <0.000024>
pat17 = r'(\d+)[ ]+(\d+:\d+:\d+\.\d+)[ ]+([a-zA-Z\_0-9]+)\((\"(.*?)\"\,(,*?))\)[ ]+=[ ]+(\-?\d+?)[ ]+\<(\d+\.\d+)\>'
pat18 = r"(\d+)[ ]+(\d+:\d+:\d+\.\d+)[ ]+\-\-\-[ ]+SIGSEGV[ ]+\(Segmentation[ ]+fault\)[ ]+@[ ]+0[ ]+\(0\)[ ]+\-\-\-"
#pat0 = r"\+\+\+ exited with \d+ \+\+\+"
#2073  22:09:09.432478 --- SIGSEGV (Segmentation fault) @ 0 (0) ---
pat19 = r"(\d+)[ ]+(\d+:\d+:\d+\.\d+)[ ]+\+\+\+[ ]+killed[ ]+by[ ]+SIGSEGV[ ]+\+\+\+"





regexp0 = re.compile(pat0)
regexp1 = re.compile(pat1)
regexp2 = re.compile(pat2)
regexp3 = re.compile(pat3)
regexp4 = re.compile(pat4)
regexp5 = re.compile(pat5)
regexp6 = re.compile(pat6)
regexp7 = re.compile(pat7)
regexp8 = re.compile(pat8)
regexp9 = re.compile(pat9)
regexp10 = re.compile(pat10)
#regexp11 = re.compile(pat11)
#regexp12 = re.compile(pat12)
regexp13 = re.compile(pat13)
regexp14 = re.compile(pat14)
regexp15 = re.compile(pat15)
regexp16 = re.compile(pat16)
regexp17 = re.compile(pat17)
regexp18 = re.compile(pat18)

regexp19 = re.compile(pat19)


autoDetectFormat()
