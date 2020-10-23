# title: number-of-sets-of-k-non-overlapping-line-segments
# detail: https://leetcode.com/submissions/detail/410557207/
# datetime: Mon Oct 19 14:52:02 2020
# runtime: 24 ms
# memory: 14.1 MB

class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        # C(n + k - 1, 2 * k)
        return math.comb(n + k -1, 2 * k) % MOD