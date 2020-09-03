# title: find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows
# detail: https://leetcode.com/submissions/detail/382749693/
# datetime: Tue Aug 18 23:50:30 2020
# runtime: 124 ms
# memory: 15.5 MB

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        n = len(mat)
        m = len(mat[0])
        heap = [(sum(mat[i][0] for i in range(n)), [0] * n)]
        prev = []
        while k > 0:
            val, cols = heapq.heappop(heap)
            if cols == prev:
                continue
            prev = cols
            k -= 1
            if k == 0:
                return val
            for i, j in enumerate(cols):
                if j < m - 1:
                    new_cols = list(cols)
                    new_cols[i] = j + 1
                    heapq.heappush(heap, (val + mat[i][j + 1] - mat[i][j], new_cols))
        
            