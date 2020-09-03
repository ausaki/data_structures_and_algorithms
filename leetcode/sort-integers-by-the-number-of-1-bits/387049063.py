# title: sort-integers-by-the-number-of-1-bits
# detail: https://leetcode.com/submissions/detail/387049063/
# datetime: Thu Aug 27 16:57:33 2020
# runtime: 76 ms
# memory: 14.1 MB

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def countbits(x):
            y = x
            cnt = 0
            while x:
                cnt += 1
                x &= x - 1
            return cnt, y
        
        arr.sort(key=countbits)
        return arr