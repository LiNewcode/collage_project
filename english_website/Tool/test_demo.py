import json

import pymysql

from end_of_term_work.Service.contrast_pee_service import contrast_service
from end_of_term_work.Service.get_article_service import get_article_info
from end_of_term_work.Service.get_dir_service import get_dir
from end_of_term_work.Service.history_record_service import history_record
from end_of_term_work.main_function_reading import SearchWord

if __name__ == '__main__':
    userId = '11111'
    contrast_service(userId).contrast_pee()
