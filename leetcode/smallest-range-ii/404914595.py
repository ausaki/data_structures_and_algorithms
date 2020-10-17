# title: smallest-range-ii
# detail: https://leetcode.com/submissions/detail/404914595/
# datetime: Tue Oct  6 02:16:09 2020
# runtime: 156 ms
# memory: 15.2 MB

class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        res = A[-1] - A[0]
        right_max = A[-1] - K
        for i in range(len(A) - 2, -1, -1):
            a = A[i]
            res = min(res, max(a + K, right_max)- min(A[0] + K, A[i + 1] - K))
            if a + K <= A[i + 1] - K:
                break
        return res    