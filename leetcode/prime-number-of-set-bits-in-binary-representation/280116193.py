# title: prime-number-of-set-bits-in-binary-representation
# detail: https://leetcode.com/submissions/detail/280116193/
# datetime: Tue Nov 19 22:47:02 2019
# runtime: 480 ms
# memory: 12.8 MB

class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
        count = 0
        for i in range(L, R + 1):
            c = 0
            while i:
                i &= i - 1
                c += 1
            if c in primes:
                count += 1
        return count
        