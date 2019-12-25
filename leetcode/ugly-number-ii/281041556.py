# title: ugly-number-ii
# detail: https://leetcode.com/submissions/detail/281041556/
# datetime: Sat Nov 23 19:22:17 2019
# runtime: 280 ms
# memory: 13 MB

import bisect
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        arr = [1]
        index = {2: -1, 3: -1, 5: -1}
        while len(arr) < n:
            mi = 2
            mv = 1 << 32
            for k, i in index.items():
                i += 1
                v = arr[i] * k
                while v <= arr[-1]:
                    i += 1
                    v = arr[i] * k
                index[k] = i - 1
                if v < mv:
                    mi = k
                    mv = v
            index[mi] += 1
            arr.append(arr[index[mi]] * mi)
        # print(arr)
        return arr[-1]
                    
            
            
        
        