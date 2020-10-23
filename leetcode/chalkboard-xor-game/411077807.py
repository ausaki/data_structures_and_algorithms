# title: chalkboard-xor-game
# detail: https://leetcode.com/submissions/detail/411077807/
# datetime: Tue Oct 20 22:58:05 2020
# runtime: 72 ms
# memory: 14.2 MB

class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        xor = 0
        for i in nums:
            xor ^= i
        return xor == 0 or len(nums) % 2 == 0
        
