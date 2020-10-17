# title: knight-dialer
# detail: https://leetcode.com/submissions/detail/403837581/
# datetime: Sat Oct  3 16:31:24 2020
# runtime: 60 ms
# memory: 25.2 MB

from functools import lru_cache

mapping = [
            [4, 6], # 0
            [6, 8], # 1
            [7, 9], # 2
            [4, 8], # 3
            [0, 3, 9], # 4
            [], # 5
            [0, 1, 7], # 6
            [2, 6], # 7
            [1, 3], # 8
            [2, 4] # 9
        ]

mod = 1000_000_007

@lru_cache(None)
def dfs(n, i):
        if n == 1:
            return 1
        
        sum_ = 0
        for nei in mapping[i]:
            sum_ = (sum_ + dfs(n -1, nei)) % mod
            
        return sum_    
    
class Solution:            
    def knightDialer(self, N: int) -> int:                
        total = 0
        for i in range(10):
            total = (total + dfs(N, i)) % mod
            
        return total