import re

# 新建Regex对象-传入正则表达式
phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# search方法传入要查找的字符串 group对象返回实际匹配的文本
mo = phoneNumberRegex.search('My number is 100-222-6789')
# print(mo)
print('Phone number found: ' + mo.group())
