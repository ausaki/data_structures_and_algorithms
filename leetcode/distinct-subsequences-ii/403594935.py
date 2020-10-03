# title: distinct-subsequences-ii
# detail: https://leetcode.com/submissions/detail/403594935/
# datetime: Sat Oct  3 01:24:47 2020
# runtime: 92 ms
# memory: 18.9 MB

class Solution:
    def distinctSubseqII(self, S: str) -> int:
        @lru_cache(None)
        def dp(i):
            if i == n:
                return 0
            a = dp(i + 1)
            result = 2 * a + 1
            idx = pos[S[i]]
            result -= cache.get(S[i], 0)
            cache[S[i]] += result - a
            return result % MOD
        MOD = 10 ** 9 + 7
        n = len(S)
        pos = collections.defaultdict(list)
        for i, c in enumerate(S):
            pos[c].append(i)
        cache = collections.Counter()
        result = dp(0)
        return result