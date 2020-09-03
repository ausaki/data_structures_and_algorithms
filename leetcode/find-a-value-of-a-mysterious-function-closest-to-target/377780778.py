# title: find-a-value-of-a-mysterious-function-closest-to-target
# detail: https://leetcode.com/submissions/detail/377780778/
# datetime: Sat Aug  8 16:12:04 2020
# runtime: 760 ms
# memory: 28.5 MB

import collections
import bisect

class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        if target == 0 or target in arr: return 0
        
        minValue = float("+Inf")
        arr = list(set(arr))
            
        for i in range(len(arr)):
            temp = arr[i]
            oldValue = float("Inf")
            for j in range(i, len(arr)):
                temp = temp & arr[j]        
                            
                if abs(temp - target) > oldValue:
                    break
                
                minValue = min(minValue, abs(temp - target))
                
                
                if minValue == 0: return 0
                oldValue = abs(temp - target)
        
        return minValue
        
                
                    