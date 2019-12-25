# title: teemo-attacking
# detail: https://leetcode.com/submissions/detail/286555945/
# datetime: Tue Dec 17 13:29:30 2019
# runtime: 260 ms
# memory: 14 MB

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        start = 0
        end = 0
        res = 0
        for tp in timeSeries:
            if tp > end:
                res += end - start
                start = tp
                end = tp + duration
            else:
                end = tp + duration
        return res + end - start
