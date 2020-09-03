# title: the-kth-factor-of-n
# detail: https://leetcode.com/submissions/detail/379788933/
# datetime: Wed Aug 12 16:29:49 2020
# runtime: 28 ms
# memory: 13.7 MB

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        m = int(math.sqrt(n))
        factors = [i for i in range(1, m + 1) if n % i == 0]
        if k <= len(factors):
            return factors[k - 1]
        k -= len(factors)
        if m ** 2 == n:
            factors.pop()
        if k > len(factors):
            return -1
        return n // factors[-k]
        