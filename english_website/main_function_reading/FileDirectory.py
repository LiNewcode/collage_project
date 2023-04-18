import json

from end_of_term_work.Tool.link_db import db_obj


class get_file_dir():
    def __init__(self, userId):
        self.db = db_obj(col='lls')
        self.clock_detail = self.get_clock_in(userId=userId)

    def run_all(self):
        dirList = []

        for i in self.db.search({}, {'_id': 1, 'title': 1, 'type': 1}):
            try:
                if i['_id'] in self.clock_detail:
                    clock = 'y'
                else:
                    clock = 'n'
            except:
                clock = 'n'
            dirList.append({'title': i['title'], '_id': i['_id'], 'type': i['type'], 'clock': clock})
        self.db.close()
        res = {'catalog': dirList}
        return json.dumps(res, ensure_ascii=True)

    def run_tjyd(self):
        db = db_obj(col='tjyd')
        catalog = db.search({'_id': 'tjyd'}, {'_id': 0})[0]['catalog']
        dirList = []
        for i in catalog:
            try:
                if i['_id'] in self.clock_detail:
                    clock = 'y'
                else:
                    clock = 'n'
            except:
                clock = 'n'
            dirList.append({'title': i['title'], '_id': i['_id'], 'type': i['type'], 'clock': clock})
        res = {'catalog': dirList}
        return json.dumps(res, ensure_ascii=True)

    def run_ztyd(self):
        dirList = []

        for i in self.db.search(content={'type': 'ky'}, limit={'_id': 1, 'title': 1, 'type': 1}):
            try:
                if i['_id'] in self.clock_detail:
                    clock = 'y'
                else:
                    clock = 'n'
            except:
                clock = 'n'
            dirList.append({'title': i['title'], '_id': i['_id'], 'type': i['type'], 'clock': clock})
        self.db.close()
        res = {'catalog': dirList}
        return json.dumps(res, ensure_ascii=True)

    def get_clock_in(self, userId):
        db = db_obj(db='userDB', col='userReadClock')
        clock_detail = []
        try:
            clock_detail = db.search({'_id': userId}, limit={'readClock': 1, '_id': 0})
        except:
            return []
        if clock_detail is not None:
            clock_detail = clock_detail[0]['readClock']
        return clock_detail
