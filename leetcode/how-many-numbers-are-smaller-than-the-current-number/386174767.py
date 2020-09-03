# title: how-many-numbers-are-smaller-than-the-current-number
# detail: https://leetcode.com/submissions/detail/386174767/
# datetime: Tue Aug 25 22:17:50 2020
# runtime: 48 ms
# memory: 13.7 MB

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        idx = list(range(n))
        idx.sort(key=nums.__getitem__)
        j = 0
        for i, k in enumerate(idx):
            if nums[k] != nums[idx[j]]:
                j = i
            result[k] = j
        return result