# title: minimum-number-of-increments-on-subarrays-to-form-a-target-array
# detail: https://leetcode.com/submissions/detail/377047837/
# datetime: Fri Aug  7 00:52:19 2020
# runtime: 1120 ms
# memory: 24.3 MB

import bisect
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        target.append(0)
        return sum(target[i - 1] - target[i] for i in range(1, len(target)) if target[i] <= target[i - 1])
        
