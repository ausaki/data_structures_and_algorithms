# title: stone-game-iii
# detail: https://leetcode.com/submissions/detail/384152696/
# datetime: Fri Aug 21 18:42:16 2020
# runtime: 3856 ms
# memory: 17.3 MB

from functools import lru_cache

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        vals = stoneValue
        n = len(vals)
        dp = collections.deque([None] * 3)
        dp[0] = [0, 0]
        
        for i in range(n - 1, -1, -1):
            p1, p2 = -1e9, -1
            s = 0
            for j in range(i, min(i + 3, n)):
                s += vals[j]
                p1_, p2_ = dp[j - i]
                p2_ += s
                if p2_ > p1:
                    p1 = p2_
                    p2 = p1_
            dp.pop()
            dp.appendleft((p1, p2))
        
        p1, p2 = dp[0]
        # print(p1, p2)
        # p2 = sum(vals) - p1
        if p1 > p2:
            return 'Alice'
        elif p1 == p2:
            return 'Tie'
        return 'Bob'