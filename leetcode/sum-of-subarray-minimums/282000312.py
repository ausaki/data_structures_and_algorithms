# title: sum-of-subarray-minimums
# detail: https://leetcode.com/submissions/detail/282000312/
# datetime: Wed Nov 27 14:19:36 2019
# runtime: 576 ms
# memory: 17.2 MB

import bisect
class Solution:
    def sumSubarrayMins1(self, A: List[int]) -> int:
        # 我这个方法和讨论区的stack方案非常类似
        dp = []
        res = 0
        cur = 0
        for n in A:
            item = [n, 1]
            while dp and dp[-1][0] > n:
                cur -= (dp[-1][0] - n) * dp[-1][1]
                item[1] += dp[-1][1]
                dp.pop()
            dp.append(item)
            cur += n
            res = (res + cur) % (10 ** 9 + 7)
        return res
    
    def sumSubarrayMins(self, A):
        N = len(A)
        left = [0] * N
        stack = []
        for i in range(N):
            cnt = 1
            while stack and A[i] <= stack[-1][0] :
                cnt += stack.pop()[1]
            stack.append([A[i], cnt])
            left[i] = cnt
        right = [0] * N
        stack = []
        for i in reversed(range(N)):
            cnt = 1
            while stack and  A[i] < stack[-1][0]:
                cnt += stack.pop()[1]
            stack.append([A[i], cnt])
            right[i] = cnt
        return sum(a * l * r for a, l, r in zip(A, left, right)) % (10 ** 9 + 7)