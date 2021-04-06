# title: maximum-average-pass-ratio
# detail: https://leetcode.com/submissions/detail/467515531/
# datetime: Sun Mar 14 12:28:45 2021
# runtime: 3992 ms
# memory: 64 MB

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        s = 0
        maxd = 0
        q = []
        for p, t in classes:
            heapq.heappush(q, (-(t - p) / (t * (t + 1)), p, t))
            s += p / t
        for i in range(extraStudents):
            d, p, t = heapq.heappop(q)
            p += 1
            t += 1
            heapq.heappush(q, (-(t - p) / (t * (t + 1)), p, t))
            s += -d
        return s / len(classes)