# title: last-stone-weight
# detail: https://leetcode.com/submissions/detail/399729603/
# datetime: Thu Sep 24 00:29:58 2020
# runtime: 20 ms
# memory: 14 MB

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            a, b = heapq.heappop(stones), heapq.heappop(stones)
            a -= b
            if a != 0:
                heapq.heappush(stones, a)
        return -stones[0] if stones else 0