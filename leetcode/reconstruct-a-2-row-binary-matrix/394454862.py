# title: reconstruct-a-2-row-binary-matrix
# detail: https://leetcode.com/submissions/detail/394454862/
# datetime: Sat Sep 12 12:09:30 2020
# runtime: 788 ms
# memory: 24.1 MB

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)
        mat = [[0] * n, [0] * n]
        m = 0
        for i, c in enumerate(colsum):
            if c == 0:
                mat[0][i] = mat[1][i] = 0
                m += 1
            elif c == 2:
                mat[0][i] = mat[1][i] = 1
                upper -= 1
                lower -= 1
                m += 1
            if upper < 0 or lower < 0:
                return []
        if n - m != upper + lower:
            return []
        for i, c in enumerate(colsum):
            if c == 1:
                if upper:
                    mat[0][i] = 1
                    mat[1][i] = 0
                    upper -= 1
                else:
                    mat[0][i] = 0
                    mat[1][i] = 1
                    lower -= 1
        return mat
                