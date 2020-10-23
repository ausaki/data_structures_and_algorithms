# title: rotated-digits
# detail: https://leetcode.com/submissions/detail/412112768/
# datetime: Fri Oct 23 11:36:16 2020
# runtime: 84 ms
# memory: 14.1 MB

class Solution:
    def rotatedDigits(self, N: int) -> int:
        result = 0
        s1 = set('2569')
        s2 = set('347')
        for i in range(1, N + 1):
            s = set(str(i))
            if s & s1 and not s & s2:
                result += 1
        return result