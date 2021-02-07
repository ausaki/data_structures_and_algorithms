# title: maximum-absolute-sum-of-any-subarray
# detail: https://leetcode.com/submissions/detail/452745129/
# datetime: Sat Feb  6 22:41:16 2021
# runtime: 464 ms
# memory: 28.5 MB

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_sum, max_sum = math.inf, -math.inf
        s1, s2 = 0, 0
        for i in nums:
            if s1 > 0:
                s1 += i
            else:
                s1 = i
            if s2 < 0:
                s2 += i
            else:
                s2 = i
            max_sum = max(max_sum, s1)
            min_sum = min(min_sum, s2)
        return max(abs(min_sum), abs(max_sum), 0)