# title: binary-watch
# detail: https://leetcode.com/submissions/detail/279834139/
# datetime: Mon Nov 18 22:43:58 2019
# runtime: 20 ms
# memory: 12.8 MB

from itertools import combinations

class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        result = []
        for com in combinations(range(10), num):
            n = 0
            for i in com:
                n |= 1 << i
            h = n >> 6
            m = n & 0x003f
            if h < 12 and m < 60:
                result.append('{}:{:02d}'.format(h, m)) 
        return result
             
                