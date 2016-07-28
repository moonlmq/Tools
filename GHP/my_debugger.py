#-*-coding:utf-8 -*-
from ctypes import *
from my_debugger_defines import *
kernel32 = windll.kernel32


class debugger():
	def __init__(self):
		self.h_process = 	None
		self.pid =			None
		self.debugger_active = False
		self.h_thread        =     None
		self.context         =     None
		self.exception =None
		self.exception_address = None
		self.breakpoints = {}
		self.first_breakpoint = True
		self.hardware_breakpoints = {}

	def load(self,path_to_exe):
		# dwCreation flag 标志位控制进程的创建方式，若希望新创建的进程独占一个新的
		#控制台窗口，而不是与父进程共用同一个控制台，可以加上标志位CREATE_NEW_CONSOLE
		creation_flags = DEBUG_PROCESS
		#实例化结构体
		startupinfo = STARTUPINFO()
		process_information = PROCESS_INFORMATION()
		# 以下两个变量的共同作用下，新建进程将在一个单独的窗体中被显示，可以通过改变
		#STARTUPINFO中的各变量来控制debugee进程的行为
		startupinfo.dwFlags = 0x1
		startupinfo.wShowWindow = 0x0

		# 设置结构体STARTUPINFO中的成员变量cb的值，用以标志结构体本身的大小
		startupinfo.cb = sizeof(startupinfo)
		#在windows下创建一个新进程的工作可以由CreateProcessA完成
		if kernel32.CreateProcessA(path_to_exe,
			None,
			None,
			None,
			None,
			creation_flags,#开启调试功能
			None,
			None,
			byref(startupinfo),#指定进程的启动方式
			byref(process_information)):#记录进程成功启动后相关状态信息
			print ("[*] The process have been successfully launched!")
			print ("[*] PID: %d" % process_information.dwProcessId)

			# Obtain a valid handle to the newly created process
			# and store it for future acccess
			self.pid = process_information.dwProcessId
			self.h_process=self.open_process(process_information.dwProcessId)
		else:
			print ("[*] Error: 0x%08x." % kernel32.GetLastError())
			

	#获取进程句柄
	def open_process(self,pid):
		print ("into open process")
		PROCESS_ALL_ACCESS =2035711
		#OpenProcess可以获取句柄
		h_process=kernel32.OpenProcess(PROCESS_ALL_ACCESS,False,pid)
		print ("the h_process is "+ str(h_process))
		return h_process

	def attach(self,pid):
		self.h_process = self.open_process(pid)
		print ("attach h_process is "+ str(self.h_process))
		#实现进程附加
		if (kernel32.DebugActiveProcess(pid)):
			self.debugger_active = True
			self.pid = int(pid)
			print ("attach ok")
		else:
			print ("[*] Unable to attach to the process")
			print("[*] Errorcode:0x%08x." % kernel32.GetLastError())  

	def run(self):
		#poll the debuggee for debugging events
		while self.debugger_active == True:
			self.get_debug_event()

	def get_debug_event(self):
		debug_event = DEBUG_EVENT()
		continue_status = DBG_CONTINUE
		#waitfordebugevent收集发生在目标进程中的调试事件
		#第一个参数指向结构体DEBUG_EVENT,用于描述一个具体的调试事件
		#第二个参数表示等待下一个调试事件发生的时间上限
		if kernel32.WaitForDebugEvent(byref(debug_event),INFINITE):
			# Not going to build any event handlers
			# just yet. Just resume the process for now.
			# raw_input("Press a key to continue...")
			# self.debugger_active = False
			self.h_thread          = self.open_thread(debug_event.dwThreadId)
			self.context           = self.get_thread_context(h_thread=self.h_thread)
			self.debug_event       = debug_event
			print "Event Code: %d Thread ID: %d" %\
			(debug_event.dwDebugEventCode,debug_event.dwThreadId)
			#若事件码显示这是一个异常事件，则进一步检测其确切类型
			if debug_event.dwDebugEventCode == EXCEPTION_DEBUG_EVENT:
				#获取异常代码
				self.exception = debug_event.u.Exception.ExceptionRecord.ExceptionCode
				self.exception_address = debug_event.u.Exception.ExceptionRecord.ExceptionAddress
				if self.exception == EXCEPTION_ACCESS_VIOLATION:
					print "Access Voilation Detected."
				elif self.exception == EXCEPTION_BREAKPOINT:
					continue_status = self.exception_handler_breakpoint()
				elif self.exception == EXCEPTION_GUARD_PAGE:
					print "Guard Page Access Dectected"
				elif self.exception == EXCEPTION_SINGLE_STEP:
					self.exception_handler_single_step()
			#将目标进程恢复至原来的执行状态
			#第一二个参数来源于DEBUG_EVENT的同名成员变量
			#第三个参数决定目标进程是继续执行（DBG_CONTINUE)还是继续处理
			#所捕获的异常事件（DBG_EXECPTION_NOT_HANDLED
		kernel32.ContinueDebugEvent(debug_event.dwProcessId,
				debug_event.dwThreadId,continue_status)

	#DebugActiveProcessStop可以使调试器与被调试进程分离
	def detach(self):
		if kernel32.DebugActiveProcessStop(self.pid):
			print ("[*] Finished debugging. Exiting...")
			return True
		else:
			print ("There was an error")
			return False


	def open_thread(self,thread_id):
		#线程句柄可由OpenThread函数取的
		h_thread=kernel32.OpenThread(THREAD_ALL_ACCESS,None,thread_id)
		if h_thread is not None:
			return h_thread
		else:
			print "[*] Could not obtain a valid thread handle."
			return False

	def enumerate_threads(self):

		thread_entry = THREADENTRY32()
		thread_list = []
		#CreateToolhelp32Snapshot函数可以获取系统进程列表，系统中的
		#线程列表，被加载人某一进程的所有模块（DLLs）列表以及
		#某一进程所属堆列表
		#第一个参数用于告知希望获取信息的确切类型（线程列表，进程列表，模块列表还是堆列表）
		snapshot = kernel32.CreateToolhelp32Snapshot(TH32CS_SNAPTHREAD,self.pid)

		if snapshot is not None:
			thread_entry.dwSize = sizeof(thread_entry)
			success = kernel32.Thread32First(snapshot,byref(thread_entry))



			while success:
				#筛选目前进程下的线程
				if thread_entry.th32OwnerProcessID == self.pid:
					thread_list.append(thread_entry.th32ThreadID)
				#获取下一个线程数据
				success = kernel32.Thread32Next(snapshot,byref(thread_entry))
			kernel32.CloseHandle(snapshot)
			return thread_list
		else:
			return False

	def get_thread_context(self,thread_id=None,h_thread=None):
		context =CONTEXT()
		context.ContextFlags = CONTEXT_FULL | CONTEXT_DEBUG_REGISTERS
		#获取线程句柄
		h_thread = self.open_thread(thread_id)
		#从线程中提取上下文环境信息
		if kernel32.GetThreadContext(h_thread,byref(context)):
			kernel32.CloseHandle(h_thread)
			return context
		else:
			return False


	def exception_handler_breakpoint(self):
		print "[*] Inside the breakpoint handler."
		print "Exception address: 0x%08x" % self.exception_address

		return DBG_CONTINUE
		#读取写入内存ReadProcessMemory和WriteProcessMemory
		#第一个参数为进程句柄，第二个参数为希望读取或写入数据所在的起始内存地址
		#第三个参数作为一个数据指针正指向着希望读取或写入的数据
		#第四个参数指明了所要读取或写入数据的大小
	def read_process_memory(self,address,length):
		data = ""
		read_buf = create_string_buffer(length)
		count = c_ulong(0)

		if not kernel32.ReadProcessMemory(self.h_process,address,read_buf,length,byref(count)):
			return False
		else:
			data += read_buf.raw
			return data
	def write_process_memory(self,address,data):
		count = c_ulong(0)
		length = len(data)

		c_data = c_char_p(data[count.value:])

		if not kernel32.WriteProcessMemory(self.h_process,address,c_data,length,byref(count)):
			return False
		else:
			return True

	def bp_set(self,address):
		print "[*] Setting breakpoint at: 0x%08x" % address
		if not self.breakpoints.has_key(address):
			try:
				#备份这个内存地址上原有的字节值
				original_byte = self.read_process_memory(address,1)
				#写入一个INT3中断指令，其操作码为0xCC
				self.write_process_memory(address,"\xCC")

				#将设下的断点记录在一个内部的断点列表中
				self.breakpoints[address] = (address,original_byte)
			except:
				return False
		return True

	def func_resolve(self,dll,function):
		#获得目标函数所在模块（可以是.dll或.exe文件）
		#取的相关模块句柄
		handle = kernel32.GetModuleHandleA(dll)
		#GetProcAddress帮助获取某一函数的虚拟内存地址
		address = kernel32.GetProcAddress(handle,function)

		kernel32.CloseHandle(handle)
		return address

	def bp_set_hw(self,address, length,condition):
		#检测硬件断点的长度是否有效
		if length not in (1,2,4):
			return False
		else:
			length -=1
		#检测硬件断点的触发条件是否有效
		if condition not in (HW_ACCESS,HW_EXECUTE,HW_WRITE):
			return False
		#检测是否存在空置的调试寄存器槽
		if not self.hardware_breakpoints.has_key(0):
			available = 0
		elif not self.hardware_breakpoints.has_key(1):
			available = 1
		elif not self.hardware_breakpoints.has_key(2):
			available = 2
		elif not self.hardware_breakpoints.has_key(3):
			available = 3
		else:
			return False

		#在每一个线程环境下设置调试寄存器
		for thread_id in self.enumerate_threads():
			context = self.get_thread_context(thread_id=thread_id)
			#通过DR7中相应的标志位来激活断点
			context.Dr7 |= 1 <<(available*2)
			#在空置的寄存器中写入断点地址
			if available == 0:
				context.Dr0 = address
			elif available == 1:
				context.Dr1 == address
			elif available == 2:
				context.Dr1 == address
			elif available == 3:
				context.Dr1 == address
			#设置硬件断点的触发条件
			context.Dr7 |= condition <<((available*4)+16)
			#设置硬件断点的长度
			context.Dr7 |= length <<((available*4)+18)
			#提交经改动后的线程上下文环境信息
			h_thread = self.open_thread(thread_id)
			kernel32.SetThreadContext(h_thread,byref(context))

		#更新内部的硬件断点列表
		self.hardware_breakpoints[available] = (address,length,condition)
		return True

	def exception_handler_single_step(self):
		#判断这个但不事件是否由一个硬件断点所触发，若是则捕获这个断点
		#事件，根据Intel给出的文档，通过检测Dr6寄存器上的BS标志位来判
		#断出这个单步事件的触发原因，然而windows系统似乎并没有正确地将
		#这个标志位传递
		