# title: k-concatenation-maximum-sum
# detail: https://leetcode.com/submissions/detail/396025317/
# datetime: Tue Sep 15 17:10:21 2020
# runtime: 404 ms
# memory: 27 MB

class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        s = 0
        s1 = 0
        max_prefix_sum = -math.inf
        result = 0
        for a in arr:
            if s > 0:
                s += a
            else:
                s = a
            result = max(result, s)
            s1 += a
            max_prefix_sum = max(max_prefix_sum, s1)
        if k == 1:
            return result % MOD
        result = max(result, max_prefix_sum + s, max_prefix_sum + s + s1 * (k - 2))
        return result % MOD