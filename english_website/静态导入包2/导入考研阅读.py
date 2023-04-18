import re
import time

from end_of_term_work.Tool.link_db import db_obj

def getYd(content, year, ky):
    wx = re.findall('Section I Use of English(.*?)Section II Reading Comprehension', content, re.S)[0]
    Text1 = re.findall('Text 1(.*?)Text 2', content, re.S)[0]
    Text2 = re.findall('Text 2(.*?)Text 3', content, re.S)[0]
    Text3 = re.findall('Text 3(.*?)Text 4', content, re.S)[0]
    Text4 = re.findall('Text 4(.*?)Part B', content, re.S)[0]
    cxyd = re.findall('Part B\nDirections\:(.*?)Part C', content, re.S)[0]
    fy = re.findall('Part C(.*?)Section III Writing', content, re.S)[0]
    print(
        f'wx:{len(wx)},Text1:{len(Text1)},Text2:{len(Text2)},Text3:{len(Text3)},Text4:{len(Text4)},cxyd:{len(cxyd)},pc:{len(fy)}')
    getParagraph(wx, str(year) + '-0', ky, str(year) + ' 年考研题--完型填空')
    getParagraph(Text1, str(year) + '-1', ky, str(year) + ' 年考研题--阅读A-Text1')
    getParagraph(Text2, str(year) + '-2', ky, str(year) + ' 年考研题--阅读A-Text2')
    getParagraph(Text3, str(year) + '-3', ky, str(year) + ' 年考研题--阅读A-Text3')
    getParagraph(Text4, str(year) + '-4', ky, str(year) + ' 年考研题--阅读A-Text4')
    getParagraph(cxyd, str(year) + '-5', ky, str(year) + ' 年考研题--创新阅读')
    getParagraph(fy, str(year) + '-6', ky, str(year) + ' 年考研题--翻译')
    pass

#
# def getYd(content, year, ky):
#     wx = re.findall('Section I   Use of English(.*?)Section II Reading Comprehension', content, re.S)[0]
#     Text1 = re.findall('Text 1(.*?)Text 2', content, re.S)[0]
#     Text2 = re.findall('Text 2(.*?)Text 3', content, re.S)[0]
#     Text3 = re.findall('Text 3(.*?)Text 4', content, re.S)[0]
#     Text4 = re.findall('Text 4(.*?)Part B', content, re.S)[0]
#     fy = re.findall('Part B\nDirections\:(.*?)Section III Reading Comprehension', content, re.S)[0]
#     # fy = re.findall('Part C(.*?)Section III Writing', content, re.S)[0]
#     print(
#         f'wx:{len(wx)},Text1:{len(Text1)},Text2:{len(Text2)},Text3:{len(Text3)},Text4:{len(Text4)},pc:{len(fy)}')
#     getParagraph(wx, str(year) + '-0', ky, str(year) + ' 年考研题--完型填空')
#     getParagraph(Text1, str(year) + '-1', ky, str(year) + ' 年考研题--阅读A-Text1')
#     getParagraph(Text2, str(year) + '-2', ky, str(year) + ' 年考研题--阅读A-Text2')
#     getParagraph(Text3, str(year) + '-3', ky, str(year) + ' 年考研题--阅读A-Text3')
#     getParagraph(Text4, str(year) + '-4', ky, str(year) + ' 年考研题--阅读A-Text4')
#     # getParagraph(cxyd, str(year) + '-5', ky, str(year) + ' 年考研题--创新阅读')
#     getParagraph(fy, str(year) + '-5', ky, str(year) + ' 年考研题--翻译')
#     pass

#
# def getYd(content, year, ky):
#     wx = re.findall('Section I   Use of English(.*?)Section II Reading Comprehension', content, re.S)[0]
#     Text1 = re.findall('Passage 1(.*?)Passage 2', content, re.S)[0]
#     Text2 = re.findall('Passage 2(.*?)Passage 3', content, re.S)[0]
#     Text3 = re.findall('Passage 3(.*?)Passage 4', content, re.S)[0]
#     Text4 = re.findall('Passage 4(.*?)Passage 5', content, re.S)[0]
#     Text5 = re.findall('Passage 5(.*?)Part III English-Chinese Translation', content, re.S)[0]
#     fy = re.findall('Part III English-Chinese Translation(.*?)Section IV Writing', content, re.S)[0]
#     print(
#         f'wx:{len(wx)},Text1:{len(Text1)},Text2:{len(Text2)},Text3:{len(Text3)},Text4:{len(Text4)},Text5:{len(Text5)},pc:{len(fy)}')
#     getParagraph(wx, str(year) + '-0', ky, str(year) + ' 年考研题--完型填空')
#     getParagraph(Text1, str(year) + '-1', ky, str(year) + ' 年考研题--阅读-Text1')
#     getParagraph(Text2, str(year) + '-2', ky, str(year) + ' 年考研题--阅读-Text2')
#     getParagraph(Text3, str(year) + '-3', ky, str(year) + ' 年考研题--阅读-Text3')
#     getParagraph(Text4, str(year) + '-4', ky, str(year) + ' 年考研题--阅读-Text4')
#     getParagraph(Text5, str(year) + '-5', ky, str(year) + ' 年考研题--阅读-Text5')
#     getParagraph(fy, str(year) + '-6', ky, str(year) + ' 年考研题--翻译')
#     pass

