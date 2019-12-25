# title: rotate-function
# detail: https://leetcode.com/submissions/detail/285439510/
# datetime: Thu Dec 12 15:34:21 2019
# runtime: 88 ms
# memory: 14.6 MB

class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        N = len(A)
        prefix_sum = []
        F0 = 0
        curr = 0
        for i, num in enumerate(A):
            curr += num
            prefix_sum.append(curr)
            F0 += i * num
        res = F0
        for i in range(1, N):
            Fi = F0 + prefix_sum[N - i - 1] * i - (prefix_sum[N - 1] - prefix_sum[N - i - 1]) * (N - i)
            res = max(res, Fi)
        return res