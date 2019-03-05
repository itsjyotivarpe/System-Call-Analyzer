import sys
import sqlite3
import re

fid1 = 0
filename1 = ''
read_cnt1 = 1
read_bytes1 = 0
write_cnt1 = 1
write_bytes1 = 0
time_spent1 = 0
temp = ''
zero = 0
null = ''
unknown = 'unknown : '
count = 0
call1 = 1
call_str1 =''
call_str = ''

conn = sqlite3.connect('sparse.db')

curs = conn.cursor()
curs1 = conn.cursor()
curs2 = conn.cursor()
curs3 = conn.cursor()
curs4 = conn.cursor()

with conn:

	
	curs.executescript("""
        DROP TABLE IF EXISTS write_tab;
        CREATE TABLE write_tab(call INTEGER, bytes INTEGER);
        """);
	curs.executescript("""
        DROP TABLE IF EXISTS write_final1;
        CREATE TABLE write_final1(filename TEXT, call TEXT, write_cnt INTEGER, write_bytes INTEGER, time INTEGER);
        """);
                    
	curs.executescript("""
        DROP TABLE IF EXISTS write_final;
        CREATE TABLE write_final(filename TEXT, call TEXT, write_cnt INTEGER, write_bytes INTEGER, time INTEGER);
        """);
	curs.executescript("""
        DROP TABLE IF EXISTS write_temp;
        CREATE TABLE write_temp(fid INTEGER, filename TEXT, call TEXT, write_cnt INTEGER, write_bytes INTEGER, time INTEGER);
        """);
    
    
    
        
	        
	curs.execute("SELECT * FROM syscall")
	
	rows = curs.fetchall()
	for row in rows:
	    
	    if row[2] == 'open':
	        fid1 = int(row[4])
	        
	        temp = row[3].split(",")
	        filename1 = temp[0]
	        
	        curs1.execute("""INSERT INTO write_temp VALUES('%s','%s','%s','%s','%s','%s');"""%(fid1, filename1, null, zero, zero, zero))
	            
	    elif row[2] == 'close':
	        
	        temp = row[3].split(",")
	        
	        fid1 = temp[0]
	        
	        curs1.execute("""SELECT * FROM write_temp WHERE fid = '%s';"""%(fid1))
	        
	        rows = curs1.fetchall()
	        for row in rows:
	            count = count + 1
	        if count == 0:
	            filename1 = 'unknown : '+fid1
	            
	            curs1.execute("""INSERT INTO write_final VALUES('%s','%s','%s','%s','%s');"""%(filename1, null, zero, zero, zero))
	            
	            
	        else:
	            curs4.execute("""SELECT * FROM write_temp WHERE fid = '%s';"""%(fid1))
	            rows = curs4.fetchall()
	            for row in rows:
	                
	                filename1 = row[1]
	                
	                call_str1 = row[2]
	                write_cnt1 = row[3]
	                
	                write_bytes1 = row[4]
	            
	                
	                time_spent1 = row[5]
	                
	            if len(filename1) == 3:
	                
	                unknown = unknown + fid1
	                curs1.execute("""DELETE FROM write_temp WHERE fid = '%s';"""%(fid1))
	                curs1.execute("""INSERT INTO write_final VALUES('%s','%s','%s','%s','%s');"""%(unknown, call_str1, write_cnt1, write_bytes1, time_spent1))
	            
	            else:
	                
	                curs1.execute("""DELETE FROM write_temp WHERE fid = '%s';"""%(fid1))
	                curs1.execute("""INSERT INTO write_final VALUES('%s','%s','%s','%s','%s');"""%(filename1, call_str1, write_cnt1, write_bytes1, time_spent1))
	            
	        count = 0
	        call_str1 = ''
	                

	        
	        
	    elif row[2] == 'write':
		if(re.match('[0-9]',row[4])):
	        
            	    
			temp = row[3].split(",")
			fid1 = temp[0]
			
			write_bytes1 = row[4]
			curs3.execute("""INSERT INTO write_tab VALUES('%s','%s');"""%(call1, write_bytes1))
			 
			time_spent1 = row[5]
			call_str1 = str(call1)
			
			curs3.execute("""SELECT * FROM write_temp WHERE fid = '%s';"""%(fid1))
			rows = curs3.fetchall()
			for row in rows:
			    count = count + 1
			if count == 0:
			    
			    filename1 = 'unknown : '+fid1
			    
			    write_cnt1 = 1
			    curs1.execute("""INSERT INTO write_temp VALUES('%s','%s','%s','%s','%s','%s');"""%(fid1, filename1, call_str1, write_cnt1, write_bytes1, time_spent1))
			    
			    
			else:
			    
			    curs1.execute("""UPDATE write_temp SET write_cnt = write_cnt + 1 WHERE fid = '%s'"""%(fid1))
			    curs1.execute("""UPDATE write_temp SET write_bytes = write_bytes + '%s' WHERE fid = '%s'"""%(write_bytes1, fid1))
			    curs1.execute("""UPDATE write_temp SET time = time + '%s' WHERE fid = '%s'"""%(time_spent1, fid1))
			    curs1.execute("""SELECT call FROM write_temp WHERE fid = '%s';"""%(fid1))
			    rows = curs1.fetchall()
			    for row in rows:
			        call_temp = row[0]
			        if call_temp == '':
			            call_str = call_temp +" "+str(call1)
			        else:
			            call_str = call_temp +" , "+str(call1)
			            
			    curs1.execute("""UPDATE write_temp SET call = '%s' WHERE fid = '%s'"""%(call_str, fid1))
			    
			count = 0   
			call1 = call1 + 1
			call_str = ''
	        
	    
	    
        read_cnt1 = 1
        read_bytes1 = 0
        write_cnt1 = 1
        write_bytes1 = 0
       
        count = 0
        
	    	
	    
	curs3.execute("select filename, call, write_cnt, write_bytes, time from write_temp;")
	rows = curs3.fetchall()
	for row in rows:
	    curs1.execute("""INSERT INTO write_final VALUES('%s','%s','%s','%s','%s');"""%(row[0], row[1], row[2], row[3], row[4]))
	    
	curs2.execute("select * from write_final;")
	
	rows = curs2.fetchall()
	for row in rows:
	      
	    if row[2]>0:
	        
	        curs1.execute("""INSERT INTO write_final1 VALUES('%s','%s','%s','%s','%s');"""%(row[0], row[1], row[2], row[3], row[4]))
	
	print ""
	
	curs.execute("select COUNT(SysName) from syscall WHERE SysName = 'write';")
	rows=curs.fetchall()
	for row in rows:
	    print "Write call Count: %s"%row[0]
	    cnt = row[0]
	curs.execute("select SUM(ret) from syscall WHERE SysName = 'write';")
	rows=curs.fetchall()
	for row in rows:
	    print "Total bytes written: %s"%row[0]
	    bytes = row[0]
	curs.execute("select SUM(time) from syscall WHERE SysName = 'write';")
	rows=curs.fetchall()
	for row in rows:
	   print "Total_time : %s(usec)"%row[0]
	   total_time = row[0]
	   avg_bytes_per_call = bytes/cnt
	print "Avg bytes per call : %s"%avg_bytes_per_call
	curs.execute("select MIN(time) from syscall WHERE SysName = 'write';")
	rows=curs.fetchall()
	for row in rows:
	    print "Min time : %s (usec)"%row[0]
	    slow_time = row[0]  
	curs.execute("select MAX(time) from syscall WHERE SysName = 'write';")
	rows=curs.fetchall()
	for row in rows:
	    print "Max time : %s (usec)"%row[0]
	    fast_time = row[0]
	

	

