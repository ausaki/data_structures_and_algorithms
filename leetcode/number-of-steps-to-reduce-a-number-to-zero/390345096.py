# title: number-of-steps-to-reduce-a-number-to-zero
# detail: https://leetcode.com/submissions/detail/390345096/
# datetime: Thu Sep  3 14:30:28 2020
# runtime: 24 ms
# memory: 14 MB

class Solution:
    def numberOfSteps (self, num: int) -> int:
        b = bin(num)
        return len(b) - 3 + b.count('1')