#!/usr/bin/env python3
"""
des:
author:
date:
"""

# 添加注释
import sys

s = []
while True:
    try:
        line = sys.stdin.readline().strip()
        # print(line)
        lines = line.split()
        # print(lines)
        s.append([lines[0], int(lines[1])])
        # print(s)
    except:
        break

# """
# 题解：使用字典处理
# """
# dic = {}
# try:
#     while True:
#         p, n = input().split(' ')
#         name = p.split('\\')[-1][-16:]
#         key = name + ' ' + n
#         if key in dic:
#             dic[key] += 1
#         else:
#             dic[key] = 1
# # except:
# #     raise
# except (EOFError, ValueError):
#     keys = list(dic)[-8:]
#     for k in keys:
#         print(k, dic[k])


# while True:
#     # 最高分是多少
#     try:
#         N, M = [int(each) for each in input().split()]
#         scores = [int(each) for each in input().split()]
#         operations = []
#
#         for i in range(M):
#             operations.append(input().split())
#         results = []
#         print(operations)
#         for each in operations:
#             if each[0] == 'U':
#                 scores[int(each[1]) - 1] = int(each[2])
#                 continue
#             else:
#                 front = min(int(each[1]), int(each[2]))
#                 back = max(int(each[1]), int(each[2]))
#                 max_ = 0
#                 for j in range(front - 1, back):
#                     if scores[j] > max_:
#                         max_ = scores[j]
#                 results.append(max_)
#         for each in results:
#             print(each)
#     except:
#         break


# def power(base, exponent):
#     result = 1
#     for i in range(exponent):
#         result *= base
#     return result
#
#
# while True:
#     try:
#         hex_num = str(input())
#         len_num = len(hex_num)
#         if hex_num[0] != "0":
#             print('------')
#             break
#         if hex_num[1].upper() != "X":
#             print('------')
#             break
#
#         for j in hex_num[2: len_num].upper():
#
#             if j not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'F']:
#                 print('-------------------')
#                 break
#         a = 0
#         sum_dict = {'A': "10", 'B': "11", 'C': '12', 'D': "13", 'E': "14", 'F': "15"}
#         hex_num = hex_num[2:]
#         len_num = len(hex_num)
#         for i in range(len_num):
#             if hex_num[i].upper() in sum_dict.keys():
#                 a += int(sum_dict.get(hex_num[i].upper())) * power(16, len_num - i - 1)
#             else:
#                 a += int(hex_num[i].upper()) * power(16, len_num - i - 1)
#         print(a)
#     except :
#         break

# while True:
#     # 明明的随机数
#     try:
#         line_num = int(input())
#         num = set()
#         for i in range(line_num):
#             num.add(int(input()))
#         for j in sorted(list(num)):
#             print(j)
#     except:
#         break


# while True:
#     # 汽水瓶子
#     try:
#         n = int(input())
#         if n == 0:
#             break
#         print(n//2)
#     except:
#         break
