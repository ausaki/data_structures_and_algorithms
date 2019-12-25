# title: partition-equal-subset-sum
# detail: https://leetcode.com/submissions/detail/285602053/
# datetime: Fri Dec 13 10:53:25 2019
# runtime: 192 ms
# memory: 13.3 MB

from functools import lru_cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        S = sum(nums)
        if S % 2:
            return False
        dp = {0}
        target = S // 2
        for num in nums:
            dp |= {num + val for val in dp}
            if target in dp:
                return True
        return False