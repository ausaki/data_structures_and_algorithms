# title: maximize-number-of-nice-divisors
# detail: https://leetcode.com/submissions/detail/473309660/
# datetime: Sun Mar 28 12:31:30 2021
# runtime: 36 ms
# memory: 14.2 MB

class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        MOD = 10 ** 9 + 7
        n = primeFactors
        if n <= 4: return n
        
        q, r = divmod(n, 3)
        if r == 1:
            return (pow(3, q - 1, MOD) * 4) % MOD
        return (pow(3, q, MOD) * (r if r else 1)) % MOD