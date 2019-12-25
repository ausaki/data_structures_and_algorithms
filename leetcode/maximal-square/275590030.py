# title: maximal-square
# detail: https://leetcode.com/submissions/detail/275590030/
# datetime: Sun Nov  3 21:36:38 2019
# runtime: 236 ms
# memory: 14.7 MB

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        N = len(matrix)
        if N == 0:
            return 0
        M = len(matrix[0])
        dp = [[0 for _ in range(M)] for _ in range(N)]
        result = 0
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == '0':
                    continue
                dp[i][j] = 1
                if dp[i][j] > result:
                    result = dp[i][j]
                if i - 1 < 0 or j - 1 < 0:
                    continue
                K = dp[i - 1][j - 1]
                if K == 0:
                    continue
                for k in range(K):
                    if matrix[i - k - 1][j] == '1' and matrix[i][j - k - 1] == '1':
                        dp[i][j] += 1
                    else:
                        break
                if dp[i][j] > result:
                    result = dp[i][j]
        print(dp)
        return result * result
                    