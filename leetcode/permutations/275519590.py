# title: permutations
# detail: https://leetcode.com/submissions/detail/275519590/
# datetime: Sun Nov  3 13:05:59 2019
# runtime: 44 ms
# memory: 13.9 MB

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''字典序'''
        if not nums:
            return []
        result = []
        curr = sorted(nums)
        result.append(list(curr))
        
        while True:
            i = len(curr) - 2
            while i >= 0 and curr[i] >= curr[i + 1]:
                i -= 1
            if i < 0:
                break
            j = len(curr) - 1
            while curr[j] <= curr[i]:
                j -= 1
            curr[i], curr[j] = curr[j], curr[i]
            i += 1
            j = len(curr) - 1
            while i < j:
                curr[i], curr[j] = curr[j], curr[i]
                i += 1
                j -= 1
            result.append(list(curr))
        return result
            
        