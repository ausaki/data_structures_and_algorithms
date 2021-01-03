# title: maximum-number-of-eaten-apples
# detail: https://leetcode.com/submissions/detail/434981642/
# datetime: Sun Dec 27 10:57:25 2020
# runtime: 736 ms
# memory: 18.8 MB

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        res = 0
        q = []
        for i, (a, d) in enumerate(zip(apples, days)):
            while q and q[0][0] <= i:
                heapq.heappop(q)
            if a > 0:
                heapq.heappush(q, [i + d, a])
            if q:
                p = heapq.heappop(q)
                p[1] -= 1
                res += 1
                if p[1] > 0:
                    heapq.heappush(q, p)
        # print(res)
        # print(q)
        i = len(apples)
        while q:
            p = heapq.heappop(q)
            if p[0] <= i:
                continue
            res += min(p[0] - i, p[1])
            i += min(p[0] - i, p[1])
        return res