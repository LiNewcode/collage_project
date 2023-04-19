from end_of_term_work.Tool.link_db import db_obj

if __name__ == '__main__':
    kyyd = db_obj(col='kyyd').search({})
    db = db_obj(col='lls')
    # c = db.search(content={'type': None})
    # print(len(c))
    # for item in c:
    #     print(item['_id'])
    #     db.update(find={'_id': item['_id']},content={'type':'lls'})
    for item in kyyd:
        db.insert(item)
    # db_obj(col='lls').delete(content={'type':'ky'},choice=2)