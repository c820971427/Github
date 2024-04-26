import keyword

print(keyword.kwlist, end='')

# print("100到1000之前的所有水仙花数如下： ")
# for i in range(100, 1000):
#     x = i // 100
#     y = i // 10 % 10
#     z = i % 10
#     if x ** 3 + y ** 3 + z ** 3 == i:
#         print(f'{i}是水仙花数')

# import threading
# from time import sleep,ctime
#
# def sing():
#     for i in range(3):
#         print("正在唱歌...%d"%i)
#         sleep(1)
#
# def dance():
#     for i in range(3):
#         print("正在跳舞...%d"%i)
#         sleep(1)
#
# if __name__ == '__main__':
#     print('---开始---:%s'%ctime())
#
#     t1 = threading.Thread(target=sing)
#     t2 = threading.Thread(target=dance)
#
#     t1.start()
#     t2.start()
#
#     while True:
#         length = len(threading.enumerate())
#         print('当前运行的线程数为：%d'%length)
#         if length<=1:
#             break
#
#         sleep(0.5)


# import json
# import xmltodict
#
#
# def xmlToJson(xml_str):
#     """
#     :param xml_str: xml字符串
#     :return: json字符
#     """
#     xml_parse = xmltodict.parse(xml_str)
#     json_str = json.dumps(xml_parse, indent=4)
#     return json_str
#
#
# XML_PATH = '../tmp_files/1.xml'
# with open(XML_PATH, 'r') as f:
#     xmlFile = f.read()
#     print(xmlFile)
#     print(xmlToJson(xmlFile))
# print(XML_PATH[:-3])
