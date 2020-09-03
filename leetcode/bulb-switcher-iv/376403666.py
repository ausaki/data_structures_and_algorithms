# title: bulb-switcher-iv
# detail: https://leetcode.com/submissions/detail/376403666/
# datetime: Wed Aug  5 16:55:33 2020
# runtime: 64 ms
# memory: 14.5 MB

class Solution:
    def minFlips(self, target: str) -> int:
        result = 0
        curr = '0'
        for c in target:
            if c != curr:
                if curr == '1':
                    result += 1
                else:
                    result += 1
                curr = c
        return result