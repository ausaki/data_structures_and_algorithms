# title: jump-game-v
# detail: https://leetcode.com/submissions/detail/390767615/
# datetime: Fri Sep  4 12:05:35 2020
# runtime: 184 ms
# memory: 13.9 MB

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        arr.append(10 ** 6)
        n = len(arr)
        dp = [1] * n
        stack = []
        result = 0
        for i, a in enumerate(arr):
            while stack and arr[stack[-1]] < a:
                for j in range(len(stack) - 2, -1, -1):
                    if arr[stack[j]] != arr[stack[j + 1]]:
                        break
                else:
                    j = -1
                for k in range(len(stack) - j - 1):
                    l = stack.pop()
                    if i - l <= d:
                        dp[i] = max(dp[i], 1 + dp[l])
                    if j >= 0 and l - stack[j] <= d:
                        dp[stack[j]] = max(dp[stack[j]], 1 + dp[l])
            stack.append(i)
        dp.pop()
        return max(dp)
