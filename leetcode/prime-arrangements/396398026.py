# title: prime-arrangements
# detail: https://leetcode.com/submissions/detail/396398026/
# datetime: Wed Sep 16 11:51:00 2020
# runtime: 52 ms
# memory: 13.8 MB

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        primes = 0
        for i in range(2, n + 1):
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    break
            else:
                primes += 1
        print(primes)
        return (math.factorial(n - primes) * math.factorial(primes)) % (10 ** 9 + 7)