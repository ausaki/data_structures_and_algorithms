# title: number-of-ways-of-cutting-a-pizza
# detail: https://leetcode.com/submissions/detail/382629290/
# datetime: Tue Aug 18 17:01:46 2020
# runtime: 208 ms
# memory: 15.6 MB

from functools import lru_cache

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        M = 10 ** 9 + 7
        
        @lru_cache(None)
        def cut(i, j, k):
            if k == 1:
                return 1 if any('A' in pizza[ii][j:] for ii in range(i, n)) else 0
            result = 0
            for ii in range(i, n):
                if 'A' in pizza[ii][j:]:
                    break
            i = ii
            for ii in range(i, n - 1):
                result += cut(ii + 1, j, k - 1) % M
            for jj in range(j, m):
                if 'A' in [pizza[ii][jj] for ii in range(i, n)]:
                    break
            j = jj
            for jj in range(j, m - 1):
                result += cut(i, jj + 1, k - 1) % M
            return result
        
        n = len(pizza)
        m = len(pizza[0])
        return cut(0, 0, k) % M