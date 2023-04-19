import json

from flask import request ,make_response

from end_of_term_work.Tool.link_db import db_obj
from end_of_term_work.main_function_reading import SearchWord


class get_word:
    word = ''

    def __init__(self):
        pass

    def check(self, word):
        if word.isalpha():
            self.word = word.lower()
            return True
        else:
            return False

    def run(self, word,userId):
        if self.check(word=word):
            word = self.word
            db = db_obj(db='thesaurus', col=word[0])
            res = db.search(content={'_id': word})
            if res is not None:
                response = json.dumps(res[0], ensure_ascii=True)
                return response
            else:
                search_word = SearchWord.SearchWordClass(word)
                res = search_word.run()

                # 返回值
                return search_word.pack2json()
        else:
            return None
