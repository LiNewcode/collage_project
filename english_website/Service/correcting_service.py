from end_of_term_work.main_function_exam.englishExam import englishExam


class ans_service:
    def __init__(self):
        pass

    def ans_correct(self, year, testType, ans,userId):
        englishExam(ans,year,testType=testType,userId=userId)
