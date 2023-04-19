"""
    filename:文件名字
    setRecord():设置记录，在退出窗口时会记录
    getRecord():获取上一次浏览记录，加载窗口时记录
"""
import time

from end_of_term_work.Tool.link_db import db_obj


class readerRecord:
    def __init__(self, filename, location):
        self.filename = filename
        self.db = db_obj(db='log', col='readRecord')
        self.date = time.ctime()
        self.location = location

    def setRecord(self):
        exits = self.db.search({'filename': self.filename}, limit={'filename': 1})
        if exits is not None:
            find = {'filename': self.filename}
            content = {'date': self.date, 'location': self.location}
            res = self.db.update(find=find, content=content)
            return res
        else:
            content = {'filename': self.filename, 'date': self.date, 'location': self.location}
            res = self.db.insert(content=content)
            return res

    def getRecord(self):
        exits = self.db.search({'filename': self.filename})
        if exits is not None:
            res_location = exits['location']
            res_time = exits['date']
            res = {'location': res_location, 'date': res_time}
            return res
        else:
            res_location = str(0)
            res_time = time.ctime()
            res = {'location': res_location, 'date': res_time}
            return res
