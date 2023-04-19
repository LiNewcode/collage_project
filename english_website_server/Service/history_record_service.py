from end_of_term_work.Tool.link_db import db_obj
from end_of_term_work.main_function_reading.QueryRecord import query_record_menu


class history_record:
    def __init__(self, _id=None, word=None, choice=None, userId=None):
        self._id = _id
        self.word = word
        self.choice = choice
        self.userId = userId

    def check(self):
        id = self._id
        word = self.word
        choice = self.choice
        if word is None:
            if id is None:

                return '000'
            elif choice is None:

                return '001'
            elif choice == 'show_all':
                return '002'
            # 删除多个 003
        if type(word) == type([]) and choice == 'delete_many':
            index = 0
            for i in self.word:
                self.word[index] = i.lower()
                index += 1
            return '003'
        #
        if word.isalpha():
            self.word = word.lower()
            if choice == 'query':
                return '004'
            elif choice == 'delete_one':
                return '005'
        if choice == 'collect':
            return '006'
        if choice == 'not_collect':
            return '007'
        else:
            return '008'

    def run(self):
        check_code = self.check()
        if check_code == '000':
            return '000'  # 文章id为空
        if check_code == '001':
            return '001'  # 选项为空
        if check_code == '008':
            return '008'  # 未知错误
        if check_code == '002':
            return query_record_menu(choice='show', filename=self._id, userId=self.userId).run()  # 展示所有
        if check_code == '003':
            return query_record_menu(choice='delete', filename=self._id, userId=self.userId).run(deleteCount='many',
                                                                                                 deleteList=self.word)  # 删除多个
        if check_code == '004':
            return query_record_menu(choice='insert', word=self.word, filename=self._id,
                                     userId=self.userId).run()  # 插入单个单词
        if check_code == '005':
            return query_record_menu(choice='delete', word=self.word, filename=self._id, userId=self.userId).run(
                deleteCount='one')  # 删除单个单词
        if check_code == '006':
            return query_record_menu(choice='collect', word=self.word, filename=self._id, userId=self.userId).run(
                deleteCount='one')
        if check_code == '007':
            return query_record_menu(choice='not_collect', word=self.word, filename=self._id, userId=self.userId).run(
                deleteCount='one')

