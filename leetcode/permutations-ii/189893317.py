# title: permutations-ii
# detail: https://leetcode.com/submissions/detail/189893317/
# datetime: Fri Nov 16 15:01:47 2018
# runtime: 268 ms
# memory: N/A

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        nums_size = len(nums)
        result = []
        indices = list(range(nums_size))
        cycles = list(range(nums_size))
        prev_item = [nums[k] for k in indices]
        result.append(prev_item)
        while True:
            for i in range(nums_size - 1, -1, -1):
                cycles[i] += 1
                if cycles[i] == nums_size:
                    indices[i:] = indices[i+1:] + indices[i:i+1]
                    cycles[i] = i
                else:
                    j = cycles[i]
                    indices[i], indices[j] = indices[j], indices[i]
                    item = [nums[k] for k in indices]
                    if item > prev_item:
                        prev_item = item
                        result.append(item)
                    break
            else:
                return result