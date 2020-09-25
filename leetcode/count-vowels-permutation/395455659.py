# title: count-vowels-permutation
# detail: https://leetcode.com/submissions/detail/395455659/
# datetime: Mon Sep 14 13:55:06 2020
# runtime: 708 ms
# memory: 14 MB

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        follows = {'a': 'e', 'e': 'ai', 'i': 'aeou', 'o': 'iu', 'u': 'a'}
        dp = dict.fromkeys('aeiou', 1)
        for i in range(n - 1):
            dp1 = dict.fromkeys('aeiou', 0)
            for j in 'aeiou':
                dp1[j] = sum(dp[k] for k in follows[j]) % MOD
            dp = dp1
        return sum(dp.values()) % MOD