# title: interval-list-intersections
# detail: https://leetcode.com/submissions/detail/401851194/
# datetime: Mon Sep 28 23:48:56 2020
# runtime: 140 ms
# memory: 14.7 MB

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(B)
        i, j = 0, 0
        result = []
        while i < m and j < n:
            if A[i][1] < B[j][1]:
                if A[i][1] >= B[j][0]:
                    result.append([max(A[i][0], B[j][0]), A[i][1]])
                i += 1
            else:
                if B[j][1] >= A[i][0]:
                    result.append([max(A[i][0], B[j][0]), B[j][1]])
                j += 1
        return result            