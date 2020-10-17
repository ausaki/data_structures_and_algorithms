# title: smallest-range-i
# detail: https://leetcode.com/submissions/detail/404838876/
# datetime: Mon Oct  5 22:35:36 2020
# runtime: 112 ms
# memory: 15.4 MB

class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        a, b = min(A), max(A)
        if a + K >= b - K:
            return 0
        return (b - K) - (a + K)