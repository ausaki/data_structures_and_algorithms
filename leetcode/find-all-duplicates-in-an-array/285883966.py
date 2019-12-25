# title: find-all-duplicates-in-an-array
# detail: https://leetcode.com/submissions/detail/285883966/
# datetime: Sat Dec 14 21:51:39 2019
# runtime: 412 ms
# memory: 20.3 MB

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            j = nums[i]
            if j < 0:
                j = -j
            if nums[j - 1] < 0:
                res.append(j)
            nums[j - 1] = -nums[j - 1]
        return res