# title: ugly-number-ii
# detail: https://leetcode.com/submissions/detail/281043584/
# datetime: Sat Nov 23 19:45:11 2019
# runtime: 400 ms
# memory: 12.8 MB

import bisect
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        arr = [1]
        index = {2: 0, 3: 0, 5: 0}
        while len(arr) < n:
            mi = 2
            mv = 1 << 32
            values = [[k, arr[i] * k] for k, i in index.items()]
            mv = min(values, key = lambda item: item[1])
            for k, v in values:
                if v == mv[1]:
                    index[k] += 1
            arr.append(mv[1])
        return arr[-1]
                    
            
            
        
        