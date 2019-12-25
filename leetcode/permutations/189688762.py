# title: permutations
# detail: https://leetcode.com/submissions/detail/189688762/
# datetime: Thu Nov 15 14:16:17 2018
# runtime: 36 ms
# memory: N/A

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.permute_recursive(nums)
        
    def permute_recursive(self, nums):
        """递归解法"""
        result = []
        nums_length = len(nums)
        if nums_length == 0:
            return []
        if nums_length == 1:
            return [[nums[0]]]
        nums = sorted(nums)
        if nums_length == 2:
            return [[nums[0], nums[1]], [nums[1], nums[0]]]
        item_length = nums_length - 1
        for item in self.permute_recursive(nums[1:]):
            for i in range(item_length + 1):
                tmp = list(item)
                tmp.insert(i, nums[0])
                result.append(tmp)
        return result
    
    def permute_py(self, iterable, r=None):
        """解法来源与Python官方collections模块的文档"""
        result = []
        pool = tuple(iterable)
        n = len(pool)
        r = n if r is None else r
        if r > n:
            return result
        indices = range(n)
        cycles = range(n, n-r, -1)
        result.append(list(pool[i] for i in indices[:r]))
        while n:
            for i in reversed(range(r)):
                cycles[i] -= 1
                if cycles[i] == 0:
                    indices[i:] = indices[i+1:] + indices[i:i+1]
                    cycles[i] = n - i
                else:
                    j = cycles[i]
                    indices[i], indices[-j] = indices[-j], indices[i]
                    result.append(list(pool[i] for i in indices[:r]))
                    break
            else:
                return result
        