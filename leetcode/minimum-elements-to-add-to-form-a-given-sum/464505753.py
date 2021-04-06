# title: minimum-elements-to-add-to-form-a-given-sum
# detail: https://leetcode.com/submissions/detail/464505753/
# datetime: Sun Mar  7 11:01:39 2021
# runtime: 832 ms
# memory: 27.1 MB

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        s = sum(nums)
        diff = goal - s
        if diff == 0:
            return 0
        diff = abs(diff)
        q, r = divmod(diff, limit)
        return q + (r != 0)
            
            
            