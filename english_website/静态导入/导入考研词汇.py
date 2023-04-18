"""
翻译：https://dict.youdao.com/w/[查询的词汇]/
{
图片：/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/img
翻译解释Xpath：/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[2]
英 音标Xpath：/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/h2/div/span[1]/span
美 音标Xpath：/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/h2/div/span[2]/span
词组Xpath：'/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div[5]/div/div[1]'
近义词Xpath：/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div[5]/div/div[2]
同根词Xpath：/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div[5]/div/div[3]
词语辨析Xpath：/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div[5]/div/div[4]
柯林斯 例句：/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div[4]/div/div/div/div/div/div/ul
}

"""
import multiprocessing
import re
import threading
import time

import pymysql
import pymongo

#from Baidu import baidu

from end_of_term_work.Tool.link_db import db_obj
from end_of_term_work.main_function_reading.SearchWord import SearchWordClass


def getDetail(word):
    # print('进来-2')
    # res=[]
    # res.append(baidu('xxxx').getExplain())
    # print(res)
    #
    # data = {'explain': res}
    data = SearchWordClass(word=word).run()
    print(data)
    return data


def writeInMongo(data, col, word):
    conn = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = conn['thesaurus']
    mycol = mydb[col]
    obj = mycol.update_one({'_id': word}, {'$set': data}, upsert=True)
    return obj


def son_thread(word):
    try:
        print('word:', word)
        time.sleep(0.3)
        col = word[0]

        data = getDetail(word)
        print(data)
        if data is None:
            return None
        return writeInMongo(data=data, col=col, word=word)
    except:
        print('线程出错！')
        return None


def run(col):
    conn = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = conn['thesaurus']
    # e_pee = db_obj(col='e_pee')
    # pee = db_obj(col='pee_word')
    # for i in e_pee.search({}):
    #     word = i['word'][0]
    #     phs = i['word'][1]
    #     des = i['word'][2]
    #     pee.update(find={'_id':word},content={'word':word,'phs':phs,'des':des})
    # pee.close()
    # e_pee.close()

    # print(offset, limit)
    # for i in col:
    _id = mydb[col].find({'explain_exist':0}, {'_id': 1})
    for j in _id:
        print(j)
        son_thread(j['_id'])


if __name__ == '__main__':
    # run('a')
    j1 = multiprocessing.Process(target=run, args=('abcde'))
    j2 = multiprocessing.Process(target=run, args=('fghij'))
    j3 = multiprocessing.Process(target=run, args=('klmno'))
    j4 = multiprocessing.Process(target=run, args=('pqrstu'))
    j5 = multiprocessing.Process(target=run, args=('vwxyz'))
    qlist = []
    for i in 'abcdefghijklmnopqrstuvwxyz':
        qlist.append(multiprocessing.Process(target=run, args=(i)))

    for i in qlist:
        i.start()
        print('start')
        time.sleep(0.3)
    for i in qlist:
        i.join()
    time.sleep(1)
    print('总线程结束')
