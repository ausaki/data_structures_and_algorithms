# title: closest-dessert-cost
# detail: https://leetcode.com/submissions/detail/461515301/
# datetime: Sun Feb 28 10:50:53 2021
# runtime: 548 ms
# memory: 14.3 MB

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        n, m = len(baseCosts), len(toppingCosts)
        min_diff = math.inf
        res = -1
        
        def dfs(i, t):
            nonlocal res, min_diff

            if i == m:
                for b in baseCosts:
                    diff = abs(t + b - target)
                    if diff < min_diff:
                        min_diff = diff
                        res = t + b
                    elif diff == min_diff:
                        res = min(res, t + b)
                return
            for j in [0, 1, 2]:
                dfs(i + 1, t + toppingCosts[i] * j)
        
        dfs(0, 0)
        return res