# title: partition-array-for-maximum-sum
# detail: https://leetcode.com/submissions/detail/400025367/
# datetime: Thu Sep 24 15:09:36 2020
# runtime: 552 ms
# memory: 15.4 MB

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k == n: return n * max(arr)
        @lru_cache(None)
        def dfs(i):
            if i == n:
                return 0
            m = 0
            result = 0
            for j in range(min(k, n - i)):
                m = max(m, arr[i + j])
                result = max(result, m * (j + 1) + dfs(i + j + 1))
            return result
        return dfs(0)