# title: array-nesting
# detail: https://leetcode.com/submissions/detail/287294656/
# datetime: Fri Dec 20 15:25:39 2019
# runtime: 128 ms
# memory: 30.1 MB

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        def dfs(i, n):
            if nums[i] == -1:
                return n
            j = nums[i]
            nums[i] = -1
            return dfs(j, n + 1)
        res = 0
        for i in range(len(nums)):
            if nums[i] >= 0:
                res = max(res, dfs(i, 0))
        return res