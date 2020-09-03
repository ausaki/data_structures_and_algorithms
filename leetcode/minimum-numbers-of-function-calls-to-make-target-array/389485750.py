# title: minimum-numbers-of-function-calls-to-make-target-array
# detail: https://leetcode.com/submissions/detail/389485750/
# datetime: Wed Sep  2 00:06:31 2020
# runtime: 556 ms
# memory: 21.4 MB

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return len(bin(max(nums))) - 3 + sum(bin(num).count('1') for num in nums)
        
        