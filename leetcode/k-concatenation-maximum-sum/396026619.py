# title: k-concatenation-maximum-sum
# detail: https://leetcode.com/submissions/detail/396026619/
# datetime: Tue Sep 15 17:15:04 2020
# runtime: 332 ms
# memory: 26.8 MB

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        s = 0
        s1 = 0
        s2 = -10 ** 5
        result = 0
        for a in arr:
            if s > 0:
                s += a
            else:
                s = a
            result = max(result, s)
            s1 += a
            s2 = max(s2, s1)
        if k == 1:
            return result % MOD
        result = max(result, s2 + s)
        if k == 2:
            return result % MOD
        if s2 + s + s1 > result:
            result = max(result, s2 + s + s1 * (k - 2))
        return result % MOD