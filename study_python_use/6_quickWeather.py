import json
import requests
import sys

# 从命令行读取请求的位置
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
sys.exit()
location = ' '.join(sys.argv[1:])
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status()
