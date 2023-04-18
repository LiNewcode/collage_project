import pymongo


class db_obj:
    # 建立无用户名密码连接 默认使用 test库
    def __init__(self, db='mymongo', col=None):
        self.conn = pymongo.MongoClient('mongodb://localhost:27017/')

        self.mydb = self.conn[db]
        # e_pee 考研英语
        self.mycol = self.mydb[col]

    def insert(self, content):
        obj = self.mycol.insert_one(content)
        return obj

    # content :搜索内容,传入搜索内容是一个dict，limit是返回值限定
    def search(self, content=None, limit=None):
        if limit is None:
            first_obj = self.mycol.find(content)
        else:
            first_obj = self.mycol.find(content, limit)
        # 未防止查询为空时无正确返回，此时将返回对象转换列表
        list_res = [response for response in first_obj]
        if len(list_res) == 0:
            print('查询为空')
            return None
        else:
            return list_res

    # 如果choice为1，则删除一个，choice>1，则删除多个
    def delete(self, content=None, choice=1):
        if choice == 1:
            res = self.mycol.delete_one(content)
            return res
        else:
            res = self.mycol.delete_many(content)
            return res

    # find 为定位元素，dict类型，content为修改内容，dict类型
    def update(self, find=None, content=None):
        self.mycol.update_one(find, {'$set': content},True)
        pass

    def dropCol(self):
        res = self.mycol.drop()
        return res

    def close(self):
        self.conn.close()
