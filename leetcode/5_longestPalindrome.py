from self import self


# 中心扩散法
class Solution:
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]


# 动态规划法
# class Solution:
#     def longestPalindrome(self, string: str) -> str:
#         length = len(string)
#         if length < 2:
#             return string
#         max_len = 1
#         begin = 0
#         dp = [[False] * length for _ in range(length)]
#         for i in range(length):
#             dp[i][i] = True
#         # 递推开始
#         # 先枚举字串长度
#         for L in range(2, length + 1):
#             for i in range(length):
#                 j = i + L - 1
#                 if j >= length:
#                     break
#                 if string[i] != string[j]:
#                     dp[i][j] = False
#                 else:
#                     if j - i < 3:
#                         dp[i][j] = True
#                     else:
#                         dp[i][j] = dp[i + 1][j - 1]
#
#                 if dp[i][j] and j - i + 1 > max_len:
#                     max_len = j - i + 1
#                     begin = i
#         return string[begin:begin + max_len]


# 暴力解法
# class Solution:
#     def longestPalindrome(self, string: str) -> str:
#         def check(s: str) -> bool:
#             return s == s[::-1]
#
#         max_length = len(string)
#         length = len(string)
#         while max_length > 0:
#             for i in range(length - max_length + 1):
#                 if check(string[i:i + max_length]):
#                     return string[i:i + max_length]
#             max_length -= 1


s1 = "bacad"
M = Solution
print(M.longestPalindrome(self, s1))
