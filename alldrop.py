import sqlite3

conn = sqlite3.connect('sparse.db')
curs = conn.cursor()

	# parse3.py

curs.execute("DROP TABLE IF EXISTS syscall;");
curs.execute("DROP TABLE IF EXISTS sysdisp;");
curs.execute("DROP TABLE IF EXISTS unfinished;");
curs.execute("DROP TABLE IF EXISTS resumed;");

	#Perticular

curs.execute("DROP TABLE IF EXISTS paccess_tab;");
curs.execute("DROP TABLE IF EXISTS fstat_tab;");
curs.execute("DROP TABLE IF EXISTS filename;");
curs.execute("DROP TABLE IF EXISTS lstat_tab;");
curs.execute("DROP TABLE IF EXISTS stat_tab;");
curs.execute("DROP TABLE IF EXISTS mmap_tab;");
curs.execute("DROP TABLE IF EXISTS mprotect_tab;");
curs.execute("DROP TABLE IF EXISTS mprotect1;");
curs.execute("DROP TABLE IF EXISTS munmup_tab;");
curs.execute("DROP TABLE IF EXISTS munmap1;");
curs.execute("DROP TABLE IF EXISTS read_tab;");
curs.execute("DROP TABLE IF EXISTS read_final1;");
curs.execute("DROP TABLE IF EXISTS read_final;");
curs.execute("DROP TABLE IF EXISTS read_temp;");
curs.execute("DROP TABLE IF EXISTS write_tab;");
curs.execute("DROP TABLE IF EXISTS write_final1;");
curs.execute("DROP TABLE IF EXISTS write_final;");
curs.execute("DROP TABLE IF EXISTS write_temp;");
curs.execute("DROP TABLE IF EXISTS rt_sigaction_tab;");

	#Comparative

curs.execute("DROP TABLE IF EXISTS count_tab;");
curs.execute("DROP TABLE IF EXISTS error_tab;");
curs.execute("DROP TABLE IF EXISTS errorper_tab;");
curs.execute("DROP TABLE IF EXISTS time_tab;");
curs.execute("DROP TABLE IF EXISTS timeper_tab;");

	#Error Analysis

curs.execute("DROP TABLE IF EXISTS errana_tab");
