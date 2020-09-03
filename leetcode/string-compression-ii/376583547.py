# title: string-compression-ii
# detail: https://leetcode.com/submissions/detail/376583547/
# datetime: Thu Aug  6 02:23:41 2020
# runtime: 3052 ms
# memory: 372 MB

from functools import lru_cache

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        if k == len(s):
            return 0
        n = len(s)
        
        @lru_cache(None)
        def count(i, last_char, last_count, k):
            if k < 0:
                return 200
            if i == n:
                return 0
            if s[i] == last_char:
                j = 0
                if last_count in (1, 9, 99):
                    j = 1
                return j + count(i + 1, last_char, last_count + 1, k)
            else:
                c1 = 1 + count(i + 1, s[i], 1, k)
                c2 = count(i + 1, last_char, last_count, k - 1)
                return min(c1, c2)
            
        return count(0, '', 0, k)
                    