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
max_addr = ''
desc = ''
success = 'Success'
fail = 'Fail'
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
        desc1 = ''


        curs.executescript("""
            DROP TABLE IF EXISTS mprotect_tab;
            CREATE TABLE mprotect_tab(StartTime TEXT, Address TEXT,Mode TEXT, Description TEXT, Status TEXT, Time INTEGER);
            """);
        curs.executescript("""
            DROP TABLE IF EXISTS mprotect1;
            CREATE TABLE mprotect1(starttime TEXT, arg TEXT, error INTEGER, time INTEGER);
            """);
        curs.execute("SELECT StartTime, arg, ret, time FROM syscall WHERE SysName = 'mprotect'")
        rows = curs.fetchall()
        for row in rows:
            count = count + 1
            curs.executescript("""INSERT INTO mprotect1 VALUES('%s','%s','%s','%s');"""%(row[0], row[1], row[2], row[3]))

        

        curs.execute("SELECT sum(time) FROM mprotect1;")
        rows = curs.fetchall()

        for row in rows:
            total_time = row[0]

        avg_time = total_time/count

        
        curs.execute("SELECT * FROM syscall WHERE SysName = 'mprotect' and ret = '1'")
        rows = curs.fetchall()

        for row in rows:
            error_count = error_count + 1

        curs.execute("SELECT * FROM syscall WHERE SysName = 'mprotect' and ret = '0'")
        rows = curs.fetchall()

        for row in rows:
            success_count = success_count + 1
        

        curs.execute("SELECT starttime, arg, error, time FROM mprotect1;")
        rows = curs.fetchall()
        for row in rows:
            temp = row[1].split(', ')
            size = temp[1]
            mode1 = temp[2]
            size1 = int(size)
            addr = int(temp[0], 16)
            addr = addr + size1
            addr1 = ChangeHex(addr)
            final_addr = temp[0] + " - " + addr1

            if mode1 == 'PROT_NONE':
                desc1 = 'This memory cannot be accessed !!!'

            if mode1 == 'PROT_READ':
                desc1 = 'This memory can be read !!!'

            if mode1 == 'PROT_WRITE':
                desc1 = 'This memory can be modified !!!'

            if mode1 == 'PROT_EXEC':
                desc1 = 'This memory can be executed !!!'

            if row[2] == 0:
                status1 = success

            if row[2] == 1:
                status1 = fail
            
            curs.executescript("""INSERT INTO mprotect_tab VALUES('%s','%s','%s','%s','%s','%s');"""%(row[0], final_addr, mode1, desc1, status1, row[3]))


        
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
