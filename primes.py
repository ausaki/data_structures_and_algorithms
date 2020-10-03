import math

def gen_primes(n):
    candidates = [1] * n
    for i in range(2, int(math.sqrt(n)) + 1):
        if candidates[i]:
            for j in range(i ** 2, n, i):
                candidates[j] = 0
    return [i for i in range(2, n) if candidates[i]]

primes = gen_primes(1000)
print(primes)
print(len(primes))
