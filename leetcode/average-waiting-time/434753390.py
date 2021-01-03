# title: average-waiting-time
# detail: https://leetcode.com/submissions/detail/434753390/
# datetime: Sat Dec 26 22:44:48 2020
# runtime: 932 ms
# memory: 55.1 MB

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        res = 0
        t = -1
        for a, b in customers:
            if t >= a:
                res += t + b - a
                t += b
            else:
                t = a + b
                res += b
        return res / len(customers)