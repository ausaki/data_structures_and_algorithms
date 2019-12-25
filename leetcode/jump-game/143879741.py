# title: jump-game
# detail: https://leetcode.com/submissions/detail/143879741/
# datetime: Wed Mar  7 15:16:49 2018
# runtime: 44 ms
# memory: N/A

class Solution(object):
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
                if zero_start >= 0 and max_jump_pos <= zero_end:
                    return False
                max_jump_pos = max(nums[i] + i, max_jump_pos)
        if zero_start >= 0:
            if max_jump_pos >= zero_end:
                return True
            else:
                return False
        else:
            return True
                        
    def _canJump2(self, nums):
        N = len(nums)
        left_pos = N - 1
        for i in range(N - 2, -1, -1):
            if i + nums[i] >= left_pos:
                left_pos = i
        return left_pos == 0
            
                
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # self.nums_length = len(nums)
        # self.cache = {}
        # return self._canJump(nums, 0)
        
        # return self._canJump1(nums)
        return self._canJump2(nums)
    
