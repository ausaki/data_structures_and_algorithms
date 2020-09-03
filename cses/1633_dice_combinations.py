import collections
M = 10 ** 9 + 7

def solution(n):
    dp = collections.deque([1, 1, 2, 4, 8, 16])
    if n < 6:
        return dp[n]
    for _ in range(n - 5):
        k = sum(dp) % M
        dp.append(k)
        dp.popleft()
    return dp[-1]

def main():
    n = input()
    n = int(n)
    res = solution(n)
    print(res) 

main()