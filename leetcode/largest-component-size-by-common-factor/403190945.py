# title: largest-component-size-by-common-factor
# detail: https://leetcode.com/submissions/detail/403190945/
# datetime: Fri Oct  2 02:08:06 2020
# runtime: 1132 ms
# memory: 16 MB

class DisjSet:
    def __init__(self, n ):
        self.disj_set = [-1] * n
        
    def find(self, x):
        while self.disj_set[x] >= 0:
            x = self.disj_set[x]
        return x
    
    def union(self, x, y):
        i = self.find(x)
        j = self.find(y)
        if i == j:
            return
        if self.disj_set[i] < self.disj_set[j]:
            self.disj_set[i] += self.disj_set[j]
            self.disj_set[j] = i
        else:
            self.disj_set[j] += self.disj_set[i]
            self.disj_set[i] = j
    
    def maxset(self):
        return -min(self.disj_set)

def gen_primes(n):
    candidates = [1] * n
    for i in range(2, int(math.sqrt(n)) + 1):
        if candidates[i]:
            for j in range(i ** 2, n, i):
                candidates[j] = 0
    return [i for i in range(2, n) if candidates[i]]
primes = gen_primes(320)

class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def factor(n):
            result = set()
            for i in primes:
                if i > n:
                    break
                if n % i == 0:
                    result.add(i)
                    while n % i == 0:
                        n //= i
            result.add(n)
            return result
        n = len(A)
        disj = DisjSet(n)
        g = {}
        for i, a in enumerate(A):
            for f in factor(a):
                if f == 1:
                    continue
                if f not in g:
                    g[f] = i
                else:
                    disj.union(i, g[f])
        return disj.maxset()