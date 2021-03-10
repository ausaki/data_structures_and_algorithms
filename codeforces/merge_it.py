def solve(arr):
    res = 0
    a, b = 0, 0
    for i in arr:
        if i % 3 == 0:
            res += 1
        if i % 3 == 1:
            a += 1
        if i % 3 == 2:
            b += 1
    return res + min(a, b) + abs(a - b) // 3

def main():
    n = int(input())
    for i in range(n):
        m = int(input())
        arr = map(int, input().split(' '))
        print(solve(arr))

main()