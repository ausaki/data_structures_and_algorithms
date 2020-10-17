# title: transpose-matrix
# detail: https://leetcode.com/submissions/detail/406865171/
# datetime: Sat Oct 10 17:11:04 2020
# runtime: 72 ms
# memory: 14.7 MB

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(A[0])
        B = [[0] * m for i in range(n)]
        for i in range(m):
            for j in range(n):
                B[j][i] = A[i][j]
        return B