from end_of_term_work.Tool.link_db import db_obj


class examRecord:
    def __init__(self, fileName):

        self.db = db_obj(db='examRecord', col=fileName)

    def exitsExamWord(self, word):
        return True
        res = db_obj(db='examRecord', col='exam_word').search({'word': word})
        if res is not None:
            return True
        else:
            return False

    def getExamWordList(self):
        res_word = self.db.search({})
        data = {'examWord': res_word}
        return data
