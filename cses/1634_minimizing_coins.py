from functools import lru_cache

def solution(n, values, target):
    M = target + 1
    # values = set(values)
    dp = [M for i in range(target + 1)]
    dp[0] = 0
    for i in range(1, target + 1):
        for v in values:
            if i - v >= 0:
                dp[i] = min(dp[i], 1 + dp[i - v])
    return dp[-1] if dp[-1] < M else -1


def solution2(n, values, target):
    M = target + 1
    
    @lru_cache(None)
    def sol(t, k):
        if t == 0:
            return 0
        if k < 0:
            return M
        res = M
        value = values[k]
        q, r = divmod(t, value)
        if r == 0:
            return q
        if k == 0:
            return M
        for i in range(q, -1, -1):
            res = min(res, i + sol(r, k - 1))
            r += value
        return res

    values = set(values)
    values = sorted(values)
    # print(len(values))
    res = sol(target, len(values) - 1)
    return res if res < M else -1



def main():
    n, target = list(map(int, input().split()))
    values = list(map(int, input().split()))
    res = solution2(n, values, target)
    print(res) 

main()