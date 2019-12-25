# title: largest-number
# detail: https://leetcode.com/submissions/detail/281506176/
# datetime: Mon Nov 25 13:43:47 2019
# runtime: 40 ms
# memory: 12.7 MB

from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        @cmp_to_key
        def compare(num1, num2):
            a = num1 + num2
            b = num2 + num1
            if a == b:
                return 0
            if a < b:
                return -1
            return 1
        nums = sorted(map(str, nums), reverse=True, key=compare)
        result = ''.join(nums)
        result = result.lstrip('0')
        if result == '':
            result = '0'
        return result
                
                        
        
        