import json

from end_of_term_work.main_function_exam.Test import get_test


class get_test_service:
    def __init__(self):
        pass

    def run(self, _id=None, choice=None, year=None, testType=None,userId=None):
        if choice == 'content':

            if year is not None and testType is not None:
                return self.get_test_content(year=year, testType=testType, _id=_id,userId=userId)
            else:
                return json.dumps({'state':'false'})
        elif choice == 'testList':
            return self.get_test_list(_id=_id,userId=userId)
        elif choice == 'ans':
            return self.get_test_ans(_id=_id,year=year,userId=userId,testType=testType)
        elif choice == 'ansDetail':
            return self.get_test_ans_detail(_id=_id)
        else:
            return json.dumps({'state':'false'})

    def get_test_content(self, year, testType, _id=None,userId=None):
        return get_test(_id=_id,userId=userId).get_test_page(year, testType)

    def get_test_list(self, _id=None,userId=None):
        return get_test(_id=_id,userId=userId).get_test_list()


    def get_test_ans(self,_id,year,testType,userId):
        return get_test(_id=_id,userId=userId).get_test_ans(year=year,testType=testType)

    def get_test_ans_detail(self,_id):

        return get_test(_id=_id,userId=None).get_test_ans_detail()