# title: coin-change
# detail: https://leetcode.com/submissions/detail/275303553/
# datetime: Sat Nov  2 22:23:02 2019
# runtime: 1916 ms
# memory: 17 MB

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.cache = {}
        return self._change(coins, amount)
        
    def _change(self, coins, amount):
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if amount in self.cache:
            return self.cache[amount]
        m = amount
        for c in coins:
            n = self._change(coins, amount - c)
            if n >= 0 and n < m:
                m = n
        if m < amount:
            self.cache[amount] = m + 1
            return m + 1
        self.cache[amount] = -1
        return -1