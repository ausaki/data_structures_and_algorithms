# title: nth-magical-number
# detail: https://leetcode.com/submissions/detail/406511680/
# datetime: Fri Oct  9 17:22:28 2020
# runtime: 184 ms
# memory: 17.9 MB

class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        MOD = 10 ** 9 + 7
        if A == B:
            return (A * N) % MOD
        C = A * B // math.gcd(A, B)
        a = [A * i for i in range(1, C // A)]
        b = [B * i for i in range(1, C // B)]
        candidates = list(heapq.merge(a, b))
        candidates.append(C)
        q, r = divmod(N - 1, len(candidates))
        return (candidates[r] + C * q % MOD) % MOD
            