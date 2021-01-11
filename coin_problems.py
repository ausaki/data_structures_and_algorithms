'''
扔硬币问题: 连续扔 n 次硬币, 其中连续 k 次(或以上)是正面的概率
'''
from functools import lru_cache
import sys
sys.setrecursionlimit(2000)

def coin_problem_1(n, k):
    '''
    使用 DP 求解.
    '''
    @lru_cache(None)
    def P(n):
        if n < k:
            return 0
        if n == k:
            return pow(2, -k)
        return P(n - 1) + (1 - P(n - k - 1)) * pow(2, -(k + 1))

    if n < k:
        return 0
    dp = [0] * n
    dp[k - 1] = pow(2, -k)
    for i in range(k, n):
        dp[i] = dp[i - 1] + (1 - dp[i - k - 1]) * pow(2, -(k + 1))
    return dp[-1]
    # return P(n)

def coin_problem_2(n, k):
    '''
    使用转移矩阵求解
    '''
    import numpy as np
    T = np.array([
        [0.5, 0.5 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0],
        [0.5, 0 , 0.5 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0],
        [0.5, 0 , 0 , 0.5 , 0 , 0 , 0 , 0 , 0 , 0 , 0],
        [0.5, 0 , 0 , 0 , 0.5 , 0 , 0 , 0 , 0 , 0 , 0],
        [0.5, 0 , 0 , 0 , 0 , 0.5 , 0 , 0 , 0 , 0 , 0],
        [0.5, 0 , 0 , 0 , 0 , 0 , 0.5 , 0 , 0 , 0 , 0],
        [0.5, 0 , 0 , 0 , 0 , 0 , 0 , 0.5 , 0 , 0 , 0],
        [0.5, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0.5 , 0 , 0],
        [0.5, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0.5 , 0],
        [0.5, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0.5],
        [0, 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 1],
    ])
    res = np.zeros((1, 11))
    res[0, 0] = 1
    for i in range(n):
        res = res @ T
    return res[0, -1]
    
print(coin_problem_1(100, 10))
print(coin_problem_2(100, 10))