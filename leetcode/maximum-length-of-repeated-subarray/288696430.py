# title: maximum-length-of-repeated-subarray
# detail: https://leetcode.com/submissions/detail/288696430/
# datetime: Thu Dec 26 21:15:32 2019
# runtime: 6220 ms
# memory: 12.7 MB

from functools import lru_cache
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        N = len(A)
        M = len(B)
        dp = {i - 1: 0 for i in range(M)}
        res = 0
        for i in range(N):
            new_dp = {}
            for j, k in dp.items():
                if j + 1 < M and A[i] == B[j + 1]:
                    new_dp[j + 1] = k + 1
                    res = max(res, k + 1)
            for j in range(M):
                if A[i] == B[j]:
                    new_dp.setdefault(j, 1)
                    res = max(res, 1)
            dp = new_dp
        return res