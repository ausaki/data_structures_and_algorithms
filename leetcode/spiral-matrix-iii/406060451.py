# title: spiral-matrix-iii
# detail: https://leetcode.com/submissions/detail/406060451/
# datetime: Thu Oct  8 15:35:44 2020
# runtime: 104 ms
# memory: 14.9 MB

class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        result = [[r0, c0]]
        l = 3
        i, j = r0, c0 + 1
        while len(result) < R * C:
            for di in range(l - 1):
                if 0 <= i + di < R and 0 <= j < C:
                    result.append([i + di, j])
            i += l - 2
            for dj in range(1, l):
                if 0 <= i < R and 0 <= j - dj < C:
                    result.append([i, j - dj])
            j -= l - 1
            for di in range(1, l):
                if 0 <= i - di < R and 0 <= j < C:
                    result.append([i - di, j])
            i -= l - 1
            for dj in range(1, l):
                if 0 <= i < R and 0 <= j + dj < C:
                    result.append([i, j + dj])
            j += l
            l += 2
        return result