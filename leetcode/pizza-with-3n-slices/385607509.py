# title: pizza-with-3n-slices
# detail: https://leetcode.com/submissions/detail/385607509/
# datetime: Mon Aug 24 18:14:25 2020
# runtime: 280 ms
# memory: 13.8 MB

class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices)
        k = n // 3
        dp1 = collections.deque([[0] * (k + 1) for i in range(2)])
        dp2 = collections.deque([[0] * (k + 1) for i in range(2)])
        for i in range(n - 2, -1, -1):
            new_dp1 = [0] * (k + 1)
            new_dp2 = [0] * (k + 1)
            for j in range(1, k + 1):
                new_dp1[j] = max(dp1[0][j], slices[i] + dp1[1][j - 1])
                new_dp2[j] = max(dp2[0][j], slices[i + 1] + dp2[1][j - 1])
            dp1.pop()
            dp1.appendleft(new_dp1)
            dp2.pop()
            dp2.appendleft(new_dp2)
        return max(dp1[0][k], dp2[0][k])
