# title: score-after-flipping-matrix
# detail: https://leetcode.com/submissions/detail/407312588/
# datetime: Sun Oct 11 18:15:53 2020
# runtime: 40 ms
# memory: 14.1 MB

class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        for i in range(m):
            flip = A[i][0] == 1
            for j in range(n):
                if flip:
                    A[i][j] = (A[i][j] + 1) % 2
                if i:
                    A[i][j] += A[i - 1][j]
        result = m * (1 << (n - 1))
        for j in range(1, n):
            result += max(A[m - 1][j], m - A[m - 1][j]) * (1 << (n - j - 1))
        return result
                
            