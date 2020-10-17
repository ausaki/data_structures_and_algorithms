# title: smallest-range-i
# detail: https://leetcode.com/submissions/detail/404841889/
# datetime: Mon Oct  5 22:45:30 2020
# runtime: 116 ms
# memory: 15.3 MB

class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        return max(max(A) - min(A) - 2 * K, 0)