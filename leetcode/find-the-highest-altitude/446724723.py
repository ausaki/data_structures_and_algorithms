# title: find-the-highest-altitude
# detail: https://leetcode.com/submissions/detail/446724723/
# datetime: Sat Jan 23 22:33:35 2021
# runtime: 32 ms
# memory: 14.3 MB

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0
        res = 0
        for g in gain:
            curr += g
            res = max(res, curr)
        return res