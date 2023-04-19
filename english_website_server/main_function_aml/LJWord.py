from end_of_term_work.Tool.link_db import db_obj


class LJ:
    def __init__(self, userId):
        self.userId = userId

    def getLj(self):
        userId = self.userId
        db = db_obj(col='lj')
        lj = db.search({}, limit={'_id': 0, 'word': 1})
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
            lj = set(lj[0]['word'])
        except:
            pass
        my = lj & my
        no = list(lj ^ my)
        my = list(my - already)
        lj = list(lj)



        return {'lj': lj, 'my': my, 'no': no}
