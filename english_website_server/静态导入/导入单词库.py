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

from end_of_term_work.main_function_reading import SearchWord


def getDetail(word):
    # print('进来-2')
    data = SearchWord.SearchWordClass(word).run()
    return data


def writeInMongo(data, col, word):
    conn = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = conn['thesaurus']
    mycol = mydb[col]
    obj = mycol.update_one({'_id': word}, {'$set': data}, upsert=True)
    conn.close()
    return obj


def son_thread(word):
    try:
        time.sleep(0.1)
        col = word[0]
        data = getDetail(word)
        print(data)
        if data is None:
            return None
        time.sleep(0.1)
        return writeInMongo(data=data, col=col, word=word)
    except:
        print(f'线程出错！{word}')
        return None


def run(offset, limit):
    db = pymysql.connect(host='localhost', user="root", passwd="root", db="mydb")
    cursor = db.cursor()
    conn = pymongo.MongoClient('mongodb://localhost:27017/')
    mydb = conn['thesaurus']

    # print(offset, limit)
    sql = 'select * from voc limit ' + str(offset) + ',' + str(limit)
    cursor.execute(sql)
    allRow = cursor.fetchall()
    print()
    cursor.close()
    print(f'进程 {offset} :启动, 长度{len(allRow)}')
    wordList = []
    for row in allRow:
        if len(re.findall('(\.|-|\s)', str(row[0]))) > 0:
            continue
        else:

            word = str(row[0]).lower()
            mycol = mydb[word[0]]
            first_obj=mycol.find({'_id':word},{'_id':1})

            # 未防止查询为空时无正确返回，此时将返回对象转换列表
            list_res = [response for response in first_obj]
            if len(list_res) == 0:
                wordList.append(word)
            else:
                continue
            if len(wordList) >= 6:
                try:
                    thread_list = []
                    # 依次新建 5 个 线程
                    for i in range(6):
                        thread_list.append(threading.Thread(target=son_thread,
                                                            kwargs={'word': wordList[i]}))
                        # print(f'线程 {i} 创建！')
                    # 多个线程依次设置 守护线程，并执行
                    for i in thread_list:
                        i.setDaemon(True)
                        # print(f'线程 {i} 启动！')
                        i.start()
                    for i in thread_list:
                        i.join()
                    time.sleep(1)
                    # son_thread(word)
                    wordList = []
                except:
                    wordList = []
                    print(f'进程 {offset} :出错')


if __name__ == '__main__':
    j1 = multiprocessing.Process(target=run, args=(0, 15000))
    j2 = multiprocessing.Process(target=run, args=(15000, 15000))
    j3 = multiprocessing.Process(target=run, args=(30000, 15000))
    j4 = multiprocessing.Process(target=run, args=(45000, 15000))
    j5 = multiprocessing.Process(target=run, args=(60000, 15000))
    j6 = multiprocessing.Process(target=run, args=(75000, 15000))
    j7 = multiprocessing.Process(target=run, args=(90000, 655))
    qlist = []
    qlist.append(j1)
    qlist.append(j2)
    qlist.append(j3)
    qlist.append(j4)
    qlist.append(j5)
    qlist.append(j6)
    qlist.append(j7)
    for i in qlist:
        time.sleep(0.3)
        i.start()
    for i in qlist:
        i.join()
    time.sleep(1)
    print('总线程结束')
