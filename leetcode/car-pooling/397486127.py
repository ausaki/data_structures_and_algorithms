# title: car-pooling
# detail: https://leetcode.com/submissions/detail/397486127/
# datetime: Fri Sep 18 22:42:45 2020
# runtime: 68 ms
# memory: 14.5 MB

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda k: k[1])
        q = []
        t = 0
        for p, s, e in trips:
            while q and q[0][0] <= s:
                t -= heapq.heappop(q)[1]
            t += p
            if t > capacity:
                return False
            heapq.heappush(q, (e, p))
        return True
            