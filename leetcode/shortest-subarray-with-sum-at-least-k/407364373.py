# title: shortest-subarray-with-sum-at-least-k
# detail: https://leetcode.com/submissions/detail/407364373/
# datetime: Sun Oct 11 22:19:25 2020
# runtime: 1076 ms
# memory: 21.7 MB

class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        s = 0
        stack = [[0, -1]]         
        n = len(A)
        result = n + 1
        for i in range(len(A)):
            s += A[i]
            while stack and s <= stack[-1][0]:
                stack.pop()
            stack.append([s, i])
            s1 = s - K
            j = bisect.bisect(stack, [s1, n])
            if j > 0 and stack:
                result = min(result, i - stack[j - 1][1])
        return result if result < n + 1 else -1