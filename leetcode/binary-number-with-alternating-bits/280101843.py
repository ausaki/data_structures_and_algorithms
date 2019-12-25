# title: binary-number-with-alternating-bits
# detail: https://leetcode.com/submissions/detail/280101843/
# datetime: Tue Nov 19 20:55:20 2019
# runtime: 28 ms
# memory: 12.7 MB

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        m = n ^ (n >> 1)
        return (m & (m + 1)) == 0
        