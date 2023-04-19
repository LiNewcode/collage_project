from end_of_term_work.Tool.link_db import db_obj

if __name__ == '__main__':
    db = db_obj(db='mymongo', col='peeQrWhole')
    con = db.search(content={}, limit={'_id': 1})
    print(con)
    com = []
    for item in con:
        id = item['_id']
        testType = id[0]
        year = id[2:6]
        num = id[-1]
        db.update(find={'_id': id}, content={'type': testType, 'year': year, 'num': num})
    print(com)
