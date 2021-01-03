# title: average-waiting-time
# detail: https://leetcode.com/submissions/detail/434785061/
# datetime: Sun Dec 27 00:04:28 2020
# runtime: 1240 ms
# memory: 55 MB

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        res = 0
        t = -1
        for a, b in customers:
            if t >= a:
                t += b
            else:
                t = a + b
            res += t - a
        return res / len(customers)