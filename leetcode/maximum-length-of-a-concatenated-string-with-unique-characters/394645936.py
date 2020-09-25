# title: maximum-length-of-a-concatenated-string-with-unique-characters
# detail: https://leetcode.com/submissions/detail/394645936/
# datetime: Sat Sep 12 23:52:45 2020
# runtime: 116 ms
# memory: 16.4 MB

from functools import lru_cache

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def countbits(n):
            c = 0
            while n:
                n &= n - 1
                c += 1
            return c
        
        def encode(s):
            n = 0
            for c in s:
                b = 1 << (ord(c) - ord('a'))
                if n & b == 0:
                    n |= b
                else:
                    return -1
            return n
        
        sets = [0]
        result = 0
        for s in arr:
            s = encode(s)
            if s == -1:
                continue
            for i in range(len(sets)):
                if s & sets[i] == 0:
                    sets.append(s | sets[i])
                    result = max(result, countbits(sets[-1]))
        return result
        