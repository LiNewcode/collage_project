"""
    接口Demo测试
    Flask

"""
# 1’安装 pip install Flask
# 2‘ 导包from flask import Flask
import json

from flask import Flask, url_for, redirect, make_response
from flask import request
# cors解决跨域问题
from flask_cors import cross_origin

# 3’ __name__ 传入当前py的名字到Flask中创建一个Flask实例
from end_of_term_work.Service.contrast_pee_service import contrast_service
from end_of_term_work.Service.correcting_service import ans_service
from end_of_term_work.Service.get_article_service import get_article_info
from end_of_term_work.Service.get_dir_service import get_dir
from end_of_term_work.Service.get_test_page_service import get_test_service
from end_of_term_work.Service.get_word_service import get_word
from end_of_term_work.Service.history_record_service import history_record
from end_of_term_work.Service.listen_write_service import listen_write_service
from end_of_term_work.Service.login_service import login_service
from end_of_term_work.Service.register_service import register_service
from end_of_term_work.main_function_reading import SearchWord

app = Flask(__name__)


# 4‘ 路由
@app.route("/Reader/getWord", methods=['GET', 'POST'])
@cross_origin()
def to_get_word():
    word = request.args.get('word')
    try:
        userId = request.args.get('userId')
    except:
        userId = None
    return get_word().run(word=word, userId=userId)


@app.route("/Reader/getCatalog", methods=['GET', 'POST'])
@cross_origin()
def to_get_catalog():
    try:
        choice = request.args.get('choice')
    except:
        choice = 'all'
    try:
        userId = request.args.get('userId')
    except:
        userId = None
    return get_dir(choice, userId).run()


@app.route("/Reader/getArticle", methods=['GET', 'POST'])
@cross_origin()
def to_get_article():
    try:
        _id = request.args.get('_id')
    except:
        _id = None
    try:
        choice = request.args.get('choice')
    except:
        choice = None
    try:
        userId = request.args.get('userId')
    except:
        userId = None
    # print(_id, choice)
    return get_article_info().run(_id=_id, choice=choice, userId=userId)


@app.route("/Reader/hr", methods=['GET', 'POST'])
@cross_origin()
def to_history_record_show():
    try:
        _id = request.args.get('_id')
    except:
        _id = None

    try:
        choice = request.args.get('choice')
    except:
        choice = None

    try:
        word = request.args.get('word')
    except:
        word = None
    try:
        userId = request.args.get('userId')
    except:
        userId = None
    print(_id, choice, word, userId)
    return history_record(_id=_id, word=word, choice=choice, userId=userId).run()


@app.route("/Test/testPage", methods=['GET', 'POST'])
@cross_origin()
def to_test():
    try:
        _id = request.args.get('_id')
    except:
        _id = None
    try:
        choice = request.args.get('choice')
    except:
        choice = None
    try:
        testType = request.args.get('testType')
    except:
        testType = None
    try:
        year = request.args.get('year')
    except:
        year = None
    try:
        userId = request.args.get('userId')
    except:
        userId = None
    print('userId', userId)
    return get_test_service().run(_id=_id, choice=choice, year=year, testType=testType, userId=userId)


@app.route("/User/login", methods=['GET', 'POST'])
@cross_origin()
def to_login():
    try:
        username = request.args.get('username')
    except:
        username = None
    try:
        password = request.args.get('password')
    except:
        password = None
    res = login_service().run(username, password)

    if res:
        return res
    else:
        return json.dumps({'state': 'false'})


@app.route("/Test/headUp", methods=['GET', 'POST'])
@cross_origin()
def to_headUp():
    try:
        userId = request.args.get('userId')
    except:
        userId = None
    try:
        ans = json.loads(request.args.get('ans'))
    except:
        ans = None
    try:
        testType = request.args.get('testType')
    except:
        testType = None
    try:
        year = request.args.get('year')
    except:
        year = None

    print(userId, type(ans), ans)
    print(type(ans['ans']), ans['ans'])
    print(ans['ans'][-2])
    print(f'year:{year},testType:{testType}')
    ans_service().ans_correct(year, testType, ans['ans'], userId)
    return 'hhh'


@app.route("/User/register", methods=['GET', 'POST'])
@cross_origin()
def to_register():
    print('aa')
    try:
        username = request.args.get('username')
    except:
        username = None
    try:
        password = request.args.get('password')
    except:
        password = None
    try:
        phone = request.args.get('phone')
    except:
        phone = None
    res = register_service().run(phone, username, password)
    if res:

        return res
    else:
        return json.dumps({'state': 'false'})


@app.route("/User/Recommend", methods=['GET', 'POST'])
@cross_origin()
def to_get_recommend():
    try:
        userId = request.args.get('userId')
    except:
        userId = None

    return json.dumps(contrast_service(userId=userId,word='').contrast_pee())


@app.route("/User/Accumulate", methods=['GET', 'POST'])
@cross_origin()
def to_get_accumulate():
    try:
        userId = request.args.get('userId')
    except:
        userId = None
    try:
        choice = request.args.get('choice')
    except:
        choice = 'ky'

    try:
        word = request.args.get('word')
    except:
        word = ''

    # contrast_service(userId).contrast_pee()
    return contrast_service(userId=userId, word=word).run(choice=choice)


@app.route("/User/ListenAndWrite", methods=['GET', 'POST'])
@cross_origin()
def to_listen_write():
    params = None
    try:
        userId = request.args.get('userId')
    except:
        userId = None
    try:
        choice = request.args.get('choice')
    except:
        choice = ''
    params = None
    if choice == 'add':
        try:
            word_list = request.args.get('word_list')
            params = word_list
        except:
            word_list = None
            return {'state': 'false'}
    elif choice == 'correct':
        try:
            res_list = request.args.get('res_list')
            params = res_list
        except:
            res_list = None
            return {'state': 'false'}
    # contrast_service(userId).contrast_pee()
    return listen_write_service(userId=userId, params=params).run(choice=choice)


if __name__ == '__main__':
    # 5’ 启动服务器
    app.run()
