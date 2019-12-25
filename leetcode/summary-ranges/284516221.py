# title: summary-ranges
# detail: https://leetcode.com/submissions/detail/284516221/
# datetime: Sun Dec  8 16:21:16 2019
# runtime: 28 ms
# memory: 12.7 MB

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        N = len(nums)
        res = []
        while i < N:
            j = i
            while j < N - 1 and nums[j] + 1 == nums[j + 1]:
                j += 1
            if i < j:
                res.append('{}->{}'.format(nums[i], nums[j]))
            else:
                res.append(str(nums[i]))
            i = j + 1
        return res