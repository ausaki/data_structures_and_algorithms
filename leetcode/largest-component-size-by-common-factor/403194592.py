# title: largest-component-size-by-common-factor
# detail: https://leetcode.com/submissions/detail/403194592/
# datetime: Fri Oct  2 02:18:18 2020
# runtime: 860 ms
# memory: 16.1 MB

class DisjSet:
    def __init__(self, n ):
        self.disj_set = [-1] * n
        self.sizes = [1] * n
        
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
            self.disj_set[j] = i
            self.sizes[i] += self.sizes[j]
            self.sizes[j] = 0
        else:
            if self.disj_set[i] == self.disj_set[j]:
                self.disj_set[j] -= 1
            self.disj_set[i] = j
            self.sizes[j] += self.sizes[i]
            self.sizes[i] = 0
    
    def maxset(self):
        return max(self.sizes)
    
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def gen_primes(n):
            candidates = [1] * n
            for i in range(2, int(math.sqrt(n)) + 1):
                if candidates[i]:
                    for j in range(i ** 2, n, i):
                        candidates[j] = 0
            return [i for i in range(2, n) if candidates[i]]
        primes = gen_primes(int(math.sqrt(max(A))) + 1)
        def factor(n):
            result = []
            for i in primes:
                if i * i > n:
                    break
                if n % i == 0:
                    result.append(i)
                    while n % i == 0:
                        n //= i
            result.append(n)
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