import json
import random

from end_of_term_work.Tool.link_db import db_obj


class register:
    def __init__(self):
        pass

    def run(self, phone, username, password):
        db = db_obj(db='userDB', col='user')
        _id = str(random.randint(1, int(phone[-1:6:-1])))
        _id += phone[-1:6:-1]

        if db.search({'phone': phone}) is None:

            if db.search({'_id': _id}) is None and db.search({'username': username}) is None:

                db.update({'_id': _id}, {'_id': _id, 'username': username, 'password': password,'phone':phone})
                id = _id
                return json.dumps({'state': 'true', 'id': id})
            else:
                return False
            return False

# if __name__ == '__main__':
#     phone = '13665025020'

#     print(random.randint(1, int(phone[-1:7:-1])))
