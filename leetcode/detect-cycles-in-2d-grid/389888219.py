# title: detect-cycles-in-2d-grid
# detail: https://leetcode.com/submissions/detail/389888219/
# datetime: Wed Sep  2 17:37:37 2020
# runtime: 2512 ms
# memory: 131.1 MB

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def find(pos):
            if parents[pos] != pos:
                parents[pos] = find(parents[pos])
            return parents[pos]

        def union(pos1, pos2):
            parent1, parent2 = find(pos1), find(pos2)
            if parent1 != parent2:
                if ranks[parent2] > ranks[parent1]:
                    parents[parent1] = parent2
                else:
                    parents[parent2] = parent1
                    if ranks[parent1] == ranks[parent2]:
                        ranks[parent1] += 1

        rows, cols = len(grid), len(grid[0])
        parents = {(i, j): (i, j) for i in range(rows) for j in range(cols)}
        ranks = collections.Counter()
        for i, row in enumerate(grid):
            for j, letter in enumerate(row):
                if i > 0 and j > 0 and grid[i-1][j] == grid[i][j-1] == letter and find((i-1, j)) == find((i, j-1)):
                    return True
                for r, c in (i - 1, j), (i, j - 1):
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == letter:
                        union((i, j), (r, c))
        return False