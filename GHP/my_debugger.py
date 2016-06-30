from ctypes import *
from my_debugger_defines import *
kernel32 = windll.kernel32


class debugger():
	def __init__(self):
		self.h_process = 	None
		self.pid =			None
		self.debugger_active = False

	def load(self,path_to_exe):
		# dwCreation flag determines how to create the process
		# set creation_flags = CREATE_NEW_CONSOLE if want to
		# see the GUI
		creation_flags = DEBUG_PROCESS
		#instantiate the structs
		startupinfo = STARTUPINFO()
		process_information = PROCESS_INFORMATION()
		# The following two options allow the started process
		# to be shown as a separate window. This also illustrates
		# how different settings in the STARTUPINFO struct can affect
		# the debuggee.
		startupinfo.dwFlags = 0x1
		startupinfo.wShowWindow = 0x0

		# Then initialize the cb variable in the STARTUPINFO struct
		# which is just the size of the struct itself
		startupinfo.cb = sizeof(startupinfo)
		if kernel32.CreateProcessA(path_to_exe,
			None,
			None,
			None,
			None,
			creation_flags,
			None,
			None,
			byref(startupinfo),
			byref(process_information)):
			print "[*] The process have been successfully launched!"
			print "[*] PID: %d" % process_information.dwProcessId

			# Obtain a valid handle to the newly created process
			# and store it for future acccess
			self.h_process=self.open_process(process_information.dwProcessId)
		else:
			print "[*] Error: 0x%08x." % kernel32.GetLastError()


	def open_process(self,pid):
		print "into open process"
		PROCESS_ALL_ACCESS =2035711
		h_process=kernel32.OpenProcess(PROCESS_ALL_ACCESS,False,pid)
		print "the h_process is "+ str(h_process)
		return h_process

	def attach(self,pid):
		self.h_process = self.open_process(pid)
		print "attach h_process is "+ str(self.h_process)
		# Attempt to attach to the process
		#if this fails  exit the call
		if kernel32.DebugActiveProcess(pid):
			self.debugger_active = True
			self.pid = int(pid)
			self.run()
		else:
			print "[*] Unable to attach to the process"

	def run(self):
		#poll the debuggee for debugging events
		while self.debugger_active == True:
			self.get_debug_event()

	def get_debug_event(self):
		debug_event = DEBUG_EVENT()
		continue_status = DBG_CONTINUE
		if kernel32.WaitForDebugEvent(byref(debug_event),INFINITE):
			# Not going to build any event handlers
			# just yet. Just resume the process for now.
			raw_input("Press a key to continue...")
			self.debugger_active = False
			kernel32.ContinueDebugEvent(debug_event.dwProcessId,
				debug_event.dwThreadId,continue_status)

	def detach(self):
		if kernel32.DebugActiveProcess(self.pid):
			print "[*] Finished debugging. Exiting..."
			return True
		else:
			print "There was an error"
			return False






deb = debugger()
pid = raw_input("Enter PID: ")
deb.attach(pid)
deb.detach()
