# title: maximum-number-of-coins-you-can-get
# detail: https://leetcode.com/submissions/detail/387608608/
# datetime: Fri Aug 28 23:17:49 2020
# runtime: 796 ms
# memory: 22.2 MB

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        heapq.heapify(piles)
        for i in range(n // 3):
            heapq.heappop(piles)
        result = 0
        while piles:
            result += heapq.heappop(piles)
            heapq.heappop(piles)
        return result
            