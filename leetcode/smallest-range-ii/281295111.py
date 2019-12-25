# title: smallest-range-ii
# detail: https://leetcode.com/submissions/detail/281295111/
# datetime: Sun Nov 24 19:09:01 2019
# runtime: 172 ms
# memory: 14 MB

class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A = sorted(A)
        N = len(A)
        mi, ma = A[0], A[-1]
        ans = ma - mi
        for i in range(N - 1):
            a, b = A[i], A[i+1]
            ans = min(ans, max(ma-K, a+K) - min(mi+K, b-K))
        return ans