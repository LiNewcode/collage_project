from end_of_term_work.Tool.link_db import db_obj


class JC:
    def __init__(self, userId):
        self.userId = userId

    def getJc(self):
        userId = self.userId
        db = db_obj(col='gz')
        jc = db.search({}, limit={'_id': 0, 'word': 1})
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
        else:
            pass
        try:
            jc = set(jc[0]['word'])
        except:
            pass

        my = jc & my
        no = list(jc ^ my)

        my = list(my - already)
        jc = list(jc)



        return {'jc': jc, 'my': my, 'no': no}
