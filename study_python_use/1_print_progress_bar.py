"""
des: print progress bar
author: Mr.Chen
date: 2023-3-18
"""
import time

for i in range(1, 101):
    time.sleep(0.5)
    print(f'\r%d%%[%-50s]sum:100' % (i, '>' * int(i)), end='', flush=True)
