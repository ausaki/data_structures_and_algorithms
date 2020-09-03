# title: check-if-there-is-a-valid-path-in-a-grid
# detail: https://leetcode.com/submissions/detail/375738683/
# datetime: Tue Aug  4 12:29:55 2020
# runtime: 4972 ms
# memory: 566.1 MB

class Solution:
    def hasValidPath(self, A: List[List[int]]) -> bool:
        m, n = len(A), len(A[0])
        uf = {(i, j): (i, j) for i in range(-1, m * 2) for j in range(-1, n * 2)}

        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        def merge(i, j, di, dj):
            uf[find((i, j))] = find((i + di, j + dj))

        for i in range(m):
            for j in range(n):
                if A[i][j] in [2, 5, 6]: merge(i * 2, j * 2, -1, 0)
                if A[i][j] in [1, 3, 5]: merge(i * 2, j * 2, 0, -1)
                if A[i][j] in [2, 3, 4]: merge(i * 2, j * 2, 1, 0)
                if A[i][j] in [1, 4, 6]: merge(i * 2, j * 2, 0, 1)
        return find((0, 0)) == find((m * 2 - 2, n * 2 - 2))
        
        