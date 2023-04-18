from end_of_term_work.Tool.link_db import db_obj


def getId(db):
    _id = db.search(content={}, limit={'_id': 1})
    return _id


def getWordList(db):
    pass


def updateData(db):
    pass


if __name__ == '__main__':
    s = set([])
    print(s)
    db = db_obj(db='mymongo', col='lls')
    id_list = getId(db)
    for item in id_list:
        print(item)
        s = set([])
        article = db.search(content={'_id':item['_id']},limit={'_id':0,'article':1})
        print(article)
        for pr in article[0]['article']:
            for word in pr['content']:
                if word['signal'] == 'en':
                    s.add(word['word'])

        db.update(find={'_id':item['_id']},content={'accumulate':list(s)})
        print(s)
