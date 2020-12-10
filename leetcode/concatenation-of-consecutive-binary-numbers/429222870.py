# title: concatenation-of-consecutive-binary-numbers
# detail: https://leetcode.com/submissions/detail/429222870/
# datetime: Thu Dec 10 21:29:55 2020
# runtime: 64 ms
# memory: 17.9 MB

class Solution:
    dp = [0]
        
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        for i in range(len(self.dp), n + 1):
            j = i.bit_length()
            self.dp.append(((self.dp[-1] << j) % MOD + i) % MOD)
        return self.dp[n]