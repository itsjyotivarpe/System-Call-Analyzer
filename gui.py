# Guinew1.py

import commands
import wx
import sqlite3
import wx.grid
import pylab as p
import os
paths = ""
newpath = ""
wildcard = "All files (*.*)|*.*"

row_no = 0
col_no = 0
column = []
col1 = 0
col2 = 0
row1 = 0
row2 = 0
row_str = ''
row_value_str = ''
name = ''
flag1 = 1
flag2 = 0

conn = sqlite3.connect('sparse.db')

curs = conn.cursor()		#for syscall
curs1 = conn.cursor()		#for unfinished
curs2 = conn.cursor()		#for timegraph

ID_FILE_OPEN = wx.NewId()
ID_FILE_INPUT = wx.NewId()
ID_FILE_HOME = wx.NewId()
ID_FILE_PERT = wx.NewId()
ID_FILE_COMP = wx.NewId()

class Example(wx.Frame):
    
	flag1 = 1
	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)
		self.InitUI()
		self.frame1 = wx.Frame(self, -1, 'System Call Analyzer', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.framedisp = wx.Frame(self, -1, 'System Call Analyser Output ', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.framePert = wx.Frame(self, -1, 'Statistics Of Special System Calls ', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.framecomp = wx.Frame(self, -1, 'Comparative Statics of All System Calls ', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameop = wx.Frame(self, -1, 'System Call Trace Output', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameUnfin = wx.Frame(self, -1, 'Unfinished And Resumed Calls Statistics', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameCode = wx.Frame(self, -1, 'Code Optimization', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameFileio = wx.Frame(self, -1, 'File Input/Output Statistics', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameErrana = wx.Frame(self, -1, 'Error Analysis', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameSummary = wx.Frame(self, -1, 'Summary of All System Calls', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameRead = wx.Frame(self, -1, 'Particular Systam Call Statistics : READ', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameWrite = wx.Frame(self, -1, 'Particular Systam Call Statistics : WRITE', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameAccess = wx.Frame(self, -1, 'Particular Systam Call Statistics : ACCESS', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.framePipe = wx.Frame(self, -1, 'Particular System Call Statistics : Pipe', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameFstat = wx.Frame(self, -1, 'Particular Systam Call Statistics : FSTAT/FSTAT64', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameStat = wx.Frame(self, -1, 'Particular Systam Call Statistics : STAT/STAT64', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameLstat = wx.Frame(self, -1, 'Particular Systam Call Statistics : LSTAT/LSTAT64', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameMmap = wx.Frame(self, -1, 'Particular Systam Call Statistics : MMAP', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameMprotect = wx.Frame(self, -1, 'Particular Systam Call Statistics : MPROTECT', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameMunmap = wx.Frame(self, -1, 'Particular System Call Statistics : MUNMAP', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameRt_sigaction = wx.Frame(self, -1, 'Particular System Call Statistics : RT_SIGACTION', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameUname = wx.Frame(self, -1, 'Particular Systam Call Statistics : UNAME', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameSigchild = wx.Frame(self, -1, 'Particular Signals Statistics : SIGCHILD', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		#self.frameSigsegv = wx.Frame(self, -1, 'Particular Signal Statistics : SIGSEGV', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameTime = wx.Frame(self, -1, 'Time Consumption of All System Calls', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.framePerTime = wx.Frame(self, -1, 'Percentage Time Consumption of All System Calls', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameErr = wx.Frame(self, -1, 'Errors in All System Calls', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.framePerErr = wx.Frame(self, -1, 'Percentage Errors in All System Calls', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameCnt = wx.Frame(self, -1, 'Count of All System Calls', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameSysTrace = wx.Frame(self, -1, 'System Call Trace Output', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameSigTrace = wx.Frame(self, -1, 'Signals Trace Output', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameUnfini = wx.Frame(self, -1, 'Unfinished System Calls', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameResumed = wx.Frame(self, -1, 'Resumed System Calls', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameInfo = wx.Frame(self, -1, 'Information of All System Calls in Particular Statistics', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameRefer1 = wx.Frame(self, -1, 'Code Optimization : Escape Charactors', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameRefer2 = wx.Frame(self, -1, 'Code Optimization : fflush(stdout)', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameRefer3 = wx.Frame(self, -1, 'Code Optimization : Pass by Value & Pass by Reference', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameRefer4 = wx.Frame(self, -1, 'Code Optimization : File Operations', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameRefer5 = wx.Frame(self, -1, 'Code Optimization : Looping Constructions', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameHints = wx.Frame(self, -1, 'Some Hints For Code Optimization', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameTest = wx.Frame(self, -1, 'Code Optimization : Test your Program', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameProgName = wx.Frame(self, -1, 'Program Name', pos = (300,300), size = (500,200), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.framePNCont = wx.Frame(self, -1, 'Program Name', pos = (300,300), size = (500,200), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.frameerr = wx.Frame(self, -1, 'Error ', pos = (300,300), size = (500,200))
		self.frameerr1 = wx.Frame(self, -1, 'Error ', pos = (300,300), size = (500,200))
		self.frameNoFind = wx.Frame(self, -1, 'Warning ', pos = (300,300), size = (500,200))
		self.frameNoDir = wx.Frame(self, -1, 'Warning ', pos = (300,300), size = (500,200))
		self.framefire = wx.Frame(self, -1, 'Warning ', pos = (300,300), size = (450,175))
		self.frameGraph = wx.Frame(self, -1, 'Graph ', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)


	def InitUI(self):
		self.SetSize((800, 400))
		self.SetPosition((150, 150))
		self.SetTitle('System Call Analyzer')
		self.Centre()
		self.Show(True)

		# Font for the text

		self.font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
		self.font.SetPointSize(15)

		# Menubar

		self.menubar = wx.MenuBar()

		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)

		self.SetMenuBar(self.menubar)

		# self.panel for main screen

		self.panel = wx.Panel(self)
		self.panel.SetBackgroundColour('LightSlateGray')
		self.vbox = wx.BoxSizer(wx.VERTICAL)

		self.stpwd = wx.StaticText(self.panel, label='Enter Password')
		self.stpwd.SetFont(self.font)
		self.vbox.Add(self.stpwd, flag=wx.CENTER, border=200)

		self.tcpwd = wx.TextCtrl(self.panel, style=wx.TE_PASSWORD)
		self.vbox.Add(self.tcpwd, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=200)

		self.btn1 = wx.Button(self.panel, label='Start', size=(200, 100))
		self.btn1.Bind(wx.EVT_BUTTON, self.OnClick1)
		self.vbox.Add(self.btn1, flag=wx.ALIGN_CENTER | wx.TOP, border=50)
		self.panel.SetSizer(self.vbox)

	def OnClick1(self, e):
		pwd = self.tcpwd.GetValue()
	
		if pwd!="sparse123":
			self.frameerr2 = wx.Frame(self, -1, 'Error ', pos = (300,300), size = (500,200))
			self.panelerrpwd = wx.Panel(self.frameerr2)
			self.hboxerrpwd = wx.BoxSizer(wx.HORIZONTAL)
			self.sterrpwd = wx.StaticText(self.panelerrpwd, label='Wrong Password ...')
			self.sterrpwd.SetFont(self.font)
			self.hboxerrpwd.Add(self.sterrpwd, flag=wx.RIGHT, border=200)
			self.panelerrpwd.SetSizer(self.hboxerrpwd)
			self.frameerr2.Show()
		else:
			if not self.frame1:
				self.frame1 = wx.Frame(self, -1, 'System Call Analyzar', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
			self.menubar = wx.MenuBar()
			self.fileMenu = wx.Menu()
			self.fitem = self.fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
			self.menubar.Append(self.fileMenu, '&File')
			self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)

			self.frame1.SetMenuBar(self.menubar)
		
		    # self.panel for screen Through Command

			self.panel1 = wx.Panel(self.frame1)
			self.panel1.SetBackgroundColour('LightSlateGray')
			self.vbox11 = wx.BoxSizer(wx.VERTICAL)
			self.hbox11 = wx.BoxSizer(wx.HORIZONTAL)

			self.st1 = wx.StaticText(self.panel1, label='Enter Command : ')
			self.st1.SetFont(self.font)
			self.hbox11.Add(self.st1, flag=wx.RIGHT, border=200)

			self.tc11 = wx.TextCtrl(self.panel1)
			self.hbox11.Add(self.tc11, proportion=1)
			self.vbox11.Add(self.hbox11, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=100)
			self.vbox11.Add((-1, 10))

			self.hbox12 = wx.BoxSizer(wx.HORIZONTAL)

			self.st2 = wx.StaticText(self.panel1, label='Enter Filename(If Required):')
			self.st2.SetFont(self.font)
			self.hbox12.Add(self.st2, flag=wx.RIGHT, border=200)

			self.tc12 = wx.TextCtrl(self.panel1)
			self.hbox12.Add(self.tc12, proportion=1)

			self.stbr = wx.StaticText(self.panel1, label='  ')
			self.stbr.SetFont(self.font)
			self.hbox12.Add(self.stbr, flag= wx.LEFT)

			self.btnbr = wx.Button(self.panel1, label='Browse', size=(100, 30))
			self.btnbr.Bind(wx.EVT_BUTTON, self.OnBr)
			self.hbox12.Add(self.btnbr, flag = wx.RIGHT, border=30) 

			self.vbox11.Add(self.hbox12, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=100)
			self.vbox11.Add((-1, 10))

			self.btn11 = wx.Button(self.panel1, label='SUBMIT', size=(200, 100))
			self.btn11.Bind(wx.EVT_BUTTON, self.OnClick11)
			self.vbox11.Add(self.btn11, flag = wx.TOP | wx.CENTER, border=100) 

			self.panel1.SetSizer(self.vbox11)
			self.frame1.Show()

	def OnBr(self, e):
		self.frame1.Hide()
		dlg = wx.FileDialog(
		    self, message="Choose a file",
		    defaultDir=os.getcwd(),
		    defaultFile="",
		    wildcard=wildcard,
		    style=wx.OPEN
		    )
		if dlg.ShowModal() == wx.ID_OK:
		    paths = dlg.GetPaths()
		    newpath = paths
		    self.tc12.SetValue(newpath[0])
		self.frame1.Show()

	def OnQuit(self, e):
		self.Close()
		commands.getstatusoutput("python alldrop.py")


	#Click on SUBMIT button

	def OnClick11(self, e):

		filenm=''
		list1 = ['./a.out', 'cat', 'find', 'cksum', 'dc', 'dd', 'expand', 'factor', 'fmt', 'fold', 'head', 'nl', 'paste', 'pr', 'sort', 'split', 'su', 'sum', 'tac', 'wc','unexpand','uniq']
		list2 = ['vi', 'firefox', 'bc', 'ed', 'fsck', 'info', 'lpc', 'passwd', 'shutdown', 'sleep','tee','top','tsort','yes']
		cmd1 = self.tc11.GetValue()
		cmd = cmd1.lower()

		if cmd in list2:
			if not self.frameerr:
				self.frameerr = wx.Frame(self, -1, 'Error ', pos = (300,300), size = (500,200))

			self.panelerr = wx.Panel(self.frameerr)
			self.vboxerr = wx.BoxSizer(wx.VERTICAL)
			self.hboxerr1 = wx.BoxSizer(wx.HORIZONTAL)
			self.sterr = wx.StaticText(self.panelerr, label='Command NOT allowed ...')
			self.sterr.SetFont(self.font)
			self.hboxerr1.Add(self.sterr, flag=wx.RIGHT, border=200)
			self.vboxerr.Add(self.hboxerr1, flag=wx.LEFT | wx.RIGHT | wx.TOP, border=15)
			self.vboxerr.Add((-1, 10))
			self.hboxerr2 = wx.BoxSizer(wx.HORIZONTAL)
			self.btnok = wx.Button(self.panelerr, label='OK', size=(100, 50))
			self.btnok.Bind(wx.EVT_BUTTON, self.Oncncl)
			self.hboxerr2.Add(self.btnok, flag=wx.LEFT | wx.RIGHT, border=50)
			self.vboxerr.Add(self.hboxerr2, flag=wx.CENTER | wx.BOTTOM, border=15)
			self.vboxerr.Add((-1, 10))
			self.panelerr.SetSizer(self.vboxerr)
			self.frameerr.Show()

		elif cmd in list1:
			filenm = self.tc12.GetValue()

			if filenm=='':
				if not self.frameerr1:
					self.frameerr1 = wx.Frame(self, -1, 'Error ', pos = (300,300), size = (500,200))
				self.panelerr = wx.Panel(self.frameerr1)
				self.hboxerr = wx.BoxSizer(wx.HORIZONTAL)
				if cmd == 'factor':
					self.sterr = wx.StaticText(self.panelerr, label='Enter Number of which prime factors to \n be calculated in the "File Name" text box please ...')
				elif cmd == 'su':
					self.sterr = wx.StaticText(self.panelerr, label='Enter the password of user in the \n text box please ...')
				else:
					self.sterr = wx.StaticText(self.panelerr, label='Enter File Name Please ...')

				self.sterr.SetFont(self.font)
				self.hboxerr.Add(self.sterr, flag=wx.RIGHT, border=200)
				self.panelerr.SetSizer(self.hboxerr)
				self.frameerr1.Show()

			elif cmd == './a.out':
				cc = 'cc '+filenm
				commands.getoutput(cc)
				commands.getoutput("strace -o sample.txt -tt -T -f ./a.out")
				commands.getoutput("python parse4.py")
				self.disp()

			elif cmd == 'dd':
				trace = 'strace -o sample.txt -tt -T -f dd if='+filenm
				commands.getoutput(trace)
				commands.getoutput("python parse4.py")
				self.disp()

			else:
				self.run()

		else:
			#strace: Can't stat 'abc': No such file or directory
			strace = "strace "+cmd
			op = commands.getstatusoutput(strace)
			find = "strace: Can't stat '"+cmd+"': No such file or directory"

			if op[1] == find:
				if not self.frameNoFind:
					self.frameNoFind = wx.Frame(self, -1, 'Warning ', pos = (300,300), size = (500,200))
				self.panelNoFind = wx.Panel(self.frameNoFind)
				self.hboxNoFind = wx.BoxSizer(wx.HORIZONTAL)
				self.stNoFind = wx.StaticText(self.panelNoFind, label='Specified command is invalid...\n Please Re-enter the command!!! ...')
				self.stNoFind.SetFont(self.font)
				self.hboxNoFind.Add(self.stNoFind, flag=wx.RIGHT, border=200)
				self.panelNoFind.SetSizer(self.hboxNoFind)
				self.frameNoFind.Show()

			else:
				self.run()

	#Click on OK button in firefox warning window

	def OnOK(self, e):
		commands.getoutput("strace -o sample.txt -tt -f -TT firefox")
		commands.getstatusoutput("python fireclose.py")
		self.framefire.Hide()
		self.disp()

	#Click on CANCEL button in firefox warning window
	def Oncncl(self, e):
		self.tc11.SetValue(" ")
		self.framefire.Hide()
		self.frameerr.Hide()
	
	#Parsing strace output
	def run(self):
		cmd1 = self.tc11.GetValue()
		cmd = cmd1.lower()
		filenm = self.tc12.GetValue()
		if cmd != 'factor':
			if filenm != '':
				cat = "cat "+filenm
				fileavail = commands.getstatusoutput(cat)
				nodir = "cat: "+filenm+": No such file or directory"

				if fileavail[1] == nodir:
					self.NoDir()
				else:
					trace = "strace -o sample.txt -tt -f -TT "+cmd+" "+filenm
					output = commands.getstatusoutput(trace)
					commands.getstatusoutput("python parse4.py")
					self.disp()
			else:
				trace = "strace -o sample.txt -tt -f -TT "+cmd
				output = commands.getstatusoutput(trace)
				commands.getstatusoutput("python parse4.py")
				self.disp()

		else:
			trace = "strace -o sample.txt -tt -f -TT "+cmd+" "+filenm
			output = commands.getstatusoutput(trace)
			commands.getstatusoutput("python parse4.py")
			self.disp()

	def NoDir(self):
		if not self.frameNoDir:
			self.frameNoDir = wx.Frame(self, -1, 'Warning ', pos = (300,300), size = (500,200))
		self.panelNoDir = wx.Panel(self.frameNoDir)
		self.hboxNoDir = wx.BoxSizer(wx.HORIZONTAL)
		self.stNoDir = wx.StaticText(self.panelNoDir, label='Specified File is not present in this Directory...\n Please Re-enter the filename!!! ...')
		self.stNoDir.SetFont(self.font)
		self.hboxNoDir.Add(self.stNoDir, flag=wx.RIGHT, border=200)
		self.panelNoDir.SetSizer(self.hboxNoDir)
		self.frameNoDir.Show()

	def OnInput(self, e):
		self.framedisp.Hide()
		self.framePert.Hide()
		self.framecomp.Hide()
		self.frameop.Hide()
		self.frameUnfin.Hide()
		#self.frameProgName.Hide()
		self.framePNCont.Hide()
		self.frameCode.Hide()
		self.frameErrana.Hide()
		self.frameFileio.Hide()
		self.frameSummary.Hide()
		self.frameRead.Hide()
		self.frameWrite.Hide()
		self.frameAccess.Hide()
		self.frameFstat.Hide()
		self.frameStat.Hide()
		self.frameLstat.Hide()
		self.frameMmap.Hide()
		self.frameMunmap.Hide()
		self.frameMprotect.Hide()
		self.frameRt_sigaction.Hide()
		self.frameUname.Hide()
		self.frameTime.Hide()
		self.framePerTime.Hide()
		self.frameErr.Hide()
		self.framePerErr.Hide()
		self.frameCnt.Hide()

	def OnHome(self, e):
		self.framedisp.Show()
		self.framePert.Hide()
		self.framecomp.Hide()
		self.frameop.Hide()
		self.frameUnfin.Hide()
		#self.frameProgName.Hide()
		self.framePNCont.Hide()
		self.frameCode.Hide()
		self.frameErrana.Hide()
		self.frameFileio.Hide()
		self.frameSummary.Hide()
		self.frameRead.Hide()
		self.frameWrite.Hide()
		self.frameAccess.Hide()
		self.frameFstat.Hide()
		self.frameStat.Hide()
		self.frameLstat.Hide()
		self.frameMmap.Hide()
		self.frameMunmap.Hide()
		self.frameMprotect.Hide()
		self.frameRt_sigaction.Hide()
		self.frameUname.Hide()
		self.frameTime.Hide()
		self.framePerTime.Hide()
		self.frameErr.Hide()
		self.framePerErr.Hide()
		self.frameCnt.Hide()
	
	def OnPerti(self,e):
		self.framePert.Show()
		self.frameRead.Hide()
		self.frameWrite.Hide()
		self.frameAccess.Hide()
		self.frameFstat.Hide()
		self.frameStat.Hide()
		self.frameLstat.Hide()
		self.frameMmap.Hide()
		self.frameMunmap.Hide()
		self.frameMprotect.Hide()
		self.frameRt_sigaction.Hide()
		self.frameUname.Hide()

	def OnCompa(self, e):
		self.framecomp.Show()
		self.frameTime.Hide()
		self.framePerTime.Hide()
		self.frameErr.Hide()
		self.framePerErr.Hide()
		self.frameCnt.Hide()

	def disp(self):

		if not self.framedisp:
			self.framedisp = wx.Frame(self, -1, 'System Call Analyzer Output', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)

		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.framedisp.SetMenuBar(self.menubar)

		self.paneldisp = wx.Panel(self.framedisp)
		self.paneldisp.SetBackgroundColour('LightSlateGray')
		self.vboxdisp = wx.BoxSizer(wx.VERTICAL)

		self.hboxdisp1 = wx.BoxSizer(wx.HORIZONTAL)

	#Particular System Call Statistics

		self.btnPerticular = wx.Button(self.paneldisp, label='Particular Statistics', size=(300, 100))
		self.btnPerticular.Bind(wx.EVT_BUTTON, self.OnPert)
		self.hboxdisp1.Add(self.btnPerticular, border=200)

		self.stdisp1 = wx.StaticText(self.paneldisp, label='            ')
		self.hboxdisp1.Add(self.stdisp1)

	#Comparitive Statistics of all System Calls

		self.btnComp = wx.Button(self.paneldisp, label='Comparitive Syscall Statistics', size=(300, 100))
		self.btnComp.Bind(wx.EVT_BUTTON, self.OnComp)
		self.hboxdisp1.Add(self.btnComp, border=200)

		self.hboxdisp1.Add(self.stdisp1)

	#Process Tree

		self.btnProc = wx.Button(self.paneldisp, label='Process Tree', size=(300, 100))
		self.btnProc.Bind(wx.EVT_BUTTON, self.OnProc)
		self.hboxdisp1.Add(self.btnProc, border=200)

		self.vboxdisp.Add(self.hboxdisp1, flag=wx.LEFT | wx.RIGHT | wx.TOP, border=100)
		self.vboxdisp.Add((-1, 10))

		self.hboxdisp2 = wx.BoxSizer(wx.HORIZONTAL)

	#Syscall Trace

		self.btnTrace = wx.Button(self.paneldisp, label='System Call and \n Signal Trace', size=(300, 100))
		self.btnTrace.Bind(wx.EVT_BUTTON, self.OnTrace)
		self.hboxdisp2.Add(self.btnTrace, border=200)

		self.stdisp2 = wx.StaticText(self.paneldisp, label='            ')
		self.hboxdisp2.Add(self.stdisp2)

	# Unfinished Syscall

		self.btnUnfin = wx.Button(self.paneldisp, label='Resumed-Unfinished \n System Calls', size=(300, 100))
		self.btnUnfin.Bind(wx.EVT_BUTTON, self.OnUnfin)
		self.hboxdisp2.Add(self.btnUnfin, border=200)

		self.hboxdisp2.Add(self.stdisp2)

	# Code Optimization

		self.btnCode = wx.Button(self.paneldisp, label='Code Optimization', size=(300, 100))
		self.btnCode.Bind(wx.EVT_BUTTON, self.OnCode)
		self.hboxdisp2.Add(self.btnCode, border=200)

		self.vboxdisp.Add(self.hboxdisp2, flag=wx.LEFT | wx.RIGHT | wx.TOP, border=100)
		self.vboxdisp.Add((-1, 10))

		self.hboxdisp3 = wx.BoxSizer(wx.HORIZONTAL)

	#File Input/Output Statistics

		self.btnFileio = wx.Button(self.paneldisp, label='File Input/Output Statistics', size=(300, 100))
		self.btnFileio.Bind(wx.EVT_BUTTON, self.OnFileio)
		self.hboxdisp3.Add(self.btnFileio, border=200)

		self.stdisp3 = wx.StaticText(self.paneldisp, label='            ')
		self.hboxdisp3.Add(self.stdisp3)

	#Error Analysis

		self.btnErrana = wx.Button(self.paneldisp, label='Error Analysis', size=(300, 100))
		self.btnErrana.Bind(wx.EVT_BUTTON, self.OnErrana)
		self.hboxdisp3.Add(self.btnErrana, border=200)

		self.hboxdisp3.Add(self.stdisp3)

	#Summary of All System Calls

		self.btnSummary = wx.Button(self.paneldisp, label='Summary of all \n System Calls', size=(300, 100))
		self.btnSummary.Bind(wx.EVT_BUTTON, self.OnSummary)
		self.hboxdisp3.Add(self.btnSummary, border=200)

		self.vboxdisp.Add(self.hboxdisp3, flag=wx.LEFT | wx.RIGHT | wx.TOP, border=100)
		self.vboxdisp.Add((-1, 10))

		self.paneldisp.SetSizer(self.vboxdisp)

		self.framedisp.Show()

# Button Cliks on Output Screen

	# Particular System Call Statistics

	def OnPert(self, e):
		if not self.framePert:
			self.framePert = wx.Frame(self, -1, 'Particular System Calls and Signals Statistics', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)

		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.framePert.SetMenuBar(self.menubar)


		self.panelPert = wx.Panel(self.framePert)
		self.panelPert.SetBackgroundColour('LightSlateGray')
		self.vboxPert = wx.BoxSizer(wx.VERTICAL)

	#File Structure Related System Calls

		self.hboxPert1 = wx.BoxSizer(wx.HORIZONTAL)

		self.stPert1 = wx.StaticText(self.panelPert, label='          *** File Structure Related System Calls *** ')
		self.hboxPert1.Add(self.stPert1)

		self.vboxPert.Add(self.hboxPert1, flag=wx.LEFT | wx.RIGHT | wx.TOP, border=30)
		self.vboxPert.Add((-1, 10))

		self.hboxPert2 = wx.BoxSizer(wx.HORIZONTAL)

	    # Read System Call

		self.sthbox1 = wx.StaticText(self.panelPert, label='         ')
		self.hboxPert2.Add(self.sthbox1)

		self.sthbox2 = wx.StaticText(self.panelPert, label='                ')

		self.btnRead = wx.Button(self.panelPert, label='Read', size=(200, 75))
		self.btnRead.Bind(wx.EVT_BUTTON, self.OnRead)
		self.hboxPert2.Add(self.btnRead, flag=wx.LEFT, border=30)

		self.hboxPert2.Add(self.sthbox2)

	    # Write System Call

		self.btnWrite = wx.Button(self.panelPert, label='Write', size=(200, 75))
		self.btnWrite.Bind(wx.EVT_BUTTON, self.OnWrite)
		self.hboxPert2.Add(self.btnWrite, border=30)

		self.hboxPert2.Add(self.sthbox2)

	    # Access System Call

		self.btnAccess = wx.Button(self.panelPert, label='Access', size=(200, 75))
		self.btnAccess.Bind(wx.EVT_BUTTON, self.OnAccess)
		self.hboxPert2.Add(self.btnAccess, border=30)

		self.hboxPert2.Add(self.sthbox2)

	    # Pipe System Call

		self.btnPipe = wx.Button(self.panelPert, label='Pipe', size=(200, 75))
		self.btnPipe.Bind(wx.EVT_BUTTON, self.OnPipe)
		self.hboxPert2.Add(self.btnPipe, border=30)

		self.vboxPert.Add(self.hboxPert2, flag=wx.LEFT | wx.RIGHT , border=30)
		self.vboxPert.Add((-1, 10))

		self.hboxPert3 = wx.BoxSizer(wx.HORIZONTAL)

	    # Stat/Stat64 System Call

		self.sthbox3 = wx.StaticText(self.panelPert, label='                ')
		self.hboxPert3.Add(self.sthbox3)

		self.btnStat = wx.Button(self.panelPert, label='Stat/Stat64', size=(200, 75))
		self.btnStat.Bind(wx.EVT_BUTTON, self.OnStat)
		self.hboxPert3.Add(self.btnStat, border=30)

		self.hboxPert3.Add(self.sthbox3)

	    # Fstat/Fstat64 System Call

		self.btnFstat = wx.Button(self.panelPert, label='Fstat/Fstat64', size=(200, 75))
		self.btnFstat.Bind(wx.EVT_BUTTON, self.OnFstat)
		self.hboxPert3.Add(self.btnFstat, border=30)

		self.hboxPert3.Add(self.sthbox3)

	    # Lstat/Lstat64 System Call

		self.btnLstat = wx.Button(self.panelPert, label='Lstat/Lstat64', size=(200, 75))
		self.btnLstat.Bind(wx.EVT_BUTTON, self.OnLstat)
		self.hboxPert3.Add(self.btnLstat, border=30)

		self.vboxPert.Add(self.hboxPert3, flag=wx.LEFT | wx.RIGHT , border=30)
		self.vboxPert.Add((-1, 10))

	#Memory Related System Calls

		self.hboxPert4 = wx.BoxSizer(wx.HORIZONTAL)

		self.stPert4 = wx.StaticText(self.panelPert, label='          *** Memory Related System Calls *** ')
		self.hboxPert4.Add(self.stPert4)

		self.vboxPert.Add(self.hboxPert4, flag=wx.LEFT | wx.RIGHT |wx.TOP, border=30)
		self.vboxPert.Add((-1, 10))

		self.hboxPert5 = wx.BoxSizer(wx.HORIZONTAL)

	    # Mmap System Call

		self.sthbox5 = wx.StaticText(self.panelPert, label='                ')
		self.hboxPert5.Add(self.sthbox5)

		self.btnMmap = wx.Button(self.panelPert, label='Mmap', size=(200, 75))
		self.btnMmap.Bind(wx.EVT_BUTTON, self.OnMmap)
		self.hboxPert5.Add(self.btnMmap, border=30)

		self.hboxPert5.Add(self.sthbox5)

	    # Mprotect System Call

		self.btnMprotect = wx.Button(self.panelPert, label='Mprotect', size=(200, 75))
		self.btnMprotect.Bind(wx.EVT_BUTTON, self.OnMprotect)
		self.hboxPert5.Add(self.btnMprotect, border=30)

		self.hboxPert5.Add(self.sthbox5)

	    # Munmap System Call

		self.btnMunmap = wx.Button(self.panelPert, label='Munmap', size=(200, 75))
		self.btnMunmap.Bind(wx.EVT_BUTTON, self.OnMunmap)
		self.hboxPert5.Add(self.btnMunmap, border=30)

		self.vboxPert.Add(self.hboxPert5, flag=wx.LEFT | wx.RIGHT , border=30)
		self.vboxPert.Add((-1, 10))

	#Signal Related System Calls

		self.hboxPert6 = wx.BoxSizer(wx.HORIZONTAL)

		self.stPert6 = wx.StaticText(self.panelPert, label='          *** Signals Related System Calls(Rt_sigaction) And Signals(SIGCHID) ***')
		self.hboxPert6.Add(self.stPert6)

		self.vboxPert.Add(self.hboxPert6, flag=wx.LEFT | wx.RIGHT | wx.TOP, border=30)
		self.vboxPert.Add((-1, 10))

		self.hboxPert7 = wx.BoxSizer(wx.HORIZONTAL)

	    # Rt_sigaction System Call

		self.sthbox7 = wx.StaticText(self.panelPert, label='                ')
		self.hboxPert7.Add(self.sthbox7)

		self.btnRt_sigaction = wx.Button(self.panelPert, label='Rt_sigaction', size=(200, 75))
		self.btnRt_sigaction.Bind(wx.EVT_BUTTON, self.OnRt_sigaction)
		self.hboxPert7.Add(self.btnRt_sigaction, border=30)

		self.hboxPert7.Add(self.sthbox7)

	    # SIGCHILD Signal

		self.btnSigchild = wx.Button(self.panelPert, label='SIGCHILD', size=(200, 75))
		self.btnSigchild.Bind(wx.EVT_BUTTON, self.OnSigchild)
		self.hboxPert7.Add(self.btnSigchild, border=30)

		self.hboxPert7.Add(self.sthbox7)

	    # SIGSEGV Signal

		#self.btnSigsegv = wx.Button(self.panelPert, label='SIGSEGV', size=(200, 75))
		#self.btnSigsegv.Bind(wx.EVT_BUTTON, self.OnSigsegv)
		#self.hboxPert7.Add(self.btnSigsegv, border=30)

		self.vboxPert.Add(self.hboxPert7, flag=wx.LEFT | wx.RIGHT , border=30)
		self.vboxPert.Add((-1, 10))

	#System Information

		self.hboxPert8 = wx.BoxSizer(wx.HORIZONTAL)

		self.stPert8 = wx.StaticText(self.panelPert, label='          *** System Information *** ')
		self.hboxPert8.Add(self.stPert8)

		self.vboxPert.Add(self.hboxPert8, flag=wx.LEFT | wx.RIGHT | wx.TOP, border=30)
		self.vboxPert.Add((-1, 10))

		self.hboxPert9 = wx.BoxSizer(wx.HORIZONTAL)

	    # Uname System Call

		self.stPert9 = wx.StaticText(self.panelPert, label='                ')
		self.hboxPert9.Add(self.stPert9)

		self.btnUname = wx.Button(self.panelPert, label='Uname', size=(200, 75))
		self.btnUname.Bind(wx.EVT_BUTTON, self.OnUname)
		self.hboxPert9.Add(self.btnUname, flag=wx.LEFT | wx.BOTTOM, border=30)

		self.stPert9 = wx.StaticText(self.panelPert, label='\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t')
		self.hboxPert9.Add(self.stPert9)

		self.btnInfo = wx.Button(self.panelPert, label='Information', size=(150, 50))
		self.btnInfo.Bind(wx.EVT_BUTTON, self.OnInfo)
		self.hboxPert9.Add(self.btnInfo, flag=wx.RIGHT | wx.BOTTOM, border = 10)

		self.vboxPert.Add(self.hboxPert9, flag=wx.LEFT | wx.RIGHT | wx.BOTTOM, border=10)
		self.vboxPert.Add((-1, 10))

		self.panelPert.SetSizer(self.vboxPert)
		self.framePert.Show()

	# Comparitive Statistics
 
	def OnComp(self, e):        
		if not self.framecomp:
			self.framecomp = wx.Frame(self, -1, 'Comparative Statistics of All System Calls ', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.framecomp.SetMenuBar(self.menubar)

		self.panelcomp = wx.Panel(self.framecomp)
		self.panelcomp.SetBackgroundColour('LightSlateGray')
		self.vboxcomp = wx.BoxSizer(wx.VERTICAL)

		self.hboxcomp1 = wx.BoxSizer(wx.HORIZONTAL)

	#Time Consumed By all System Call

		self.stcomp1 = wx.StaticText(self.panelcomp, label='                  ')
		self.hboxcomp1.Add(self.stcomp1)

		self.btnTime = wx.Button(self.panelcomp, label='Time Consumption of Syscalls', size=(250, 100))
		self.btnTime.Bind(wx.EVT_BUTTON, self.OnTime)
		self.hboxcomp1.Add(self.btnTime, border=150)

		self.hboxcomp1.Add(self.stcomp1)

	# Percentage Time Consumption of all System Calls

		self.btnPerTime = wx.Button(self.panelcomp, label='Percentage Time Consumption \n of Syscalls', size=(250, 100))
		self.btnPerTime.Bind(wx.EVT_BUTTON, self.OnPerTime)
		self.hboxcomp1.Add(self.btnPerTime, border=150)

		self.hboxcomp1.Add(self.stcomp1)

	#System Call Count
		self.btnCnt = wx.Button(self.panelcomp, label='System Call Count', size=(250, 100))
		self.btnCnt.Bind(wx.EVT_BUTTON, self.OnCnt)
		self.hboxcomp1.Add(self.btnCnt, border=100)

		self.vboxcomp.Add(self.hboxcomp1, flag=wx.LEFT | wx.RIGHT | wx.TOP, border=200)
		self.vboxcomp.Add((-1, 10))

		self.hboxcomp2 = wx.BoxSizer(wx.HORIZONTAL)

	# Errors in All System Calls

		self.stcomp2 = wx.StaticText(self.panelcomp, label='                                                                ')
		self.hboxcomp2.Add(self.stcomp2)

		self.btnErr = wx.Button(self.panelcomp, label='System Call Errors', size=(250, 100))
		self.btnErr.Bind(wx.EVT_BUTTON, self.OnErr)
		self.hboxcomp2.Add(self.btnErr, border=150)

		self.hboxcomp2.Add(self.stcomp2)

	# Percentage Errors in All System Calls

		self.btnPerErr = wx.Button(self.panelcomp, label='Percentage Errors in System Calls', size=(250, 100))
		self.btnPerErr.Bind(wx.EVT_BUTTON, self.OnPerErr)
		self.hboxcomp2.Add(self.btnPerErr, border=150)

		self.vboxcomp.Add(self.hboxcomp2, flag=wx.LEFT | wx.RIGHT | wx.TOP, border=100)
		self.vboxcomp.Add((-1, 10))

		self.panelcomp.SetSizer(self.vboxcomp)

		self.framecomp.Show()

# Tracing of all System Calls and Signals

	def OnTrace(self, e):        
		if not self.frameop:
			self.frameop = wx.Frame(self, -1, 'System Call and Signal Trace Output', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.frameop.SetMenuBar(self.menubar)
		self.vboxop = wx.BoxSizer(wx.VERTICAL)

		self.panelop = wx.Panel(self.frameop)
		self.panelop.SetBackgroundColour('LightSlateGray')
		self.vboxop = wx.BoxSizer(wx.VERTICAL)
		self.hboxop = wx.BoxSizer(wx.HORIZONTAL)
		self.btnSysop = wx.Button(self.panelop, label='System Call Trace', size=(400, 150))
		self.btnSysop.Bind(wx.EVT_BUTTON, self.OnSysTrace)
		self.hboxop.Add(self.btnSysop, flag=wx.LEFT, border=150)
		self.btnSigop = wx.Button(self.panelop, label='Signals Trace', size=(400, 150))
		self.btnSigop.Bind(wx.EVT_BUTTON, self.OnSigTrace)
		self.hboxop.Add(self.btnSigop, flag=wx.LEFT, border=150)
		self.vboxop.Add(self.hboxop, flag=wx.TOP, border=200)

		self.panelop.SetSizer(self.vboxop)		        
		self.frameop.Show()

# Tracing of Unfinished and Resumed System Calls

	def OnUnfin(self, e):        
		if not self.frameUnfin:
			self.frameUnfin = wx.Frame(self, -1, 'Unfinished And Resumed Calls Statistics', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.frameUnfin.SetMenuBar(self.menubar)

		self.panelUnfin = wx.Panel(self.frameUnfin)
		self.panelUnfin.SetBackgroundColour('LightSlateGray')
		self.vboxUnfin = wx.BoxSizer(wx.VERTICAL)
		self.hboxUnfin = wx.BoxSizer(wx.HORIZONTAL)
		self.btnUnfin = wx.Button(self.panelUnfin, label='Unfinihed System Calls', size=(400, 150))
		self.btnUnfin.Bind(wx.EVT_BUTTON, self.OnUnfini)
		self.hboxUnfin.Add(self.btnUnfin, flag=wx.LEFT, border=150)
		self.btnResumed = wx.Button(self.panelUnfin, label='Resumed System Calls', size=(400, 150))
		self.btnResumed.Bind(wx.EVT_BUTTON, self.OnResumed)
		self.hboxUnfin.Add(self.btnResumed, flag=wx.LEFT, border=150)
		self.vboxUnfin.Add(self.hboxUnfin, flag=wx.TOP, border=200)

		self.panelUnfin.SetSizer(self.vboxUnfin)		        
		self.frameUnfin.Show()

# Process Tree Of System Calls

	def OnProc(self, e):
		commands.getoutput("python pt2.py")        
		commands.getoutput("python tree3.py")		

# Code Optimization

	def OnCode(self, e):        
		if not self.frameCode:
			self.frameCode = wx.Frame(self, -1, 'Code Optimization', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.frameCode.SetMenuBar(self.menubar)

		self.panelCode = wx.Panel(self.frameCode)
		self.panelCode.SetBackgroundColour('LightSlateGray')
		self.vboxCode = wx.BoxSizer(wx.VERTICAL)

		self.hboxCode1 = wx.BoxSizer(wx.HORIZONTAL)
		self.stCode1 = wx.StaticText(self.panelCode, label='   1.  Please avoid use of "\ n"(New Line Character) where possible. (Instead \n \t  of "\ n"use "\ t"(Tab) if required). ')
		self.stCode1.SetFont(self.font)
		self.stCode1.SetForegroundColour("White")
		self.hboxCode1.Add(self.stCode1, flag=wx.LEFT, border=50)
		self.stCode11 = wx.StaticText(self.panelCode, label='      \t\t\t\t\t')
		self.stCode11.SetFont(self.font)
		self.hboxCode1.Add(self.stCode11, flag=wx.CENTER, border=50)
		self.btnrefer1 = wx.Button(self.panelCode, label='REFER', size=(75, 35))
		self.btnrefer1.Bind(wx.EVT_BUTTON, self.OnRefer1)
		self.hboxCode1.Add(self.btnrefer1, flag=wx.RIGHT, border=50)
		self.vboxCode.Add(self.hboxCode1, flag=wx.EXPAND | wx.CENTER | wx.TOP, border=50)
		self.vboxCode.Add((-1, 10))

		self.hboxCode2 = wx.BoxSizer(wx.HORIZONTAL)
		self.stCode2 = wx.StaticText(self.panelCode, label='   2.  Please avoid use of "fflush()" function whenever possible. ')
		self.stCode2.SetFont(self.font)
		self.stCode2.SetForegroundColour("White")
		self.hboxCode2.Add(self.stCode2, flag=wx.LEFT, border=50)
		self.stCode22 = wx.StaticText(self.panelCode, label='     \t\t\t\t\t\t\t\t')
		self.stCode22.SetFont(self.font)
		self.hboxCode2.Add(self.stCode22, flag=wx.CENTER, border=50)
		self.btnrefer2 = wx.Button(self.panelCode, label='REFER', size=(75, 35))
		self.btnrefer2.Bind(wx.EVT_BUTTON, self.OnRefer2)
		self.hboxCode2.Add(self.btnrefer2, flag=wx.RIGHT, border=50)
		self.vboxCode.Add(self.hboxCode2, flag=wx.EXPAND | wx.CENTER | wx.TOP, border=50)
		self.vboxCode.Add((-1, 10))

		self.hboxCode3 = wx.BoxSizer(wx.HORIZONTAL)
		self.stCode3 = wx.StaticText(self.panelCode, label='   3.  Generally "Pass By Reference" is better than "Pass By Value" ')
		self.stCode3.SetFont(self.font)
		self.stCode3.SetForegroundColour("White")
		self.hboxCode3.Add(self.stCode3, flag=wx.LEFT, border=50)
		self.stCode33 = wx.StaticText(self.panelCode, label='-----------------------------------')
		self.stCode33.SetFont(self.font)
		self.stCode33.SetForegroundColour("LightSlateGray")
		self.hboxCode3.Add(self.stCode33, flag=wx.CENTER, border=50)
		self.btnrefer3 = wx.Button(self.panelCode, label='REFER', size=(75, 35))
		self.btnrefer3.Bind(wx.EVT_BUTTON, self.OnRefer3)
		self.hboxCode3.Add(self.btnrefer3, flag=wx.RIGHT, border=50)
		self.vboxCode.Add(self.hboxCode3, flag=wx.EXPAND | wx.CENTER | wx.TOP, border=50)
		self.vboxCode.Add((-1, 10))

		self.hboxCode4 = wx.BoxSizer(wx.HORIZONTAL)
		self.stCode4 = wx.StaticText(self.panelCode, label='   4.  While performing "File Operations" it is better to use array or \n \t  string( E.g. fgets() ) rather than using single character( E.g. fgetc() ) ')
		self.stCode4.SetFont(self.font)
		self.stCode4.SetForegroundColour("White")
		self.hboxCode4.Add(self.stCode4, flag=wx.LEFT, border=50)
		self.stCode44 = wx.StaticText(self.panelCode, label='----------------------------')
		self.stCode44.SetFont(self.font)
		self.stCode44.SetForegroundColour("LightSlateGray")
		self.hboxCode4.Add(self.stCode44, flag=wx.CENTER, border=50)
		self.btnrefer4 = wx.Button(self.panelCode, label='REFER', size=(75, 35))
		self.btnrefer4.Bind(wx.EVT_BUTTON, self.OnRefer4)
		self.hboxCode4.Add(self.btnrefer4, flag=wx.RIGHT, border=50)
		self.vboxCode.Add(self.hboxCode4, flag=wx.EXPAND | wx.CENTER | wx.TOP, border=50)
		self.vboxCode.Add((-1, 10))

		self.hboxCode5 = wx.BoxSizer(wx.HORIZONTAL)
		self.stCode5 = wx.StaticText(self.panelCode, label='   5.  Generally "For" loops give Better performance than "While" loops. ')
		self.stCode5.SetFont(self.font)
		self.stCode5.SetForegroundColour("White")
		self.hboxCode5.Add(self.stCode5, flag=wx.LEFT, border=50)
		self.stCode55 = wx.StaticText(self.panelCode, label='------------------------------')
		self.stCode55.SetFont(self.font)
		self.stCode55.SetForegroundColour("LightSlateGray")
		self.hboxCode5.Add(self.stCode55, flag=wx.CENTER, border=50)
		self.btnrefer5 = wx.Button(self.panelCode, label='REFER', size=(75, 35))
		self.btnrefer5.Bind(wx.EVT_BUTTON, self.OnRefer5)
		self.hboxCode5.Add(self.btnrefer5, flag=wx.RIGHT, border=50)
		self.vboxCode.Add(self.hboxCode5, flag=wx.EXPAND | wx.CENTER | wx.TOP, border=50)
		self.vboxCode.Add((-1, 10))

		self.hboxCode6 = wx.BoxSizer(wx.HORIZONTAL)
		self.btntest = wx.Button(self.panelCode, label='Take A Test', size=(150, 70))
		self.btntest.Bind(wx.EVT_BUTTON, self.OnTest)
		self.hboxCode6.Add(self.btntest, flag=wx.LEFT, border=250)

		self.stCode6 = wx.StaticText(self.panelCode, label='\t\t\t\t\t\t\t\t\t\t\t\t')
		self.stCode6.SetFont(self.font)
		self.hboxCode6.Add(self.stCode6, flag=wx.CENTER, border=150)

		self.btnhints = wx.Button(self.panelCode, label='Some More Hints', size=(150, 70))
		self.btnhints.Bind(wx.EVT_BUTTON, self.OnHints)
		self.hboxCode6.Add(self.btnhints, flag=wx.RIGHT, border=150)

		self.vboxCode.Add(self.hboxCode6, flag=wx.EXPAND | wx.TOP, border=50)
		self.vboxCode.Add((-1, 10))

		self.panelCode.SetSizer(self.vboxCode)		        
		self.frameCode.Show()

# File Input/Output Statistics

	def OnFileio(self, e):        
		if not self.frameFileio:
			self.frameFileio = wx.Frame(self, -1, 'File Input/Output Statistics', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.frameFileio.SetMenuBar(self.menubar)

		commands.getstatusoutput("python fileio.py")
		name = "fileio_tab"		
		self.frameFileio = TestFrame(self,name)
		while len(column) > 0 : column.pop()
		self.frameFileio.Show()

# Errana Of All System Calls
	def OnErrana(self, e):        
		if not self.frameErrana:
			self.frameErrana = wx.Frame(self, -1, 'Error Analysis', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.frameErrana.SetMenuBar(self.menubar)

		commands.getstatusoutput("python errana.py")
		name = "errors"		
		self.frameErrana = TestFrame(self,name)
		while len(column) > 0 : column.pop()
		self.frameErrana.Show()

	# Summary Of All System Calls

	def OnSummary(self, e):        
		if not self.frameSummary:
			self.frameSummary = wx.Frame(self, -1, 'Summary of All System Calls', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.frameSummary.SetMenuBar(self.menubar)
		commands.getstatusoutput("python summary.py")
		name = "summary_tab"
		self.frameSummary = TestFrame(self,name)
		while len(column) > 0 : column.pop()
		#self.frameSummary.SetBackgroundColour('LightSlateGray')

		self.frameSummary.Show()

	def OnRead(self, e):

		if not self.frameRead:
			self.frameRead = wx.Frame(self, -1, 'Perticular System Call Statistics : Read', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.fitem3 = self.fileMenu.Append(ID_FILE_PERT, 'Particular', 'Particular Syscalls')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.Bind(wx.EVT_MENU, self.OnPerti, self.fitem3)
		self.frameRead.SetMenuBar(self.menubar)

		self.panelRead = wx.Panel(self.frameRead)
		self.panelRead.SetBackgroundColour('LightSlateGray')
		output = commands.getstatusoutput("python pread.py")
		#persyscall.persyscallstat('read_tab')
		self.hboxRead = wx.BoxSizer(wx.HORIZONTAL)

		self.vboxRead1 = wx.BoxSizer(wx.VERTICAL)

		self.hboxRead11 = wx.BoxSizer(wx.HORIZONTAL)
		self.stRead11 = wx.StaticText(self.panelRead, label='Read Graph')
		self.stRead11.SetFont(self.font)
		self.hboxRead11.Add(self.stRead11, flag=wx.CENTER | wx.TOP, border=5)
		self.vboxRead1.Add(self.hboxRead11, flag=wx.EXPAND | wx.CENTER , border=10)
		self.vboxRead1.Add((-1, 10))

		self.hboxRead12 = wx.BoxSizer(wx.HORIZONTAL)

		self.imgRead = wx.EmptyImage(800,500)
		self.imgReadCtrl = wx.StaticBitmap(self.panelRead, wx.ID_ANY, wx.BitmapFromImage(self.imgRead))

		#self.persyscallstat('Read_tab')
		commands.getoutput("python gread1.py")
		filepath = "Graphs/readgr.png"
		self.imgRead = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
		self.imgReadCtrl.SetBitmap(wx.BitmapFromImage(self.imgRead))

		self.hboxRead12.Add(self.imgReadCtrl, flag=wx.EXPAND | wx.CENTER , border=20)
		self.vboxRead1.Add(self.hboxRead12, flag=wx.EXPAND | wx.CENTER | wx.BOTTOM, border=5)
		self.vboxRead1.Add((-1, 10))

		self.hboxRead.Add(self.vboxRead1, flag=wx.LEFT | wx.TOP, border=20)

		self.vboxRead3 = wx.BoxSizer(wx.VERTICAL)

		self.stRead3 = wx.StaticText(self.panelRead, label='\t')
		self.stRead3.SetFont(self.font)

		self.vboxRead3.Add(self.stRead3, flag=wx.EXPAND | wx.CENTER , border=20)
		self.vboxRead3.Add((-1, 10))

		self.hboxRead.Add(self.vboxRead3, flag=wx.CENTER | wx.TOP, border=20)

		self.vboxRead2 = wx.BoxSizer(wx.VERTICAL)

		self.hboxRead23 = wx.BoxSizer(wx.HORIZONTAL)
		self.stRead23 = wx.StaticText(self.panelRead, label='Read Statistics')
		self.stRead23.SetFont(self.font)
		self.hboxRead23.Add(self.stRead23, flag=wx.CENTER)
		self.vboxRead2.Add(self.hboxRead23, flag=wx.EXPAND | wx.CENTER , border=5)
		self.vboxRead2.Add((-1, 10))

		self.hboxRead21 = wx.BoxSizer(wx.HORIZONTAL)
		self.tcRead21 = wx.TextCtrl(self.panelRead, wx.ID_ANY, size=(400,250), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.VSCROLL)
		self.font.SetPointSize(13)
		self.tcRead21.SetFont(self.font)
		self.tcRead21.SetValue(output[1])
		self.hboxRead21.Add(self.tcRead21, flag=wx.TOP | wx.RIGHT)
		self.vboxRead2.Add(self.hboxRead21, flag=wx.CENTER | wx.TOP | wx.RIGHT, border=20)
		self.vboxRead2.Add((-1, 10))

		self.hboxRead24 = wx.BoxSizer(wx.HORIZONTAL)
		self.stRead24 = wx.StaticText(self.panelRead, label='Read Files Table')
		self.stRead24.SetFont(self.font)
		self.hboxRead24.Add(self.stRead24, flag=wx.CENTER)
		self.vboxRead2.Add(self.hboxRead24, flag=wx.EXPAND | wx.CENTER , border=5)
		self.vboxRead2.Add((-1, 10))

		self.hboxRead22 = wx.BoxSizer(wx.HORIZONTAL)

		self.tcRead22 = wx.TextCtrl(self.panelRead, wx.ID_ANY, size=(400,250), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.VSCROLL)
		self.font.SetPointSize(13)
		self.tcRead22.SetFont(self.font)
		string = ''
		curs.execute("SELECT filename, call FROM read_final1")
		self.tcRead22.AppendText("FileName    ->   Call No.\n")
		
		rows = curs.fetchall()
		for row in rows:
		    string = "\n*) "+row[0]+"  ->    "+row[1]
		    self.tcRead22.AppendText(string)
		self.hboxRead22.Add(self.tcRead22, flag=wx.TOP | wx.RIGHT)

		self.vboxRead2.Add(self.hboxRead22, flag=wx.CENTER | wx.BOTTOM | wx.RIGHT, border=20)
		self.vboxRead2.Add((-1, 10))

		self.hboxRead.Add(self.vboxRead2, flag=wx.TOP | wx.RIGHT, border=20)

		self.panelRead.SetSizer(self.hboxRead)		        
		self.frameRead.Show()


	# Write System Call

	def OnWrite(self, e):        
		if not self.frameWrite:
			self.frameWrite = wx.Frame(self, -1, 'Particular System Call Statistics : Write', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.fitem3 = self.fileMenu.Append(ID_FILE_PERT, 'Particular', 'Particular Syscalls')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.Bind(wx.EVT_MENU, self.OnPerti, self.fitem3)
		self.frameWrite.SetMenuBar(self.menubar)

		self.panelWrite = wx.Panel(self.frameWrite)
		self.panelWrite.SetBackgroundColour('LightSlateGray')

		output = commands.getstatusoutput("python pwrite.py")

		self.hboxWrite = wx.BoxSizer(wx.HORIZONTAL)

		self.vboxWrite1 = wx.BoxSizer(wx.VERTICAL)

		self.hboxWrite11 = wx.BoxSizer(wx.HORIZONTAL)
		self.stWrite11 = wx.StaticText(self.panelWrite, label='Write Graph')
		self.stWrite11.SetFont(self.font)
		self.hboxWrite11.Add(self.stWrite11, flag=wx.CENTER | wx.TOP, border=5)
		self.vboxWrite1.Add(self.hboxWrite11, flag=wx.EXPAND | wx.CENTER , border=10)
		self.vboxWrite1.Add((-1, 10))

		self.hboxWrite12 = wx.BoxSizer(wx.HORIZONTAL)

		self.imgWrite = wx.EmptyImage(800,500)
		self.imgWriteCtrl = wx.StaticBitmap(self.panelWrite, wx.ID_ANY, wx.BitmapFromImage(self.imgWrite))

		#self.persyscallstat('Write_tab')
		commands.getoutput("python gwrite.py")
		filepath = "Graphs/write.png"
		self.imgWrite = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
		self.imgWriteCtrl.SetBitmap(wx.BitmapFromImage(self.imgWrite))

		self.hboxWrite12.Add(self.imgWriteCtrl, flag=wx.EXPAND | wx.CENTER , border=20)
		self.vboxWrite1.Add(self.hboxWrite12, flag=wx.EXPAND | wx.CENTER | wx.BOTTOM, border=5)
		self.vboxWrite1.Add((-1, 10))

		self.hboxWrite.Add(self.vboxWrite1, flag=wx.LEFT | wx.TOP, border=20)

		self.vboxWrite3 = wx.BoxSizer(wx.VERTICAL)

		self.stWrite3 = wx.StaticText(self.panelWrite, label='\t')
		self.stWrite3.SetFont(self.font)

		self.vboxWrite3.Add(self.stWrite3, flag=wx.EXPAND | wx.CENTER , border=20)
		self.vboxWrite3.Add((-1, 10))

		self.hboxWrite.Add(self.vboxWrite3, flag=wx.CENTER | wx.TOP, border=20)

		self.vboxWrite2 = wx.BoxSizer(wx.VERTICAL)

		self.hboxWrite23 = wx.BoxSizer(wx.HORIZONTAL)
		self.stWrite23 = wx.StaticText(self.panelWrite, label='Write Statistics')
		self.stWrite23.SetFont(self.font)
		self.hboxWrite23.Add(self.stWrite23, flag=wx.CENTER)
		self.vboxWrite2.Add(self.hboxWrite23, flag=wx.EXPAND | wx.CENTER , border=5)
		self.vboxWrite2.Add((-1, 10))

		self.hboxWrite21 = wx.BoxSizer(wx.HORIZONTAL)
		self.tcWrite21 = wx.TextCtrl(self.panelWrite, wx.ID_ANY, size=(400,250), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.VSCROLL)
		self.font.SetPointSize(13)
		self.tcWrite21.SetFont(self.font)
		self.tcWrite21.SetValue(output[1])
		self.hboxWrite21.Add(self.tcWrite21, flag=wx.TOP | wx.RIGHT)
		self.vboxWrite2.Add(self.hboxWrite21, flag=wx.CENTER | wx.TOP | wx.RIGHT, border=20)
		self.vboxWrite2.Add((-1, 10))

		self.hboxWrite24 = wx.BoxSizer(wx.HORIZONTAL)
		self.stWrite24 = wx.StaticText(self.panelWrite, label='Write files Table')
		self.stWrite24.SetFont(self.font)
		self.hboxWrite24.Add(self.stWrite24, flag=wx.CENTER)
		self.vboxWrite2.Add(self.hboxWrite24, flag=wx.EXPAND | wx.CENTER , border=5)
		self.vboxWrite2.Add((-1, 10))

		self.hboxWrite22 = wx.BoxSizer(wx.HORIZONTAL)

		self.tcWrite22 = wx.TextCtrl(self.panelWrite, wx.ID_ANY, size=(400,250), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.VSCROLL)
		self.font.SetPointSize(13)
		self.tcWrite22.SetFont(self.font)
		string = ''
		curs.execute("SELECT filename, call FROM write_final1")
		self.tcWrite22.AppendText("FileName    ->   Call No.\n")
		
		rows = curs.fetchall()
		for row in rows:
		    string = "\n*) "+row[0]+"  ->    "+row[1]
		    self.tcWrite22.AppendText(string)
		
		#self.tcWrite22.SetValue(" Put Ur Contents here jyo ")
		self.hboxWrite22.Add(self.tcWrite22, flag=wx.TOP | wx.RIGHT)

		self.vboxWrite2.Add(self.hboxWrite22, flag=wx.CENTER | wx.BOTTOM | wx.RIGHT, border=20)
		self.vboxWrite2.Add((-1, 10))

		self.hboxWrite.Add(self.vboxWrite2, flag=wx.TOP | wx.RIGHT, border=20)

		self.panelWrite.SetSizer(self.hboxWrite)		        
		self.frameWrite.Show()

		# Access System Call

	def OnAccess(self, e):        
		if not self.frameAccess:
			self.frameAccess = wx.Frame(self, -1, 'Particular System Call Statistics : ACCESS', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.fitem3 = self.fileMenu.Append(ID_FILE_PERT, 'Particular', 'Particular Syscalls')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.Bind(wx.EVT_MENU, self.OnPerti, self.fitem3)
		self.frameAccess.SetMenuBar(self.menubar)
		self.panelAccess = wx.Panel(self.frameAccess)
		#self.panelAccess.SetBackgroundColour('LightSlateGray')

		commands.getstatusoutput("python paccess.py")
		name = 'access_tab'		
		self.frameAccess = TestFrame(self,name)
		while len(column) > 0 : column.pop()
		self.frameAccess.Show()

		# Pipe System Call
	def OnPipe(self, e):        
		if not self.framePipe:
			self.framePipe = wx.Frame(self, -1, 'Particular System Call Statistics : Pipe', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.fitem3 = self.fileMenu.Append(ID_FILE_PERT, 'Particular', 'Particular Syscalls')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.Bind(wx.EVT_MENU, self.OnPerti, self.fitem3)
		self.framePipe.SetMenuBar(self.menubar)
		commands.getstatusoutput("python ppipe.py")
		name = 'pipe_tab'		
		self.framePipe = TestFrame(self,name)
		while len(column) > 0 : column.pop()
		self.framePipe.Show()

	# Fstat System Call

	def OnFstat(self, e):        
		if not self.frameFstat:
			self.frameFstat = wx.Frame(self, -1, 'Particular System Call Statistics : FSTAT', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.fitem3 = self.fileMenu.Append(ID_FILE_HOME, 'Particular', 'Particular Syscalls')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.Bind(wx.EVT_MENU, self.OnPerti, self.fitem3)
		self.frameFstat.SetMenuBar(self.menubar)
	
		commands.getstatusoutput("python pfstat.py")
		name = 'fstat_tab'		
		self.frameFstat = TestFrame(self,name)
		while len(column) > 0 : column.pop()
		self.frameFstat.Show()

		# Stat System Call

	def OnStat(self, e):        
		if not self.frameStat:
			self.frameStat = wx.Frame(self, -1, 'Particular System Call Statistics : STAT', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.fitem3 = self.fileMenu.Append(ID_FILE_PERT, 'Particular', 'Particular Syscalls')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.Bind(wx.EVT_MENU, self.OnPerti, self.fitem3)
		self.frameStat.SetMenuBar(self.menubar)

		commands.getstatusoutput("python pstat.py")
		name = 'stat_tab'		
		self.frameStat = TestFrame(self,name)
		while len(column) > 0 : column.pop()
		self.frameStat.Show()

		# Lstat System Call

	def OnLstat(self, e):        
		if not self.frameLstat:
			self.frameLstat = wx.Frame(self, -1, 'Particular System Call Statistics : Lstat', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.fitem3 = self.fileMenu.Append(ID_FILE_PERT, 'Particular', 'Particular Syscalls')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.Bind(wx.EVT_MENU, self.OnPerti, self.fitem3)
		self.frameLstat.SetMenuBar(self.menubar)

		commands.getstatusoutput("python plstat.py")
		name = 'lstat_tab'		
		self.frameLstat = TestFrame(self,name)
		while len(column) > 0 : column.pop()
		self.frameLstat.SetBackgroundColour('LightSlateGray')

		self.frameLstat.Show()

		# Mmap System Call

	def OnMmap(self, e):        
		if not self.frameMmap:
			self.frameMmap = wx.Frame(self, -1, 'Particular System Call Statistics : READ', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.fitem3 = self.fileMenu.Append(ID_FILE_PERT, 'Particular', 'Particular Syscalls')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.Bind(wx.EVT_MENU, self.OnPerti, self.fitem3)
		self.frameMmap.SetMenuBar(self.menubar)

		commands.getstatusoutput("python pmmap.py")
		name = 'mmap_tab'		
		self.frameMmap = TestFrame(self,name)
		while len(column) > 0 : column.pop()
		self.frameMmap.Show()

		# Mprotect System Call

	def OnMprotect(self, e):        
		if not self.frameMprotect:
			self.frameMprotect = wx.Frame(self, -1, 'Particular System Call Statistics : MPROTECT', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.fitem2 = self.fileMenu.Append(ID_FILE_PERT, 'Particular', 'Particular Syscalls')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.Bind(wx.EVT_MENU, self.OnPerti, self.fitem3)
		self.frameMprotect.SetMenuBar(self.menubar)

		commands.getstatusoutput("python pmprotect.py")
		name = 'mprotect_tab'		
		self.frameMprotect = TestFrame(self,name)
		while len(column) > 0 : column.pop()
		self.frameMprotect.Show()

		# Munmap System Call
	
	def OnMunmap(self, e):        
		if not self.frameMunmap:
			self.frameMunmap = wx.Frame(self, -1, 'Particular System Call Statistics : MUNMAP', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.fitem3 = self.fileMenu.Append(ID_FILE_PERT, 'Particular', 'Particular Syscalls')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.Bind(wx.EVT_MENU, self.OnPerti, self.fitem3)
		self.frameMunmap.SetMenuBar(self.menubar)

		commands.getstatusoutput("python pmunmap.py")
		name = 'munmap_tab'		
		self.frameMunmap = TestFrame(self,name)
		while len(column) > 0 : column.pop()
		self.frameMunmap.Show()

		# Rt_sigaction System Call

	def OnRt_sigaction(self, e):        
		if not self.frameRt_sigaction:
			self.frameRt_sigaction = wx.Frame(self, -1, 'Particular System Call Statistics : RT_SIGACTION', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.fitem3 = self.fileMenu.Append(ID_FILE_PERT, 'Particular', 'Particular Syscalls')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.Bind(wx.EVT_MENU, self.OnPerti, self.fitem3)
		self.frameRt_sigaction.SetMenuBar(self.menubar)

		commands.getstatusoutput("python prt_sigaction.py")
		name = 'rt_sigaction_tab'		
		self.frameRt_sigaction = TestFrame(self,name)
		while len(column) > 0 : column.pop()
		self.frameRt_sigaction.Show()

		# Uname System Call
	def OnUname(self, e):        
		if not self.frameUname:
			self.frameUname = wx.Frame(self, -1, 'Particular System Call Statistics : UNAME', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.fitem3 = self.fileMenu.Append(ID_FILE_PERT, 'Particular', 'Particular Syscalls')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.Bind(wx.EVT_MENU, self.OnPerti, self.fitem3)
		self.frameUname.SetMenuBar(self.menubar)

		commands.getstatusoutput("python punam.py")
		name = 'uname_tab'		
		self.frameUname = TestFrame(self,name)
		while len(column) > 0 : column.pop()
		self.frameUname.Show()


		# SIGCHILD Signal
	def OnSigchild(self, e):        
		if not self.frameSigchild:
			self.frameSigchild = wx.Frame(self, -1, 'Particular Signals Statistics : SIGCHILD', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.fitem3 = self.fileMenu.Append(ID_FILE_PERT, 'Particular', 'Particular Syscalls')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.Bind(wx.EVT_MENU, self.OnPerti, self.fitem3)
		self.frameSigchild.SetMenuBar(self.menubar)

		commands.getstatusoutput("python psigchld.py")
		name = 'sigchld'		
		self.frameSigchild = TestFrame(self,name)
		while len(column) > 0 : column.pop()
		self.frameSigchild.Show()
	'''	
# SIGSEGV System Call
	def OnSigsegv(self, e):        
		if not self.frameSigsegv:
			self.frameSigsegv = wx.Frame(self, -1, 'Particular Signal Statistics : SIGSEGV', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem)
		self.frameSigsegv.SetMenuBar(self.menubar)

		self.panelSigsegv = wx.Panel(self.frameSigsegv)
		self.panelSigsegv.SetBackgroundColour('LightSlateGray')

		self.hboxSigsegv = wx.BoxSizer(wx.HORIZONTAL)

		self.tcSigsegv = wx.TextCtrl(self.panelSigsegv, wx.ID_ANY, size=(1000,500), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.VSCROLL)
		self.font.SetPointSize(14)
		self.tcSigsegv.SetFont(self.font)
		ProgName = self.tc12.GetValue()

		output = commands.getstatusoutput("python sigsegv.py")
		self.tcSigsegv.AppendText("Reasons for Segmentation Fault in your Program...\n")
		self.tcSigsegv.AppendText(output[1])
		
		self.hboxSigsegv.Add(self.tcSigsegv, flag=wx.LEFT | wx.RIGHT, border=20)
		self.panelSigsegv.SetSizer(self.hboxSigsegv)
		self.frameSigsegv.Show()
		#ProgName = ''
	'''


# Information of All System Calls

	def OnInfo(self, e):        
		if not self.frameInfo:
			self.frameInfo = wx.Frame(self, -1, 'Information of All System Calls and Signals in Particular Statistics', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.frameInfo.SetMenuBar(self.menubar)

		self.panelInfo = wx.Panel(self.frameInfo)
		self.panelInfo.SetBackgroundColour('LightSlateGray')
		self.vboxInfo = wx.BoxSizer(wx.VERTICAL)

		self.hboxInfo1 = wx.BoxSizer(wx.HORIZONTAL)
		self.tcInfo1 = wx.TextCtrl(self.panelInfo, wx.ID_ANY, size=(1200,600), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.VSCROLL)
		self.font.SetPointSize(13)
		self.tcInfo1.SetFont(self.font)

		self.tcInfo1.AppendText("\n\t\t *** System Call Information ***\n\n")

		self.tcInfo1.AppendText("   1. Read     : \n\t\t Structure: ssize_t read(int fd, void *buf, size_t count); \n\t\t Read system call reads data, in bytes as specified by the caller, from the file specified in terms of fid and stores then into a buffer supplied \t\t\t by the calling process.\n\n")

		self.tcInfo1.AppendText("   2. Write    : \n\t\t Structure: size_t write(int fd, const void *buf, size_t nbytes); \n\t\t Write system call writes data, in bytes as specified by the caller, from a buffer declared by the user in the program and then writes it into \t\t\t the file specified in terms of fid supplied by the calling process.\n\n")

		self.tcInfo1.AppendText("   3. Access   : \n\t\t Structure: int access(const char *pathname, int mode);\n\t\t The access system call determines whether the calling process has access permission to a file. It can check any combination of read, write, \t\t\t and execute permission, and it can also check for a file's existence.\n\n")

		self.tcInfo1.AppendText("   4. Pipe   : \n\t\t Structure: int pipe2(int pipefd[2], int flags);\n\t\t pipe()  creates  a pipe, a unidirectional data channel that can be used for interprocess communication.\n\n")

		self.tcInfo1.AppendText("   5. Fstat/Fstat64   : \n\t\t Structure: int fstat(int fd, struct stat *buf);\n\t\t The fstat system call takes a file descriptor as argument and returns attributes of the file that it identifies in a struct stat structure. While \t\t\t fstat64 return attributes in a struct stat64 structure, which represents file sizes with a 64-bit type, allowing the functions to work on files \t\t\t 2 GB and larger.\n\n")

		self.tcInfo1.AppendText("   6. Stat/Stat64   : \n\t\t Structure: int stat(const char *path, struct stat *buf);\n\t\t The stat system call take a filename as argument and returns attributes of the file. If the file name is a symbolic link, it returns attributes \t\t of the eventual target of the link. While stat64 return attributes in a struct stat64 structure, which represents file sizes with a 64-bit \n\t\t type, allowing the functions to work on files 2 GB and larger.\n\n")

		self.tcInfo1.AppendText("   7. Lstat/Lstat64   : \n\t\t Structure: int lstat(const char *path, struct stat *buf);\n\t\t The lstat functions take a filename as argument and returns attributes of the file. If the file name is a symbolic link, it returns attributes of \t\t\t the link itself. While ltat64 return attributes in a struct stat64 structure, which represents file sizes with a 64-bit type, allowing the \t\t\t functions to work on files 2 GB and larger.\n\n")

		self.tcInfo1.AppendText("   8. Mprotect   : \n\t\t Structure: int mprotect(const void *addr, size_t len, int prot);\n\t\t The system call mprotect specifies the desired protection for the memory page(s) containing part or all of the interval [addr,addr+len-1]. If \t\t\t an access is disallowed by the protection given it, the program receives a SIGSEGV.\n\n")

		self.tcInfo1.AppendText("   9. Munmap   : \n\t\t Structure: int munmap(void *start, size_t length);\n\t\t The munmap system call deletes the mappings for the specified address range, and causes further references to addresses within the range \t\t\t to generate invalid memory references.\n\n")

		self.tcInfo1.AppendText("   10. Mmap   : \n\t\t Structure: void *mmap(void *addr, size_t length, int prot, int flags, int fd, off_t offset);\n\t\t mmap asks the kernel to map len bytes of the object represented by the file descriptorfd, starting at offsetbytes into the file, into memory. \t\t\t That maps files or devices into memory. It is a method of memory-mapped file I/O.It used to map a file into memory so that then you can \t\t\t read and/or write the data in the file by accessing memory - no need for file I/O directly.\n\n")

		self.tcInfo1.AppendText("   11. Rt_sigaction   : \n\t\t Structure: int sigaction(int signum, const struct sigaction *act, struct sigaction *oldact);\n\t\t The sigaction system call is used to change the action taken by a process on receipt of a specific signal. system call allows users to specify \t\t\t an action for a signal; of course, if no signal action is defined, the kernel executes the default action associated with the delivered signal.\n\n")

		self.tcInfo1.AppendText("   12. Uname   : \n\t\tThe uname system call gives informatio about System.\n\n\n")

		self.tcInfo1.AppendText("\n\t\t\t *** Signals Information ***\n\n")

		self.tcInfo1.AppendText("   1. SIGCHILD     : \n\t\t The SIGCHLD signal is sent to a process when a child process terminates,  interrupts,\n\t\t or resumes after being interrupted. One common usage of the signal is to instruct the operating system to clean up the resources used by a \n\t\t child process after its termination without an explicit call to the wait system call.\n\n")

		#self.tcInfo1.AppendText("   2. SIGSEGV    : \n\t\t The SIGSEGV signal is sent to a process when it makes an invalid virtual memory reference,\n\t\t or segmentation fault, i.e. when it performs a segmentation violation.\n\n")

		self.hboxInfo1.Add(self.tcInfo1, flag=wx.LEFT, border=50)
		self.vboxInfo.Add(self.hboxInfo1, flag=wx.EXPAND | wx.CENTER | wx.TOP, border=50)
		self.vboxInfo.Add((-1, 10))

		self.panelInfo.SetSizer(self.vboxInfo)		        
		self.frameInfo.Show()

	# Comparitive Statistics

		# Time Graph

	def OnTime(self, e):
		if not self.frameTime:
			self.frameTime = wx.Frame(self, -1, 'Time Consumption of All System Calls', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.fitem3 = self.fileMenu.Append(ID_FILE_COMP, 'Comparative', 'Comparative Study of Syscalls')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.Bind(wx.EVT_MENU, self.OnCompa, self.fitem3)
		self.frameTime.SetMenuBar(self.menubar)

		self.panelTime = wx.Panel(self.frameTime)
		self.panelTime.SetBackgroundColour('LightSlateGray')

		self.vboxTime = wx.BoxSizer(wx.VERTICAL)
		self.hboxTime1 = wx.BoxSizer(wx.HORIZONTAL)
		
		self.vboxTime11 = wx.BoxSizer(wx.VERTICAL)
		self.stTime = wx.StaticText(self.panelTime, label='\t')
		self.stTime.SetFont(self.font)
		self.vboxTime11.Add(self.stTime, flag=wx.EXPAND | wx.LEFT , border=10)
		self.vboxTime11.Add((-1, 10))
		self.hboxTime1.Add(self.vboxTime11, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=5)
		
		self.vboxTime12 = wx.BoxSizer(wx.VERTICAL)
		self.imgtime = wx.EmptyImage(700,500)
		self.imgtimeCtrl = wx.StaticBitmap(self.panelTime, wx.ID_ANY, wx.BitmapFromImage(self.imgtime))

		output = commands.getstatusoutput("python ctime.py")
		commands.getoutput("python gtime.py")
		filepath = "Graphs/timegr.png"
		self.imgtime = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
		self.imgtimeCtrl.SetBitmap(wx.BitmapFromImage(self.imgtime))

		self.vboxTime12.Add(self.imgtimeCtrl, flag=wx.EXPAND | wx.RIGHT , border=10)
		self.vboxTime12.Add((-1, 10))
		self.hboxTime1.Add(self.vboxTime12, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5)

		self.vboxTime14 = wx.BoxSizer(wx.VERTICAL)
		self.stTime1 = wx.StaticText(self.panelTime, label='\t')
		self.stTime1.SetFont(self.font)
		self.vboxTime14.Add(self.stTime1, flag=wx.EXPAND | wx.LEFT , border=10)
		self.vboxTime14.Add((-1, 10))
		self.hboxTime1.Add(self.vboxTime14, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=5)

		self.vboxTime13 = wx.BoxSizer(wx.VERTICAL)
		self.tcTime1 = wx.TextCtrl(self.panelTime, wx.ID_ANY, size=(300,600), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.VSCROLL)
		self.font.SetPointSize(13)
		self.tcTime1.SetFont(self.font)
		string = ''
		self.tcTime1.AppendText(" System call       Time (usec)\n")
		self.tcTime1.AppendText("")
		curs.execute("SELECT * FROM time_tab")
		rows = curs.fetchall()
		for row in rows:
		    string = "\n*) "+row[0]+"  ->    "+str(row[1])
		    self.tcTime1.AppendText(string)		
		self.vboxTime13.Add(self.tcTime1, flag=wx.EXPAND | wx.RIGHT, border=5)
		self.vboxTime13.Add((-1, 10))

		self.hboxTime1.Add(self.vboxTime13, flag=wx.EXPAND | wx.RIGHT, border=5)

		self.vboxTime.Add(self.hboxTime1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=5)
		self.vboxTime.Add((-1, 10))

		self.hboxTime2 = wx.BoxSizer(wx.HORIZONTAL)
		self.tcTime = wx.TextCtrl(self.panelTime, wx.ID_ANY, size=(1200,50), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL | wx.VSCROLL)

		name = 'time_tab'
		self.tcTime.SetValue(output[1])

		self.hboxTime2.Add(self.tcTime, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP)

		self.vboxTime.Add(self.hboxTime2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=5)
		self.vboxTime.Add((-1, 10))

		self.panelTime.SetSizer(self.vboxTime)
		self.frameTime.Show()

		# Percentage Time Graph

	def OnPerTime(self, e):
		if not self.framePerTime:
			self.framePerTime = wx.Frame(self, -1, 'Percentage Time Consumption of All System Calls', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.fitem3 = self.fileMenu.Append(ID_FILE_COMP, 'Comparative', 'Comparative Study of Syscalls')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.Bind(wx.EVT_MENU, self.OnCompa, self.fitem3)
		self.framePerTime.SetMenuBar(self.menubar)

		self.panelPerTime = wx.Panel(self.framePerTime)
		self.panelPerTime.SetBackgroundColour('LightSlateGray')

		self.vboxPerTime = wx.BoxSizer(wx.VERTICAL)
		self.hboxPerTime1 = wx.BoxSizer(wx.HORIZONTAL)

		self.stPerTime = wx.StaticText(self.panelPerTime, label='\t')
		self.stPerTime.SetFont(self.font)
		self.hboxPerTime1.Add(self.stPerTime, flag=wx.EXPAND | wx.LEFT , border=5)

	
		self.imgPerTime = wx.EmptyImage(1100,700)
		self.imgPerTimeCtrl = wx.StaticBitmap(self.panelPerTime, wx.ID_ANY, wx.BitmapFromImage(self.imgPerTime))

		output = commands.getstatusoutput("python ctime.py")
		output = commands.getstatusoutput("python ctime_per.py")
		commands.getoutput("python gpertime.py")
		filepath = "Graphs/pertimegr.png"
		self.imgPerTime = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
		self.imgPerTimeCtrl.SetBitmap(wx.BitmapFromImage(self.imgPerTime))

		self.hboxPerTime1.Add(self.imgPerTimeCtrl, flag=wx.EXPAND | wx.LEFT, border=5)
		self.vboxPerTime.Add(self.hboxPerTime1, flag=wx.EXPAND | wx.LEFT | wx.TOP, border=5)

		self.vboxPerTime.Add((-1, 10))

		self.hboxPerTime2 = wx.BoxSizer(wx.HORIZONTAL)

		self.tcPerTime = wx.TextCtrl(self.panelPerTime, wx.ID_ANY, size=(1200,50), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL | wx.VSCROLL)

		name = 'timeper_tab'
		self.tcPerTime.SetValue(output[1])

		self.hboxPerTime2.Add(self.tcPerTime, flag=wx.EXPAND | wx.LEFT | wx.RIGHT , border=10)

		self.vboxPerTime.Add(self.hboxPerTime2, flag=wx.EXPAND | wx.CENTER | wx.BOTTOM, border=5)

		self.vboxPerTime.Add((-1, 10))

		self.panelPerTime.SetSizer(self.vboxPerTime)
		self.framePerTime.Show()

		# Error Graph

	def OnErr(self, e):
		if not self.frameErr:
			self.frameErr = wx.Frame(self, -1, 'Errors in All System Calls', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.fitem3 = self.fileMenu.Append(ID_FILE_COMP, 'Comparative', 'Comparative Study of Syscalls')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.Bind(wx.EVT_MENU, self.OnCompa, self.fitem3)
		self.frameErr.SetMenuBar(self.menubar)

		self.panelErr = wx.Panel(self.frameErr)
		self.panelErr.SetBackgroundColour('LightSlateGray')

		self.vboxErr = wx.BoxSizer(wx.VERTICAL)
		self.hboxErr1 = wx.BoxSizer(wx.HORIZONTAL)
		
		self.vboxErr11 = wx.BoxSizer(wx.VERTICAL)
		self.stErr = wx.StaticText(self.panelErr, label='\t')
		self.stErr.SetFont(self.font)
		self.vboxErr11.Add(self.stErr, flag=wx.EXPAND | wx.LEFT , border=10)
		self.vboxErr11.Add((-1, 10))
		self.hboxErr1.Add(self.vboxErr11, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=5)
		
		self.vboxErr12 = wx.BoxSizer(wx.VERTICAL)
		self.imgErr = wx.EmptyImage(700,500)
		self.imgErrCtrl = wx.StaticBitmap(self.panelErr, wx.ID_ANY, wx.BitmapFromImage(self.imgErr))

		output = commands.getstatusoutput("python cerror.py")
		commands.getoutput("python gerror.py")
		filepath = "Graphs/errorgr.png"
		self.imgErr = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
		self.imgErrCtrl.SetBitmap(wx.BitmapFromImage(self.imgErr))

		self.vboxErr12.Add(self.imgErrCtrl, flag=wx.EXPAND | wx.RIGHT , border=10)
		self.vboxErr12.Add((-1, 10))
		self.hboxErr1.Add(self.vboxErr12, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5)

		self.vboxErr14 = wx.BoxSizer(wx.VERTICAL)
		self.stErr1 = wx.StaticText(self.panelErr, label='\t')
		self.stErr1.SetFont(self.font)
		self.vboxErr14.Add(self.stErr1, flag=wx.EXPAND | wx.LEFT , border=10)
		self.vboxErr14.Add((-1, 10))
		self.hboxErr1.Add(self.vboxErr14, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=5)

		self.vboxErr13 = wx.BoxSizer(wx.VERTICAL)
		self.tcErr1 = wx.TextCtrl(self.panelErr, wx.ID_ANY, size=(300,600), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.VSCROLL)
		self.font.SetPointSize(13)
		self.tcErr1.SetFont(self.font)
		string = ''
		self.tcErr1.AppendText("System call      Error Count\n")
		curs.execute("SELECT * FROM error_tab")
		rows = curs.fetchall()
		for row in rows:
		    string = "\n*) "+row[0]+"  ->    "+str(row[1])
		    self.tcErr1.AppendText(string)

		self.vboxErr13.Add(self.tcErr1, flag=wx.EXPAND | wx.RIGHT, border=5)
		self.vboxErr13.Add((-1, 10))

		self.hboxErr1.Add(self.vboxErr13, flag=wx.EXPAND | wx.RIGHT, border=5)

		self.vboxErr.Add(self.hboxErr1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=5)
		self.vboxErr.Add((-1, 10))

		self.hboxErr2 = wx.BoxSizer(wx.HORIZONTAL)
		self.tcErr = wx.TextCtrl(self.panelErr, wx.ID_ANY, size=(1200,50), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL | wx.VSCROLL)

		name = 'error_tab'
		self.tcErr.SetValue(output[1])

		self.hboxErr2.Add(self.tcErr, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP)

		self.vboxErr.Add(self.hboxErr2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=5)
		self.vboxErr.Add((-1, 10))

		self.panelErr.SetSizer(self.vboxErr)
		self.frameErr.Show()

	# Percentage of Errors of system calls

		# Percentage Error Graph

	def OnPerErr(self, e):
		if not self.framePerErr:
			self.framePerErr = wx.Frame(self, -1, 'Percentage Errors in All System Calls', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.fitem3 = self.fileMenu.Append(ID_FILE_COMP, 'Comparative', 'Comparative Study of Syscalls')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.Bind(wx.EVT_MENU, self.OnCompa, self.fitem3)
		self.framePerErr.SetMenuBar(self.menubar)

		self.panelPerErr = wx.Panel(self.framePerErr)
		self.panelPerErr.SetBackgroundColour('LightSlateGray')

		self.vboxPerErr = wx.BoxSizer(wx.VERTICAL)
		self.hboxPerErr1 = wx.BoxSizer(wx.HORIZONTAL)

		self.stPerErr = wx.StaticText(self.panelPerErr, label='\t')
		self.stPerErr.SetFont(self.font)
		self.hboxPerErr1.Add(self.stPerErr, flag=wx.EXPAND | wx.LEFT , border=5)

	
		self.imgPerErr = wx.EmptyImage(1000,300)
		self.imgPerErrCtrl = wx.StaticBitmap(self.panelPerErr, wx.ID_ANY, wx.BitmapFromImage(self.imgPerErr))

		output = commands.getstatusoutput("python cerror.py")
		output = commands.getstatusoutput("python cerror_per.py")
		commands.getoutput("python gpererror.py")
		filepath = "Graphs/pererrorgr.png"
		self.imgPerErr = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
		self.imgPerErrCtrl.SetBitmap(wx.BitmapFromImage(self.imgPerErr))

		self.hboxPerErr1.Add(self.imgPerErrCtrl, flag=wx.EXPAND | wx.LEFT , border=5)
		self.vboxPerErr.Add(self.hboxPerErr1, flag=wx.EXPAND | wx.LEFT | wx.TOP, border=5)

		self.vboxPerErr.Add((-1, 10))

		self.hboxPerErr2 = wx.BoxSizer(wx.HORIZONTAL)

		self.tcPerErr = wx.TextCtrl(self.panelPerErr, wx.ID_ANY, size=(1200,50), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL | wx.VSCROLL)

		name = 'errorper_tab'
		self.tcPerErr.SetValue(output[1])

		self.hboxPerErr2.Add(self.tcPerErr, flag=wx.EXPAND | wx.LEFT | wx.RIGHT , border=10)

		self.vboxPerErr.Add(self.hboxPerErr2, flag=wx.EXPAND | wx.CENTER | wx.BOTTOM, border=5)

		self.vboxPerErr.Add((-1, 10))

		self.panelPerErr.SetSizer(self.vboxPerErr)
		self.framePerErr.Show()

	# Count of all System Calls

	def OnCnt(self, e):
		if not self.frameCnt:
			self.frameCnt = wx.Frame(self, -1, 'Count of All System Calls', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.fitem3 = self.fileMenu.Append(ID_FILE_COMP, 'Comparative', 'Comparative Study of Syscalls')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.Bind(wx.EVT_MENU, self.OnCompa, self.fitem3)
		self.frameCnt.SetMenuBar(self.menubar)

		self.panelCnt = wx.Panel(self.frameCnt)
		self.panelCnt.SetBackgroundColour('LightSlateGray')

		self.vboxCnt = wx.BoxSizer(wx.VERTICAL)
		self.hboxCnt1 = wx.BoxSizer(wx.HORIZONTAL)
		
		self.vboxCnt11 = wx.BoxSizer(wx.VERTICAL)
		self.stCnt = wx.StaticText(self.panelCnt, label='\t')
		self.stCnt.SetFont(self.font)
		self.vboxCnt11.Add(self.stCnt, flag=wx.EXPAND | wx.LEFT , border=10)
		self.vboxCnt11.Add((-1, 10))
		self.hboxCnt1.Add(self.vboxCnt11, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=5)
		
		self.vboxCnt12 = wx.BoxSizer(wx.VERTICAL)
		self.imgCnt = wx.EmptyImage(700,500)
		self.imgCntCtrl = wx.StaticBitmap(self.panelCnt, wx.ID_ANY, wx.BitmapFromImage(self.imgCnt))

		output = commands.getstatusoutput("python ccount.py")
		commands.getoutput("python gcount.py")
		filepath = "Graphs/countgr.png"
		self.imgCnt = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
		self.imgCntCtrl.SetBitmap(wx.BitmapFromImage(self.imgCnt))

		self.vboxCnt12.Add(self.imgCntCtrl, flag=wx.EXPAND | wx.RIGHT , border=10)
		self.vboxCnt12.Add((-1, 10))
		self.hboxCnt1.Add(self.vboxCnt12, flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5)

		self.vboxCnt14 = wx.BoxSizer(wx.VERTICAL)
		self.stCnt1 = wx.StaticText(self.panelCnt, label='\t')
		self.stCnt1.SetFont(self.font)
		self.vboxCnt14.Add(self.stCnt1, flag=wx.EXPAND | wx.LEFT , border=10)
		self.vboxCnt14.Add((-1, 10))
		self.hboxCnt1.Add(self.vboxCnt14, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=5)

		self.vboxCnt13 = wx.BoxSizer(wx.VERTICAL)
		self.tcCnt1 = wx.TextCtrl(self.panelCnt, wx.ID_ANY, size=(300,600), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.VSCROLL)
		self.font.SetPointSize(13)
		self.tcCnt1.SetFont(self.font)
		string = ''
		self.tcCnt1.AppendText("System call     Count\n")
		curs.execute("SELECT * FROM count_tab")
		rows = curs.fetchall()
		for row in rows:
		    string = "\n*) "+row[0]+"  ->    "+str(row[1])
		    self.tcCnt1.AppendText(string)
		
		self.vboxCnt13.Add(self.tcCnt1, flag=wx.EXPAND | wx.RIGHT, border=5)
		self.vboxCnt13.Add((-1, 10))

		self.hboxCnt1.Add(self.vboxCnt13, flag=wx.EXPAND | wx.RIGHT, border=5)

		self.vboxCnt.Add(self.hboxCnt1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=5)
		self.vboxCnt.Add((-1, 10))

		self.hboxCnt2 = wx.BoxSizer(wx.HORIZONTAL)
		self.tcCnt = wx.TextCtrl(self.panelCnt, wx.ID_ANY, size=(1200,50), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL | wx.VSCROLL)

		name = 'count_tab'
		self.tcCnt.SetValue(output[1])

		self.hboxCnt2.Add(self.tcCnt, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP)

		self.vboxCnt.Add(self.hboxCnt2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, border=5)
		self.vboxCnt.Add((-1, 10))

		self.panelCnt.SetSizer(self.vboxCnt)
		self.frameCnt.Show()

	# System Call Trace Output

	def OnSysTrace(self, e):        
		if not self.frameSysTrace:
			self.frameSysTrace = wx.Frame(self, -1, 'System Call Trace Output', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.frameSysTrace.SetMenuBar(self.menubar)

		self.vboxSysTrace = wx.BoxSizer(wx.VERTICAL)
		self.panelSysTrace = wx.Panel(self.frameSysTrace)
		self.panelSysTrace.SetBackgroundColour('LightSlateGray')

		name = 'sysdisp'
		self.frameSysTrace = TestFrame(self,name)
		while len(column) > 0 : column.pop()
		self.frameSysTrace.Show()

	# Signals Trace Output

	def OnSigTrace(self, e):        
		if not self.frameSigTrace:
			self.frameSigTrace = wx.Frame(self, -1, 'Signals Trace Output', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'Sigtem Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'Sigtem Call Analyzer Output')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.frameSigTrace.SetMenuBar(self.menubar)

		self.vboxSigTrace = wx.BoxSizer(wx.VERTICAL)
		self.panelSigTrace = wx.Panel(self.frameSigTrace)
		self.panelSigTrace.SetBackgroundColour('LightSlateGray')

		name = 'signals'
		self.frameSigTrace = TestFrame(self,name)
		while len(column) > 0 : column.pop()
		self.frameSigTrace.Show()

	# Unfinished  System Calls

	def OnUnfini(self, e):        
		if not self.frameUnfini:
			self.frameUnfini = wx.Frame(self, -1, 'Unfinished System Calls', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.frameUnfini.SetMenuBar(self.menubar)

		name = 'unfinished'
		self.frameUnfini = TestFrame(self,name)
		while len(column) > 0 : column.pop()
		self.frameUnfini.Show()

	# Resumed System Calls

	def OnResumed(self, e):        
		if not self.frameResumed:
			self.frameResumed = wx.Frame(self, -1, 'Resumed System Calls', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.frameResumed.SetMenuBar(self.menubar)

		name = 'resumed'
		self.frameResumed = TestFrame(self,name)
		while len(column) > 0 : column.pop()
		self.frameResumed.Show()

	#Click on refer button1 : \n and \t

	def OnRefer1(self, e):        
		if not self.frameRefer1:
			self.frameRefer1 = wx.Frame(self, -1, 'Code Optimization : Escape Charactors', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.frameRefer1.SetMenuBar(self.menubar)

		self.panelRefer1 = wx.Panel(self.frameRefer1)
		self.panelRefer1.SetBackgroundColour('LightSlateGray')

		self.hboxRefer = wx.BoxSizer(wx.HORIZONTAL)

		self.vboxRefer1 = wx.BoxSizer(wx.VERTICAL)

		self.hboxRefer13 = wx.BoxSizer(wx.HORIZONTAL)
		self.stRefer13 = wx.StaticText(self.panelRefer1, label='Using \ n')
		self.stRefer13.SetFont(self.font)
		self.hboxRefer13.Add(self.stRefer13, flag=wx.CENTER, border=50)
		self.vboxRefer1.Add(self.hboxRefer13, flag=wx.EXPAND | wx.LEFT , border=100)

		self.hboxRefer11 = wx.BoxSizer(wx.HORIZONTAL)
		self.tcRefer11 = wx.TextCtrl(self.panelRefer1, wx.ID_ANY, size=(300,250), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.VSCROLL)
		self.font.SetPointSize(13)
		self.tcRefer11.SetFont(self.font)
		self.tcRefer11.AppendText('\n #include<stdio.h>')
		self.tcRefer11.AppendText('\n void main()')
		self.tcRefer11.AppendText('\n {')
		self.tcRefer11.AppendText('\n\t printf("\ n hiii1");')
		self.tcRefer11.AppendText('\n\t printf("\ n hiii2");')
		self.tcRefer11.AppendText('\n\t printf("\ n hiii3");')
		self.tcRefer11.AppendText('\n\t printf("\ n hiii4");')
		self.tcRefer11.AppendText('\n\t printf("\ n hiii5");')
		self.tcRefer11.AppendText('\n }')
		self.hboxRefer11.Add(self.tcRefer11, flag=wx.CENTER, border=20)
		self.vboxRefer1.Add(self.hboxRefer11, flag=wx.EXPAND | wx.CENTER | wx.TOP, border=20)
		self.vboxRefer1.Add((-1, 10))

		self.hboxRefer12 = wx.BoxSizer(wx.HORIZONTAL)
		self.imgRefer1 = wx.EmptyImage(500,300)
		self.imgReferCtrl1 = wx.StaticBitmap(self.panelRefer1, wx.ID_ANY, wx.BitmapFromImage(self.imgRefer1))
		filepath = "Codeop/newline.png"
		self.imgRefer1 = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
		self.imgReferCtrl1.SetBitmap(wx.BitmapFromImage(self.imgRefer1))
		self.hboxRefer12.Add(self.imgReferCtrl1, flag=wx.CENTER, border=20)
		self.vboxRefer1.Add(self.hboxRefer12, flag=wx.EXPAND | wx.CENTER | wx.BOTTOM, border=20)
		self.vboxRefer1.Add((-1, 10))

		self.hboxRefer.Add(self.vboxRefer1, flag=wx.EXPAND | wx.LEFT , border=100)

		self.vboxRefer3 = wx.BoxSizer(wx.VERTICAL)
		self.stRefer3 = wx.StaticText(self.panelRefer1, label='\t\t\t\t')
		self.stRefer3.SetFont(self.font)
		self.vboxRefer3.Add(self.stRefer3, flag=wx.CENTER, border=50)
		self.hboxRefer.Add(self.vboxRefer3, flag=wx.EXPAND | wx.LEFT , border=100)

		self.vboxRefer2 = wx.BoxSizer(wx.VERTICAL)

		self.hboxRefer23 = wx.BoxSizer(wx.HORIZONTAL)
		self.stRefer23 = wx.StaticText(self.panelRefer1, label='Without using \ n')
		self.stRefer23.SetFont(self.font)
		self.hboxRefer23.Add(self.stRefer23, flag=wx.CENTER, border=50)
		self.vboxRefer2.Add(self.hboxRefer23, flag=wx.EXPAND | wx.LEFT , border=100)

		self.hboxRefer21 = wx.BoxSizer(wx.HORIZONTAL)
		self.tcRefer21 = wx.TextCtrl(self.panelRefer1, wx.ID_ANY, size=(300,250), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.VSCROLL)
		self.font.SetPointSize(13)
		self.tcRefer21.SetFont(self.font)
		self.tcRefer21.AppendText('\n #include<stdio.h>')
		self.tcRefer21.AppendText('\n void main()')
		self.tcRefer21.AppendText('\n {')
		self.tcRefer21.AppendText('\n\t printf("\ t hiii1");')
		self.tcRefer21.AppendText('\n\t printf("\ t hiii2");')
		self.tcRefer21.AppendText('\n\t printf("\ t hiii3");')
		self.tcRefer21.AppendText('\n\t printf("\ t hiii4");')
		self.tcRefer21.AppendText('\n\t printf("\ t hiii5");')
		self.tcRefer21.AppendText('\n}')
		self.hboxRefer21.Add(self.tcRefer21, flag=wx.CENTER , border=20)
		self.vboxRefer2.Add(self.hboxRefer21, flag=wx.EXPAND | wx.CENTER | wx.TOP, border=20)
		self.vboxRefer2.Add((-1, 10))

		self.hboxRefer22 = wx.BoxSizer(wx.HORIZONTAL)
		self.imgRefer2 = wx.EmptyImage(500,300)
		self.imgReferCtrl2 = wx.StaticBitmap(self.panelRefer1, wx.ID_ANY, wx.BitmapFromImage(self.imgRefer2))

		filepath = "Codeop/tab.png"
		self.imgRefer2 = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
		self.imgReferCtrl2.SetBitmap(wx.BitmapFromImage(self.imgRefer2))
		self.hboxRefer22.Add(self.imgReferCtrl2, flag=wx.CENTER, border=20)
		self.vboxRefer2.Add(self.hboxRefer22, flag=wx.EXPAND | wx.CENTER | wx.BOTTOM, border=20)
		self.vboxRefer2.Add((-1, 10))
		self.hboxRefer.Add(self.vboxRefer2, flag=wx.EXPAND | wx.RIGHT , border=100)
		self.panelRefer1.SetSizer(self.hboxRefer)
		self.frameRefer1.Show()

	#Click on refer button2 : fflush(stdout)

	def OnRefer2(self, e):        
		if not self.frameRefer2:
			self.frameRefer2 = wx.Frame(self, -1, 'Code Optimization : fflush(stdout)', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem)
		self.frameRefer2.SetMenuBar(self.menubar)

		self.panelRefer2 = wx.Panel(self.frameRefer2)
		self.panelRefer2.SetBackgroundColour('LightSlateGray')

		self.hboxRefer2 = wx.BoxSizer(wx.HORIZONTAL)

		self.vboxRefer21 = wx.BoxSizer(wx.VERTICAL)
		self.hboxRefer211 = wx.BoxSizer(wx.HORIZONTAL)
		self.stRefer211 = wx.StaticText(self.panelRefer2, label='Using fflush(stdout)')
		self.stRefer211.SetFont(self.font)
		self.hboxRefer211.Add(self.stRefer211, flag=wx.CENTER, border=50)
		self.vboxRefer21.Add(self.hboxRefer211, flag=wx.EXPAND | wx.LEFT , border=100)
		self.vboxRefer21.Add((-1, 10))

		self.hboxRefer212 = wx.BoxSizer(wx.HORIZONTAL)
		self.tcRefer212 = wx.TextCtrl(self.panelRefer2, wx.ID_ANY, size=(300,250), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.VSCROLL)
		self.font.SetPointSize(13)
		self.tcRefer212.SetFont(self.font)
		self.tcRefer212.AppendText('\n #include<stdio.h>')
		self.tcRefer212.AppendText('\n void main()')
		self.tcRefer212.AppendText('\n {')
		self.tcRefer212.AppendText('\n\t printf(" hiii1");')
		self.tcRefer212.AppendText('\n\t printf(" hiii2");')
		self.tcRefer212.AppendText('\n\t fflush(stdout);')
		self.tcRefer212.AppendText('\n\t printf(" hiii3");')
		self.tcRefer212.AppendText('\n\t printf(" hiii4");')
		self.tcRefer212.AppendText('\n\t printf(" hiii5");')
		self.tcRefer212.AppendText('\n }')
		self.hboxRefer212.Add(self.tcRefer212, flag=wx.CENTER, border=20)
		self.vboxRefer21.Add(self.hboxRefer212, flag=wx.EXPAND | wx.CENTER | wx.TOP, border=20)
		self.vboxRefer21.Add((-1, 10))

		self.hboxRefer213 = wx.BoxSizer(wx.HORIZONTAL)
		self.imgRefer213 = wx.EmptyImage(500,300)
		self.imgReferCtrl213 = wx.StaticBitmap(self.panelRefer2, wx.ID_ANY, wx.BitmapFromImage(self.imgRefer213))
		filepath = "Codeop/fflushm.png"
		self.imgRefer213 = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
		self.imgReferCtrl213.SetBitmap(wx.BitmapFromImage(self.imgRefer213))
		self.hboxRefer213.Add(self.imgReferCtrl213, flag=wx.CENTER, border=20)
		self.vboxRefer21.Add(self.hboxRefer213, flag=wx.EXPAND | wx.CENTER | wx.BOTTOM, border=20)
		self.vboxRefer21.Add((-1, 10))

		self.hboxRefer2.Add(self.vboxRefer21, flag=wx.EXPAND | wx.LEFT , border=100)

		self.vboxRefer22 = wx.BoxSizer(wx.VERTICAL)
		self.stRefer22 = wx.StaticText(self.panelRefer2, label='\t\t\t\t')
		self.stRefer22.SetFont(self.font)
		self.vboxRefer22.Add(self.stRefer22, flag=wx.CENTER, border=50)
		self.hboxRefer2.Add(self.vboxRefer22, flag=wx.EXPAND | wx.LEFT , border=100)

		self.vboxRefer23 = wx.BoxSizer(wx.VERTICAL)
		self.hboxRefer231 = wx.BoxSizer(wx.HORIZONTAL)
		self.stRefer231 = wx.StaticText(self.panelRefer2, label='Without Using fflush(stdout)')
		self.stRefer231.SetFont(self.font)
		self.hboxRefer231.Add(self.stRefer231, flag=wx.CENTER, border=50)
		self.vboxRefer23.Add(self.hboxRefer231, flag=wx.EXPAND | wx.LEFT , border=100)
		self.vboxRefer23.Add((-1, 10))

		self.hboxRefer232 = wx.BoxSizer(wx.HORIZONTAL)
		self.tcRefer232 = wx.TextCtrl(self.panelRefer2, wx.ID_ANY, size=(300,250), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.VSCROLL)
		self.font.SetPointSize(13)
		self.tcRefer232.SetFont(self.font)
		self.tcRefer232.AppendText('\n #include<stdio.h>')
		self.tcRefer232.AppendText('\n void main()')
		self.tcRefer232.AppendText('\n {')
		self.tcRefer232.AppendText('\n\t printf(" hiii1");')
		self.tcRefer232.AppendText('\n\t printf(" hiii2");')
		self.tcRefer232.AppendText('\n\t printf(" hiii3");')
		self.tcRefer232.AppendText('\n\t printf(" hiii4");')
		self.tcRefer232.AppendText('\n\t printf(" hiii5");')
		self.tcRefer232.AppendText('\n }')
		self.hboxRefer232.Add(self.tcRefer232, flag=wx.CENTER, border=20)
		self.vboxRefer23.Add(self.hboxRefer232, flag=wx.EXPAND | wx.CENTER | wx.TOP, border=20)
		self.vboxRefer23.Add((-1, 10))

		self.hboxRefer233 = wx.BoxSizer(wx.HORIZONTAL)
		self.imgRefer233 = wx.EmptyImage(500,300)
		self.imgReferCtrl233 = wx.StaticBitmap(self.panelRefer2, wx.ID_ANY, wx.BitmapFromImage(self.imgRefer233))
		filepath = "Codeop/wofflushm.png"
		self.imgRefer233 = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
		self.imgReferCtrl233.SetBitmap(wx.BitmapFromImage(self.imgRefer233))
		self.hboxRefer233.Add(self.imgReferCtrl233, flag=wx.CENTER, border=20)
		self.vboxRefer23.Add(self.hboxRefer233, flag=wx.EXPAND | wx.CENTER | wx.BOTTOM, border=20)
		self.vboxRefer23.Add((-1, 10))

		self.hboxRefer2.Add(self.vboxRefer23, flag=wx.EXPAND | wx.LEFT , border=100)

		self.panelRefer2.SetSizer(self.hboxRefer2)
		self.frameRefer2.Show()

	#Click on Refer Button3 : Pass by Value & Reference

	def OnRefer3(self, e):        
		if not self.frameRefer3:
			self.frameRefer3 = wx.Frame(self, -1, 'Code Optimization : Pass by Value & Pass by Reference', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem)
		self.frameRefer3.SetMenuBar(self.menubar)

		self.panelRefer3 = wx.Panel(self.frameRefer3)
		self.panelRefer3.SetBackgroundColour('LightSlateGray')

		self.hboxRefer3 = wx.BoxSizer(wx.HORIZONTAL)

		self.vboxRefer31 = wx.BoxSizer(wx.VERTICAL)
		self.hboxRefer311 = wx.BoxSizer(wx.HORIZONTAL)
		self.stRefer311 = wx.StaticText(self.panelRefer3, label='Using Pass By Value')
		self.stRefer311.SetFont(self.font)
		self.hboxRefer311.Add(self.stRefer311, flag=wx.CENTER, border=50)
		self.vboxRefer31.Add(self.hboxRefer311, flag=wx.EXPAND | wx.LEFT , border=100)
		self.vboxRefer31.Add((-1, 10))

		self.hboxRefer312 = wx.BoxSizer(wx.HORIZONTAL)
		self.tcRefer312 = wx.TextCtrl(self.panelRefer3, wx.ID_ANY, size=(300,250), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.VSCROLL)
		self.font.SetPointSize(13)
		self.tcRefer312.SetFont(self.font)
		self.tcRefer312.AppendText('\n #include<stdio.h>')
		self.tcRefer312.AppendText('\n int add(int a, int B);')
		self.tcRefer312.AppendText('\n void main()')
		self.tcRefer312.AppendText('\n {')
		self.tcRefer312.AppendText('\n\t int a=2, b=3, c;')
		self.tcRefer312.AppendText('\n\t printf(" a = %d",a);')
		self.tcRefer312.AppendText('\n\t printf(" b = %d",b);')
		self.tcRefer312.AppendText('\n\t c = add(a,b);')
		self.tcRefer312.AppendText('\n\t printf(" a = %d",a);')
		self.tcRefer312.AppendText('\n\t printf(" b = %d",b);')
		self.tcRefer312.AppendText('\n\t printf(" c = %d",c);')
		self.tcRefer312.AppendText('\n }')
		self.tcRefer312.AppendText('\n int add(int a,int b)')
		self.tcRefer312.AppendText('\n {')
		self.tcRefer312.AppendText('\n\t int c = 0;')
		self.tcRefer312.AppendText('\n\t c = a + b;')
		self.tcRefer312.AppendText('\n\t a = a + b;')
		self.tcRefer312.AppendText('\n\t return c;')
		self.tcRefer312.AppendText('\n }')
		self.hboxRefer312.Add(self.tcRefer312, flag=wx.CENTER, border=30)
		self.vboxRefer31.Add(self.hboxRefer312, flag=wx.EXPAND | wx.CENTER | wx.TOP, border=30)
		self.vboxRefer31.Add((-1, 10))

		self.hboxRefer313 = wx.BoxSizer(wx.HORIZONTAL)
		self.imgRefer313 = wx.EmptyImage(500,300)
		self.imgReferCtrl313 = wx.StaticBitmap(self.panelRefer3, wx.ID_ANY, wx.BitmapFromImage(self.imgRefer313))
		filepath = "Codeop/passvm.png"
		self.imgRefer313 = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
		self.imgReferCtrl313.SetBitmap(wx.BitmapFromImage(self.imgRefer313))
		self.hboxRefer313.Add(self.imgReferCtrl313, flag=wx.CENTER, border=30)
		self.vboxRefer31.Add(self.hboxRefer313, flag=wx.EXPAND | wx.CENTER | wx.BOTTOM, border=30)
		self.vboxRefer31.Add((-1, 10))

		self.hboxRefer3.Add(self.vboxRefer31, flag=wx.EXPAND | wx.LEFT , border=100)

		self.vboxRefer32 = wx.BoxSizer(wx.VERTICAL)
		self.stRefer32 = wx.StaticText(self.panelRefer3, label='\t\t\t\t')
		self.stRefer32.SetFont(self.font)
		self.vboxRefer32.Add(self.stRefer32, flag=wx.CENTER, border=50)
		self.hboxRefer3.Add(self.vboxRefer32, flag=wx.EXPAND | wx.LEFT , border=100)

		self.vboxRefer33 = wx.BoxSizer(wx.VERTICAL)
		self.hboxRefer331 = wx.BoxSizer(wx.HORIZONTAL)
		self.stRefer331 = wx.StaticText(self.panelRefer3, label='Using Pass By Reference')
		self.stRefer331.SetFont(self.font)
		self.hboxRefer331.Add(self.stRefer331, flag=wx.CENTER, border=50)
		self.vboxRefer33.Add(self.hboxRefer331, flag=wx.EXPAND | wx.CENTER , border=100)
		self.vboxRefer33.Add((-1, 10))

		self.hboxRefer332 = wx.BoxSizer(wx.HORIZONTAL)
		self.tcRefer332 = wx.TextCtrl(self.panelRefer3, wx.ID_ANY, size=(300,250), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.VSCROLL)
		self.font.SetPointSize(13)
		self.tcRefer332.SetFont(self.font)
		self.tcRefer332.AppendText('\n #include<stdio.h>')
		self.tcRefer332.AppendText('\n int add(int *a, int *b);')
		self.tcRefer332.AppendText('\n void main()')
		self.tcRefer332.AppendText('\n {')
		self.tcRefer332.AppendText('\n\t int a=2, b=3, c;')
		self.tcRefer332.AppendText('\n\t printf(" a = %d",a);')
		self.tcRefer332.AppendText('\n\t printf(" b = %d",b);')
		self.tcRefer332.AppendText('\n\t c = add(&a,&b);')
		self.tcRefer332.AppendText('\n\t printf(" a = %d",a);')
		self.tcRefer332.AppendText('\n\t printf(" b = %d",b);')
		self.tcRefer332.AppendText('\n\t printf(" c = %d",c);')
		self.tcRefer332.AppendText('\n }')
		self.tcRefer332.AppendText('\n int add(int *a,int *b)')
		self.tcRefer332.AppendText('\n {')
		self.tcRefer332.AppendText('\n\t int c = 0;')
		self.tcRefer332.AppendText('\n\t c = *a + *b;')
		self.tcRefer332.AppendText('\n\t *a = *a + *b;')
		self.tcRefer332.AppendText('\n\t return c;')
		self.tcRefer332.AppendText('\n }')
		self.hboxRefer332.Add(self.tcRefer332, flag=wx.CENTER, border=30)
		self.vboxRefer33.Add(self.hboxRefer332, flag=wx.EXPAND | wx.CENTER | wx.TOP, border=30)
		self.vboxRefer32.Add((-1, 10))

		self.hboxRefer333 = wx.BoxSizer(wx.HORIZONTAL)
		self.imgRefer333 = wx.EmptyImage(500,300)
		self.imgReferCtrl333 = wx.StaticBitmap(self.panelRefer3, wx.ID_ANY, wx.BitmapFromImage(self.imgRefer333))
		filepath = "Codeop/passrm.png"
		self.imgRefer333 = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
		self.imgReferCtrl333.SetBitmap(wx.BitmapFromImage(self.imgRefer333))
		self.hboxRefer333.Add(self.imgReferCtrl333, flag=wx.CENTER, border=30)
		self.vboxRefer33.Add(self.hboxRefer333, flag=wx.EXPAND | wx.CENTER | wx.BOTTOM, border=30)
		self.vboxRefer33.Add((-1, 10))

		self.hboxRefer3.Add(self.vboxRefer33, flag=wx.EXPAND | wx.RIGHT , border=100)

		self.panelRefer3.SetSizer(self.hboxRefer3)
		self.frameRefer3.Show()

	#Click on Refer Button4 : File Operation

	def OnRefer4(self, e):        
		if not self.frameRefer4:
			self.frameRefer4 = wx.Frame(self, -1, 'Code Optimization : File Operation', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem)
		self.frameRefer4.SetMenuBar(self.menubar)

		self.panelRefer4 = wx.Panel(self.frameRefer4)
		self.panelRefer4.SetBackgroundColour('LightSlateGray')

		self.hboxRefer4 = wx.BoxSizer(wx.HORIZONTAL)

		self.vboxRefer41 = wx.BoxSizer(wx.VERTICAL)
		self.hboxRefer411 = wx.BoxSizer(wx.HORIZONTAL)
		self.stRefer411 = wx.StaticText(self.panelRefer4, label='File Operation (Using String)')
		self.stRefer411.SetFont(self.font)
		self.hboxRefer411.Add(self.stRefer411, flag=wx.CENTER, border=50)
		self.vboxRefer41.Add(self.hboxRefer411, flag=wx.EXPAND | wx.LEFT , border=100)
		self.vboxRefer41.Add((-1, 10))

		self.hboxRefer412 = wx.BoxSizer(wx.HORIZONTAL)
		self.tcRefer412 = wx.TextCtrl(self.panelRefer4, wx.ID_ANY, size=(300,250), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.VSCROLL)
		self.font.SetPointSize(14)
		self.tcRefer412.SetFont(self.font)
		self.tcRefer412.AppendText('\n #include<stdio.h>')
		self.tcRefer412.AppendText('\n void main()')
		self.tcRefer412.AppendText('\n {')
		self.tcRefer412.AppendText('\n\t FILE *fp;')
		self.tcRefer412.AppendText('\n\t char s[80];')
		self.tcRefer412.AppendText('\n\t fp = fopen("input.txt","r");')
		self.tcRefer412.AppendText('\n\t if(fp == NULL)')
		self.tcRefer412.AppendText('\n\t {')
		self.tcRefer412.AppendText('\n\t\t puts("Cannot Open File...");')
		self.tcRefer412.AppendText('\n\t }')
		self.tcRefer412.AppendText('\n\t while(fgets(s,79,fp)!= NULL)')
		self.tcRefer412.AppendText('\n\t {')
		self.tcRefer412.AppendText('\n\t\t printf("%s",s);')
		self.tcRefer412.AppendText('\n\t }')
		self.tcRefer412.AppendText('\n\t fclose(fp);')
		self.tcRefer412.AppendText('\n }')
		self.hboxRefer412.Add(self.tcRefer412, flag=wx.CENTER, border=40)
		self.vboxRefer41.Add(self.hboxRefer412, flag=wx.EXPAND | wx.CENTER | wx.TOP, border=40)
		self.vboxRefer41.Add((-1, 10))

		self.hboxRefer413 = wx.BoxSizer(wx.HORIZONTAL)
		self.imgRefer413 = wx.EmptyImage(500,300)
		self.imgReferCtrl413 = wx.StaticBitmap(self.panelRefer4, wx.ID_ANY, wx.BitmapFromImage(self.imgRefer413))
		filepath = "Codeop/filecharam.png"
		self.imgRefer413 = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
		self.imgReferCtrl413.SetBitmap(wx.BitmapFromImage(self.imgRefer413))
		self.hboxRefer413.Add(self.imgReferCtrl413, flag=wx.CENTER, border=40)
		self.vboxRefer41.Add(self.hboxRefer413, flag=wx.EXPAND | wx.CENTER | wx.BOTTOM, border=40)
		self.vboxRefer41.Add((-1, 10))

		self.hboxRefer4.Add(self.vboxRefer41, flag=wx.EXPAND | wx.LEFT , border=100)

		self.vboxRefer42 = wx.BoxSizer(wx.VERTICAL)
		self.stRefer42 = wx.StaticText(self.panelRefer4, label='\t\t\t\t')
		self.stRefer42.SetFont(self.font)
		self.vboxRefer42.Add(self.stRefer42, flag=wx.CENTER, border=50)
		self.hboxRefer4.Add(self.vboxRefer42, flag=wx.EXPAND | wx.LEFT , border=100)

		self.vboxRefer43 = wx.BoxSizer(wx.VERTICAL)
		self.hboxRefer431 = wx.BoxSizer(wx.HORIZONTAL)
		self.stRefer431 = wx.StaticText(self.panelRefer4, label='File Operations Using Charactor')
		self.stRefer431.SetFont(self.font)
		self.hboxRefer431.Add(self.stRefer431, flag=wx.CENTER, border=50)
		self.vboxRefer43.Add(self.hboxRefer431, flag=wx.EXPAND | wx.CENTER , border=100)
		self.vboxRefer43.Add((-1, 10))

		self.hboxRefer432 = wx.BoxSizer(wx.HORIZONTAL)
		self.tcRefer432 = wx.TextCtrl(self.panelRefer4, wx.ID_ANY, size=(300,250), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.VSCROLL)
		self.font.SetPointSize(13)
		self.tcRefer432.SetFont(self.font)

		self.tcRefer432.AppendText('\n #include<stdio.h>')
		self.tcRefer432.AppendText('\n void main()')
		self.tcRefer432.AppendText('\n {')
		self.tcRefer432.AppendText('\n\t FILE *fp;')
		self.tcRefer432.AppendText('\n\t char ch;')
		self.tcRefer432.AppendText('\n\t fp = fopen("input.txt","r");')
		self.tcRefer432.AppendText('\n\t while(1)')
		self.tcRefer432.AppendText('\n\t {')
		self.tcRefer432.AppendText('\n\t\t ch = fgetc(ch);')
		self.tcRefer432.AppendText('\n\t\t if(ch == EOF)')
		self.tcRefer432.AppendText('\n\t\t break;')
		self.tcRefer432.AppendText('\n\t\t printf("%c"),ch')
		self.tcRefer432.AppendText('\n\t }')
		self.tcRefer432.AppendText('\n\t fclose(fp);')
		self.tcRefer432.AppendText('\n }')
		self.hboxRefer432.Add(self.tcRefer432, flag=wx.CENTER, border=40)
		self.vboxRefer43.Add(self.hboxRefer432, flag=wx.EXPAND | wx.CENTER | wx.TOP, border=40)
		self.vboxRefer43.Add((-1, 10))

		self.hboxRefer433 = wx.BoxSizer(wx.HORIZONTAL)
		self.imgRefer433 = wx.EmptyImage(500,300)
		self.imgReferCtrl433 = wx.StaticBitmap(self.panelRefer4, wx.ID_ANY, wx.BitmapFromImage(self.imgRefer433))
		filepath = "Codeop/filestringm.png"
		self.imgRefer433 = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
		self.imgReferCtrl433.SetBitmap(wx.BitmapFromImage(self.imgRefer433))
		self.hboxRefer433.Add(self.imgReferCtrl433, flag=wx.CENTER, border=40)
		self.vboxRefer43.Add(self.hboxRefer433, flag=wx.EXPAND | wx.CENTER | wx.BOTTOM, border=40)
		self.vboxRefer43.Add((-1, 10))

		self.hboxRefer4.Add(self.vboxRefer43, flag=wx.EXPAND | wx.RIGHT , border=100)

		self.panelRefer4.SetSizer(self.hboxRefer4)
		self.frameRefer4.Show()

	#Click on Refer Button5 : Looping Constructions

	def OnRefer5(self, e):        
		if not self.frameRefer5:
			self.frameRefer5 = wx.Frame(self, -1, 'Code Optimization : Looping Constructions', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem)
		self.frameRefer5.SetMenuBar(self.menubar)

		self.panelRefer5 = wx.Panel(self.frameRefer5)
		self.panelRefer5.SetBackgroundColour('LightSlateGray')

		self.hboxRefer5 = wx.BoxSizer(wx.HORIZONTAL)

		self.vboxRefer51 = wx.BoxSizer(wx.VERTICAL)
		self.hboxRefer511 = wx.BoxSizer(wx.HORIZONTAL)
		self.stRefer511 = wx.StaticText(self.panelRefer5, label='Using For Loop')
		self.stRefer511.SetFont(self.font)
		self.hboxRefer511.Add(self.stRefer511, flag=wx.CENTER, border=50)
		self.vboxRefer51.Add(self.hboxRefer511, flag=wx.EXPAND | wx.LEFT , border=100)
		self.vboxRefer51.Add((-1, 10))

		self.hboxRefer512 = wx.BoxSizer(wx.HORIZONTAL)
		self.tcRefer512 = wx.TextCtrl(self.panelRefer5, wx.ID_ANY, size=(300,250), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.VSCROLL)
		self.font.SetPointSize(13)
		self.tcRefer512.SetFont(self.font)
		self.tcRefer512.AppendText('\n #include<stdio.h>')
		self.tcRefer512.AppendText('\n void main()')
		self.tcRefer512.AppendText('\n {')
		self.tcRefer512.AppendText('\n\t int i,j,k=1;')
		self.tcRefer512.AppendText('\n\t for(i=1;i<=100;i++)')
		self.tcRefer512.AppendText('\n\t {')
		self.tcRefer512.AppendText('\n\t\t printf(" %d",k++);')
		self.tcRefer512.AppendText('\n\t }')
		self.tcRefer512.AppendText('\n }')
		self.hboxRefer512.Add(self.tcRefer512, flag=wx.CENTER, border=20)
		self.vboxRefer51.Add(self.hboxRefer512, flag=wx.EXPAND | wx.CENTER | wx.TOP, border=20)
		self.vboxRefer51.Add((-1, 10))

		self.hboxRefer513 = wx.BoxSizer(wx.HORIZONTAL)
		self.imgRefer513 = wx.EmptyImage(500,300)
		self.imgReferCtrl513 = wx.StaticBitmap(self.panelRefer5, wx.ID_ANY, wx.BitmapFromImage(self.imgRefer513))
		filepath = "Codeop/form.png"
		self.imgRefer513 = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
		self.imgReferCtrl513.SetBitmap(wx.BitmapFromImage(self.imgRefer513))
		self.hboxRefer513.Add(self.imgReferCtrl513, flag=wx.CENTER, border=20)
		self.vboxRefer51.Add(self.hboxRefer513, flag=wx.EXPAND | wx.CENTER | wx.BOTTOM, border=20)
		self.vboxRefer51.Add((-1, 10))

		self.hboxRefer5.Add(self.vboxRefer51, flag=wx.EXPAND | wx.LEFT , border=100)

		self.vboxRefer52 = wx.BoxSizer(wx.VERTICAL)
		self.stRefer52 = wx.StaticText(self.panelRefer5, label='\t\t\t\t')
		self.stRefer52.SetFont(self.font)
		self.vboxRefer52.Add(self.stRefer52, flag=wx.CENTER, border=50)
		self.hboxRefer5.Add(self.vboxRefer52, flag=wx.EXPAND | wx.LEFT , border=100)

		self.vboxRefer53 = wx.BoxSizer(wx.VERTICAL)
		self.hboxRefer531 = wx.BoxSizer(wx.HORIZONTAL)
		self.stRefer531 = wx.StaticText(self.panelRefer5, label='Using While Loop')
		self.stRefer531.SetFont(self.font)
		self.hboxRefer531.Add(self.stRefer531, flag=wx.CENTER, border=50)
		self.vboxRefer53.Add(self.hboxRefer531, flag=wx.EXPAND | wx.CENTER , border=100)
		self.vboxRefer53.Add((-1, 10))
		self.hboxRefer532 = wx.BoxSizer(wx.HORIZONTAL)
		self.tcRefer532 = wx.TextCtrl(self.panelRefer5, wx.ID_ANY, size=(300,250), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.VSCROLL)
		self.font.SetPointSize(13)
		self.tcRefer532.SetFont(self.font)
		self.tcRefer532.AppendText('\n #include<stdio.h>')
		self.tcRefer532.AppendText('\n void main()')
		self.tcRefer532.AppendText('\n {')
		self.tcRefer532.AppendText('\n\t while(i<=100)')
		self.tcRefer532.AppendText('\n\t {')
		self.tcRefer532.AppendText('\n\t\t printf(" %d",k++);')
		self.tcRefer532.AppendText('\n\t\t i++;')
		self.tcRefer532.AppendText('\n\t }')
		self.tcRefer532.AppendText('\n }')
		self.hboxRefer532.Add(self.tcRefer532, flag=wx.CENTER, border=20)
		self.vboxRefer53.Add(self.hboxRefer532, flag=wx.EXPAND | wx.CENTER | wx.TOP, border=20)
		self.vboxRefer53.Add((-1, 10))

		self.hboxRefer533 = wx.BoxSizer(wx.HORIZONTAL)
		self.imgRefer533 = wx.EmptyImage(500,300)
		self.imgReferCtrl533 = wx.StaticBitmap(self.panelRefer5, wx.ID_ANY, wx.BitmapFromImage(self.imgRefer533))
		filepath = "Codeop/whilem.png"
		self.imgRefer533 = wx.Image(filepath, wx.BITMAP_TYPE_ANY)
		self.imgReferCtrl533.SetBitmap(wx.BitmapFromImage(self.imgRefer533))
		self.hboxRefer533.Add(self.imgReferCtrl533, flag=wx.CENTER, border=20)
		self.vboxRefer53.Add(self.hboxRefer533, flag=wx.EXPAND | wx.CENTER | wx.BOTTOM, border=20)
		self.vboxRefer53.Add((-1, 10))

		self.hboxRefer5.Add(self.vboxRefer53, flag=wx.EXPAND | wx.RIGHT , border=100)

		self.panelRefer5.SetSizer(self.hboxRefer5)
		self.frameRefer5.Show()


	# Some More Hints of Code Optimization

	def OnHints(self, e):        
		if not self.frameHints:
			self.frameHints = wx.Frame(self, -1, 'Some Hints For Code Optimization', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem1 = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem2 = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem1)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem2)
		self.frameHints.SetMenuBar(self.menubar)

		self.panelHints = wx.Panel(self.frameHints)
		self.panelHints.SetBackgroundColour('LightSlateGray')

		self.vboxHints = wx.BoxSizer(wx.VERTICAL)

		self.hboxHints1 = wx.BoxSizer(wx.HORIZONTAL)
		self.tcHints1 = wx.TextCtrl(self.panelHints, wx.ID_ANY, size=(1200,600), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.VSCROLL)
		self.font.SetPointSize(13)
		self.tcHints1.SetFont(self.font)
		self.tcHints1.AppendText("   1.  Minimize the use of global variables in the program.\n\n")
		self.tcHints1.AppendText("   2.  Declare all functions other than global variables as static within the file.\n\n")
		self.tcHints1.AppendText("   3.  Use word size variables such as int and float instead of char, short, and double.\n\n")
		self.tcHints1.AppendText("   4.  Avoid using recursion.\n\n")
		self.tcHints1.AppendText("   5.  Use single-dimensional arrays.\n\n")
		self.tcHints1.AppendText("   6.  Avoid using the sqrt() function as it is CPU intensive.\n\n")
		self.tcHints1.AppendText("   7.  Do not split closely related functions into separate files.\n\n")
		self.tcHints1.AppendText("   8.  Use puts() function instead of the printf function.\n\n")
		self.tcHints1.AppendText("   9. Use mallopt() if the compiler supports this function to control malloc function.\n\n")
		self.tcHints1.AppendText("   10. Use inline functions instead of small functions to save CPU time.\n\n")

		self.hboxHints1.Add(self.tcHints1, flag=wx.LEFT, border=50)
		self.vboxHints.Add(self.hboxHints1, flag=wx.EXPAND | wx.CENTER | wx.TOP, border=50)
		self.vboxHints.Add((-1, 10))

		self.panelHints.SetSizer(self.vboxHints)		        
		self.frameHints.Show()

# Test Your Program
	def OnTest(self, e):        
		if not self.frameTest:
			self.frameTest = wx.Frame(self, -1, 'Code Optimization : Test your Program', pos = (25,25), size = (1300,700), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
		self.menubar = wx.MenuBar()
		self.fileMenu = wx.Menu()
		self.fitem = self.fileMenu.Append(ID_FILE_OPEN, 'Quit', 'Quit application')
		self.fitem = self.fileMenu.Append(ID_FILE_INPUT, 'Main', 'System Call Analyzer')
		self.fitem = self.fileMenu.Append(ID_FILE_HOME, 'Home', 'System Call Analyzer Output')
		self.menubar.Append(self.fileMenu, '&File')
		self.Bind(wx.EVT_MENU, self.OnQuit, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnInput, self.fitem)
		self.Bind(wx.EVT_MENU, self.OnHome, self.fitem)
		self.frameTest.SetMenuBar(self.menubar)

		self.panelTest = wx.Panel(self.frameTest)
		self.panelTest.SetBackgroundColour('LightSlateGray')

		self.vboxTest = wx.BoxSizer(wx.VERTICAL)
		self.hboxTest1 = wx.BoxSizer(wx.HORIZONTAL)
		self.hboxTest2 = wx.BoxSizer(wx.HORIZONTAL)
		self.vboxTest1 = wx.BoxSizer(wx.VERTICAL)
		self.vboxTest2 = wx.BoxSizer(wx.VERTICAL)
		self.vboxTest3 = wx.BoxSizer(wx.VERTICAL)
		self.hboxTest3 = wx.BoxSizer(wx.HORIZONTAL)

		self.stTest = wx.StaticText(self.panelTest, label='\t')
		self.hboxTest1.Add(self.stTest, border=10)
		self.vboxTest.Add(self.hboxTest1, flag=wx.EXPAND | wx.CENTER | wx.TOP, border=10)
		self.vboxTest.Add((-1, 10))

		self.tcTest = wx.TextCtrl(self.panelTest, wx.ID_ANY, size=(800,500), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.VSCROLL)
		self.font.SetPointSize(14)
		self.tcTest.SetFont(self.font)
		ProgName = self.tc12.GetValue()
		#flag1 = 0
		self.tcTest.AppendText("\nPlease do the following if possible...\n")

		if ProgName != '':

			if not self.framePNCont:
				self.framePNCont = wx.Frame(self, -1, 'Program Name', pos = (300,300), size = (500,200), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
			self.panelPNCont = wx.Panel(self.framePNCont)

			self.vboxPNCont = wx.BoxSizer(wx.VERTICAL)
			self.hboxPNCont1 = wx.BoxSizer(wx.HORIZONTAL)
			self.hboxPNCont2 = wx.BoxSizer(wx.HORIZONTAL)

			self.stpnc = wx.StaticText(self.panelPNCont, label='Do you want to Continue With the Program \n Name Entered on Main Screen ???')

			self.stpnc.SetFont(self.font)
			self.hboxPNCont1.Add(self.stpnc, flag=wx.CENTER | wx.TOP, border=15)

			self.vboxPNCont.Add(self.hboxPNCont1, flag=wx.CENTER | wx.TOP, border=15)
			self.vboxPNCont.Add((-1, 10))

			self.btny = wx.Button(self.panelPNCont, label='YES', size=(150, 50))
			self.btny.Bind(wx.EVT_BUTTON, self.OnY)
			self.hboxPNCont2.Add(self.btny, flag=wx.ALIGN_LEFT | wx.BOTTOM, border=15)

			self.btnn = wx.Button(self.panelPNCont, label='NO', size=(150, 50))
			self.btnn.Bind(wx.EVT_BUTTON, self.OnN)
			self.hboxPNCont2.Add(self.btnn, flag=wx.ALIGN_RIGHT | wx.BOTTOM, border=15)

			self.vboxPNCont.Add(self.hboxPNCont2, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=15)
			self.vboxPNCont.Add((-1, 10))

			self.panelPNCont.SetSizer(self.vboxPNCont)
			self.framePNCont.Show()
			ProgName = ''

		else:
			flag1 = 0
			self.Ask()


	def OnOpt(self):
		
		lineno = []
		lineno1 = []
		lineno2 = []
		lineno4 = []
		string = ''
		string1 = ''
		i = 1
		
		ProgName = self.tc12.GetValue()
		#print ProgName
		if ProgName == '':
			ProgName = self.tcp.GetValue()
		#print flag1
		if flag1 == 1:
			ProgName = self.tcp.GetValue()
		#print ProgName
		#flag = 1

		#if flag2 == 1:
			
		flag2 = 0

		while len(lineno) > 0 : lineno.pop()
		lineno = self.checkw(ProgName)
		if lineno != []:
			for no in lineno:
				string = string+", "+str(no)
			string1 = "\n\t"+str(i)+". In line numbers: "+string+" ->You can use 'for loop' instead of 'while loop' !!!"
			self.tcTest.AppendText(string1)
			i=i+1
			flag2 = 1
		i = 1
		string = ''
		string1 = ''

		while len(lineno1) > 0 : lineno1.pop()
		lineno1 = self.checkf(ProgName)
		if lineno1 != []:
			for no1 in lineno1:
				string = string+", "+str(no1)
			string1 = "\n\t"+str(i)+". In line numbers: "+string+" ->Please avoide use of 'fflush' !!!"
			self.tcTest.AppendText(string1)
			i=i+1
			flag2 = 1
		i = 1
		string = ''
		string1 = ''
		while len(lineno2) > 0 : lineno2.pop()
		lineno2 = self.checkc(ProgName)

		if lineno2 != []:
			for no2 in lineno2:
				string = string+", "+str(no2)
			string1 = "\n\t"+str(i)+". In line numbers: "+string+" ->You can use 'fgets insted of 'fgetc' !!!"
			self.tcTest.AppendText(string1)
			i=i+1
			flag2 = 1
		i = 1
		string = ''
		string1 = ''
		while len(lineno4) > 0 : lineno4.pop()
		lineno4 = self.checkp(ProgName)

		if lineno4 != []:
			for no4 in lineno4:
				string = string+", "+str(no4)
			string1 = "\n\t"+str(i)+". In line numbers: "+string+" ->You can use 'puts' instead of 'printf' !!!"
			self.tcTest.AppendText(string1)
			i=i+1
			flag2 = 1
		i = 1
		
		if flag2 == 0:
			string1 = "\n\t No need to Optimize... Your program is Perfect !!! "
			self.tcTest.AppendText(string1)

		self.vboxTest1.Add(self.tcTest, flag=wx.LEFT, border=10)
		self.hboxTest2.Add(self.vboxTest1, flag=wx.LEFT, border=20)

		self.stTest = wx.StaticText(self.panelTest, label='\t')
		self.vboxTest2.Add(self.stTest, border=10)
		self.hboxTest2.Add(self.vboxTest2, flag=wx.CENTER)

		self.tcTestopt = wx.TextCtrl(self.panelTest, wx.ID_ANY, size=(300,500), style = wx.TE_MULTILINE | wx.TE_READONLY | wx.VSCROLL)
		self.font.SetPointSize(14)
		self.tcTestopt.SetFont(self.font)
		self.tcTestopt.AppendText("This is the information about \n timing requirment of your code :- ")

		cc = 'cc '+ProgName
		op = commands.getoutput(cc)
		
		commands.getoutput("strace -o sample1.txt -tt -T -f ./a.out")
		commands.getoutput("python codeoptiparser.py")
		codeop = commands.getstatusoutput("python codeop.py")
		self.tcTestopt.AppendText(codeop[1])
		self.vboxTest3.Add(self.tcTestopt, flag=wx.RIGHT, border=10)
		self.hboxTest2.Add(self.vboxTest3, flag=wx.RIGHT)

		self.vboxTest.Add(self.hboxTest2, flag=wx.EXPAND | wx.CENTER | wx.TOP, border=50)
		self.vboxTest.Add((-1, 10))

		self.btnback = wx.Button(self.panelTest, label='BACK', size=(150, 50))
		self.btnback.Bind(wx.EVT_BUTTON, self.OnBack)
		self.hboxTest3.Add(self.btnback, flag=wx.ALIGN_RIGHT | wx.BOTTOM, border=10)

		self.vboxTest.Add(self.hboxTest3, flag=wx.EXPAND | wx.RIGHT | wx.BOTTOM, border=10)
		self.vboxTest.Add((-1, 10))

		self.panelTest.SetSizer(self.vboxTest)
		self.frameTest.Show()
		#self.frameProgName.Hide()
		self.frameCode.Hide()
		ProgName = ''

	def OnBack(self, e):
		self.frameTest.Close()
		self.frameCode.Show()


	def OnY(self, e):
		flag1 = 0
		self.OnOpt()
		self.framePNCont.Hide()

	def OnN(self, e):
		#flag1 = 1
		self.Ask()
		self.framePNCont.Hide()

	def checkw(self, name):
		datafile = file(name)
		found = False
		lineno = 0
		lineno3 = []
		while len(lineno3) > 0 : lineno3.pop()
		for line in datafile:
			lineno = lineno + 1
			if 'while' in line:
				lineno3.append(lineno)
		return lineno3

	def checkf(self, name):
		datafile = file(name)
		found = False
		lineno = 0
		lineno7 = []
		while len(lineno7) > 0 : lineno7.pop()
		for line in datafile:
			lineno = lineno + 1
			if 'fflush' in line:
		                lineno7.append(lineno)
	        return lineno7

	def checkc(self, name):
		datafile = file(name)
		found = False
		lineno1 = 0
		lineno5 = []
		while len(lineno5) > 0 : lineno5.pop()

		for line in datafile:
			lineno1 = lineno1 + 1
			if 'fgetc' in line:
			        lineno5.append(lineno1)
		return lineno5

	def checkp(self, name):
		datafile = file(name)
		found = False
		lineno1 = 0
		lineno6 = []
		while len(lineno6) > 0 : lineno6.pop()

		for line in datafile:
			lineno1 = lineno1 + 1
			if 'printf' in line:
				lineno6.append(lineno1)
	        return lineno6

	def Ask(self):

			if not self.frameProgName:
				self.frameProgName = wx.Frame(self, -1, 'Program Name', pos = (300,300), size = (500,200), style = wx.RESIZE_BORDER | wx.CLOSE_BOX)
			self.panelProgName = wx.Panel(self.frameProgName)

			self.vboxProgName = wx.BoxSizer(wx.VERTICAL)

			ProgName = self.tc12.GetValue()

			if ProgName == '':
				self.stp = wx.StaticText(self.panelProgName, label='You havent entered Program Name in the \n Main Screen... Please Enter it here...')
			else:
				self.stp = wx.StaticText(self.panelProgName, label='Please Enter the Program Name here...')

			self.stp.SetFont(self.font)
			self.vboxProgName.Add(self.stp, flag=wx.CENTER | wx.TOP, border=15)
			self.vboxProgName.Add((-1, 10))

			self.tcp = wx.TextCtrl(self.panelProgName)
			self.vboxProgName.Add(self.tcp, flag=wx.EXPAND | wx.LEFT | wx.RIGHT , border=100)
			#print self.tcp.GetValue()
			self.vboxProgName.Add((-1, 10))

			self.btn = wx.Button(self.panelProgName, label='DONE', size=(150, 50))
			self.btn.Bind(wx.EVT_BUTTON, self.OnDone)
			self.vboxProgName.Add(self.btn, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=15)
			self.vboxProgName.Add((-1, 10))

			self.panelProgName.SetSizer(self.vboxProgName)
			self.frameProgName.Show()
			ProgName = ''


	def OnDone(self, e):
		ProgName = ''
		#print ProgName
		ProgName = self.tcp.GetValue()
		#print ProgName
		cat = "cat "+ProgName
		fileavail = commands.getstatusoutput(cat)
		nodir = "cat: "+ProgName+": No such file or directory"

		if fileavail[1] == nodir:
			self.NoDir()
		else:
			self.OnOpt()
			self.frameProgName.Close()
		#self.OnOpt()
		#ProgName = ''

# Tabular Display
class SimpleGrid(wx.grid.Grid):
	def __init__(self, parent,name):
		row_no = 0
		col_no = 0
		col1 = 0
		col2 = 0
		row1 = 0 
		row2 = 1
		wx.grid.Grid.__init__(self, parent, -1)
		conn = sqlite3.connect('sparse.db')

		curs = conn.cursor()
		with conn:
			curs.execute("SELECT COUNT(*) FROM %s" % (name))
			rows = curs.fetchall()

			for row in rows:
				row_no = row[0]

		curs.execute("pragma table_info(%s);" % (name))
		rows = curs.fetchall()

		for row in rows:
		        col_no = col_no + 1
		        column.append(row[1])

		self.CreateGrid(row_no, col_no)
		'''
		if row_no == 0:
			row_str = "No Entries In This Table "
			self.SetRowLabelValue(row1, row_str)
		else:
		'''	
		if name == 'sysdisp':
			self.SetColSize(0,200)
			self.SetColSize(1,200)
			self.SetColSize(2,200)
			self.SetColSize(3,200)
			self.SetColSize(4,200)
			self.SetColSize(5,200)
			#self.SetColSize(6,200)
		if name == 'signals':
			self.SetColSize(0,200)
			self.SetColSize(1,200)
			self.SetColSize(2,200)
			self.SetColSize(3,800)
		if name == 'unfinished':
			self.SetColSize(0,200)
			self.SetColSize(1,200)
			self.SetColSize(2,200)
			self.SetColSize(3,400)
		if name == 'resumed':
			self.SetColSize(0,200)
			self.SetColSize(1,200)
			self.SetColSize(2,200)
			self.SetColSize(3,400)
		elif name == 'errors':
			self.SetColSize(0,200)
			self.SetColSize(1,200)
			self.SetColSize(2,600)
			self.SetColSize(3,500)
		elif name == 'fileio_tab':
			self.SetColSize(0,300)
			self.SetColSize(1,125)
			self.SetColSize(2,125)
			self.SetColSize(3,125)
			self.SetColSize(4,125)
			self.SetColSize(5,125)
			self.SetColSize(6,125)
		elif name == 'summary_tab':
			self.SetColSize(0,200)
			self.SetColSize(1,200)
			self.SetColSize(2,200)
			self.SetColSize(3,200)
			self.SetColSize(4,200)
			self.SetColSize(5,200)
		elif name == 'access_tab':
			self.SetColSize(0,250)
			self.SetColSize(1,300)
			self.SetColSize(2,250)
			self.SetColSize(3,300)
		elif  name == 'pipe_tab':
			self.SetColSize(0,100)
			self.SetColSize(1,150)
			self.SetColSize(2,300)
			self.SetColSize(3,300)
			self.SetColSize(4,100)
			self.SetColSize(5,100)
			self.SetColSize(6,500)
		elif name == 'fstat_tab':
			self.SetColSize(0,400)
			self.SetColSize(1,250)
			self.SetColSize(2,250)
			self.SetColSize(3,250)
		elif name == 'stat_tab':
			self.SetColSize(0,400)
			self.SetColSize(1,250)
			self.SetColSize(2,250)
			self.SetColSize(3,250)
		elif name == 'lstat_tab':
			self.SetColSize(0,400)
			self.SetColSize(1,250)
			self.SetColSize(2,250)
			self.SetColSize(3,250)
		elif  name == 'mmap_tab':
			self.SetColSize(0,200)
			self.SetColSize(1,170)
			self.SetColSize(2,200)
			self.SetColSize(3,300)
			self.SetColSize(4,400)
		elif name == 'mprotect_tab':
			self.SetColSize(0,170)
			self.SetColSize(1,250)
			self.SetColSize(2,200)
			self.SetColSize(3,300)
			self.SetColSize(4,200)
			self.SetColSize(5,200)
		elif name == 'munmap_tab':
			self.SetColSize(0,200)
			self.SetColSize(1,300)
			self.SetColSize(2,250)
			self.SetColSize(3,250)
		elif name == 'rt_sigaction_tab':
			self.SetColSize(0,200)
			self.SetColSize(1,200)
			self.SetColSize(2,400)
			self.SetColSize(3,200)
		elif name == 'uname_tab':
			self.SetColSize(0,300)
			self.SetColSize(1,400)
		elif name == 'sigchld':
			self.SetColSize(0,200)
			self.SetColSize(1,200)
			self.SetColSize(2,200)
			self.SetColSize(3,200)
			self.SetColSize(4,300)
			

		for col in column:
			self.SetColLabelValue(col1, col)
			col1 = col1 + 1
        
            
		curs.execute("SELECT * FROM %s" % (name))
		rows = curs.fetchall()
        
		for row in rows:
			row_str = str(row2)
			self.SetRowLabelValue(row1, row_str)
			while col2<col_no:
				row_value_str = str(row[col2])
				self.SetCellValue(row1, col2, row_value_str)
				self.SetReadOnly(row1,col2,1)
				col2 = col2 + 1
			row1 = row1 + 1
			col2 = 0
			row2 = row2 + 1

class TestFrame(wx.Frame):
	def __init__(self, parent,name):
		if name == 'sysdisp':
			string = 'System Call Trace '
		elif name == 'signals':
			string = 'Signal Trace '
		elif name == 'errors':
			string = 'Error Analysis '
		elif name == 'fileio_tab':
			string = 'File Input/Output Analysis '
		elif name == 'summary_tab':
			string = 'Summary '
		elif name == 'access_tab':
			string = 'Particular System Call Statistics - ACCESS'
		elif name == 'pipe_tab':
			string = 'Particular System Call Statistics - PIPE'
		elif name == 'fstat_tab':
			string = 'Particular System Call Statistics - FSTAT'
		elif name == 'stat_tab':
			string = 'Particular System Call Statistics - STAT'
		elif name == 'lstat_tab':
			string = 'Particular System Call Statistics - LSTAT'
		elif name == 'mmap_tab':
			string = 'Particular System Call Statistics - MMAP'
		elif name == 'mprotect_tab':
			string = 'Particular System Call Statistics - MPROTECT'
		elif name == 'rt_sigaction_tab':
			string = 'Particular System Call Statistics - RT_SIGACTION'
		elif name == 'munmap_tab':
			string = 'Particular System Call Statistics - Munmap'
		elif name == 'uname_tab':
			string = 'Particular System Call Statistics - Uname'
		elif name == 'unfinished':
			string = 'Unfinished System Calls'
		elif name == 'resumed':
			string = 'Resumed System Call'
		elif name == 'sigchld':
			string = 'SIGCHILD Signals'

		wx.Frame.__init__(self, parent, title = string, pos = (25,25), size = (1300,700))
		grid = SimpleGrid(self,name)

def main():

	ex = wx.App()
	main = Example(None)
	ex.MainLoop()    

if __name__ == '__main__':
	main()
