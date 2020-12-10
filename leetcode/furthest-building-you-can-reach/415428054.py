# title: furthest-building-you-can-reach
# detail: https://leetcode.com/submissions/detail/415428054/
# datetime: Sun Nov  1 11:03:35 2020
# runtime: 544 ms
# memory: 29.1 MB

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        diffs = 0
        q = []
        sq = 0
        k = 0
        for i in range(1, len(heights)):
            d = heights[i] - heights[i - 1]
            if d <= 0:
                k = i
                continue
            if len(q) < ladders:
                heapq.heappush(q, d)
            elif q and d > q[0]:
                diffs += heapq.heappushpop(q, d)
            else:
                diffs += d
            if diffs <= bricks:
                k = i
            else:
                break
        return k
            