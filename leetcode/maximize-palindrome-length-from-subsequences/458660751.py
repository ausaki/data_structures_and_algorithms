# title: maximize-palindrome-length-from-subsequences
# detail: https://leetcode.com/submissions/detail/458660751/
# datetime: Sun Feb 21 12:19:02 2021
# runtime: 3772 ms
# memory: 745.1 MB

class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s = word1 + word2
        n = len(word1)
        m = len(word2)
        
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
            for j in range(m):
                if word1[i] == word2[j]:
                    res = max(res, 2 + dp(i + 1, n + j - 1))
        return res