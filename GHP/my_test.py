#-*-coding:utf-8 -*-
import my_debugger

debugger = my_debugger.debugger()

pid = raw_input("PID:")

debugger.attach(int(pid))
printf_address = debugger.func_resolve("msvcrt.dll","printf")
print "[*] Address of printf: 0x%08x" % printf_address
debugger.bp_set(printf_address)
debugger.run()

# print "go list"
# list = debugger.enumerate_threads()

# for thread in list:

# 	thread_context = debugger.get_thread_context(thread)

# 	print "[*] Dumping registers for thread ID: 0x%08x" % thread
# 	print "[**] EIP: 0x%08x" % thread_context.Eip
# 	print "[**] ESP: 0x%08x" % thread_context.Esp
# 	print "[**] EBP: 0x%08x" % thread_context.Ebp
# 	print "[**] EAX: 0x%08x" % thread_context.Eax
# 	print "[**] EBX: 0x%08x" % thread_context.Ebx
# 	print "[**] ECX: 0x%08x" % thread_context.Ecx
# 	print "[**] EDX: 0x%08x" % thread_context.Edx
# 	print "[*] END DUNP"

debugger.detach()