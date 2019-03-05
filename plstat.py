import sys
import sqlite3

filename = ''
Description = {}
lstat = ['lstat','lstat64']

conn = sqlite3.connect('sparse.db')

curs = conn.cursor()
curs2 = conn.cursor()

Description["S_IFMT"] = 'type of file mask'
Description["S_IFIFO"] = 'named pipe (fifo)'
Description["S_IFCHR"] = 'character special'
Description["S_IFDIR"] = 'directory'
Description["S_IFBLK"] = 'block special'
Description["S_IFREG"] = 'regular'
Description["S_IFLNK"] = 'symbolic link'
Description["S_IFSOCK"] = 'socket'
Description["S_IFWHT"] = 'whiteout'
Description["S_ISUID"] = 'set user id on execution'
Description["S_ISGID"] = 'set group id on execution'
Description["S_ISVTX"] = 'save swapped text even after use'
Description["S_IRWXU"] = 'RWX mask for owner'
Description["S_IRUSR"] = 'read permission, owner'
Description["S_IWUSR"] = 'write permission, owner'
Description["S_IXUSR"] = 'execute/search permission, owner'
Description["S_IRWXG"] = 'RWX mask for group'
Description["S_IRGRP"] = 'read permission, group'
Description["S_IWGRP"] = 'write permission, group'
Description["S_IXGRP"] = 'execute/search permission, group'
Description["S_IRWXO"] = 'RWX mask for other'
Description["S_IROTH"] = 'read permission, other'
Description["S_IWOTH"] = 'write permission, other'
Description["S_IXOTH"] = 'execute/search permission, other'

with conn:

	curs.executescript("""
		DROP TABLE IF EXISTS lstat_tab;
		CREATE TABLE lstat_tab(FileName TEXT, Mode TEXT, Description TEXT, Size INTEGER);
		""");

	curs2.execute("SELECT * FROM syscall")
	
	rows = curs2.fetchall()

	for row in rows:
		if row[2] in lstat:
			if row[4] =='0':
				tmp = row[3].split(",")
				filename = tmp[0]
				curs.execute("SELECT FILENAME FROM lstat_tab WHERE FileName = '%s';"%(filename))
				row = curs.fetchone()
				
				if row ==None:
					mode1 = tmp[1].split("{")
					mode2 = mode1[1].split("=")
					mode3 = mode2[1].split("|")
					mode = mode3[0]

					size1 = tmp[2].split("=")

					if size1[0]==' st_size':
						size = int(size1[1])
					else:
						size = '----'

					desc = Description[mode]

					curs.execute("INSERT INTO lstat_tab VALUES('%s','%s','%s','%s');"%(filename, mode, desc, size))

	'''
	curs.execute("SELECT * from lstat_tab")
	rows = curs.fetchall()

	for row in rows:
		print(' %s %15s %15s %10s ' %(row[0],row[1],row[2],row[3]))	
	'''

#define S_IFMT   0170000  /* type of file mask */
#define S_IFIFO  0010000  /* named pipe (fifo) */
#define S_IFCHR  0020000  /* character special */
#define S_IFDIR  0040000  /* directory */
#define S_IFBLK  0060000  /* block special */
#define S_IFREG  0100000  /* regular */
#define S_IFLNK  0120000  /* symbolic link */
#define S_IFSOCK 0140000  /* socket */
#define S_IFWHT  0160000  /* whiteout */
#define S_ISUID  0004000  /* set user id on execution */
#define S_ISGID  0002000  /* set group id on execution */
#define S_ISVTX  0001000  /* save swapped text even after use */
#define S_IRWXU  0000700  /* RWX mask for owner */
#define S_IRUSR  0000400  /* read permission, owner */
#define S_IWUSR  0000200  /* write permission, owner */
#define S_IXUSR  0000100  /* execute/search permission, owner */
#define S_IRWXG  0000070  /* RWX mask for group */
#define S_IRGRP  0000040  /* read permission, group */
#define S_IWGRP  0000020  /* write permission, group */
#define S_IXGRP  0000010  /* execute/search permission, group */
#define S_IRWXO  0000007  /* RWX mask for other */
#define S_IROTH  0000004  /* read permission, other */
#define S_IWOTH  0000002  /* write permission, other */
#define S_IXOTH  0000001  /* execute/search permission, other */

'''
st_rdev :  This field should be used only by administrative commands.  It
               is valid only for block special, character special, and files
               and directories accessed via "lofs" file systems. It only has
               meaning on the system where the file was configured.
'''
