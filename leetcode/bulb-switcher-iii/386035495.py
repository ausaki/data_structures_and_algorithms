# title: bulb-switcher-iii
# detail: https://leetcode.com/submissions/detail/386035495/
# datetime: Tue Aug 25 14:11:02 2020
# runtime: 416 ms
# memory: 20.3 MB

class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        m = 0
        l = 0
        result = 0
        for i in light:
            if i > m:
                m = i
            l += 1
            if l == m:
                result += 1
        return result
                