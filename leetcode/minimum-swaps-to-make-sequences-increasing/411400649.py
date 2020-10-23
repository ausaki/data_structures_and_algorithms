# title: minimum-swaps-to-make-sequences-increasing
# detail: https://leetcode.com/submissions/detail/411400649/
# datetime: Wed Oct 21 16:50:06 2020
# runtime: 104 ms
# memory: 17.4 MB

class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        @lru_cache(None)
        def dp(i, j):
            if i == n:
                return 0
            a, b = (A[i - 1], B[i - 1]) if i else (-1, -1)
            if j:
                a, b = b, a
            result = n
            if A[i] > a and B[i] > b:
                result = min(result, dp(i + 1, 0))
            if B[i] > a and A[i] > b:
                result = min(result, 1 + dp(i + 1, 1))
            return result
        
        n = len(A)
        return dp(0, 0)