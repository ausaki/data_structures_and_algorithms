# title: palindromic-substrings
# detail: https://leetcode.com/submissions/detail/276763641/
# datetime: Thu Nov  7 17:36:52 2019
# runtime: 336 ms
# memory: 21.4 MB

class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        dp = [[0 for i in range(N)] for i in range(N)]
        count = 0
        for i in reversed(range(N)):
            for j in range(i, N):
                if i == j:
                    dp[i][j] = 1
                    count += 1
                elif j == i + 1:
                    if s[i] == s[j]:
                        dp[i][j] = 1
                        count += 1
                else:
                    if s[i] == s[j] and dp[i + 1][j - 1]:
                        dp[i][j] = 1
                        count += 1
        return count
                    