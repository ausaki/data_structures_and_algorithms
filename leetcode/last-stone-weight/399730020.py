# title: last-stone-weight
# detail: https://leetcode.com/submissions/detail/399730020/
# datetime: Thu Sep 24 00:31:14 2020
# runtime: 32 ms
# memory: 13.8 MB

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i, j in enumerate(stones):
            stones[i] = -j
        heapq.heapify(stones)
        while len(stones) > 1:
            a, b = heapq.heappop(stones), heapq.heappop(stones)
            a -= b
            if a != 0:
                heapq.heappush(stones, a)
        return -stones[0] if stones else 0