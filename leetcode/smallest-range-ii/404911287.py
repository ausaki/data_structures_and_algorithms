# title: smallest-range-ii
# detail: https://leetcode.com/submissions/detail/404911287/
# datetime: Tue Oct  6 02:07:30 2020
# runtime: 152 ms
# memory: 15.3 MB

class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        res = A[-1] - A[0]
        last = A[-1] - K
        right_max = last
        for i in range(len(A) - 2, -1, -1):
            a = A[i]
            if a + K <= last:
                res = min(res, right_max - A[0] - K)
                break
            else:
                res = min(res, max(a + K, right_max)- min(A[0] + K, last))
                last = a - K
        return res    