# title: tallest-billboard
# detail: https://leetcode.com/submissions/detail/403064787/
# datetime: Thu Oct  1 18:27:35 2020
# runtime: 708 ms
# memory: 14.4 MB

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)
        rods.sort()
        prefixsum = [0]
        for i in rods:
            prefixsum.append(prefixsum[-1] + i)
        s = prefixsum[-1]
        dp = [-1] * (s + 1) * 2
        dp[s] = 0
        for i in range(n - 1, -1, -1):
            new_dp = [-1] * (s + 1) * 2
            for d in range(prefixsum[i] + 1):
                if prefixsum[-1] - prefixsum[i] < d:
                    new_dp[d + s] = new_dp[-d + s] = -1
                    break
                for d in [-d, d]:
                    m = -1
                    if dp[rods[i] + d + s] >= 0:
                        m = max(m, dp[rods[i] + d + s] + rods[i])
                    if dp[d - rods[i] + s] >= 0:
                        m = max(m, dp[d - rods[i] + s])
                    if dp[d + s] >= 0:
                        m = max(m, dp[d + s])
                    new_dp[d + s] = m
            dp = new_dp
        return dp[s]
            