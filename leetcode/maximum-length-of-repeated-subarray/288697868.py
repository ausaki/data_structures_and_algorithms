# title: maximum-length-of-repeated-subarray
# detail: https://leetcode.com/submissions/detail/288697868/
# datetime: Thu Dec 26 21:26:46 2019
# runtime: 3544 ms
# memory: 12.9 MB

from functools import lru_cache
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        N = len(A)
        M = len(B)
        cache = collections.defaultdict(list)
        for j in range(N):
            cache[B[j]].append(j)
        dp = {}
        res = 0
        for i in range(N):
            new_dp = {}
            for j in cache[A[i]]:
                if j - 1 in dp:
                    new_dp[j] = dp[j - 1] + 1
                    res = max(res, dp[j - 1] + 1)
                else:
                    new_dp[j] = 1
                    res = max(res, 1)
            dp = new_dp
        return res