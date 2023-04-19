import json
import re
import time

from docx import Document
import docx
import openpyxl
from openpyxl import load_workbook

from end_of_term_work.Tool.link_db import db_obj

for i in [1, 2]:
    for year in range(2011, 2021):
        if i == 1:
            S = '一'
        else:
            S = '二'
        with open(f'英{S}{year}.json', 'r', encoding='utf-8') as fp1:
            res = json.loads(fp1.read())
        k = 0
        TiHao = 1
        for item in res['Questions']:
            if k > 8:
                break
            db = db_obj(col='peeQuestion')
            Name = item['SbjTypeName']
            Content = []
            for j in item['SbjContentList']:
                Content.append(j['QContent'])

            if k in [6, 7, 8]:
                if k ==6:
                    _id = f'{str(i)}-{str(year)}-sec_2-c-{str(k)}'
                elif k==7:
                    _id = f'{str(i)}-{str(year)}-sec_3-a-{str(k)}'
                else:
                    _id = f'{str(i)}-{str(year)}-sec_3-b-{str(k)}'
                db.update({'_id': _id},
                          {'TestType': str(i), 'Year': str(year), 'Sign': k, 'Name': Name, 'Content': Content,
                           'QuestionList': ''})
            else:

                XiaoTiCount = item['XiaoTiCount']


                QuestionList = []

                for j in item['SbjSubContentList']:
                    qs = j['SbjContentList'][0]
                    print(qs)
                    if k == 0:
                        Question = {'TiHao': TiHao, 'Question': qs['smallXuHao'], 'Choice': j['SbjChoice']}
                    else:
                        Question = {'TiHao': TiHao, 'Question': qs['QContent'], 'Choice': j['SbjChoice']}
                    QuestionList.append(Question)
                    TiHao += 1

                if k == 0:
                    _id = f'{str(i)}-{str(year)}-sec_1-a-0'
                if k in [1, 2, 3, 4]:
                    _id = f'{str(i)}-{str(year)}-sec_2-a-{str(k)}'
                if k == 5:
                    _id = f'{str(i)}-{str(year)}-sec_2-b-{str(k)}'

                db.update({'_id': _id},
                          {'TestType': str(i), 'Year': str(year), 'Sign': k, 'Name': Name, 'Content': Content,
                           'QuestionList': QuestionList})

            k += 1
            db.close()