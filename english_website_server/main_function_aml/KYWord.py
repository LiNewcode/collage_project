from end_of_term_work.Tool.link_db import db_obj


class KY:
    def __init__(self, userId):
        self.userId = userId

    def getKy(self):
        userId = self.userId
        db = db_obj(col='ky')
        ky = db.search({}, limit={'_id': 0, 'word': 1})

        db.close()

        db = db_obj(db='userDB', col='userWord')
        accumulate = db.search({}, limit={'_id': 0, 'accumulate': 1})

        db.close()
        my = set([])
        already = set([])
        if accumulate is not None:
            for item in accumulate[0]['accumulate']:
                my.add(item['word'])
                if item['state'] == 'zw':
                    already.add(item['word'])
        try:
            ky = set(ky[0]['word'])
        except:
            pass
        my = ky & my
        no = list(ky ^ my)
        my = list(my - already)
        ky = list(ky)



        return {'ky': ky, 'my': my, 'no': no}
