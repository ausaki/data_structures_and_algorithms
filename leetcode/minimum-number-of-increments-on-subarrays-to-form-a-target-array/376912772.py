# title: minimum-number-of-increments-on-subarrays-to-form-a-target-array
# detail: https://leetcode.com/submissions/detail/376912772/
# datetime: Thu Aug  6 17:47:27 2020
# runtime: 7124 ms
# memory: 37.8 MB

import bisect

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        sorted_target = sorted(zip(target, range(n)))
        parts = [n]
        levels = {n: 0}
        result = 0
        i = 0
        while i < n:
            t, j = sorted_target[i]            
            k = bisect.bisect(parts, j)
            # print(parts)
            # print(k)
            result += t - max(levels[parts[k - 1]], levels[parts[k]])
            parts.insert(k, j)
            levels[j] = t
            i += 1
        return result