# title: count-primes
# detail: https://leetcode.com/submissions/detail/193988429/
# datetime: Sat Dec  8 17:41:12 2018
# runtime: 488 ms
# memory: 57.4 MB

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        table = [1] * n
        table[0] = 0
        table[1] = 0
        i = 2
        while i * i < n:
            if table[i]:
                for j in range(i * i, n, i):
                    table[j] = 0
            i += 1
        return sum(table)