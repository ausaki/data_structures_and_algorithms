# title: maximum-number-of-coins-you-can-get
# detail: https://leetcode.com/submissions/detail/387608519/
# datetime: Fri Aug 28 23:17:36 2020
# runtime: 844 ms
# memory: 22.4 MB

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        heapq.heapify(piles)
        for i in range(n // 3):
            heapq.heappop(piles)
        result = 0
        while piles:
            result += heapq.heappop(piles)
            heapq.heappop(piles)
        return result
            