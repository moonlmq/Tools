# -*- coding:utf-8-*-
import immlib

def main(args):
	imm = immlib.Debugger()
	search_code = " ".join(args)

	#将要搜索的指令转换为相应的字节码
	search_bytes = imm.Assemble(search_code)
	#借助Search函数搜索出目标二进制模块中包含这一指令的所有内存地址
	search_results = imm.Search(search_bytes)

	for hit in search_results:
		#取的这个内存地址所在的内存页并确保此内存页可被执行
		code_page = imm.getMemoryPagebyAddress(hit)
		access = code_page.getAccesss(human = True)

		if "execute" in access.lower():
			imm.log("[*] Found: %s (0x%08x)" % (search_code, hit),address = hit)

	return "[*] Finished searching for instructions,check the Log window."