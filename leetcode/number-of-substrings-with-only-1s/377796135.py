# title: number-of-substrings-with-only-1s
# detail: https://leetcode.com/submissions/detail/377796135/
# datetime: Sat Aug  8 17:08:21 2020
# runtime: 76 ms
# memory: 14.3 MB

class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        s += '0'
        result = 0
        l = -1
        for i, bit in enumerate(s):
            if bit == '0':
                if l != -1:
                    result = (result + (i - l) * (i - l + 1) // 2) % MOD
                    l = -1
                continue
            if l == -1:
                l = i
        return result
            