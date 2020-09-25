# title: shortest-common-supersequence-
# detail: https://leetcode.com/submissions/detail/397779321/
# datetime: Sat Sep 19 16:47:33 2020
# runtime: 528 ms
# memory: 22.2 MB

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[0 for j in range(n)] for i in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if str1[i] == str2[j]:
                    dp[i][j] = 1 + (dp[i + 1][j + 1] if i + 1 < m and j + 1 < n else 0)
                else:
                    dp[i][j] = max(dp[i + 1][j] if i + 1 < m else 0, dp[i][j + 1] if j + 1 < n else 0)
        i = 0
        j = 0
        result = ''
        while i < m and j < n:
            if str1[i] == str2[j]:
                result += str1[i]
                i += 1
                j += 1
            else:
                s1 = dp[i + 1][j] if i + 1 < m else 0
                s2 = dp[i][j + 1] if j + 1 < n else 0
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