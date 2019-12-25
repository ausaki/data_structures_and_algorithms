# title: maximum-length-of-a-concatenated-string-with-unique-characters
# detail: https://leetcode.com/submissions/detail/280293648/
# datetime: Wed Nov 20 15:06:02 2019
# runtime: 168 ms
# memory: 28.3 MB

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
                c = _countbits(n)
                if c > result[0]:
                    result[0] = c
                return
            m = _encode(arr[i])
            if m == -1:
                _dfs(n, i + 1)
                return
            if m & n == 0:
                _dfs(n | m, i + 1)
            _dfs(n, i + 1)
        
        _dfs(0, 0)
        return result[0]
        