# title: maximum-length-of-repeated-subarray
# detail: https://leetcode.com/submissions/detail/288709341/
# datetime: Thu Dec 26 22:52:24 2019
# runtime: 3004 ms
# memory: 12.7 MB

from functools import lru_cache
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        N = len(A)
        M = len(B)
        cache = collections.defaultdict(list)
        for j in range(M):
            cache[B[j]].append(j)
        dp = {}
        res = 0
        for i in range(N):
            new_dp = {}
            for j in cache[A[i]]:
                new_dp[j] = 1 + dp.get(j - 1, 0)
                res = max(res, new_dp[j])
            dp = new_dp
        return res