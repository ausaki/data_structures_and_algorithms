# title: tallest-billboard
# detail: https://leetcode.com/submissions/detail/403065518/
# datetime: Thu Oct  1 18:31:15 2020
# runtime: 740 ms
# memory: 14.4 MB

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)
        rods.sort()
        prefixsum = [0]
        for i in rods:
            prefixsum.append(prefixsum[-1] + i)
        s = prefixsum[-1]
        dp = {0: 0}
        for i in range(n - 1, -1, -1):
            new_dp = {}
            for d in range(prefixsum[i] + 1):
                if prefixsum[-1] - prefixsum[i] < d:
                    break
                for d in [-d, d]:
                    m = -1
                    a = dp.get(rods[i] + d, -1)
                    if a >= 0:
                        m = a + rods[i]
                    new_dp[d] = max(m, dp.get(d - rods[i], -1), dp.get(d, -1))
            dp = new_dp
        return dp[0]
            