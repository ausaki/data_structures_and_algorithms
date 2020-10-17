# title: magic-squares-in-grid
# detail: https://leetcode.com/submissions/detail/408276454/
# datetime: Wed Oct 14 00:08:39 2020
# runtime: 36 ms
# memory: 14.2 MB

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def test(i, j):
            if not (i + 2 < m and j + 2 < n):
                return False
            cols = [0] * 3
            rows = [0] * 3
            dia1 = 0
            dia2 = 0
            digits = [0] * 10
            for di in range(3):
                for dj in range(3):
                    val = grid[i + di][j + dj]
                    if not (1 <= val <= 9) or digits[val]:
                        return False
                    digits[val] = 1
                    rows[di] += val
                    cols[dj] += val
                    if di == dj:
                        dia1 += val
                    if di + dj == 2:
                        dia2 += val
            return len(set(cols) | set(rows) | set([dia1, dia2])) == 1
        
        return sum(test(i, j) for i in range(m) for j in range(n))
