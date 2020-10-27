import math

def gen_primes(n):
    bools = [True] * n
    for i in range(2, int(math.sqrt(n)) + 1):
        if bools[i]:
            for j in range(i ** 2, n, i):
                bools[j] = False
    return [i for i in range(2, n) if bools[i]]


def segment_sieve(n):
    root = int(math.sqrt(n)) + 1
    primes = gen_primes(root)
    all_primes = primes[:]
    low = root
    high = root * 2
    while low < n:
        high = min(high, n)
        bools = [True] * (high - low)
        for p in primes:
            i = (low + p - 1) // p * p
            for i in range(i, high, p):
                bools[i - low] = False
        all_primes.extend(low + i for i, b in enumerate(bools) if b)
        low, high = high, high + root
    return all_primes


def main():
    primes = segment_sieve(100000000)
    t = int(input())
    for i in range(t):
        n = int(input())
        print(primes[n - 1])

main()
