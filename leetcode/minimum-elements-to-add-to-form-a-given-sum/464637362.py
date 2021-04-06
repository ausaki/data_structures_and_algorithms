# title: minimum-elements-to-add-to-form-a-given-sum
# detail: https://leetcode.com/submissions/detail/464637362/
# datetime: Sun Mar  7 16:47:16 2021
# runtime: 712 ms
# memory: 27.1 MB

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        s = sum(nums)
        diff = abs(goal - s)
        if diff == 0: return 0
        q, r = divmod(diff, limit)
        return q + (r != 0)
            
            
            