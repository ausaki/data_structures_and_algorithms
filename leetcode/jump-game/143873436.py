# title: jump-game
# detail: https://leetcode.com/submissions/detail/143873436/
# datetime: Wed Mar  7 14:42:20 2018
# runtime: 55 ms
# memory: N/A

class Solution(object):
    def _canJump(self, nums, i=0):
        # n is nums length from i to end
        print 'i ->', i
        n = self.nums_length - i
        if n <= 1:
            return True
        elif n == 2:
            if nums[i] >= 1:
                return True
            else:
                return False
        else:
            if nums[i] <= 0:
                return False
            else:
                if i + nums[i] >= self.nums_length - 1:
                    return True
                if i in self.cache:
                    return False
                for j in range(nums[i], 0, -1):
                    k = i + j
                    if self._canJump(nums, k):
                        return True
                self.cache[i] = False
                return False
            
    def _canJump1(self, nums):
        N = len(nums)
        zero_start = -1
        zero_end = -1
        max_jump_pos = 0
        
        if N <= 1:
            return True
        
        for i in range(N):
            if nums[i] == 0:
                if zero_start == -1:
                    zero_start = i
                    zero_end = i
                else:
                    zero_end = i
            else:
                if zero_start >= 0:
                    if max_jump_pos <= zero_end:
                        return False
                    else:
                        max_jump_pos = max(nums[i] + i, max_jump_pos)
                else:
                    max_jump_pos = max(nums[i] + i, max_jump_pos)
        if zero_start >= 0:
            if max_jump_pos >= zero_end:
                return True
            else:
                return False
        else:
            return True
                        
                    
            
                
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # self.nums_length = len(nums)
        # self.cache = {}
        # return self._canJump(nums, 0)
        
        return self._canJump1(nums)
    
