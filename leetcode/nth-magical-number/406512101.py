# title: nth-magical-number
# detail: https://leetcode.com/submissions/detail/406512101/
# datetime: Fri Oct  9 17:24:24 2020
# runtime: 176 ms
# memory: 17 MB

class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        MOD = 10 ** 9 + 7
        if A == B:
            return (A * N) % MOD
        C = A * B // math.gcd(A, B)
        candidates = list(heapq.merge((A * i for i in range(1, C // A)), (B * i for i in range(1, C // B + 1))))
        q, r = divmod(N - 1, len(candidates))
        return (candidates[r] + C * q % MOD) % MOD
            