from end_of_term_work.Tool.link_db import db_obj

if __name__ == '__main__':
    db = db_obj(col='lls')
    res = db.search({})
    for article in res:
        _id = article['_id']
        article_pee = set(article['article_pee'])
        db.update(find={'_id':_id},content={'article_pee':list(article_pee)})

