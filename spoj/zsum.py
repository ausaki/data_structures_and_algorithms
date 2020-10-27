# your code goes here
def binpow(a, n, mod):
    res = 1
    while n:
        if n & 1:
            res = (res * a) % mod
        a = (a * a) % mod
        n >>= 1
    return res

def solve(n, k):
    MOD = 10 ** 7 + 7
    result = (2 * binpow(n - 1, n - 1, MOD) + binpow(n, n, MOD) + 2 * binpow(n - 1, k, MOD) + binpow(n, k, MOD)) % MOD
    return result

def main():
    while True:
        line = input()
        if not line:
            break
        n, k = map(int, line.split())
        if n == 0 and k == 0:
            break
        print(solve(n, k))
        

main()