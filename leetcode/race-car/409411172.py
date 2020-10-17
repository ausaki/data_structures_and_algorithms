# title: race-car
# detail: https://leetcode.com/submissions/detail/409411172/
# datetime: Fri Oct 16 17:55:03 2020
# runtime: 276 ms
# memory: 14.3 MB

class Solution:
    def racecar(self, target: int) -> int:
        dp = [0, 1, 4] + [float('inf')] * target
        for t in range(3, target + 1):
            k = t.bit_length()
            if t == 2**k - 1:
                dp[t] = k
                continue
            for j in range(k - 1):
                dp[t] = min(dp[t], dp[t - 2**(k - 1) + 2**j] + k - 1 + j + 2)
            if 2**k - 1 - t < t:
                dp[t] = min(dp[t], dp[2**k - 1 - t] + k + 1)
        return dp[target]
                    
        
            
            