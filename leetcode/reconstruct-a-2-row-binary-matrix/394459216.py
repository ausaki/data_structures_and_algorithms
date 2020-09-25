# title: reconstruct-a-2-row-binary-matrix
# detail: https://leetcode.com/submissions/detail/394459216/
# datetime: Sat Sep 12 12:23:56 2020
# runtime: 844 ms
# memory: 24.2 MB

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)
        mat = [[0] * n, [0] * n]
        for i, c in enumerate(colsum):
            mat[0][i] += c == 2 or (c == 1 and upper >= lower)
            mat[1][i] += c == 2 or (c == 1 and lower > upper)
            upper -= mat[0][i]
            lower -= mat[1][i]
        return mat if upper == 0 and lower == 0 else []
                