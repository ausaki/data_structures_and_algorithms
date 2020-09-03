# title: delete-and-earn
# detail: https://leetcode.com/submissions/detail/290165092/
# datetime: Wed Jan  1 11:01:54 2020
# runtime: 56 ms
# memory: 13.7 MB

from functools import lru_cache
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(i):
            if i < 0:
                return 0
            if i - 1 >= 0 and nums[i - 1] == nums[i] - 1:
                a = nums[i] * counter[nums[i]] + dfs(i - 2)
                b = dfs(i - 1)
                return max(a, b)
            return nums[i] * counter[nums[i]] + dfs(i - 1)        
        counter = collections.Counter(nums)
        nums = sorted(counter.keys())
        return dfs(len(nums) - 1)