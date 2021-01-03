# title: count-good-meals
# detail: https://leetcode.com/submissions/detail/437838408/
# datetime: Sun Jan  3 12:12:36 2021
# runtime: 1956 ms
# memory: 20.7 MB

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10 ** 9 + 7
        deliciousness.sort()
        res = 0
        cnt = collections.Counter()
        for d in deliciousness:
            for i in range(22):
                if (1 << i) < d:
                    continue
                a = (1 << i) - d
                res = (res + cnt.get(a, 0)) % MOD
            cnt[d] += 1
        return res