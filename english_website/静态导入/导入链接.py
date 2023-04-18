import json
import os
import re

import requests

# with open('英语1.txt', 'r', encoding='utf-8') as fp:
#     text = fp.read()
#     print(text)
#     index = 21
#     for i in re.findall(r'(http.*?)\n', text):
#
#         print(f'英一 20{index},{i}')
#         try:
#             res = requests.get(url=i).content
#             res_1 = json.loads(res)
#             print(res_1)
#             if index == 16 or index == 19 or index == 20:
#                 index -= 1
#                 continue
#             with open(f'英一20{index}.json', 'w') as fp1:
#                 fp1.write(json.dumps(res_1, ensure_ascii=True))
#             print(f'20{index} is OK！')
#         except:
#             pass
#         index -= 1


# index = 21
# while index >= 11:
#     with open(f'英一20{index}.json', 'r', encoding='utf-8') as fp1:
#         text = json.loads(fp1.read())
#         questions = text['Questions']
#         for item in questions:
#             SbjTypeName = item['SbjTypeName']
#             print(SbjTypeName)
#
#             SbjContentList=item['SbjContentList']
#             # print(SbjContentList)
#             title = ''
#             for i in SbjContentList:
#                 title+='\n'+i['QContent']
#             print(title)
#             try:
#                 for question in item['SbjSubContentList']:
#                     qsn = question['SbjContentList'][0]
#                     choice = question['SbjChoice']
#                     ans = question['Answer']
#                     explain = question['Explain']
#                     print(qsn)
#                     print(choice)
#                     print(ans)
#                     print(explain)
#             except:
#                 continue
#
#     index-=1


# with open('英语2.txt', 'r', encoding='utf-8') as fp:
#     text = fp.read()
#     print(text)
#     index = 21
#     for i in re.findall(r'(http.*?)\n', text):
#
#         print(f'英二 20{index},{i}')
#         try:
#             res = requests.get(url=i).content
#             res_1 = json.loads(res)
#             print(res_1)
#             # if index == 16 or index == 19 or index == 20:
#             #     index -= 1
#             #     continue
#             with open(f'英二20{index}.json', 'w') as fp1:
#                 fp1.write(json.dumps(res_1, ensure_ascii=True))
#             print(f'20{index} is OK！')
#         except:
#             pass
#         index -= 1

index = 20
# {smallXuHao: '', bigXuHao: '', year: '', e_type: '1', }
while index >= 20:

    with open(f'英一20{index}.json', 'r', encoding='utf-8') as fp1:
        text = json.loads(fp1.read())
        questions = text['Questions']
        j = 1
        for item in questions:
            SbjTypeName = item['SbjTypeName']
            print(f'SbjTypeName:{SbjTypeName}')

            SbjContentList = item['SbjContentList']
            print(f'20{index}-{j}:{len(SbjContentList)}')
            j += 1
            title = ''
            # for i in SbjContentList:
            #     title+='\n'+i['QContent']
            # print(f'title:{title}')
            try:
                for question in item['SbjSubContentList']:
                    qsn = question['SbjContentList'][0]
                    choice = question['SbjChoice']
                    ans = question['Answer']
                    explain = question['Explain']
                    exp = ''
                    for l in explain:
                        exp += l['QContent'] + '\n'
                    print(f'qsn:{qsn}')
                    print(f'choice:{choice}')
                    print(f'ans:{ans}')
                    print(f'explain:{exp}')
            except:
                continue

    index -= 1
