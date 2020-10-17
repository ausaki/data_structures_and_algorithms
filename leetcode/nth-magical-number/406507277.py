# title: nth-magical-number
# detail: https://leetcode.com/submissions/detail/406507277/
# datetime: Fri Oct  9 17:02:08 2020
# runtime: 28 ms
# memory: 13.9 MB

class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        MOD = 10 ** 9 + 7
        if A == B:
            return (A * N) % MOD
        if B < A:
            A, B = B, A
        l, r = A, A * N
        C = A * B // math.gcd(A, B)
        while l <= r:
            m = (l + r) // 2
            i = m // A + m // B - m // C
            if i < N:
                l = m + 1
            else:
                r = m - 1
        return l % MOD
            