# title: find-kth-largest-xor-coordinate-value
# detail: https://leetcode.com/submissions/detail/446984615/
# datetime: Sun Jan 24 11:06:26 2021
# runtime: 4912 ms
# memory: 37 MB

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        res = []
        for i in range(m):
            for j in range(n):
                matrix[i][j] ^= ((matrix[i][j - 1] if j else 0) ^ 
                                (matrix[i - 1][j] if i else 0) ^ 
                                (matrix[i - 1][j - 1] if i and j else 0))
                if len(res) < k:
                    heapq.heappush(res, matrix[i][j])
                else:
                    if matrix[i][j] > res[0]:
                        heapq.heappushpop(res, matrix[i][j])
        return res[0]
                