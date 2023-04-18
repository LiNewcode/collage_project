import json

from end_of_term_work.main_function_aml.JCWord import JC
from end_of_term_work.main_function_aml.KYWord import KY
from end_of_term_work.main_function_aml.LJWord import LJ
from end_of_term_work.main_function_aml.ZHXS import zhxs
from end_of_term_work.main_function_aml.contrast_word import contrast_word
from end_of_term_work.main_function_aml.wordState import wordState


class contrast_service:
    def __init__(self, userId, word):
        self.userId = userId
        self.word = word
        pass

    def contrast_pee(self):

        return contrast_word(userId=self.userId).get_recommend()

    def run(self, choice):

        if choice == 'ky':
            return self.get_ky()
        elif choice == 'jc':
            return self.get_jc()
        elif choice == 'lj':
            return self.get_lj()
        elif choice == 'zh':
            return self.get_zh()
        elif choice == 'xs':
            return self.get_xs()
        elif choice == 'getState':
            return self.get_word_state()
        elif choice == 'addZH':
            return self.add_zh()
        elif choice == 'addZW':
            return self.add_zw()
        elif choice == 'addXS':
            return self.add_xs()
        elif choice == 'addJX':
            return self.add_jx()
        elif choice == 'getNum':
            return self.get_num()
        else:
            return json.dumps({'state': 'false', 'data': 'null'})

    def get_ky(self):
        ky = []
        my = []
        no = []
        data = KY(userId=self.userId).getKy()
        return json.dumps({'state': 'true', 'data': data})

    def get_jc(self):
        jc = []
        my = []
        no = []
        data = JC(userId=self.userId).getJc()
        return json.dumps({'state': 'true', 'data': data})

    def get_lj(self):
        lj = []
        my = []
        no = []

        data = LJ(userId=self.userId).getLj()
        return json.dumps({'state': 'true', 'data': data})

    def get_word_state(self):
        data = wordState().run(word=self.word, userId=self.userId, choice='getState')
        return json.dumps({'state': 'true', 'data': data})

    def get_zh(self):
        zh = []
        zh = zhxs(userId=self.userId).getZH()

        return json.dumps({'state': 'true', 'data': zh})

    def get_xs(self):
        xs = []
        xs = zhxs(userId=self.userId).getXS()

        return json.dumps({'state': 'true', 'data': xs})

    def add_zh(self):
        data = wordState().run(word=self.word, userId=self.userId, choice='addZH')
        return json.dumps({'state': 'true', 'data': data})

    def add_xs(self):
        data = wordState().run(word=self.word, userId=self.userId, choice='addXS')
        return json.dumps({'state': 'true', 'data': data})

    def add_jx(self):
        data = wordState().run(word=self.word, userId=self.userId, choice='addJX')
        return json.dumps({'state': 'true', 'data': data})

    def add_zw(self):
        data = wordState().run(word=self.word, userId=self.userId, choice='addZW')
        return json.dumps({'state': 'true', 'data': data})

    def get_num(self):
        data = wordState().run(word=self.word, userId=self.userId, choice='getNum')
        return json.dumps({'state': 'true', 'data': data})