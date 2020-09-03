# title: last-substring-in-lexicographical-order
# detail: https://leetcode.com/submissions/detail/375345391/
# datetime: Mon Aug  3 17:04:59 2020
# runtime: 540 ms
# memory: 33.1 MB

class Solution:
    def lastSubstring(self, s: str) -> str:
        N = len(s)
        dp = list(range(N))
        for i in reversed(range(N - 1)):
            start = dp[i + 1]
            if s[i] > s[start]:
                dp[i] = i
            elif s[i] < s[start]:
                dp[i] = start
            else:
                for j in range(1, min(start - i + 1, N - start)):
                    if s[i + j] > s[start + j]:
                        dp[i] = i
                        break
                    elif s[i + j] < s[start + j]:
                        dp[i] = start
                        break
                else:
                    dp[i] = i
        return s[dp[0]:]