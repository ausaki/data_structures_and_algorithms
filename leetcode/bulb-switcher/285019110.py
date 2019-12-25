# title: bulb-switcher
# detail: https://leetcode.com/submissions/detail/285019110/
# datetime: Tue Dec 10 20:52:22 2019
# runtime: 32 ms
# memory: 12.7 MB

class Solution:
    def bulbSwitch(self, n: int) -> int:
        res = 0
        i = 1
        while i ** 2 <= n:
            res += 1
            i += 1
        return res