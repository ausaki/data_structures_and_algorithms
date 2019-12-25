# title: super-pow
# detail: https://leetcode.com/submissions/detail/285050510/
# datetime: Wed Dec 11 00:45:08 2019
# runtime: 164 ms
# memory: 12.8 MB

from functools import lru_cache
class Solution:
    def superPow(self, a, b):
        result = 1
        for digit in b:
            result = pow(result, 10, 1337) * pow(a, digit, 1337) % 1337
        return result
        
        