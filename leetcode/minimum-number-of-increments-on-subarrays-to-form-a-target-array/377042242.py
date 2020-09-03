# title: minimum-number-of-increments-on-subarrays-to-form-a-target-array
# detail: https://leetcode.com/submissions/detail/377042242/
# datetime: Fri Aug  7 00:37:36 2020
# runtime: 924 ms
# memory: 24.4 MB

import bisect
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        target.append(0)
        n = len(target)
        result = 0
        i = 1
        while i < n:
            while i < n and target[i] >= target[i - 1]:
                i += 1
            peek = target[i - 1]
            while i < n and target[i] <= target[i - 1]:
                i += 1
            result += peek - target[i - 1]
        return result