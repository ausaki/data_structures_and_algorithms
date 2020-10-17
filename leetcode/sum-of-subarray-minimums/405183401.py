# title: sum-of-subarray-minimums
# detail: https://leetcode.com/submissions/detail/405183401/
# datetime: Tue Oct  6 15:44:09 2020
# runtime: 420 ms
# memory: 18.3 MB

class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        MOD = 10 ** 9 + 7
        stack = []
        result = 0
        for i, a in enumerate(A):
            while stack and a <= A[stack[-1][0]]:
                stack.pop()
            s = 0
            if stack:
                s = stack[-1][1] + (i - stack[-1][0]) * a
            else:
                s = a * (i + 1)
            s %= MOD
            stack.append([i, s])
            result = (result + s) % MOD
        return result