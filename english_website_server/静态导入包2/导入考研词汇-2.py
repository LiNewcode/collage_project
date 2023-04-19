from end_of_term_work.Tool.link_db import db_obj
if __name__ == '__main__':

    w_l =  db_obj(col='e_pee').search({},limit={'_id':0,'word':1})
    word = []
    for item in w_l:
        word.append(item['word'][0])
    print(word)
    db_obj(col='ky').insert({'word': word})