# title: maximize-palindrome-length-from-subsequences
# detail: https://leetcode.com/submissions/detail/458664824/
# datetime: Sun Feb 21 12:28:56 2021
# runtime: 4472 ms
# memory: 650.5 MB

'''
我一开始就想到了将 word1 和 word2 连接起来, 然后使用 dp 求解最长回文子序列.
但是一直没想明白如何保证这个最长回文子序列是同时包括  word1 和 word2 的子序列的.

看了一下题目的提示才豁然开朗, 首先对比每对 word1[i] 和 word2[j], 如果两者相等, 则使用 dp 求解 [i + 1, j - 1] 之间的最长回文子序列.
'''
class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s = word1 + word2
        n = len(word1)
        m = len(word2)
        # dp = [[0] for i in range(len(s))]
        # for 
        
        @lru_cache(None)
        def dp(i, j):
            if i > j:
                return 0
            if i == j:
                return 1
            if s[i] == s[j]:
                return 2 + dp(i + 1, j - 1)
            l1 = dp(i + 1, j)
            l2 = dp(i, j - 1)
            return max(l1, l2)
        
        res = 0
        for i in range(n):
            for j in reversed(range(m)):
                if word1[i] == word2[j]:
                    res = max(res, 2 + dp(i + 1, n + j - 1))
                    break
        return res