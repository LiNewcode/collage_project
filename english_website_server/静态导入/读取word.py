'''
    #利用python读取word文档，表格文档
'''
# 导入所需库
import re
from lxml import etree

# /html/body/div/div/div/div/span
with open('F:\\英语\\20-4\\Oct.30 · 2021.html', 'r', encoding='utf-8') as fp:
    page = fp.read()

content = re.split('<span.*?</span>', page)
print(len(content))
sentence = re.findall('<span.*?</span>', page)
page = []
index = 0
for i in sentence:
    sen = re.findall('>(.*?)</span>', i)[0]
    print(sen)
    fix = re.findall('<span.*?>',i)[0]
    # print(fix)
    en = re.split('("|\'|\s|,|\.|\d{1,2})', sen)
    # print(en)
    word = []
    for j in en:
        if len(re.findall('\w', j)) > 0:
            word.append('<a class = "en" >' + str(j) + '</a>')
        else:
            word.append(j)
    sen = ''.join(word)
    # print(sen)
#     fix = '<span>'
    if len(re.findall('<span.*?>', i))>0:
        fix = re.findall('<span.*?>', i)[0]
    subfix = '</span>'
    page.append(content[index])
    sen =fix + sen + subfix
    # print(sen)
    page.append(sen)
    index += 1
page.append(content[index])
with open('/end_of_term_work/vo.html', 'w', encoding='utf-8') as fp:
    fp.write(''.join(page))

# from docx import Document
# import docx
#
# # 打开文件
# document = Document("F://英语//20-4//Oct.30 · 2021.docx")
# prefix = '<tr><td>'
# subfix = '</td></tr><tr><td></td></tr>'
# page = '<!DOCTYPE html>\
# <html lang="en">\
# <head>\
#     <meta charset="UTF-8">\
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">\
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">\
#     <title>Document</title>\
# </head>\
# <body> \
# <table>'
# for paragraph in document.paragraphs:
#     content = re.split('("|\'|\s|,|\.|\d{1,2})', str(paragraph.text))
#     word = []
#     for i in content:
#         if len(re.findall('\w', i)) > 0:
#             word.append('<a class = "en" >' + i + '</a>')
#         else:
#             word.append(i)
#     page += prefix+''.join(word)+subfix+'\n'
# page+='</table></body>\
# </html>'
# with open('F:\\PyCourseDemo\\end_of_term_work\\vo.html','w',encoding='utf-8') as fp:
#     fp.write(page)

# 获取文档所有表格
# all_tables = document.tables
# print(all_tables)
# #打印all_tables类型
# print(type(all_tables)) #得到<class 'list'>，即列表
# #开始循环读取表格列表
# for table in all_tables:
# print(table)
# #循环读取表格的每一行
# for row in table.rows:
#     #print(row)
#     #循环读取表格的每一个单元格
#     for cell in row.cells:
#         #打印单元格里的内容
#         print(cell.text) #打印
