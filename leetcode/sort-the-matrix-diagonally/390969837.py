# title: sort-the-matrix-diagonally
# detail: https://leetcode.com/submissions/detail/390969837/
# datetime: Sat Sep  5 00:05:14 2020
# runtime: 84 ms
# memory: 14 MB

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        dia = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                dia[i - j].append(mat[i][j])
        for d in dia.values():
            d.sort(reverse=True)
        for i in range(m):
            for j in range(n):
                mat[i][j] = dia[i - j].pop()
        return mat