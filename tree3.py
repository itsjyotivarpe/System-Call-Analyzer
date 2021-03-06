#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

import sqlite3
import sys
from collections import defaultdict

countr=0

conn = sqlite3.connect('sparse.db')

curs = conn.cursor()
curs1 = conn.cursor()
childDict = defaultdict(list)

parents=[]
i=0


with conn:

	curs.execute("SELECT Parent,Child FROM temp1;")
	rows = curs.fetchall()
	for row in rows:
		#print row[0]
		pid=row[0]
		          
		if pid not in parents:
			print "new parent"
			parents.append(str(row[0]))
			i=i+1

			
		else:
			print "nothing"

	curs.execute("SELECT * FROM temp1;")
	rows = curs.fetchall()
	for row in rows:
		
		for Pid in parents:
			if(row[0]==Pid):
				childDict[Pid].append(str(row[1]))		
			#print childDict[Pid]	

	print childDict
	print childDict.keys()
	print childDict.values()
	#print parents
		
		

class BasicTreeView1:

    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        return False

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.window.set_title("PROCESS TREE")

        self.window.set_size_request(300, 300)

        self.window.connect("delete_event", self.delete_event)

        self.treestore = gtk.TreeStore(str)

        for parent in parents:
		piter = self.treestore.append(None, ['parent %s' % parent])
	    
                for child in childDict[parent]:
			print child
			print piter
			self.treestore.append(None, ['    |-- child %s of parent %s' % (child,parent)])

        self.treeview = gtk.TreeView(self.treestore)

        self.tvcolumn = gtk.TreeViewColumn('Column 0')

        self.treeview.append_column(self.tvcolumn)

        self.cell = gtk.CellRendererText()

        self.tvcolumn.pack_start(self.cell, True)

        self.tvcolumn.add_attribute(self.cell, 'text', 0)

        self.treeview.set_search_column(0)

        self.tvcolumn.set_sort_column_id(0)

        self.treeview.set_reorderable(True)

        self.window.add(self.treeview)

        self.window.show_all()

def main():
    gtk.main()

if __name__ == "__main__":
    tvexample = BasicTreeView1()
    main()

