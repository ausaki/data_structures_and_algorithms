# title: minimum-numbers-of-function-calls-to-make-target-array
# detail: https://leetcode.com/submissions/detail/389483165/
# datetime: Wed Sep  2 00:00:02 2020
# runtime: 1464 ms
# memory: 21.2 MB

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        m = 0
        for num in nums:
            j = 1
            for i in range(32):
                if num & j:
                    result += 1
                if num <= j:
                    m = max(m, i if num == j else i - 1)
                    break
                j <<= 1
        result += m
        return result
        
        