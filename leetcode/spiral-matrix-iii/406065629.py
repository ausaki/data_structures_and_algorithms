# title: spiral-matrix-iii
# detail: https://leetcode.com/submissions/detail/406065629/
# datetime: Thu Oct  8 15:51:37 2020
# runtime: 100 ms
# memory: 14.9 MB

class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        result = [[r0, c0]]
        l = 3
        i, j = r0, c0 + 1
        while len(result) < R * C:
            if 0 <= j < C and i < R and i + l - 2 >= 0:
                for ii in range(max(i, 0), min(i + l - 1, R)):
                    result.append([ii , j])
            i += l - 2
            if 0 <= i < R and j - l + 1 < C and j - 1 >= 0:
                for jj in range(min(j - 1, C - 1), max(j - l, -1), -1):
                    result.append([i, jj])
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