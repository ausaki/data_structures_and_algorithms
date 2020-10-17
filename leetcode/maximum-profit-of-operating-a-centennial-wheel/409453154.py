# title: maximum-profit-of-operating-a-centennial-wheel
# detail: https://leetcode.com/submissions/detail/409453154/
# datetime: Fri Oct 16 21:29:05 2020
# runtime: 968 ms
# memory: 17.6 MB

class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        boarded = 0
        waiting = 0
        max_profit = 0
        k = -1
        for i, c in enumerate(customers, 1):
            waiting += c
            if waiting >= 4:
                waiting -= 4
                boarded += 4
            else:
                boarded += waiting
                waiting = 0
            profit = boarded * boardingCost - runningCost * i
            if profit > max_profit:
                k = i
                max_profit = profit
        if waiting and 4 * boardingCost - runningCost > 0:
            r = i + waiting // 4
            profit = (boarded + (waiting // 4) * 4) * boardingCost - runningCost * r
            if profit > max_profit:
                k = r
                max_profit = profit
            profit += (waiting % 4) * boardingCost - runningCost
            if profit > max_profit:
                k = r + 1
        return k