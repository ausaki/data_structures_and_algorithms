# title: count-good-meals
# detail: https://leetcode.com/submissions/detail/437788447/
# datetime: Sun Jan  3 10:51:10 2021
# runtime: 3704 ms
# memory: 20.4 MB

class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        MOD = 10 ** 9 + 7
        deliciousness.sort()
        res = 0
        cnt = collections.Counter()
        for d in deliciousness:
            for i in range(31):
                if (1 << i) < d:
                    continue
                a = (1 << i) - d
                res = (res + cnt.get(a, 0)) % MOD
            cnt[d] += 1
        return res