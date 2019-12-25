# title: minimum-path-sum
# detail: https://leetcode.com/submissions/detail/145532150/
# datetime: Sat Mar 17 15:34:08 2018
# runtime: 81 ms
# memory: N/A

def minPathSum_(grid, m, n, cache):
    if cache[m][n] >= 0:
        return cache[m][n]
    cache[m][n] = grid[m][n] + min(minPathSum_(grid, m, n + 1, cache), minPathSum_(grid, m + 1, n, cache))
    return cache[m][n]

def minPathSum(grid):
    """
    :param grid: list[list]
    [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    :return: 
    """
    row = len(grid)
    col = len(grid[0])
    cache = [[-1 for _ in range(col)] for _ in range(row)]
    for i in range(col):
        cache[row - 1][i] = sum(grid[row - 1][i:])
    for i in range(row):
        cache[i][col - 1] = sum([grid[j][col - 1] for j in range(i, row)])

    return minPathSum_(grid, 0, 0, cache)

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return minPathSum(grid)
        