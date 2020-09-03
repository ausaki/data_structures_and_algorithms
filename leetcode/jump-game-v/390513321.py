# title: jump-game-v
# detail: https://leetcode.com/submissions/detail/390513321/
# datetime: Thu Sep  3 23:45:04 2020
# runtime: 544 ms
# memory: 14.1 MB

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [0] * n
        new_arr = [(a, i) for i, a in enumerate(arr)]
        new_arr.sort()
        result = 0
        for a, i in new_arr:
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[j] >= a:
                    break
                dp[i] = max(dp[i], dp[j])
            for j in range(i - 1, max(i - d - 1, -1), -1):
                if arr[j] >= a:
                    break
                dp[i] = max(dp[i], dp[j])
            dp[i] += 1
            result = max(result, dp[i])
        return result
