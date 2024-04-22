import os

current_path = os.getcwd()
print(current_path)
with open('../readme.txt') as tmp:
    # for contents in tmp:
    # contents = tmp.read()
    #     print(contents, end='')
    # 去除尾部空格
    #     print(contents.rstrip())
    lines = tmp.readlines()
    print(lines)
    words = ""
    for line in lines:
        words += line
    print(words)
    # 字符串 分割成列表
    word = words.split()
    print(word)
    number_words = len(word)
    print(number_words)
