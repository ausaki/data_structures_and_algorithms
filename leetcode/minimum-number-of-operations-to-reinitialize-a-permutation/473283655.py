# title: minimum-number-of-operations-to-reinitialize-a-permutation
# detail: https://leetcode.com/submissions/detail/473283655/
# datetime: Sun Mar 28 11:32:24 2021
# runtime: 40 ms
# memory: 14.2 MB

class Solution:
    def reinitializePermutation(self, n: int) -> int:
        if n == 2: return 1
        x = 2
        res = 1
        while x != 1:
            if x < n // 2:
                x *= 2
            else:
                x = (x - n // 2) * 2 + 1
            res += 1
        return res
        