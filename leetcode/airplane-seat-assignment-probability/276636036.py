# title: airplane-seat-assignment-probability
# detail: https://leetcode.com/submissions/detail/276636036/
# datetime: Thu Nov  7 08:31:58 2019
# runtime: 1040 ms
# memory: 16.7 MB

from functools import lru_cache

class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
#         seats = [-1 for i in range(n)]
#         total, ok = 0, 0
#         for i in range(n):
#             seats[i] = 0
#             t, o = self._dfs(n, 1, seats)
#             seats[i] = -1
#             total += t
#             ok += o
            
#         return ok / total
        return self._dp(n)
    
    def _dfs(self, n, curr, seats):
        if curr == n:
            return 1, 1 if seats[curr - 1] == curr - 1 else 0
        if seats[curr] < 0:
            seats[curr] = curr
            total, ok = self._dfs(n, curr + 1, seats)
            seats[curr] = -1
            return total, ok
        else:
            total, ok = 0, 0
            for i in range(n):
                if seats[i] < 0:
                    seats[i] = curr
                    t, o = self._dfs(n, curr + 1, seats)
                    seats[i] = -1
                    total += t
                    ok += o
            return total, ok
    
    def _dp(self, n):
        '''
        dp[i]表示第i个乘客选择座位后使得第n个乘客可以得到正确座位的概率
        dp[i] = 1 / (n - i + 1) + (n - i - 1) / (n - i + 1) * (dp[i + 1] + dp[i + 2] + ... + dp[n - 1])
        '''
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[n] = 0
        for i in reversed(range(1, n)):
            dp[i] = 1 / (n - i + 1)
            dp[i] += (n - i - 1) / (n - i + 1) * dp[i + 1]
        return dp[1]
        
                
            
        