# title: find-all-duplicates-in-an-array
# detail: https://leetcode.com/submissions/detail/285883901/
# datetime: Sat Dec 14 21:50:57 2019
# runtime: 404 ms
# memory: 20.3 MB

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x)-1] *= -1
        return res