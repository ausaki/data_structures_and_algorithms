# title: find-valid-matrix-given-row-and-column-sums
# detail: https://leetcode.com/submissions/detail/409687512/
# datetime: Sat Oct 17 12:20:32 2020
# runtime: 924 ms
# memory: 18.8 MB

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        mat = []
        for i in range(m):
            row = []
            s = rowSum[i]
            mat.append(row)
            for j in range(n):
                if colSum[j] <= s:
                    row.append(colSum[j])
                    s -= colSum[j]
                    colSum[j] = 0
                else:
                    colSum[j] -= s
                    row.append(s)
                    s = 0
        return mat