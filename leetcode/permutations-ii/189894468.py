# title: permutations-ii
# detail: https://leetcode.com/submissions/detail/189894468/
# datetime: Fri Nov 16 15:08:23 2018
# runtime: 60 ms
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
                    while j < nums_size and nums[indices[i]] == nums[indices[j]]:
                        j += 1
                    if j < nums_size:
                        cycles[i] = j
                        indices[i], indices[j] = indices[j], indices[i]
                        result.append([nums[i] for i in indices])
                        break
                    else:
                        indices[i:] = indices[i+1:] + indices[i:i+1]
                        cycles[i] = i
            else:
                return result