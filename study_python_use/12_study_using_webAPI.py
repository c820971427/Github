# Web API是网站的一部分，用于与使用非常具体的URL请求特定信息的程序交互。这种请求称为API调用。
# 请求的数据将以易于处理的格式（如JSON或CSV）返回
import requests

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
# print(r)
print(r.status_code)
# 将API响应存储在一个变量中
response_dict = r.json()
with open('../tmp_files/API.txt', 'w') as f:
    for key, value in response_dict:
        f.write(key)
        f.write(value)
print(response_dict.keys())
