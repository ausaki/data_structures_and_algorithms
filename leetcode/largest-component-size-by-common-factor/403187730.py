# title: largest-component-size-by-common-factor
# detail: https://leetcode.com/submissions/detail/403187730/
# datetime: Fri Oct  2 01:58:46 2020
# runtime: 884 ms
# memory: 16.2 MB

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
    
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def gen_primes(n):
            candidates = [1] * n
            for i in range(2, int(math.sqrt(n)) + 1):
                if candidates[i]:
                    for j in range(i ** 2, n, i):
                        candidates[j] = 0
            return [i for i in range(2, n) if candidates[i]]
        primes = gen_primes(int(math.sqrt(max(A))) + 2)
        def factor(n):
            result = set()
            while n > 1:
                s = int(math.sqrt(n))
                f = True
                for i in primes:
                    if i > s:
                        break
                    if n % i == 0:
                        result.add(i)
                        while n % i == 0:
                            n //= i
                        f = False
                        break
                if f:
                    result.add(n)
                    break
            return result
        n = len(A)
        disj = DisjSet(n)
        g = {}
        for i, a in enumerate(A):
            factors = factor(a)
            for f in factors:
                if f == 1:
                    continue
                if f not in g:
                    g[f] = i
                else:
                    disj.union(i, g[f])
        return disj.maxset()