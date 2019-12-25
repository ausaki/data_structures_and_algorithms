# title: find-all-duplicates-in-an-array
# detail: https://leetcode.com/submissions/detail/285883252/
# datetime: Sat Dec 14 21:44:11 2019
# runtime: 392 ms
# memory: 18.9 MB

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        i = 0
        for i in range(len(nums)):
            if nums[i] == -1:
                continue
            curr = nums[i]
            nums[i] = 0
            while curr != 0 and nums[curr - 1] != -1:
                t = nums[curr - 1]
                nums[curr - 1] = -1
                curr = t
            if curr != 0:
                res.append(curr)
        return res