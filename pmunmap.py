import sqlite3
import sys
count = 0
total_time = 0
avg_time = 0
temp = ''
size = ''
size = 0
mode1 = ''
addr = 0
addr1 = ''
final_addr = ''
error_count = 0
success_count = 0
min_time = 0
max_time = 0
min_addr = ''
success = 'Success'
fail = 'Fail'
max_addr = ''
status1 = ''

conn = sqlite3.connect('sparse.db')

curs = conn.cursor()
curs1 = conn.cursor()
def prot():

    with conn:
        
        count = 0
        total_time = 0
        avg_time = 0
        temp = ''
        size = ''
        size = 0
        mode1 = ''
        addr = 0
        addr1 = ''
        final_addr = ''
        error_count = 0
        success_count = 0
        min_time = 0
        max_time = 0
        min_addr = ''
        max_addr = ''


        curs.executescript("""
            DROP TABLE IF EXISTS munmap_tab;
            CREATE TABLE munmap_tab(StartTime TEXT, Address TEXT, Status TEXT, Time INTEGER);
            """);
        curs.executescript("""
            DROP TABLE IF EXISTS munmap1;
            CREATE TABLE munmap1(starttime TEXT, arg TEXT, error INTEGER, time INTEGER);
            """);
        curs.execute("SELECT StartTime, arg, ret, time FROM syscall WHERE SysName = 'munmap'")
        rows = curs.fetchall()
        for row in rows:
            count = count + 1
            curs.executescript("""INSERT INTO munmap1 VALUES('%s','%s','%s','%s');"""%(row[0], row[1], row[2], row[3]))
        #curs.execute("SELECT * FROM munmap1;")
        #rows = curs.fetchall()
        #for row in rows:
        #print row

        curs.execute("SELECT sum(time) FROM munmap1;")
        rows = curs.fetchall()

        for row in rows:
            total_time = row[0]

        avg_time = total_time/count
        #print "count : %s"%count
        #print "Total time : %s"%total_time
        #print "Avg time : %s"%avg_time

        curs.execute("SELECT * FROM syscall WHERE SysName = 'munmap' and ret = '1'")
        rows = curs.fetchall()

        for row in rows:
            error_count = error_count + 1

        curs.execute("SELECT * FROM syscall WHERE SysName = 'munmap' and ret = '0'")
        rows = curs.fetchall()

        for row in rows:
            success_count = success_count + 1

        #print "Unsuccessful munmap calls: %s"%error_count
        #print "Successful munmap calls: %s"%success_count

        curs.execute("SELECT starttime, arg, error, time FROM munmap1;")
        rows = curs.fetchall()

        for row in rows:
            #print row[1]
            temp = row[1].split(', ')
            #print temp[0]
            #print temp[1]
            size = temp[1]
            #print size
            #mode1 = temp[2]
            #print mode1
            size1 = int(size)
            addr = int(temp[0], 16)
            addr = addr + size1
            addr1 = ChangeHex(addr)
            final_addr = temp[0] + " - " + addr1

            if row[2] == 0:
                status1 = success

            if row[2] == 1:
                status1 = fail
                
            curs.executescript("""INSERT INTO munmap_tab VALUES('%s','%s','%s','%s');"""%(row[0], final_addr, status1, row[3]))

        curs1.execute("SELECT * FROM munmap_tab;")
        rows = curs1.fetchall()
        #print " Following addresses are unmapped if one tries to access it then error will occur"
       
	'''
        for row in rows:
            print row
        curs.execute("SELECT addr, min(time) FROM munmap2;")
        rows = curs.fetchall()
        for row in rows:
            min_addr = row[0]
            min_time = row[1]
        print "Min time : %s is consumed for unmapping addr %s"%(min_time, min_addr)
        curs.execute("SELECT addr, max(time) FROM munmap2;")
        rows = curs.fetchall()
        for row in rows:
            max_addr = row[0]
            max_time = row[1]
        print "Max time : %s is consumed for unmapping  addr %s"%(max_time, max_addr)
        '''

def ChangeHex(n):
    x = (n % 16)
    c = ""
    if (x < 10):
        c = x
    if (x == 10):
        c = "A"
    if (x == 11):
        c = "B"
    if (x == 12):
        c = "C"
    if (x == 13):
        c = "D"
    if (x == 14):
        c = "E"
    if (x == 15):
        c = "F"

    if (n - x != 0):
        
        return ChangeHex(n / 16) + str(c)
    else:
        return str(c)
	
	

prot()
