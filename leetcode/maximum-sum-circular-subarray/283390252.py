# title: maximum-sum-circular-subarray
# detail: https://leetcode.com/submissions/detail/283390252/
# datetime: Tue Dec  3 14:53:15 2019
# runtime: 468 ms
# memory: 16.9 MB

class Solution:
    # def maxSubarraySumCircular(self, A: List[int]) -> int:
    #     N = len(A)
    #     res, curr = A[0], A[0]
    #     for i in range(1, N):
    #         curr = max(curr + A[i], A[i])
    #         res = max(res, curr)
    #     print(res)
    #     maxrightsum = [0] * N
    #     maxrightsum[-1] = A[-1]
    #     prev = A[-1]
    #     for i in range(N - 2, -1, -1):
    #         maxrightsum[i] = max(maxrightsum[i + 1], prev + A[i])
    #         prev += A[i]
    #     print(maxrightsum)
    #     prev = 0
    #     for i in range(0, N - 1):
    #         res = max(res, prev + A[i] + maxrightsum[i + 1])
    #         prev += A[i]
    #     return res        
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        total = max_sum = min_sum = curr_max = curr_min = A[0]
        for i in range(1, len(A)):
            total += A[i]
            curr_max = A[i] + (0 if curr_max <= 0 else curr_max)
            curr_min = A[i] + (curr_min if curr_min <= 0 else 0)
            if curr_max > max_sum: max_sum = curr_max
            if curr_min < min_sum: min_sum = curr_min
        if total == min_sum:
            return max_sum
        if max_sum > total - min_sum:
            return max_sum
        return total - min_sum
        