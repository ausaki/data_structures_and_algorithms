# title: largest-submatrix-with-rearrangements
# detail: https://leetcode.com/submissions/detail/443923052/
# datetime: Sun Jan 17 11:01:41 2021
# runtime: 1424 ms
# memory: 41.1 MB

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 0
        for i in range(m):
            bars = []
            for j in range(n):
                if matrix[i][j] == 0:
                    continue
                matrix[i][j] += matrix[i - 1][j] if i else 0
                heapq.heappush(bars, matrix[i][j])
            while bars:
                res = max(res, bars[0] * len(bars))
                heapq.heappop(bars)
        return res