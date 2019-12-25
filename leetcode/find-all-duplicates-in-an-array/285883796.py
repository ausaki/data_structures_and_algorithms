# title: find-all-duplicates-in-an-array
# detail: https://leetcode.com/submissions/detail/285883796/
# datetime: Sat Dec 14 21:49:50 2019
# runtime: 436 ms
# memory: 20.4 MB

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            j = abs(nums[i])
            if nums[j - 1] < 0:
                res.append(j)
            nums[j - 1] = -nums[j - 1]
        return res