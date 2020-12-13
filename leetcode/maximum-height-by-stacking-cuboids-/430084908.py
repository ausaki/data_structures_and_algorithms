# title: maximum-height-by-stacking-cuboids-
# detail: https://leetcode.com/submissions/detail/430084908/
# datetime: Sun Dec 13 12:01:13 2020
# runtime: 492 ms
# memory: 14.4 MB

class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        cubs = []
        for i, cub in enumerate(cuboids):
            cubs.append((cub[0], min(cub[1], cub[2]), max(cub[1], cub[2]), i))
            cubs.append((cub[1], min(cub[0], cub[2]), max(cub[0], cub[2]), i))
            cubs.append((cub[2], min(cub[0], cub[1]), max(cub[0], cub[1]), i))
        cubs.sort(reverse=True)
        
        n = len(cubs)
        dp = [0] * n 
        for i in range(n): 
            dp[i] = cubs[i][0]
        for i in range(1, n): 
            for j in range(i): 
                if (cubs[i][3] != cubs[j][3] and
                    cubs[i][0] <= cubs[j][0] and
                    cubs[i][1] <= cubs[j][1] and 
                    cubs[i][2] <= cubs[j][2]): 
                    dp[i] = max(dp[i], dp[j] + cubs[i][0])
        return max(dp)
        