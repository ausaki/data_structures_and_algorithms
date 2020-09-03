# title: maximum-number-of-non-overlapping-subarrays-with-sum-equals-target
# detail: https://leetcode.com/submissions/detail/378747231/
# datetime: Mon Aug 10 14:23:29 2020
# runtime: 644 ms
# memory: 21.2 MB

class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        prefix_sum = {0, }
        prev_sum = 0
        result = 0
        for num in nums:
            prev_sum += num
            left = prev_sum - target
            if left in prefix_sum:
                result += 1
                prefix_sum.clear()
                prev_sum = 0
                prefix_sum.add(0)
            else:
                prefix_sum.add(prev_sum)
        return result