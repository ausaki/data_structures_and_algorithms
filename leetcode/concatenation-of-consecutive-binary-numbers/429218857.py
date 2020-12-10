# title: concatenation-of-consecutive-binary-numbers
# detail: https://leetcode.com/submissions/detail/429218857/
# datetime: Thu Dec 10 21:08:52 2020
# runtime: 1108 ms
# memory: 14 MB

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        res = 0
        for i in range(1, n + 1):
            j = i.bit_length()
            res = ((res << j) % MOD + i) % MOD
        return res