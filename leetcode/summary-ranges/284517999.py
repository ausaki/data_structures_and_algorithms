# title: summary-ranges
# detail: https://leetcode.com/submissions/detail/284517999/
# datetime: Sun Dec  8 16:34:47 2019
# runtime: 28 ms
# memory: 12.8 MB

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        nums.append((nums[-1] if nums else 0) + 2)
        N = len(nums)
        res = []
        prev = 0
        for i in range(N):
            if nums[i] - nums[prev] > i - prev:
                if prev < i - 1:
                    res.append('{}->{}'.format(nums[prev], nums[i - 1]))
                else:
                    res.append(str(nums[prev]))
                prev = i
        return res