import re

from end_of_term_work.main_function_foundation.Login import login


class login_service:
    username = None
    password = None

    def __init__(self):
        pass

    def run(self, username, password):

        if self.check(username, password):
            return self.login()
        return False

    def check(self, username: str, password: str):

        if self.check_username(username):
            self.username = username
        else:
            return False

        if self.check_password(password):
            self.password = password
        else:
            return False

        return True

    def check_username(self, username):
        pattern = r'(true|false)'

        if len(re.findall(pattern, username)) > 0:
            return False
        elif type(username) is not str:
            return False
        elif len(username) > 12:
            return False
        else:
            return True

    def check_password(self, password):
        pattern_1 = r'\w'  # 匹配是否全为英文、数字、下划线
        pattern_2 = r'\W'
        pattern_3 = r'(true|false)'
        for i in password:
            if len(re.findall(pattern_1, password)) == 0:

                return False
            elif len(re.findall(pattern_2, password)) > 0:
                return False
            elif len(password) > 16 or len(password) < 6:
                return False
            elif type(password) is not str:
                return False
            elif len(re.findall(pattern_3, password)) > 0:
                return False
            else:

                return True

    def login(self):
        if self.username is not None and self.password is not None:
            return login().run(self.username, self.password)
        return False
