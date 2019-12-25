# title: power-of-four
# detail: https://leetcode.com/submissions/detail/279514538/
# datetime: Sun Nov 17 18:09:14 2019
# runtime: 32 ms
# memory: 12.8 MB

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        # for i in range(16):
        #     if 1 << (2 * i) == num:
        #         return True
        # return False
        return num > 0 and (num & (num - 1)) == 0 and (num & 0x55555555) != 0