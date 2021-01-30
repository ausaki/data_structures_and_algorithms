# title: count-ways-to-make-array-with-product
# detail: https://leetcode.com/submissions/detail/447093034/
# datetime: Sun Jan 24 15:39:47 2021
# runtime: 652 ms
# memory: 19.9 MB

def gen_primes(n):
    bools = [True] * n
    for i in range(2, int(math.sqrt(n)) + 1):
        if bools[i]:
            for j in range(i ** 2, n, i):
                bools[j] = False
    return [i for i in range(2, n) if bools[i]]

def factor(n):
    res = []
    for i in primes:
        if i > n:
            break
        j = 0
        while n % i == 0:
            n //= i
            j += 1
        res.append(j)
    if n != 1:
        res.append(1)
    return res

primes = gen_primes(int(math.sqrt(10 ** 4)) + 2)


class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        '''
        朴素的 DP 复杂度太高.
        
        质因数分界我又没想明白如何计算组合数.
        '''
        MOD = 10 ** 9 + 7
        res = []        
        for n, k in queries:
            if k == 1:
                res.append(1)
                continue
            ps = factor(k)
            cnt = 1
            for p in ps:
                cnt = (cnt * math.comb(n + p - 1, n - 1)) % MOD
            res.append(cnt)
        return res
            