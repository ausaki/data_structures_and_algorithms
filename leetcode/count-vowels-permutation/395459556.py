# title: count-vowels-permutation
# detail: https://leetcode.com/submissions/detail/395459556/
# datetime: Mon Sep 14 14:04:34 2020
# runtime: 164 ms
# memory: 19.1 MB

class Solution:
    dp = [[1] * 5]
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        follows = {0: [1], 1: [0, 2], 2: [0, 1, 3, 4], 3: [2, 4], 4: [0]}
        for i in range(len(self.dp), n):
            dp1 = [0] * 5
            for j in range(5):
                dp1[j] = sum(self.dp[-1][k] for k in follows[j]) % MOD
            self.dp.append(dp1)
        return sum(self.dp[n - 1]) % MOD