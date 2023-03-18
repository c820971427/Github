"""
des: print progress bar
author: Mr.Chen
date: 2023-3-18
"""
import time
# 第一种方式
for i in range(1, 101):
    # time.sleep(0.5)
    print(f'\r%d%%[%-50s]sum:100' % (i, '>' * int(i)), end='', flush=True)
# 带时间的普通进度条
len_list = 60
start_time = time.perf_counter()
for i in range(len_list+1):
    finish = "▓" * i
    need_to_do = "-" * (len_list - i)
    progress = (i/len_list) * 100
    dur = time.perf_counter() - start_time
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(progress, finish, need_to_do, dur), end="")
    time.sleep(0.5)
# 其它方法使用python自带的模块库

