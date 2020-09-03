# title: bulb-switcher-iii
# detail: https://leetcode.com/submissions/detail/386036654/
# datetime: Tue Aug 25 14:13:49 2020
# runtime: 872 ms
# memory: 20.5 MB

class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        m = 0
        l = 0
        result = 0
        for i in light:
            m = max(m, i)
            l += 1
            result += l == m
        return result
                