# title: ones-and-zeroes
# detail: https://leetcode.com/submissions/detail/286382221/
# datetime: Mon Dec 16 21:45:03 2019
# runtime: 1640 ms
# memory: 197 MB

from functools import lru_cache
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @lru_cache(None)
        def find(i, m, n):
            if m < 0 or n < 0: return -1
            if i == N: return 0
            return max(1 + find(i + 1, m - strs[i][0], n - strs[i][1]), find(i + 1, m, n))
        N = len(strs)
        new_strs = []
        for s in strs:
            cnt = collections.Counter(s)
            new_strs.append([cnt['0'], cnt['1']])
        strs = new_strs
        return find(0, m, n)