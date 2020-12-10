# title: sell-diminishing-valued-colored-balls
# detail: https://leetcode.com/submissions/detail/418053015/
# datetime: Sun Nov  8 18:06:20 2020
# runtime: 644 ms
# memory: 25.4 MB

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        def asum(a, b):
            return (a + b) * (b - a + 1) // 2
        
        MOD = 10 ** 9 + 7
        inventory.sort(reverse=True)
        ans = 0
        curr = inventory[0]
        cnt = 0
        i = 0
        n = len(inventory)
        while orders:
            while i < n and inventory[i] == curr:
                i += 1
                cnt += 1
            k = cnt * (curr - inventory[i]) if i < n else cnt * curr
            if orders > k:
                s = asum(inventory[i] + 1, curr) * cnt
                ans = (ans + s) % MOD
                orders -= k
                curr = inventory[i]
            else:
                q, r = divmod(orders, cnt)
                ans = (ans + asum(curr - q + 1, curr) * cnt + (curr - q) * r) % MOD
                orders = 0
        return ans