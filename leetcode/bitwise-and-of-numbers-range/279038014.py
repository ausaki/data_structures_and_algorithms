# title: bitwise-and-of-numbers-range
# detail: https://leetcode.com/submissions/detail/279038014/
# datetime: Fri Nov 15 23:36:52 2019
# runtime: 44 ms
# memory: 12.6 MB

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while n > m:
            n &= n - 1
        return n
        