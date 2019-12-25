# title: find-all-duplicates-in-an-array
# detail: https://leetcode.com/submissions/detail/285881894/
# datetime: Sat Dec 14 21:30:16 2019
# runtime: 404 ms
# memory: 20.1 MB

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        i = 0
        for i in range(len(nums)):
            if nums[i] == i + 1:
                continue
            curr = nums[i]
            nums[i] = -1
            while curr != -1 and nums[curr - 1] != curr:
                # print(curr)
                t = nums[curr - 1]
                nums[curr - 1] = curr
                curr = t
            if curr != -1:
                res.append(curr)
        return res