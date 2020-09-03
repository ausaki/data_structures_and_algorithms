# title: bulb-switcher-iii
# detail: https://leetcode.com/submissions/detail/386035151/
# datetime: Tue Aug 25 14:10:12 2020
# runtime: 500 ms
# memory: 20.2 MB

class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        m = 0
        l = 0
        result = 0
        for i in light:
            if i > m:
                m = i
                l += 1
            else:
                l += 1
            if l == m:
                result += 1
        return result
                