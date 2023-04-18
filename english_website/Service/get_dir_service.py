from end_of_term_work.main_function_reading.FileDirectory import get_file_dir


class get_dir:
    def __init__(self, choice, userId):
        self.choice = choice
        self.userId = userId
        pass

    def run(self):
        if self.choice == 'all':
            # 获取全部
            return get_file_dir(userId=self.userId).run_all()
        elif self.choice == 'tjyd':
            # 推荐阅读
            return get_file_dir(userId=self.userId).run_tjyd()
        elif self.choice == 'ztyd':
            # 真题阅读
            return get_file_dir(userId=self.userId).run_ztyd()
