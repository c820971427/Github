import time
import threading
import subprocess


def takeANap():
    time.sleep(5)
    print('Wake up!')


print('Start of program.')
subprocess.Popen(r'"D:\Program Files (x86)\HuyaClient\HuyaClient\huya.exe"')
subprocess.Popen(r'"C:\Program Files (x86)\Tencent\QQ\Bin\QQScLauncher.exe"')

threadObj = threading.Thread(target=takeANap)
threadObj.start()
print('End of program.')
