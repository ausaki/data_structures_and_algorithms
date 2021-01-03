# title: average-waiting-time
# detail: https://leetcode.com/submissions/detail/434785535/
# datetime: Sun Dec 27 00:05:59 2020
# runtime: 1668 ms
# memory: 55.1 MB

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        res = 0
        t = -1
        for a, b in customers:
            t = max(t, a) + b
            res += t - a
        return res / len(customers)