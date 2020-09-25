# title: number-of-submatrices-that-sum-to-target
# detail: https://leetcode.com/submissions/detail/399587700/
# datetime: Wed Sep 23 15:42:32 2020
# runtime: 1208 ms
# memory: 15.1 MB

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        result = 0
        for i in range(m):
            sums = [collections.Counter([0]) for k in range(i + 1)]
            for j in range(n):
                matrix[i][j] += (matrix[i][j - 1] if j else 0) + (matrix[i - 1][j] if i else 0) - (matrix[i - 1][j - 1] if i and j else 0)
                for k in range(i + 1):
                    a = matrix[i][j] - (matrix[k - 1][j] if k else 0)
                    s = a - target
                    if s in sums[k]:
                        result += sums[k][s]
                    sums[k][a] += 1
        return result
                    