# title: binary-gap
# detail: https://leetcode.com/submissions/detail/406593535/
# datetime: Fri Oct  9 23:36:46 2020
# runtime: 28 ms
# memory: 14.1 MB

class Solution:
    def binaryGap(self, n: int) -> int:
        b = bin(n)[2:]
        k = 30
        result = 0
        for i, j in enumerate(b):
            if j == '1':
                result = max(result, i - k)
                k = i
        return result