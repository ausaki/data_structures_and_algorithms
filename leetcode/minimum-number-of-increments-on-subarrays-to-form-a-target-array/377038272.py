# title: minimum-number-of-increments-on-subarrays-to-form-a-target-array
# detail: https://leetcode.com/submissions/detail/377038272/
# datetime: Fri Aug  7 00:27:24 2020
# runtime: 1388 ms
# memory: 24.3 MB

import bisect
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        target.append(0)
        n = len(target)
        result = 0
        left_low = 0
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
            result += peek - max(left_low, right_low)
            if right_low < left_low:
                result += left_low - right_low
                left_low = right_low
        return result