from end_of_term_work.main_function_reading.ArticleReader import get_article


class get_article_info:
    def __init__(self):
        pass

    def run(self, _id, choice, userId):
        if choice == 'content':
            return self.get_article_content(_id=_id)
        elif choice == 'pee':
            return self.get_article_pee(_id=_id, userId=userId)
        elif choice == 'collect':
            return self.get_article_collect(_id=_id, userId=userId)
        elif choice == 'clockIn':
            return self.clock_in(_id=_id, userId=userId)
        else:
            return None

    def get_article_content(self, _id):
        return get_article(_id=_id).get_article()

    def get_article_pee(self, _id, userId):
        return get_article(_id=_id).get_pee_list(userId)

    def get_article_collect(self, _id, userId):
        return get_article(_id=_id).get_collect_list(userId)

    def clock_in(self, _id, userId):
        return get_article(_id=_id).punch_clock(userId)
