# title: maximum-length-of-a-concatenated-string-with-unique-characters
# detail: https://leetcode.com/submissions/detail/394637068/
# datetime: Sat Sep 12 23:25:40 2020
# runtime: 204 ms
# memory: 29.4 MB

from functools import lru_cache

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        result = [0]
        
        def _countbits(n):
            c = 0
            while n:
                n &= n - 1
                c += 1
            return c
        
        def _encode(s):
            n = 0
            for c in s:
                b = 1 << (ord(c) - ord('a'))
                if n & b == 0:
                    n |= b
                else:
                    return -1
            return n
        
        @lru_cache(None)
        def _dfs(n, i):
            if i == len(arr):
                return _countbits(n)
            m = _encode(arr[i])
            if m == -1:
                return _dfs(n, i + 1)
            result = 0
            if m & n == 0:
                result = _dfs(n | m, i + 1)
            return max(result, _dfs(n, i + 1))
        
        return _dfs(0, 0)
        