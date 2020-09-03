# title: maximum-number-of-coins-you-can-get
# detail: https://leetcode.com/submissions/detail/387607806/
# datetime: Fri Aug 28 23:15:34 2020
# runtime: 632 ms
# memory: 26.2 MB

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        return sum(piles[i] for i in range(n // 3, n, 2))
            