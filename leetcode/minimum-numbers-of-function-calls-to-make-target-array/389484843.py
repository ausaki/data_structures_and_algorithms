# title: minimum-numbers-of-function-calls-to-make-target-array
# detail: https://leetcode.com/submissions/detail/389484843/
# datetime: Wed Sep  2 00:04:17 2020
# runtime: 608 ms
# memory: 21.6 MB

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0
        m = 0
        def bitcount(a):
            cnt = 0
            while a:
                cnt += 1
                a &= a - 1
            return cnt
        
        for num in nums:
            result += bitcount(num)
            m = max(m, num)
        for i in range(32):
            if m > 1:
                result += 1
            else:
                break
            m >>= 1
        return result
        
        