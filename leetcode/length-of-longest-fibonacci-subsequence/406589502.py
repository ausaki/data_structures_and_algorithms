# title: length-of-longest-fibonacci-subsequence
# detail: https://leetcode.com/submissions/detail/406589502/
# datetime: Fri Oct  9 23:22:29 2020
# runtime: 1128 ms
# memory: 33.2 MB

class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        dp = [{} for i in range(n)]
        result = 0
        for i in range(n):
            for j in range(i):
                prev = A[i] - A[j]
                if prev in dp[j]:
                    l = dp[i][A[j]] = dp[j][prev] + 1
                    result = max(result, l)
                else:
                    dp[i][A[j]] = 2
        return result