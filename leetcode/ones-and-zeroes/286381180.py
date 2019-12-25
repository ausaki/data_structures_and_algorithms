# title: ones-and-zeroes
# detail: https://leetcode.com/submissions/detail/286381180/
# datetime: Mon Dec 16 21:36:26 2019
# runtime: 4436 ms
# memory: 97.9 MB

from functools import lru_cache
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        @lru_cache(None)
        def find(i, m, n):
            if m < 0 or n < 0:
                return -1
            if i == N:
                return 0
            cnt = collections.Counter(strs[i])
            return max(1 + find(i + 1, m - cnt['0'], n - cnt['1']),
                       find(i + 1, m, n))
        N = len(strs)
        strs.sort(key=len)
        return find(0, m, n)