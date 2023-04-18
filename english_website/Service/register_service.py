import re

from end_of_term_work.main_function_foundation.Register import register


class register_service:
    phone = None
    username = None
    password = None

    def __init__(self):
        pass

    def run(self, phone: str, username: str, password: str):
        if self.check(phone, username, password):
            return self.register()
        return False

    def check(self, phone: str, username: str, password: str):
        if self.check_phone(phone):
            self.phone = phone
        else:

            return False

        if self.check_username(username):
            self.username = username
        else:

            return False

        if self.check_password(password):
            self.password = password
        else:

            return False

        return True

    def check_phone(self, phone):

        # 移动：134、135、136、137、138、139、150、151、157(TD)、158、159、187、188
        # 联通：130、131、132、152、155、156、185、186
        # 电信：133、153、180、189、（1349
        # 卫通）
        # 总结起来就是第一位必定为1，第二位必定为3或5或8，其他位置的可以为0 - 9

        # 验证手机
        if type(phone) is not str:
            return False
        pattern = r'1[358]{1}\d{9}'
        res = re.findall(pattern, phone)

        if len(res) > 0:
            return True
        else:

            return False

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

        return True

    def register(self):
        return register().run(self.phone, self.username, self.password)
