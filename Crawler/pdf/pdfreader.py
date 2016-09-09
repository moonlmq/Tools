#-*-coding:utf-8 -*-
"""
from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice

python3.0 pdfminer 3k
#获取文档对象
fp = open("基于Python的新浪微博数据爬虫_周中华.pdf","rb")

#创建一个与文档关联的解释器
parser = PDFParser(fp)

#PDF文档的对象
doc = PDFDocument()

#连接解释器和文档对象
parser.set_document(doc)
doc.set_parser(parser)

#初始化文档
doc.initialize("")

#创建PDF资源管理器
resource - PDFResourceManager()

#参数分析器
laparam = LAParams()

#创建一个聚合器
device = PDFPageAggregator(resource,laparam=laparam)

#创建一个PDF页面解释器
interpreter = PDFPageInterpreter(resource,device)

#使用文档对象得到页面的集合
for page in doc.get_pages():
	#使用页面解释器来读取
	interpreter.process_page(page)

	#使用聚合器来获取内容
	layout - device.get_result()

	for out in layout:
		if hasattr(out,"get_text"):
			print(out.get_text())
"""
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
# Open a PDF file.
fp = open(u"基于Python的新浪微博数据爬虫_周中华.pdf", 'rb')
# Create a PDF parser object associated with the file object.
parser = PDFParser(fp)
# Create a PDF document object that stores the document structure.
# Supply the password for initialization.
document = PDFDocument(parser, "")
# Check if the document allows text extraction. If not, abort.
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed
# Create a PDF resource manager object that stores shared resources.
rsrcmgr = PDFResourceManager()
# # Create a PDF device object.
# device = PDFDevice(rsrcmgr)
# Set parameters for analysis.
laparams = LAParams()
# Create a PDF page aggregator object.
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
# Create a PDF interpreter object.
interpreter = PDFPageInterpreter(rsrcmgr, device)
# Process each page contained in the document.
for page in PDFPage.create_pages(document):
    interpreter.process_page(page)
    # receive the LTPage object for the page.
    layout = device.get_result()
    for out in layout:
		if hasattr(out,"get_text"):
			print(out.get_text())