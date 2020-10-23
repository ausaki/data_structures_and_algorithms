# title: number-of-subarrays-with-bounded-maximum
# detail: https://leetcode.com/submissions/detail/411869764/
# datetime: Thu Oct 22 21:13:36 2020
# runtime: 412 ms
# memory: 15.4 MB

class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        stack = []
        result = 0
        for i, a in enumerate(A):
            while stack and a >= A[stack[-1][0]]:
                stack.pop()
            cnt = 0
            if L <= a <= R:
                cnt += i - (stack[-1][0] if stack else -1)
            if stack:
                cnt += stack[-1][1]
            stack.append([i, cnt])
            result += cnt
        return result