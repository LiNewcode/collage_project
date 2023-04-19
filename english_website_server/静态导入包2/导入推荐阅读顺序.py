from end_of_term_work.Tool.link_db import db_obj


def getLls():
    db = db_obj(col='lls')
    all_article = db.search({}, limit={'_id': 1, 'article_pee': 1})
    print(len(all_article))
    db.close()
    num = 0
    max_similarity = 0
    index = 0
    peach = 0
    id_list = []
    db = db_obj(col='ky')
    ky = db.search({}, limit={'_id': 0})[0]['word']
    print(len(ky))
    db.close()
    result = []
    res_len = 0
    res_list = set([])
    while peach < 150:
        peach += 1

        max_similarity = 0
        maxArticle = None
        maxId = None
        for article in all_article:
            # print(article)
            similarity = len(set(article['article_pee'])) - len(set(article['article_pee']) & res_list)
            if similarity > max_similarity:
                max_similarity = similarity
                maxArticle = article
                maxId = article['_id']
        # print(max_similarity)
        #
        # print('[ maxArticle ]:', maxArticle)
        all_article.remove(maxArticle)
        result.append(maxId)
        num = len(result)
        now_len = len(maxArticle['article_pee'])
        for word in maxArticle['article_pee']:
            res_list.add(word.lower())
        # print(f'[ peach ]:{peach},[ sum ]:{len(res_list)},[word_sum]:{len(res_list)} [ len ]:{now_len}')
        # print(f'[ peach ]:{peach}, [ result ]:{res_list}')
        _id = maxId
        # print(f'[ id ] :{_id}')
        id_list.append(_id)
    # return list(res_list)
    return id_list


def getKy1():
    db = db_obj(col='peeQuestion')
    accumulate_list = db.search(content={'TestType': '1'}, limit={'accumulate': 1, '_id': 0})
    res_list = set([])
    for item in accumulate_list:
        for word in list(set(item['accumulate'])):
            res_list.add(word.lower())
    return res_list


def getKy2():
    db = db_obj(col='peeQuestion')
    accumulate_list = db.search(content={'TestType': '2'}, limit={'accumulate': 1, '_id': 0})
    res_list = set([])
    for item in accumulate_list:
        for word in list(set(item['accumulate'])):
            res_list.add(word.lower())
    return res_list


def getPee():
    db = db_obj(col='ky')
    return set(db.search({}, limit={'word': 1})[0]['word'])


if __name__ == '__main__':
    lls_list = getLls()
    db = db_obj(col='lls')
    dirList = []
    for nam in lls_list:
        i = db.search({'_id':nam}, {'_id': 1, 'title': 1, 'type': 1})[0]
        dirList.append({'title': i['title'], '_id': i['_id'], 'type': i['type']})
    db_obj(col='tjyd').insert({'_id': 'tjyd', 'catalog': dirList})
    print(lls_list)
    db.close()
    # ky1_list = getKy1()
    # ky2_list = getKy2()
    # common = ky1_list & ky2_list
    #
    # # print(f'{len(lls_list)}')#2382
    # print(common)
    # print(f'{len(common)}')  # 总8659 研一5844 研二5411 共用2596

    # pee = getPee()
    # print(f'1&pee:{len(ky1_list&pee)},2&pee:{len(ky2_list&pee)}')
    # print(f'{len(lls_list)} [ lls_list ]:{lls_list}')
    # print(f'{len(ky2_list)} [ ky2_list ]:{ky2_list}')
    # print(f'{len(ky2_list)} [ ky2_list ]:{ky2_list}')
    # print(f'总共：{len(set(lls_list)&set(ky_list))}\n[ lls_list & ky_list]:{list(set(lls_list)&set(ky_list))}')
    pass
