# title: largest-number
# detail: https://leetcode.com/submissions/detail/281507609/
# datetime: Mon Nov 25 13:50:21 2019
# runtime: 40 ms
# memory: 12.6 MB

from functools import cmp_to_key
import itertools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:
            return ''
        
        @cmp_to_key
        def compare(num1, num2):
            a = itertools.chain(num1, num2)
            b = itertools.chain(num2, num1)
            for i, j in zip(a, b):
                if i < j:
                    return -1
                if i > j:
                    return 1
            return 0
        
        nums = sorted(map(str, nums), reverse=True, key=compare)
        result = ''.join(nums)
        if result[0] == '0':
            return '0'
        return result
                
                        
        
        