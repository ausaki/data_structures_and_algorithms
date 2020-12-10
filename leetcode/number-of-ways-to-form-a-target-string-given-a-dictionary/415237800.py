# title: number-of-ways-to-form-a-target-string-given-a-dictionary
# detail: https://leetcode.com/submissions/detail/415237800/
# datetime: Sat Oct 31 23:09:53 2020
# runtime: 2804 ms
# memory: 253.7 MB

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10 ** 9 + 7
        m, n, t = len(words), len(words[0]), len(target)
        cols = [collections.Counter() for i in range(n)]
        for i in range(m):
            for j in range(n):
                cols[j][words[i][j]] += 1
        
        @lru_cache(None)
        def dp(i, j):
            if j == t:
                return 1
            if i == n:
                return 0
            result = dp(i + 1, j)
            if target[j] in cols[i]:
                result = (result + cols[i][target[j]] * dp(i + 1, j + 1)) % MOD
            return result
        
        return dp(0, 0)