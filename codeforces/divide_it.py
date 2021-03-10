def solve(x):
    res = 0
    while x > 1 and x % 2 == 0:
        res += 1
        x //= 2
    while x > 1 and x % 3 == 0:
        x //= 3
        res += 2
    while x > 1 and x % 5 == 0:
        x //= 5
        res += 3
    return res if x == 1 else -1
        

def main():
    n = int(input())
    for i in range(n):
        x = int(input())
        print(solve(x))

main()