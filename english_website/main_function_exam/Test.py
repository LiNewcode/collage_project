import json

from end_of_term_work.Tool.link_db import db_obj


class get_test:
    word_pee = []

    def __init__(self, _id, userId):
        self._id = _id
        self.userId = userId
        self.db = db_obj(col='peeQuestion')

    def get_test_ans(self, year, testType):
        res_db = db_obj(db='userDB', col='userExamRecord')

        user_res = res_db.search(content={'userId': str(self.userId), 'type': str(testType), 'year': str(year)},
                                 limit={'res': 1, 'score': 1, '_id': 0})[0]
        res = user_res['res']
        res_tmp = []
        res_tmp.append(res[0:20])
        res_tmp.append(res[20:25])
        res_tmp.append(res[25:30])
        res_tmp.append(res[30:35])
        res_tmp.append(res[35:40])
        res_tmp.append(res[40:45])
        res_tmp.append(res[45:50])
        res_db.close()
        user_res['res'] = res_tmp
        detail = db_obj(col='peeQrWhole').search(content={'year': year, 'type': testType})
        user_res['detail'] = detail

        return json.dumps(user_res)

    def get_test_ans_detail(self):
        res_db = db_obj(db='mymongo', col='peeQrSection')
        ans = res_db.search(content={'_id': self._id})[0]

        return json.dumps(ans)

    def get_test_page(self, year, testType):

        dic = self.db.search({'TestType': str(testType), 'Year': str(year)})

        sorted(dic, key=lambda x: x['Sign'], reverse=False)

        self.db.close()
        test_page = {'testPage': dic}
        return json.dumps(test_page)

    def get_test_list(self):
        test_list_1 = []
        test_list_2 = []

        res_1 = self.db.search({'TestType': '1'}, {'Year': 1, '_id': 0})
        res_2 = self.db.search({'TestType': '1'}, {'Year': 1, '_id': 0})
        self.db.close()
        for item in res_1:
            if item['Year'] in test_list_1:
                continue
            else:
                test_list_1.append(item['Year'])
        for item in res_2:
            if item['Year'] in test_list_2:
                continue
            else:
                test_list_2.append(item['Year'])
        test_list_1.sort()
        test_list_2.sort()
        tl1 = []
        tl2 = []
        db = db_obj(db='userDB', col='userExamRecord')

        for item in test_list_1:
            if db.search({'type': '1', 'year': item, 'userId': self.userId}) is not None:
                score = db.search({'type': '1', 'year': item, 'userId': self.userId}, {'score': 1, '_id': 0})[0][
                    'score']
                tl1.append({'year': item, 'beDone': 'true', 'score': score})
            else:
                tl1.append({'year': item, 'beDone': 'false', 'score': None})
        for item in test_list_2:
            if db.search({'type': '2', 'year': item, 'userId': self.userId}) is not None:
                score = db.search({'type': '2', 'year': item, 'userId': self.userId}, {'score': 1, '_id': 0})
                tl2.append({'year': item, 'beDone': 'true', 'score': score})
            else:
                tl2.append({'year': item, 'beDone': 'false', 'score': None})

        test_list = {'e1': tl1, 'e2': tl2}

        return json.dumps(test_list)
