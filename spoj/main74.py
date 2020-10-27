'''
Euclids algorithm revisited 
'''
MOD = 10 ** 9 + 7

def fib(n):
    '''
    fib(2 * k) = fib(k) * (fib(k) + 2 * fib(k - 1))
    fib(2 * k + 1) = fib(k) ** 2 + fib(k + 1) ** 2
    '''
    if n == 0:
        return 0, 1
    a, b = fib(n >> 1)
    c = (a * (2 * b - a)) % MOD
    d = (a ** 2 + b ** 2) % MOD
    if n & 1:
        return d, (c + d) % MOD
    return c, d

def solve(n):
    if n <= 1:
        return n + 1
    return fib(n + 3)[0]

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        print(solve(n))

main()