# title: number-of-orders-in-the-backlog
# detail: https://leetcode.com/submissions/detail/470395941/
# datetime: Sun Mar 21 10:58:14 2021
# runtime: 1100 ms
# memory: 54 MB

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        sell = []
        buy = []
        for price, amount, type_ in orders:
            if type_ == 0:
                while sell and amount > 0 and sell[0][0] <= price:
                    p, a = sell[0]
                    min_a = min(a, amount)
                    a -= min_a
                    amount -= min_a
                    if a > 0:
                        sell[0][1] = a
                    else:
                        heapq.heappop(sell)
                if amount:
                    heapq.heappush(buy, [-price, amount])
            else:
                while buy and amount > 0 and -buy[0][0] >= price:
                    p, a = buy[0]
                    min_a = min(a, amount)
                    a -= min_a
                    amount -= min_a
                    if a > 0:
                        buy[0][1] = a
                    else:
                        heapq.heappop(buy)
                if amount:
                    heapq.heappush(sell, [price, amount])
        res = 0
        for _, amount in sell:
            res = (res + amount) % MOD
        for _, amount in buy:
            res = (res + amount) % MOD
        return res