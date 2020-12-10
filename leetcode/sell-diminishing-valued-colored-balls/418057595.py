# title: sell-diminishing-valued-colored-balls
# detail: https://leetcode.com/submissions/detail/418057595/
# datetime: Sun Nov  8 18:30:20 2020
# runtime: 652 ms
# memory: 25 MB

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = 10 ** 9 + 7
        
        def asum(a, b):
            return (a + b) * (b - a + 1) // 2
        
        inventory.sort(reverse=True)
        n = len(inventory)
        inventory.append(0)
        ans = 0
        curr = inventory[0]
        cnt = 0
        i = 0
        while orders:
            while i < n and inventory[i] == curr:
                i += 1
                cnt += 1
            k = cnt * (curr - inventory[i])
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