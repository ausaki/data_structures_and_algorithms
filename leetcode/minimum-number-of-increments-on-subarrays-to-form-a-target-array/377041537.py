# title: minimum-number-of-increments-on-subarrays-to-form-a-target-array
# detail: https://leetcode.com/submissions/detail/377041537/
# datetime: Fri Aug  7 00:35:51 2020
# runtime: 1196 ms
# memory: 24.5 MB

import bisect
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        target.append(0)
        n = len(target)
        result = 0
        right_low = 0
        peek = 0
        i = 1
        while i < n:
            while i < n and target[i] >= target[i - 1]:
                i += 1
            peek = target[i - 1]
            while i < n and target[i] <= target[i - 1]:
                i += 1
            right_low = target[i - 1]
            result += peek - right_low
        return result