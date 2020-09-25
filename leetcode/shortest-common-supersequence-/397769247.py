# title: shortest-common-supersequence-
# detail: https://leetcode.com/submissions/detail/397769247/
# datetime: Sat Sep 19 16:08:04 2020
# runtime: 840 ms
# memory: 144.5 MB

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        @lru_cache(None)
        def dp(i, j):
            if i == m or j == n:
                return 0
            if str1[i] == str2[j]:
                return 1 + dp(i + 1, j + 1)
            return max(dp(i + 1, j), dp(i, j + 1))
        dp(0, 0)
        i = 0
        j = 0
        result = ''
        while i < m and j < n:
            if str1[i] == str2[j]:
                result += str1[i]
                i += 1
                j += 1
            else:
                s1 = dp(i + 1, j)
                s2 = dp(i, j + 1)
                if s1 > s2:
                    result += str1[i]
                    i += 1
                else:
                    result += str2[j]
                    j += 1
        if i < m:
            result += str1[i:]
        if j < n:
            result += str2[j:]
        return result