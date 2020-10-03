# title: distinct-subsequences-ii
# detail: https://leetcode.com/submissions/detail/403593431/
# datetime: Sat Oct  3 01:19:58 2020
# runtime: 612 ms
# memory: 18.9 MB

class Solution:
    def distinctSubseqII(self, S: str) -> int:
        @lru_cache(None)
        def dp(i):
            if i == n:
                return 0
            result = 2 * dp(i + 1) + 1
            idx = pos[S[i]]
            j = bisect.bisect(idx, i)
            for j in range(j, len(idx)):
                result -= dp(idx[j]) - dp(idx[j] + 1)
            return result % MOD
        MOD = 10 ** 9 + 7
        n = len(S)
        pos = collections.defaultdict(list)
        for i, c in enumerate(S):
            pos[c].append(i)
        result = dp(0)
        return result