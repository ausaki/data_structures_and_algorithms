# title: shift-2d-grid
# detail: https://leetcode.com/submissions/detail/394156170/
# datetime: Fri Sep 11 18:33:36 2020
# runtime: 192 ms
# memory: 14.1 MB

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def reverse(i, j):
            while i < j:
                i1, i2 = divmod(i, n)
                j1, j2 = divmod(j, n)
                grid[i1][i2], grid[j1][j2] = grid[j1][j2], grid[i1][i2]
                i += 1
                j -= 1
        m, n = len(grid), len(grid[0])
        k %= m * n
        reverse(0, m * n - k - 1)
        reverse(m * n - k, m * n - 1)
        reverse(0, m * n - 1)
        return grid            