# title: make-sum-divisible-by-p
# detail: https://leetcode.com/submissions/detail/399104918/
# datetime: Tue Sep 22 15:28:43 2020
# runtime: 864 ms
# memory: 32.3 MB

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        r = 0
        for i, a in enumerate(nums):
            r = (r + a) % p
        if r == 0:
            return 0        
        result = n 
        s = 0
        pos = {0: -1}
        for i, a in enumerate(nums):
            s = (s + a) % p
            r1 = (s - r) % p
            if r1 in pos:
                result = min(result, i - pos.get(r1, -n))
            pos[s] = i
        return result if result < n else -1
        
        