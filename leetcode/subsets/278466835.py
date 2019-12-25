# title: subsets
# detail: https://leetcode.com/submissions/detail/278466835/
# datetime: Wed Nov 13 20:16:38 2019
# runtime: 32 ms
# memory: 12.9 MB

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = 1
        subsets = [[]]
        while n < 2 ** len(nums):
            s = []
            i = 0
            while i < len(nums):
                if (1 << i) & n:
                    s.append(nums[i])
                i += 1
            n += 1
            subsets.append(s)
        return subsets
        
        