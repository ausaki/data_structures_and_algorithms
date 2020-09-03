# title: running-sum-of-1d-array
# detail: https://leetcode.com/submissions/detail/380668243/
# datetime: Fri Aug 14 14:28:56 2020
# runtime: 36 ms
# memory: 14 MB

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        result = []
        for n in nums:
            s += n
            result.append(s)
        return result