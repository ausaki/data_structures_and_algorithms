# title: combination-sum-iii
# detail: https://leetcode.com/submissions/detail/284461789/
# datetime: Sun Dec  8 11:38:35 2019
# runtime: 36 ms
# memory: 12.9 MB

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def _find(k, n, m):
            if n == 0 and k == 0:
                return [[]]
            if n < 0 or k <= 0 or m > 9:
                return None
            res = []
            for i in range(m, 10):
                combs = _find(k - 1, n - i, i + 1)
                if combs is None:
                    continue
                for comb in combs:
                    res.append([i] + comb)
            return res
        return _find(k, n, 1)