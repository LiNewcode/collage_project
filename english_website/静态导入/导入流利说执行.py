import multiprocessing
import os
import threading
import time
from glob import glob

from end_of_term_work.静态导入.导入流利说 import import_lls


def run(src,index):
    src_list = src['src']
    num=1

    for i in src_list:
        num+=1
        import_lls(i).run(str(index)+'-'+str(num))

if __name__ == '__main__':
    # for i in range(4,11):
    program_list = []
    index = 1
    for i in range(1,5):
        src_dir = 'F:\\英语\\流利说\\待导入'+str(i)+'\\'
        src_file_list = glob(src_dir + '*')  # glob获得路径下所有文件，可根据需要修改
        print(src_file_list)
        src = {'src':src_file_list}
        program_list.append(multiprocessing.Process(target=run, args=(src,index)))
        index+=1
            # src_f = glob(src + '*')
    for i in program_list:
        time.sleep(1)
        i.start()
    for i in program_list:
        i.join()
    print('执行完毕！')