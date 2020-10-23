# title: minimum-swaps-to-make-sequences-increasing
# detail: https://leetcode.com/submissions/detail/411493418/
# datetime: Wed Oct 21 23:36:50 2020
# runtime: 96 ms
# memory: 14.3 MB

class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        dp = [0, 0]
        for i in range(n - 1, -1, -1):
            dp2 = [n, n]
            for j in range(2):
                a, b = (A[i - 1], B[i - 1]) if i else (-1, -1)
                if j:
                    a, b = b, a
                if A[i] > a and B[i] > b:
                    dp2[j] = min(dp2[j], dp[0])
                if B[i] > a and A[i] > b:
                    dp2[j] = min(dp2[j], 1 + dp[1])
            dp = dp2
        return dp[0]