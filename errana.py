import sqlite3
import sys
string={}


countr=0

conn = sqlite3.connect('sparse.db')

curs = conn.cursor()

with conn:

	curs.executescript("""
        DROP TABLE IF EXISTS errors;
        CREATE TABLE errors(SYSNAME TEXT,TIME INTEGER,ERRORS TEXT,SOLUTION TEXT);
        """);

	
	curs.execute("SELECT Pid,SysName,arg,Error,StartTime,desc FROM syscall WHERE ret LIKE '-1';")
	rows = curs.fetchall()
	for row in rows:
		string=row[2].split(" ")
		
		if(row[3]=='ENOENT'):
			Line="Call failed as,The File Specified by %s  Not Found!" %(string[0])
			soln="Check for path and directories"
			curs.execute("INSERT INTO errors VALUES('%s','%s','%s','%s');"%(row[1],row[4],Line,soln))

			
		elif(row[3]=='ECHILD'):
			Line="The process specified by pid  %s does not exist or is not a child of the calling process"%(row[0])
			soln="Check for valid child"
			curs.execute("INSERT INTO errors VALUES('%s','%s','%s','%s');"%(row[1],row[4],Line,soln))

		elif(row[3]=='EAGAIN'):
			Line="There is nothing to read now.. ! or Timeout reading from the socket."
			soln="Try again later"
			curs.execute("INSERT INTO errors VALUES('%s','%s','%s','%s');"%(row[1],row[4],Line,soln))

		elif(row[3]=='EPERM'):
			Line="Operation is not permitted"
			soln="Please check for privileges"
			curs.execute("INSERT INTO errors VALUES('%s','%s','%s','%s');"%(row[1],row[4],Line,soln))


		
		elif(row[3]=='ENOTDIR'):
			Line="A component of the path prefix is not a directory!"
			soln=" check for valid directory in the path"
			curs.execute("INSERT INTO errors VALUES('%s','%s','%s','%s');"%(row[1],row[4],Line,soln))

		
		elif(row[3]=='ENOMEM'):
			Line="System Out Of Memory as it is holding onto objects for too long, or trying to process too much data at a time.!"
			soln="Try read block method!!Or compress data "
			curs.execute("INSERT INTO errors VALUES('%s','%s','%s','%s');"%(row[1],row[4],Line,soln))

		elif(row[3]=='ENOTSOCK'):
			Line="Socket operation has been performed on non-socket!"
			soln="Check for socket connection"
			curs.execute("INSERT INTO errors VALUES('%s','%s','%s','%s');"%(row[1],row[4],Line,soln))

		elif(row[3]=='EMULTIHOP'):
			Line="Components of path require hopping to multiple remote machines and the file system does not allow it!"
		 	soln="Check the config for multihop entry device if their is an exit OR Execute in safe mode"
			curs.execute("INSERT INTO errors VALUES('%s','%s','%s','%s');"%(row[1],row[4],Line,soln))

		elif(row[3]=='ENAMETOOLONG'):
			Line="The length of the path argument exceeds {PATH_MAX}, or the length of a path component exceeds {NAME_MAX}!"
			soln="Check the path components "
			curs.execute("INSERT INTO errors VALUES('%s','%s','%s','%s');"%(row[1],row[4],Line,soln))

		elif(row[3]=='ENOLINK'):
			Line="path points to a remote machine and the link to that machine is no longer active!"
			soln="Check for link pointed by pa`zth "
			curs.execute("INSERT INTO errors VALUES('%s','%s','%s','%s');"%(row[1],row[4],Line,soln))

		elif(row[3]=='EOVERFLOW'):
			Line="A component is too large to store in the structure pointed to by buf!"
			soln="Reduce the component size! "
			curs.execute("INSERT INTO errors VALUES('%s','%s','%s','%s');"%(row[1],row[4],Line,soln))

		elif(row[3]=='EBADF'):
			Line="file descriptor is not a valid !"
			soln="check for valid file decsriptor"
			curs.execute("INSERT INTO errors VALUES('%s','%s','%s','%s');"%(row[1],row[4],Line,soln))

		elif(row[3]=='EFAULT'):
			Line="buf or path points to an Invalid Address or invalid Descriptor"
			soln="Check for Address or Descriptor"
			curs.execute("INSERT INTO errors VALUES('%s','%s','%s','%s');"%(row[1],row[4],Line,soln))

		
		elif(row[3]=='EINTR'):
			Line="Interrupted function call.An asynchronous signal occurred and prevented completion of the call"
			soln="Try the call again. !"
	
			curs.execute("INSERT INTO errors VALUES('%s','%s','%s','%s');"%(row[1],row[4],Line,soln))
		
		elif(row[3]=='ESRCH'):
			Line="No process matches the specified Process Id"
			soln=" Verify the process Id "
	
			curs.execute("INSERT INTO errors VALUES('%s','%s','%s','%s');"%(row[1],row[4],Line,soln))
		
			
		elif(row[3]=='EACCES'):
			Line="Permission Denied"
			soln="Check for the Permissions on File "
	
			curs.execute("INSERT INTO errors VALUES('%s','%s','%s','%s');"%(row[1],row[4],Line,soln))
		
		elif(row[3]=='EBUSY'):
			Line="Resource being accessed is busy and cannot be shared"
			soln="Try after some time.. "
	
			curs.execute("INSERT INTO errors VALUES('%s','%s','%s','%s');"%(row[1],row[4],Line,soln))
		
		elif(row[3]=='EEXIST'):
			Line="File specified by %s already exists "%(string[0])
			soln="Check for the Permissions on File "
	
			curs.execute("INSERT INTO errors VALUES('%s','%s','%s','%s');"%(row[1],row[4],Line,soln))
				
		elif(row[3]=='EFBIG'):
			Line="File specified by %s is too large "%(string[0])
			soln="Check for the file size "
	
			curs.execute("INSERT INTO errors VALUES('%s','%s','%s','%s');"%(row[1],row[4],Line,soln))				

		elif(row[3]=='ENOTTY'):
			Line="An attempt is made to configure device properties on a file which is not a special file."
			soln="Check for the Permissions on File accessed by ioctl."
	
			curs.execute("INSERT INTO errors VALUES('%s','%s','%s','%s');"%(row[1],row[4],Line,soln))				
		else:
			soln="Check for the Permissions on File accessed by ioctl."
			curs.execute("INSERT INTO errors VALUES('%s','%s','%s','%s');"%(row[1],row[4],row[5],soln))



	curs.execute("SELECT * FROM errors ;")
	rows = curs.fetchall()
	for row in rows:
		print(' %s %15s %15s' %(row[0],row[1],row[2]))
	
		
