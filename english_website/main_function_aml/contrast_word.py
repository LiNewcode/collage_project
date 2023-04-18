from end_of_term_work.Tool.link_db import db_obj


class contrast_word:
    def __init__(self, userId):
        self.userId = userId
        pass

    def get_recommend(self):
        pee = db_obj(db='mymongo', col='peeQuestion').search(content={}, limit={'_id': 1, 'accumulate': 1})
        user_db = db_obj(db='userDB', col='userWord')
        if user_db.search(content={'_id': self.userId},
                          limit={'_id': 0, 'accumulate': 1}) is None:
            user_accumulate = set([])
        else:
            accumulate = user_db.search(content={'_id': self.userId},
                                        limit={'_id': 0, 'accumulate': 1})[0]['accumulate']
            user_accumulate = []
            for item in accumulate:
                user_accumulate.append(item['word'])

        similarity_list = []


        for article in pee:
            _id = article['_id']
            article_index = _id[-1]
            if article_index == '7' or article_index == '8':
                continue
            similarity = len(set(article['accumulate']).intersection(user_accumulate)) / len(
                set(article['accumulate']))

            testType = _id[0]
            if testType == '1':
                testType = '英语一'
            else:
                testType = '英语二'

            year = _id[2:6]

            if article_index == '0':
                article_index = '完型填空'
            elif article_index == '1':
                article_index = '阅读理解-Text1'
            elif article_index == '2':
                article_index = '阅读理解-Text2'
            elif article_index == '3':
                article_index = '阅读理解-Text3'
            elif article_index == '4':
                article_index = '阅读理解-Text4'
            elif article_index == '5':
                article_index = '创新阅读'
            elif article_index == '6':
                article_index = '翻译'
            elif article_index == '7':
                article_index = '小作文'
            elif article_index == '8':
                article_index = '大作文'

            similarity_list.append(
                {'id': _id, 'similarity': round(similarity, 4), 'year': year, 'type': testType, 'index': article_index})



        return {'similarity_list': similarity_list}
