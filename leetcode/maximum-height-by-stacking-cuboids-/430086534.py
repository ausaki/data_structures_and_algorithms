# title: maximum-height-by-stacking-cuboids-
# detail: https://leetcode.com/submissions/detail/430086534/
# datetime: Sun Dec 13 12:06:25 2020
# runtime: 168 ms
# memory: 14.5 MB

class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for cub in cuboids:
            cub.sort(reverse=True)
        cuboids.sort(reverse=True)
        
        n = len(cuboids)
        dp = [0] * n 
        for i in range(n): 
            dp[i] = cuboids[i][0]
        for i in range(1, n): 
            for j in range(i): 
                if (cuboids[i][0] <= cuboids[j][0] and
                    cuboids[i][1] <= cuboids[j][1] and 
                    cuboids[i][2] <= cuboids[j][2]): 
                    dp[i] = max(dp[i], dp[j] + cuboids[i][0])
        return max(dp)
        