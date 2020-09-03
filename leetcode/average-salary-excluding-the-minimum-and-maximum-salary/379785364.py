# title: average-salary-excluding-the-minimum-and-maximum-salary
# detail: https://leetcode.com/submissions/detail/379785364/
# datetime: Wed Aug 12 16:17:44 2020
# runtime: 32 ms
# memory: 13.8 MB

class Solution:
    def average(self, salary: List[int]) -> float:
        total = 0
        mi, ma = 10 ** 6, 0
        for s in salary:
            total += s
            if s < mi: mi = s
            if s > ma: ma = s
        return (total - mi - ma) / (len(salary) - 2)