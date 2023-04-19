from end_of_term_work.Tool.link_db import db_obj


class zhxs:

    def __init__(self, userId):
        self.userId = userId

    def getZH(self):
        user_accumulate = self.getAccumulate()
        if len(user_accumulate) == 0:
            return {'my':[],'no':[]}

        res = []

        for item in user_accumulate:
            if item['state'] == 'zh':
                res.append(item['word'])
        return {'my':res,'no':res}

    def getXS(self):
        user_accumulate = self.getAccumulate()
        if len(user_accumulate) == 0:
            return {'my': [], 'no': []}

        res = []

        for item in user_accumulate:
            if item['state'] == 'xs':
                res.append(item['word'])
        return {'my':res,'no':res}

    def getAccumulate(self):
        db = db_obj(db='userDB', col='userWord')
        userId = self.userId
        accumulate = db.search(content={'_id': userId})
        db.close()
        if accumulate is None:
            return []
        else:
            return accumulate[0]['accumulate']
