# title: reconstruct-a-2-row-binary-matrix
# detail: https://leetcode.com/submissions/detail/394456485/
# datetime: Sat Sep 12 12:14:48 2020
# runtime: 800 ms
# memory: 24.2 MB

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)
        mat = [[0] * n, [0] * n]
        for i, c in enumerate(colsum):
            if c == 0:
                mat[0][i] = mat[1][i] = 0
            elif c == 2:
                mat[0][i] = mat[1][i] = 1
                upper -= 1
                lower -= 1
            else:
                if upper > lower:
                    mat[0][i] = 1
                    upper -= 1
                    mat[1][i] = 0
                else:
                    mat[1][i] = 1
                    lower -= 1
                    mat[0][i] = 0
        return mat if upper == 0 and lower == 0 else []
                