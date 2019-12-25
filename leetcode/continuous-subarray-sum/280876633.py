# title: continuous-subarray-sum
# detail: https://leetcode.com/submissions/detail/280876633/
# datetime: Sat Nov 23 00:46:38 2019
# runtime: 852 ms
# memory: 12.8 MB

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            for i in range(len(nums) - 1):
                if nums[i] + nums[i + 1] == 0:
                    return True
            return False
        dp = set()
        for i in range(len(nums)):
            r = nums[i] % k
            if ((k - r) % k) in dp:
                return True
            dp = {(r + rr) % k for rr in dp}
            dp.add(r)
        return False
            
            
        
        