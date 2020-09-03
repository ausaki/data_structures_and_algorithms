# title: minimum-value-to-get-positive-step-by-step-sum
# detail: https://leetcode.com/submissions/detail/383619190/
# datetime: Thu Aug 20 15:42:47 2020
# runtime: 28 ms
# memory: 13.9 MB

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        m = 0
        s = 0
        for n in nums:
            s += n
            m = min(m, s)
        return 1 - m