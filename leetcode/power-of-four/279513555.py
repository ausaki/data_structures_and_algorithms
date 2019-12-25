# title: power-of-four
# detail: https://leetcode.com/submissions/detail/279513555/
# datetime: Sun Nov 17 17:59:56 2019
# runtime: 28 ms
# memory: 12.8 MB

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        for i in range(16):
            if 1 << (2 * i) == num:
                return True
        return False
        