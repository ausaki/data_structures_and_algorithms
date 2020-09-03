# title: water-bottles
# detail: https://leetcode.com/submissions/detail/377280648/
# datetime: Fri Aug  7 12:26:15 2020
# runtime: 24 ms
# memory: 14.1 MB

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # def drink(i, j):
        #     if i <= 0:
        #         return 0
        #     return i + drink(*)
        emptyBottles = 0
        result = 0
        while numBottles:
            result += numBottles
            numBottles, emptyBottles = divmod(numBottles + emptyBottles, numExchange)
        return result