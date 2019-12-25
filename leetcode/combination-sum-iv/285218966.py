# title: combination-sum-iv
# detail: https://leetcode.com/submissions/detail/285218966/
# datetime: Wed Dec 11 16:06:41 2019
# runtime: 36 ms
# memory: 17.6 MB

from functools import lru_cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = []
        @lru_cache(None)
        def find(target):
            if target == 0:
                return 1
            cnt = 0
            for num in nums:
                if num <= target:
                    cnt += find(target - num)
                else:
                    break
            return cnt
        return find(target)
