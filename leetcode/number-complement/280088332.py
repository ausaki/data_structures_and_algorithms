# title: number-complement
# detail: https://leetcode.com/submissions/detail/280088332/
# datetime: Tue Nov 19 18:36:09 2019
# runtime: 28 ms
# memory: 12.6 MB

class Solution:
    def findComplement(self, num: int) -> int:
        old_num = num
        num = num | (num >> 1)
        num = num | (num >> 2)
        num = num | (num >> 4)
        num = num | (num >> 8)
        num = num | (num >> 16)
        
        return ~old_num & num
        