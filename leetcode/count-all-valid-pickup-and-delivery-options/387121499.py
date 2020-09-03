# title: count-all-valid-pickup-and-delivery-options
# detail: https://leetcode.com/submissions/detail/387121499/
# datetime: Thu Aug 27 21:51:31 2020
# runtime: 20 ms
# memory: 13.8 MB

class Solution:
    def __init__(self):
        self.dp = [1, 6, 90]
        
    def countOrders(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        for i in range(len(self.dp), n):
            j = i * 2 + 2
            k = self.dp[-1] * j * (j - 1) // 2
            k %= MOD
            self.dp.append(k)
        return self.dp[n - 1]