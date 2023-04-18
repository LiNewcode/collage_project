import re

from end_of_term_work.Tool.link_db import db_obj


def getId(db):
    _id = db.search(content={}, limit={'_id': 1})
    return _id


if __name__ == '__main__':
    s = set([])
    print(s)
    db = db_obj(db='mymongo', col='peeQuestion')
    id_list = getId(db)
    for item in id_list:
        # print(item)
        s = set([])
        Content = db.search(content={'_id': item['_id']}, limit={'_id': 0, 'Content': 1})
        # print(Content)
        for l in Content[0]['Content']:

            word = re.split(r'\s|\d{1,2}\.{0,1}|\.|\(|\)|）|（|_|‘|“|，|,|!|/|\?|;|&emsp|\[|\]',l)
            # print(word)
            for j in word:
                if len(j)<=2:
                    continue
                elif len(re.findall('[\u4e00-\u9fa5]',j))>0:
                    continue
                else:
                    s.add(j)
        db.update(find={'_id': item['_id']}, content={'accumulate': list(s)})
        print(s)
        # break