import os
import sys
import shutil

current_path = os.path.abspath(os.path.dirname(__file__))
src_path = os.path.join(current_path, '知识付费文件')
add_path = 'pack_path'
copy_des_path = os.path.join(current_path, add_path)

if src_path:
    for root, dirs, files in os.walk(src_path):
        if files.endswith('.pdf'):
            print(files)
            # shutil.copy(root + files, copy_des_path + files)
else:
    print('src_path 不存在')
