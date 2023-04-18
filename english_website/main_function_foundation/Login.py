import json

from end_of_term_work.Tool.link_db import db_obj


class login:
    def __init__(self):
        pass

    def run(self, username, password):
        db = db_obj(db='userDB', col='user')
        if db.search({'username': username, 'password': password}) is not None:
            id = db.search({'username': username, 'password': password}, limit={'_id': 1})[0]
            return json.dumps({'state': 'true', 'id': id['_id']})
        return False
