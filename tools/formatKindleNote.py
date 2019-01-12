# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 23:05:14 2019

@author: zcy

将从Kindle中复制的文字格式化，清除文字间的空格，去掉额外的书籍信息，覆盖原文件。
"""

# 打开文件，读取一行，关闭文件
file = open('D:\\Documents\\formatKindleNote.txt', 'r', encoding='utf8')
notes = file.readlines()
file.close()

# 处理文字
for i, n in enumerate(notes):   
    if "(Kindle" in n: 
        notes[i] = ''
#        print(n)  
        continue
    if '#' in n:
        notes[i] = '\n\n'
#        print(n)  
        continue
    notes[i] = ''.join(n.split()) 
#notes = ''.join(notes)  
print(notes)



# 清除文字
file = open('D:\\Documents\\formatKindleNote.txt', 'w', encoding='utf8')
file.close()


# 打开文件，写入处理后的文字，关闭文件
file = open('D:\\Documents\\formatKindleNote.txt', 'a', encoding='utf8')             
for n in notes:
    file.write(n)    
file.close()