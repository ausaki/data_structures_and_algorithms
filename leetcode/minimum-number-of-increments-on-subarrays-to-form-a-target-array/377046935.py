# title: minimum-number-of-increments-on-subarrays-to-form-a-target-array
# detail: https://leetcode.com/submissions/detail/377046935/
# datetime: Fri Aug  7 00:49:58 2020
# runtime: 880 ms
# memory: 24.5 MB

import bisect
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        target.append(0)
        n = len(target)
        result = 0
        for i in range(1, n):
            if target[i] <= target[i - 1]:
                result += target[i - 1] - target[i]
        return result
