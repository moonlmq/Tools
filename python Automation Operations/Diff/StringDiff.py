# -*- coding: utf-8 -*-
#################################################
#'-' 包含在第一个序列行中，但不包含在第二个序列行
#'+' 包含在第二个序列行中，但不包含在第一个序列行
#''   两个序列行一致
#'?' 标志两个序列行存在增量差异
#'^' 标志出两个序列行存在的差异字符
#################################################

####################################################
#运行python StringDiff.py > diff.html 可以用html查看
####################################################

import difflib
text1 = """text1 :
sdklfjslfvdk
fewfs
sefsefesfes
"""
text1_lines = text1.splitlines()
text2 = """text2 :
sdklfjslf22k
fewf3
sefse344es
"""
text2_lines =text2.splitlines()
# d = difflib.Differ()
# diff = d.compare(text1_lines,text2_lines)
# print '\n'.join(list(diff))

e = difflib.HtmlDiff()
print e.make_file(text1_lines,text2_lines)