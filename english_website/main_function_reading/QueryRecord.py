"""
    查询单词 的 历史记录
    单词查询记录
    filename:所在文件
    word:单词
    date:时间
    frequency:次数
    location:位置
    signal:是否星标
    exam:是否考研
    插入：先查询，若没有，则插入；若有，则修改次数、时间
    修改：查询对应文件的星标，取非重置
    删除：查询对应文件的单词。删除文档
"""
import json
import time

from end_of_term_work.Service.get_word_service import get_word
from end_of_term_work.Tool.link_db import db_obj
from end_of_term_work.main_function_reading.ExamRecord import examRecord


class query_data:
    def __init__(self, filename=None, word=None, date=None, frequency=None, location=None, signal='n', exam=None,
                 userId=None):
        self.filename = filename
        self.word = word
        self.date = date
        self.frequency = frequency
        self.location = location
        self.signal = signal
        self.exam = exam
        self.userId = userId
        self.DB = db_obj(db='queryRecord', col=filename)

    def run(self):
        return {'filename': self.filename, 'word': self.word, 'date': self.date, 'frequency': self.frequency,
                'location': self.location, 'signal': self.signal, 'exam': self.exam, 'DB': self.DB,
                'userId': self.userId}


class query_record_menu:
    def __init__(self, choice, filename=None, word=None, date=None, frequency=None, location=None, signal=None,
                 exam=None, userId=None):
        if date is None:
            date = time.time()
        self.data = query_data(filename, word, date, frequency, location, signal, exam, userId).run()
        self.choice = choice


    def run(self, deleteCount='one', deleteList=None):
        if self.choice == 'query':
            pass
            # return self.query(self.data)
        elif self.choice == 'delete':
            return self.delete(self.data, deleteCount, deleteList)
        elif self.choice == 'update':
            return self.update(self.data)
        elif self.choice == 'insert':
            return self.insert(self.data)
        elif self.choice == 'show':
            return self.show(self.data)
        elif self.choice == 'collect':
            return self.collect(self.data)
        elif self.choice == 'not_collect':
            return self.cancel_collect(self.data)

    def dataSet(self, data):
        obj = {'word': data['word'], 'date': data['date'], 'frequency': data['frequency'],
               'location': data['location'], 'signal': data['signal'], 'exam': data['exam'], 'userId': data['userId']}
        return obj

    def show(self, data):
        res = data['DB'].search({'userId': data['userId']})
        response = []

        if res is None:
            return json.dumps({'code': '404', 'data': []})
        for i in res:

            if i['signal'] is None:
                signal = 'n'
            else:
                signal = i['signal']
            response.append({'word': i['word'], 'signal': signal})

        return json.dumps({'code': 'success', 'data': response})

    # 删除 历史查询 的单词数据
    def delete(self, data, deleteCount='one', deleteList=None):
        if deleteCount == 'one':
            res = data['DB'].search(content={'word': data['word'], 'userId': data['userId']}, limit={'word': 1})
            if res is not None:
                res = data['DB'].delete(content={'word': data['word'], 'userId': data['userId']})
                return 'success'
            else:

                return 'fail'
        if deleteCount == 'many' and deleteList is not None:
            response = []
            for i in deleteList:
                res = data['DB'].search(content={'word': i, 'userId': data['userId']}, limit={'word': 1})
                if res is not None:
                    res = data['DB'].delete(content={'word': i})
                    response.append('success')
                else:

                    response.append('fail')
            return response

    # 更新 历史查询 数据
    def update(self, data) -> bool:
        db = data['DB']
        res = db.search(content={'word': data['word'], 'userId': data['userId']},
                        limit={'date': 1, 'frequency': 1})
        if res is not None:
            for r in res:
                try:
                    date = time.time()
                    frequency = str(int(r['frequency']) + 1)
                except:

                    return 'fail'
                # if data['signal'] is not None:
                #     content = {'date': date, 'frequency': frequency, 'signal': data['signal']}
                # else:
                content = {'date': date, 'frequency': frequency}
                db.update(find={'word': data['word'], 'userId': data['userId']}, content=content)
                response = get_word().run(word=data['word'], userId=data['userId'])
        return {'code': 'success', 'data': response}

    # 插入 历史查询单词 数据
    def insert(self, data):

        accumulate = self.accumulateWord(data)
        content = {'word': data['word'], 'userId': data['userId']}
        limit = {'word': 1}


        res = data['DB'].search(content=content, limit=limit)
        # 检查是否存在，存在则更新
        if res is not None:
            self.update(data)
        # 不存在则插入
        else:
            data['frequency'] = '1'
            # 查询是否为考研单词，是 1 否 0
            if False:  # examRecord.exitsExamWord(data['word'])
                data['exam'] = 1
            else:
                data['exam'] = 0
            dataset = self.dataSet(data=data)
            res = data['DB'].insert(dataset)
            response = get_word().run(word=data['word'], userId=data['userId'])
            return {'code': 'success', 'data': response}

    def collect(self, data):
        db_tmp = db_obj(db='userDB', col='userWordCollect')
        db = data['DB']
        word = data['word']
        filename = data['filename']
        userId = data['userId']
        db.update(find={'userId': userId, 'word': word}, content={'signal': 'y'})
        user_collect = db_tmp.search(content={'_id': userId})
        if user_collect is not None:
            user_collect = set(user_collect[0]['collect'])
            user_collect.add(word)
            db_tmp.update(find={'_id': userId},
                          content={'collect': list(user_collect), '_id': userId})
        else:
            user_collect = set([])
            user_collect.add(word)
            db_tmp.update(find={'_id': userId},
                          content={'collect': list(user_collect), '_id': userId})
        return {'code': 'success', 'data': word}

    def cancel_collect(self, data):
        db_tmp = db_obj(db='userDB', col='userWordCollect')
        db = data['DB']
        word = data['word']
        filename = data['filename']
        userId = data['userId']
        db.update(find={'userId': userId, 'word': word}, content={'signal': 'n'})
        user_collect = db_tmp.search(content={'_id': userId})
        if user_collect is not None:
            user_collect = set(user_collect[0]['collect'])
            user_collect.remove(word)
            db_tmp.update(find={'_id': userId},
                          content={'collect': list(user_collect), '_id': userId})
        else:
            user_collect = set([])
            # user_collect.add(word)
            db_tmp.update(find={'_id': userId},
                          content={'collect': list(user_collect), '_id': userId})
        return {'code': 'success', 'data': word}

    def accumulateWord(self, data):
        w = data['word']
        db_tmp = db_obj(db='userDB', col='userWord')
        user_accumulate = db_tmp.search(content={'_id': data['userId']}, limit={'accumulate': 1, '_id': 0})

        if user_accumulate is not None:
            if len(user_accumulate) > 0:
                user_accumulate = user_accumulate[0]['accumulate']
        else:
            # 状态 zh朝花 xs夕拾 zw掌握
            user_accumulate = [{'word': w, 'num': 0, 'state': 'zh'}]
            db_tmp.update(find={'_id': data['userId']},
                          content={'accumulate': user_accumulate, '_id': data['userId']})
            return True

        # 已存在
        for item in user_accumulate:
            if item['word'] == w:
                return True

        user_accumulate.append({'word': w, 'num': 0, 'state': 'zh'})
        db_tmp.update(find={'_id': data['userId']},
                      content={'accumulate': user_accumulate, '_id': data['userId']})

        return True

        #                 if len(user_accumulate) > 0:
#                     user_accumulate = set(user_accumulate)
#                     user_accumulate.add(w)
#                     db_tmp.update(find={'_id': data['userId']},
#                                   content={'accumulate': list(user_accumulate), '_id': data['userId']})
#             else:
#                 user_accumulate = set([])
#                 user_accumulate.add(w)
#                 db_tmp.update(find={'_id': data['userId']},
#                               content={'accumulate': list(user_accumulate), '_id': data['userId']})
#         else:
#             user_accumulate = set([])
#             user_accumulate.add(w)
#             db_tmp.update(find={'_id': data['userId']},
#                           content={'accumulate': list(user_accumulate), '_id': data['userId']})

# time.ctime() is str
# W
# e
# d
#
# D
# e
# c
#
# 1
#
# 1
# 0
# :
# 2
# 9
# :
# 4
# 6
#
# 2
# 0
# 2
# 1
