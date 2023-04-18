import os
import shutil
from glob import glob


def mymovefile(srcfile, dstpath):  # 移动函数
    print('sss!',srcfile)
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(srcfile)  # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)  # 创建路径
        shutil.move(srcfile, dstpath + fname)  # 移动文件
        print("move %s -> %s" % (srcfile, dstpath + fname))
#\\2021-'+str(i)+'/0'+str(i)
if __name__ == '__main__':
    # for i in range(4,11):
        src_dir = 'F:\\英语\\流利说\\2021-'+str(3)+'\\'
        dst_dir = 'F:\\英语\\流利说\\'  # 目的路径记得加斜杠
        src_file_list = glob(src_dir + '*')  # glob获得路径下所有文件，可根据需要修改
        print(src_file_list)
        for srcfile in src_file_list:
            src = srcfile+'\\'
            print(src)
            src_f = glob(src + '*')
            for sr in src_f:
                mymovefile(sr, dst_dir)  # 移动文件
