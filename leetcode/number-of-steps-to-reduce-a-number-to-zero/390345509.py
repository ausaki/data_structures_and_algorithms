# title: number-of-steps-to-reduce-a-number-to-zero
# detail: https://leetcode.com/submissions/detail/390345509/
# datetime: Thu Sep  3 14:31:26 2020
# runtime: 28 ms
# memory: 14 MB

class Solution:
    def numberOfSteps (self, num: int) -> int:
        cnt = 0
        while num:
            if num & 1:
                num -= 1
            else:
                num >>= 1
            cnt += 1
        return cnt