import re

from end_of_term_work.Tool.link_db import db_obj

with open('./❤  考研英语二真题答案速查版（2010-2021）.txt', 'r', encoding='utf-8') as fp:
    txt = fp.read()
# print(txt)
anslist = re.split('20\d{2}   年全真试题答案', txt, re.S)[1:]
print(len(anslist))
print(anslist)
year = 2010
Ptype = 2
for item in anslist[1:]:
    # ans_1 = re.findall('SectionⅠUse     of English(.*?)SectionⅡReading        of English', item, re.S)[0]
    # ans_2 = re.findall('Text1(.*?)Text2', item, re.S)[0]
    # ans_3 = re.findall('Text2(.*?)Text3', item, re.S)[0]
    # ans_4 = re.findall('Text3(.*?)Text4', item, re.S)[0]
    # ans_5 = re.findall('Text4(.*?)Part   B', item, re.S)[0]
    # ans_6 = re.findall('Part   B(.*?)Part   C', item, re.S)[0]
    # ans_7 = re.findall('Part   C(.*?)Section   Ⅲ   Writing', item, re.S)[0]
    ans_1 = re.findall('SectionⅠUse       of English(.*?)SectionⅡReading        of English', item, re.S)[0]
    ans_2 = re.findall('Text1(.*?)Text2', item, re.S)[0]
    ans_3 = re.findall('Text2(.*?)Text3', item, re.S)[0]
    ans_4 = re.findall('Text3(.*?)Text4', item, re.S)[0]
    ans_5 = re.findall('Text4(.*?)Part   B', item, re.S)[0]
    ans_6 = re.findall('Part   B(.*?)Section   Ⅲ        Translation', item, re.S)[0]
    ans_7 = re.findall('Section   Ⅲ        Translation(.*?)SectionⅣ        Writing', item, re.S)[0]

    ans_1 = re.findall('\d{1,2}\.(.)', ans_1, re.S)
    ans_2 = re.findall('\d\d\.(.)', ans_2, re.S)
    ans_3 = re.findall('\d\d\.(.)', ans_3, re.S)
    ans_4 = re.findall('\d\d\.(.)', ans_4, re.S)
    ans_5 = re.findall('\d\d\.(.)', ans_5, re.S)
    ans_6 = re.findall('\d\d\.(.)', ans_6, re.S)
    ans_7 = re.split('\d\d\.', ans_7, re.S)[1:]
    print(year)
    print(ans_1)
    print(ans_2)
    print(ans_3)
    print(ans_4)
    print(ans_5)
    print(ans_6)
    print(len(ans_7), ans_7)
    ans = {
        'ans_1': ans_1, 'ans_2': ans_2, 'ans_3': ans_3, 'ans_4': ans_4, 'ans_5': ans_5, 'ans_6': ans_6, 'ans_7': ans_7
    }
    db_obj(col='ans').update(find={'year': str(year), 'type': '1'},content={'ans':ans,'year':year,'type':Ptype})
    year = year + 1
regix = '20   年全真试题答案'
