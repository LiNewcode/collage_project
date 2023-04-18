from end_of_term_work.Tool.link_db import db_obj


class wordState:
    def __init__(self):
        pass

    def run(self, word, userId, choice):
        if choice == 'getState':
            return self.getState(word, userId)
        if choice == 'addXS':
            return self.addXS(word, userId)
        if choice == 'addZH':
            return self.addZH(word, userId)
        if choice == 'addJX':
            return self.addJX(word, userId)
        if choice == 'addZW':
            return self.addZW(word, userId)
        if choice == 'getNum':
            return self.getNum(word, userId)
        return 'no'
        pass

    def getState(self, word, userId):

        db = db_obj(db='userDB', col='userWord')
        user_accumulate = db.search(content={'_id': userId})
        db.close()
        if user_accumulate is not None:
            user_accumulate = user_accumulate[0]['accumulate']
        else:
            return 'no'
        # 状态 zh朝花 xs夕拾 zw掌握
        for item in user_accumulate:

            if item['word'] == word:
                return item['state']

        return 'no'

    def addJX(self, word, userId):
        state = self.getState(word=word, userId=userId)
        if state == 'zw' or state == 'jx' or state == 'no':
            return state

        if state == 'xs':
            db = db_obj(db='userDB', col='userWord')
            user_accumulate = db.search(content={'_id': userId})

            user_accumulate = user_accumulate[0]['accumulate']
            index = 0
            for item in user_accumulate:
                if item['word'] == word:
                    user_accumulate[index]['num'] = item['num'] + 1
                    user_accumulate[index]['state'] = 'jx'
                    db.update(find={'_id': userId}, content={'_id': userId, 'accumulate': user_accumulate})
                    db.close()
                    return 'jx'
                index += 1
        return 'no'

    def addXS(self, word, userId):
        state = self.getState(word=word, userId=userId)

        if state == 'xs' or state == 'zw' or state == 'jx':
            return state

        if state == 'zh':
            db = db_obj(db='userDB', col='userWord')
            user_accumulate = db.search(content={'_id': userId})

            user_accumulate = user_accumulate[0]['accumulate']
            index = 0
            for item in user_accumulate:
                if item['word'] == word:
                    user_accumulate[index]['state'] = 'xs'
                    db.update(find={'_id': userId}, content={'_id': userId, 'accumulate': user_accumulate})
                    db.close()
                    return 'xs'
                index += 1
        return 'no'

    def addZH(self, word, userId):

        state = self.getState(word=word, userId=userId)
        if state == 'zh' or state == 'xs' or state == 'zw':
            return state

        db = db_obj(db='userDB', col='userWord')
        user_accumulate = db.search(content={'_id': userId})

        if state == 'no':

            if user_accumulate is not None:
                user_accumulate = user_accumulate[0]['accumulate']
                user_accumulate.append({'word': word, 'num': 0, 'state': 'zh'})
            else:
                user_accumulate = [{'word': word, 'num': 0, 'state': 'zh'}]

            db.update(find={'_id': userId}, content={'_id': userId, 'accumulate': user_accumulate})
            db.close()
            return 'zh'

        if state == 'jx':
            index = 0
            user_accumulate = user_accumulate[0]['accumulate']
            for item in user_accumulate:
                if item['word'] == word:
                    user_accumulate[index]['state'] = 'zh'
                    db.update(find={'_id': userId}, content={'_id': userId, 'accumulate': user_accumulate})
                    db.close()
                    return 'zh'
                index += 1

    def addZW(self, word, userId):
        state = self.getState(word=word, userId=userId)
        if state == 'zw':
            return state

        db = db_obj(db='userDB', col='userWord')
        user_accumulate = db.search(content={'_id': userId})

        if user_accumulate is None:
            user_accumulate.append({'word': word, 'num': 1, 'state': 'zw'})
            db.update(find={'_id': userId}, content={'_id': userId, 'accumulate': user_accumulate})
            return 'zw'
        user_accumulate = user_accumulate[0]['accumulate']
        index = 0
        for item in user_accumulate:
            if item['word'] == word:
                user_accumulate[index]['num'] = item['num'] + 1
                user_accumulate[index]['state'] = 'zw'

                db.update(find={'_id': userId}, content={'_id': userId, 'accumulate': user_accumulate})
                db.close()
                return 'zw'
            index += 1

        user_accumulate.append({'word': word, 'num': 1, 'state': 'zw'})
        db.update(find={'_id': userId}, content={'_id': userId, 'accumulate': user_accumulate})
        return 'zw'

    def getNum(self, word, userId):
        db = db_obj(db='userDB', col='userWord')
        user_accumulate = db.search(content={'_id': userId})

        user_accumulate = user_accumulate[0]['accumulate']
        for item in user_accumulate:
            if item['word'] == word:
                return item['num']
        return 0
