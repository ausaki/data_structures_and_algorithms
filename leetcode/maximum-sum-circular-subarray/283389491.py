# title: maximum-sum-circular-subarray
# detail: https://leetcode.com/submissions/detail/283389491/
# datetime: Tue Dec  3 14:49:33 2019
# runtime: 596 ms
# memory: 16.8 MB

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
            curr_max = max(A[i], curr_max + A[i])
            curr_min = min(A[i], curr_min + A[i])
            max_sum = max(max_sum, curr_max)
            min_sum = min(min_sum, curr_min)
        return max(max_sum, total - min_sum) if total != min_sum else max_sum
        