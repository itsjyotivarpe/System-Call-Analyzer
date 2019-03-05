import sys
import sqlite3

fid1 = 0
filename1 = ''
read_cnt1 = 1
read_bytes1 = 0
write_cnt1 = 1
write_bytes1 = 0
temp = ''
zero = 0
unknown = 'unknown : '
count = 0
normal_file = '----'
lib_file = 'Library File'
lib1 = '/lib/'
lib2 = '/lib64/'
desc1 = ''


conn = sqlite3.connect('sparse.db')

curs = conn.cursor()
curs1 = conn.cursor()
curs2 = conn.cursor()
curs3 = conn.cursor()
curs4 = conn.cursor()

with conn:

	
	curs.executescript("""
        DROP TABLE IF EXISTS fileio_tab;
        CREATE TABLE fileio_tab(Filename TEXT, Description TEXT, Open_cnt INTEGER, Read_cnt INTEGER, Read_bytes INTEGER, Write_cnt INTEGER, Write_bytes INTEGER);
        """);
                    
	curs.executescript("""
        DROP TABLE IF EXISTS fileio_final;
        CREATE TABLE fileio_final(filename TEXT, read_cnt INTEGER, read_bytes INTEGER, write_cnt INTEGER, write_bytes INTEGER);
        """);
	curs.executescript("""
        DROP TABLE IF EXISTS fileio_temp;
        CREATE TABLE fileio_temp(fid INTEGER, filename TEXT, read_cnt INTEGER, read_bytes INTEGER, write_cnt INTEGER, write_bytes INTEGER);
        """);
    
    
    
        
	curs.execute("SELECT * FROM syscall")
	
	rows = curs.fetchall()
	for row in rows:
	    if row[2] == 'open':
	        fid1 = int(row[4])
	        temp = row[3].split(",")
	        filename1 = temp[0]
	        curs1.execute("""INSERT INTO fileio_temp VALUES('%s','%s','%s','%s','%s','%s');"""%(fid1, filename1, zero, zero, zero, zero))
	            
	    elif row[2] == 'close':
	        
	        temp = row[3].split(",")
	        fid1 = temp[0]
	        curs1.execute("""SELECT * FROM fileio_temp WHERE fid = '%s';"""%(fid1))
	        rows = curs1.fetchall()
	        for row in rows:
	            count = count + 1
	        if count == 0:
	            filename1 = 'unknown : '+fid1
	            curs1.execute("""INSERT INTO fileio_final VALUES('%s','%s','%s','%s','%s');"""%(filename1, zero, zero, zero, zero))
	            
	            
	        else:
	            curs4.execute("""SELECT * FROM fileio_temp WHERE fid = '%s';"""%(fid1))
	            rows = curs4.fetchall()
	            for row in rows:
	                filename1 = row[1]
	                read_cnt1 = row[2]
	                read_bytes1 = row[3]
	                write_cnt1 = row[4]
	                write_bytes1 = row[5]
	            if len(filename1) == 3:
	                unknown = unknown + fid1
	                curs1.execute("""DELETE FROM fileio_temp WHERE fid = '%s';"""%(fid1))
	                curs1.execute("""INSERT INTO fileio_final VALUES('%s','%s','%s','%s','%s');"""%(unknown, read_cnt1, read_bytes1, write_cnt1, write_bytes1))
	            
	            else:
	                curs1.execute("""DELETE FROM fileio_temp WHERE fid = '%s';"""%(fid1))
	                curs1.execute("""INSERT INTO fileio_final VALUES('%s','%s','%s','%s','%s');"""%(filename1, read_cnt1, read_bytes1, write_cnt1, write_bytes1))
	            
	        count = 0
	                
	        
	        
	    elif row[2] == 'read':
	    
	        temp = row[3].split(",")
	        fid1 = temp[0]
	        read_bytes1 = row[4]
	        curs3.execute("""SELECT * FROM fileio_temp WHERE fid = '%s';"""%(fid1))
	        rows = curs3.fetchall()
	        for row in rows:
	            count = count + 1
	        if count == 0:
	            filename1 = 'unknown : '+fid1
	            read_cnt1 = 1
	            curs1.execute("""INSERT INTO fileio_temp VALUES('%s','%s','%s','%s','%s','%s');"""%(fid1, filename1, read_cnt1, read_bytes1, zero, zero))
	            
	            
	        else:
	        
	            curs1.execute("""UPDATE fileio_temp SET read_cnt = read_cnt + 1 WHERE fid = '%s'"""%(fid1))
	            curs1.execute("""UPDATE fileio_temp SET read_bytes = read_bytes + '%s' WHERE fid = '%s'"""%(read_bytes1, fid1))
	        count = 0   
	        
	        
	    elif row[2] == 'write':
	        temp = row[3].split(",")
	        
	        fid1 = temp[0]
	        write_bytes1 = row[4]
	        curs3.execute("""SELECT * FROM fileio_temp WHERE fid = '%s';"""%(fid1))
	        rows = curs3.fetchall()
	        for row in rows:
	            count = count + 1
	        if count == 0:
	            write_cnt1 = 1
	            filename1 = 'unknown : '+fid1
	            curs1.execute("""INSERT INTO fileio_temp VALUES('%s','%s','%s','%s','%s','%s');"""%(fid1, filename1, zero, zero, write_cnt1, write_bytes1))
	        
	        else:
	        
	            curs1.execute("""UPDATE fileio_temp SET write_cnt = write_cnt + 1 WHERE fid = '%s'"""%(fid1))
	            curs1.execute("""UPDATE fileio_temp SET write_bytes = write_bytes + '%s' WHERE fid = '%s'"""%(write_bytes1, fid1))
	        count = 0
	    read_cnt1 = 1
        read_bytes1 = 0
        write_cnt1 = 1
        write_bytes1 = 0
       
        count = 0
	   
	    
	curs2.execute("select filename, COUNT(filename), sum(read_cnt), sum(read_bytes), sum(write_cnt), sum(write_bytes) from fileio_final GROUP BY filename;")
	rows = curs2.fetchall()
	for row in rows:
	    desc1 = normal_file
	    if lib1 in row[0]:
	        desc1 = lib_file
	    if lib2 in row[0]:
	        desc1 = lib_file
	    curs1.execute("""INSERT INTO fileio_tab VALUES('%s','%s','%s','%s','%s','%s','%s');"""%(row[0], desc1, row[1], row[2], row[3], row[4], row[5]))
	

	