def getParagraph(article, _id, ky, title):
    paragraph_list = list(article.split('\n'))
    for paragraph in paragraph_list:
        tmp = paragraph
        if len(tmp.strip()) <= 1:
            paragraph_list.remove(paragraph)
    new_list = []
    pee = set([])
    accumulate = set([])
    for index in range(1, len(paragraph_list) + 1):
        res = getWord(paragraph_list[index - 1], ky, index, accumulate)
        new_list.append(res['item'])
        pee = pee.union(res['pee'])
        accumulate = res['accumulate']

    data = {'_id': _id, 'article': new_list, 'article_pee': list(pee), 'title': title, 'title_des': '',
            'annotation': [],
            'accumulate': list(accumulate), 'type': 'ky'}
    print('[ id ]:', _id)
    db = db_obj(col='kyyd')
    db.insert(content=data)
    db.close()


def getWord(paragraph, ky, index, accumulate):
    res = []
    article_pee = set([])
    tmp = re.split('("|，|。|”|“|\s|,|\.|\d{1,2}|\(|\))', paragraph)
    for i in tmp:
        isPee = False
        if i.isalpha():
            if i in ky:
                isPee = True

                article_pee.add(i)

                item = {'word': i, 'signal': 'en', 'isPee': isPee}
            else:
                item = {'word': i, 'signal': 'en', 'isPee': isPee}
            if len(i) > 2:
                accumulate.add(i)
        else:
            item = {'word': i, 'signal': 'other', 'isPee': isPee}
        res.append(item)

    return {'item': {'paragraph': index, 'content': res, 'des': ''}, 'pee': article_pee, 'accumulate': accumulate}


if __name__ == '__main__':
    with open('./test/2005-2009.txt', 'r', encoding='utf-8') as fp:
        content = fp.read()
    # print(content)
    content_list = re.split('\d{4}年全国硕士研究生招生考试英语\（一\）试题', content)
    content_list.remove(content_list[0])
    ky = set(db_obj(col='ky').search({})[0]['word'])
    year = 2009
    for item in content_list:
        print(f'第 {year} 年：')
        getYd(item, year, ky)
        year -= 1
    # db_obj(col='lls').update(find={},content={'type':'lls'})

# 2005-2009
# def getYd(content, year, ky):
#     wx = re.findall('Section I Use of English(.*?)Section II Reading Comprehension', content, re.S)[0]
#     Text1 = re.findall('Text 1(.*?)Text 2', content, re.S)[0]
#     Text2 = re.findall('Text 2(.*?)Text 3', content, re.S)[0]
#     Text3 = re.findall('Text 3(.*?)Text 4', content, re.S)[0]
#     Text4 = re.findall('Text 4(.*?)Part B', content, re.S)[0]
#     cxyd = re.findall('Part B\nDirections\:(.*?)Part C', content, re.S)[0]
#     fy = re.findall('Part C(.*?)Section III Writing', content, re.S)[0]
#     print(
#         f'wx:{len(wx)},Text1:{len(Text1)},Text2:{len(Text2)},Text3:{len(Text3)},Text4:{len(Text4)},cxyd:{len(cxyd)},pc:{len(fy)}')
#     getParagraph(wx, str(year) + '-0', ky, str(year) + ' 年考研题--完型填空')
#     getParagraph(Text1, str(year) + '-1', ky, str(year) + ' 年考研题--阅读A-Text1')
#     getParagraph(Text2, str(year) + '-2', ky, str(year) + ' 年考研题--阅读A-Text2')
#     getParagraph(Text3, str(year) + '-3', ky, str(year) + ' 年考研题--阅读A-Text3')
#     getParagraph(Text4, str(year) + '-4', ky, str(year) + ' 年考研题--阅读A-Text4')
#     getParagraph(cxyd, str(year) + '-5', ky, str(year) + ' 年考研题--创新阅读')
#     getParagraph(fy, str(year) + '-6', ky, str(year) + ' 年考研题--翻译')
#     pass
#
#
# def getParagraph(article, _id, ky, title):
#     paragraph_list = list(set(article.split('\n')))
#     for paragraph in paragraph_list:
#         tmp = paragraph
#         if len(tmp.strip()) <= 1:
#             paragraph_list.remove(paragraph)
#     new_list = []
#     pee = set([])
#     accumulate = set([])
#     for index in range(1, len(paragraph_list) + 1):
#         res = getWord(paragraph_list[index - 1], ky, index, accumulate)
#         new_list.append(res['item'])
#         pee = pee.union(res['pee'])
#         accumulate = res['accumulate']
#
#     data = {'_id': _id, 'article': new_list, 'article_pee': list(pee), 'title': title, 'title_des': '',
#             'annotation': [],
#             'accumulate': list(accumulate), 'type': 'ky'}
#     print('[ id ]:', _id, data)
#     # db = db_obj(col='kyyd')
#     # db.insert(content=data)
#     # db.close()
#
#
# def getWord(paragraph, ky, index, accumulate):
#     res = []
#     article_pee = set([])
#     tmp = re.split('("|，|。|”|“|\s|,|\.|\d{1,2}|\(|\))', paragraph)
#     for i in tmp:
#         isPee = False
#         if i.isalpha():
#             if i in ky:
#                 isPee = True
#
#                 article_pee.add(i)
#
#                 item = {'word': i, 'signal': 'en', 'isPee': isPee}
#             else:
#                 item = {'word': i, 'signal': 'en', 'isPee': isPee}
#             if len(i)>2:
#                 accumulate.add(i)
#         else:
#             item = {'word': i, 'signal': 'other', 'isPee': isPee}
#         res.append(item)
#
#     return {'item': {'paragraph': index, 'content': res, 'des': ''}, 'pee': article_pee, 'accumulate': accumulate}
