# title: check-if-it-is-a-good-array
# detail: https://leetcode.com/submissions/detail/394551633/
# datetime: Sat Sep 12 17:48:41 2020
# runtime: 268 ms
# memory: 24.3 MB

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        return reduce(math.gcd, nums) == 1
