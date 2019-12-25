# title: maximum-sum-circular-subarray
# detail: https://leetcode.com/submissions/detail/283387706/
# datetime: Tue Dec  3 14:41:26 2019
# runtime: 672 ms
# memory: 16.9 MB

class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        N = len(A)
        res, curr = A[0], A[0]
        for i in range(1, N):
            curr = max(curr + A[i], A[i])
            res = max(res, curr)
        print(res)
        maxrightsum = [0] * N
        maxrightsum[-1] = A[-1]
        prev = A[-1]
        for i in range(N - 2, -1, -1):
            maxrightsum[i] = max(maxrightsum[i + 1], prev + A[i])
            prev += A[i]
        print(maxrightsum)
        prev = 0
        for i in range(0, N - 1):
            res = max(res, prev + A[i] + maxrightsum[i + 1])
            prev += A[i]
        return res        
            
        