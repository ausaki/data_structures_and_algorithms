# title: maximum-number-of-coins-you-can-get
# detail: https://leetcode.com/submissions/detail/387607412/
# datetime: Fri Aug 28 23:14:31 2020
# runtime: 636 ms
# memory: 26.3 MB

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        return sum(piles[n // 3:n:2])
            