import difflib
import json
import time

from end_of_term_work.Tool.link_db import db_obj


class englishExam:
    def __init__(self, ans, year, testType, userId):
        self.ans = ans
        self.year = year
        self.testType = testType
        self.getUserAns(userId, testType, year)


        pass

    # 获取用户所填的答案
    def getUserAns(self, userId, testType, year):
        score = 0
        res = []
        try:
            ans = db_obj(col='ans').search(content={'year': int(self.year), 'type': int(self.testType)},
                                           limit={'ans': 1, '_id': 0})[0]['ans']
        except:
            return None
        # 完型
        u_wx = self.ans[0:20]
        for index in range(0, 20):
            if u_wx[index] == ans['ans_1'][index]:
                res.append('y')
                score += 0.5
            else:
                res.append('n')

        # 阅读1
        u_y1 = self.ans[20:25]
        for index in range(0, 5):
            if u_y1[index] == ans['ans_2'][index]:
                res.append('y')
                score += 2
            else:
                res.append('n')
        # 阅读2
        u_y2 = self.ans[25:30]
        for index in range(0, 5):
            if u_y2[index] == ans['ans_3'][index]:
                res.append('y')
                score += 2
            else:
                res.append('n')
        # 阅读3
        u_y3 = self.ans[30:35]
        for index in range(0, 5):
            if u_y3[index] == ans['ans_4'][index]:
                res.append('y')
                score += 2
            else:
                res.append('n')
        # 阅读4
        u_y4 = self.ans[35:40]
        for index in range(0, 5):
            if u_y4[index] == ans['ans_5'][index]:
                res.append('y')
                score += 2
            else:
                res.append('n')
        # 阅读5
        u_y5 = self.ans[40:45]
        for index in range(0, 5):
            if u_y5[index] == ans['ans_6'][index]:
                res.append('y')
                score += 2
            else:
                res.append('n')

        print(f'得分：{score}')
        # 翻译
        u_fy = self.ans[45:50]
        for index in range(0, 5):
            match_degree = 0.0  ## 文本匹配度
            likely_question = ''  ## 寻求最匹配问题
            s = difflib.SequenceMatcher(None, u_fy[index], ans['ans_7'][index])
            match_degree = s.ratio()
            score += match_degree * 2
            res.append(score)

        # # 作文
        # u_xzw = self.ans[51]
        #
        # u_dzw = self.ans[52]
        date = time.asctime()
        resp = {'res': res, 'ans': ans, 'userId': userId, 'score': score, 'year': year, 'type': testType, 'date': date,
                'userAns': self.ans}
        db_obj(db='userDB', col='userExamRecord').update(find={'userId': userId, 'year': year, 'type': testType},
                                                         content=resp)
        return json.dumps(resp)
        pass

    # 获取正确的答案
    def getTestAns(self):
        pass


p = ['a', 'b', 'c', 'd']

