# title: water-bottles
# detail: https://leetcode.com/submissions/detail/377279733/
# datetime: Fri Aug  7 12:23:39 2020
# runtime: 32 ms
# memory: 13.9 MB

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        def drink(i, j):
            if i <= 0:
                return 0
            return i + drink(*divmod(i + j, numExchange))
        return drink(numBottles, 0)