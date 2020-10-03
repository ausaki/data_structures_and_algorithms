# title: tallest-billboard
# detail: https://leetcode.com/submissions/detail/403066289/
# datetime: Thu Oct  1 18:34:57 2020
# runtime: 716 ms
# memory: 14.4 MB

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)
        rods.sort()
        prefixsum = [0]
        for i in rods:
            prefixsum.append(prefixsum[-1] + i)
        dp = {0: 0}
        for i in range(n - 1, -1, -1):
            new_dp = {}
            for d in range(prefixsum[i] + 1):
                if prefixsum[-1] - prefixsum[i] < d:
                    break
                for d in [-d, d]:
                    a = max(dp.get(rods[i] + d, -rods[i] - 1) + rods[i], dp.get(d - rods[i], -1), dp.get(d, -1))
                    if a != -1:
                        new_dp[d] = a
            dp = new_dp
        return dp[0]
            