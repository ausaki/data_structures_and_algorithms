# title: arithmetic-slices
# detail: https://leetcode.com/submissions/detail/277060906/
# datetime: Fri Nov  8 22:11:58 2019
# runtime: 2356 ms
# memory: 223 MB

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        '''
        dp[i][j] = dp[i + 1][j] and A[i + 1] - A[i] == A[i + 2] - A[i + 1]
        '''
        N = len(A)
        dp = [[0 for _ in range(N)] for _ in range(N)]
        count = 0
        for i in reversed(range(N - 2)):
            for j in range(i + 2, N):
                if j == i + 2:
                    if A[j] - A[j - 1] == A[j - 1] - A[j - 2]:
                        dp[i][j] = 1
                        count += 1
                else:
                    if dp[i + 1][j] and A[i + 1] - A[i] == A[i + 2] - A[i + 1]:
                        dp[i][j] = 1
                        count += 1
        return count
        