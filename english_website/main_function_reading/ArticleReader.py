import json

from end_of_term_work.Tool.link_db import db_obj


class get_article:
    word_pee = []

    def __init__(self, _id):
        self._id = _id
        self.db = db_obj(col='lls')

    def get_article(self):
        _id = self._id
        res = self.db.search(content={'_id': _id}, limit={'_id': 0})
        if type(res) is type([]):
            res = res[0]

        self.db.close()
        annotation = res['annotation']
        return json.dumps(
            {'annotation': annotation, 'title': res['title'], 'title_des': ['title_des'], 'article': res['article']})

    def get_pee_list(self, userId):
        _id = self._id
        res = self.db.search(content={'_id': _id}, limit={'_id': 0})
        if type(res) is type([]):
            res = res[0]

        pee = res['article_pee']
        self.db.close()
        db = db_obj(db='queryRecord', col=_id)
        for item in pee:
            signal = db.search(content={'word': item, 'userId': userId}, limit={'_id': 0, 'signal': 1})
            if signal is not None:
                signal = signal[0]['signal']
                if signal is None:
                    signal = 'n'
            else:
                signal = 'n'
            self.word_pee.append({'word': item, 'signal': signal})
        return json.dumps({'pee': self.word_pee})

    def get_collect_list(self, userId):
        _id = self._id
        db = db_obj(db='queryRecord', col=_id)
        collect_list = db.search(content={'userId': userId, 'signal': 'y'}, limit={'_id': 0, 'word': 1})

        return json.dumps({'collect': collect_list})

    def punch_clock(self, userId):

        _id = self._id
        clock = None
        userClockList = []
        db = db_obj(db='userDB', col='userReadClock')
        try:
            userClockList = db.search({'_id': userId})[0]['readClock']
            if _id in userClockList:
                clock = True
                return json.dumps({'state': 'fail'})
        except:
            clock = False
        if not clock:
            userClockList.append(_id)
        db.update(find={'_id': userId}, content={'_id': userId, 'readClock': userClockList})
        return json.dumps({'state': 'success'})
