# title: combination-sum-iii
# detail: https://leetcode.com/submissions/detail/284468130/
# datetime: Sun Dec  8 12:01:33 2019
# runtime: 28 ms
# memory: 12.8 MB

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def _find(k, n, m):
            if n == 0 and k == 0:
                return [[]]
            if n < 0 or k <= 0 or m > 9:
                return []
            res = []
            for i in range(m, 10):
                if i > n:
                    break
                for comb in _find(k - 1, n - i, i + 1):
                    res.append([i] + comb)
            return res
        return _find(k, n, 1)