# title: check-if-there-is-a-valid-path-in-a-grid
# detail: https://leetcode.com/submissions/detail/375731654/
# datetime: Tue Aug  4 12:11:59 2020
# runtime: 1568 ms
# memory: 137.7 MB

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        M = len(grid)
        N = len(grid[0])
        OPT_1 = [0, 1, {1, 3, 5}, 0]
        OPT_2 = [0, -1, {1, 4, 6}, 2]
        OPT_3 = [1, 0, {2, 5, 6}, 1]
        OPT_4 = [-1, 0, {2, 3, 4}, 3]
        cell_map = {
            1: {0: OPT_1, 2: OPT_2},
            2: {1: OPT_3, 3: OPT_4},
            3: {0: OPT_3, 3: OPT_2},
            4: {2: OPT_3, 3: OPT_1},
            5: {0: OPT_4, 1: OPT_2},
            6: {1: OPT_1, 2: OPT_4},
        }
        visited = set()
        def walk(i, j, from_):
            # print(i, j, from_)
            if i < 0 or i >= M or j < 0 or j >= N:
                return False
            if i == M - 1 and j == N - 1:
                return True
            if (i * N + j) in visited:
                return False
            cell = grid[i][j]
            cell_opt = cell_map[cell]
            if from_ not in cell_opt:
                return False
            next_cell = cell_opt[from_]
            ii = i + next_cell[0]
            jj = j + next_cell[1]
            if 0 <= ii < M and 0 <= jj < N and grid[ii][jj] in next_cell[2]:
                visited.add(i * N + j)
                res = walk(ii, jj, next_cell[3])
                visited.remove(i * N + j)
                return res
            return False
        
        cell = grid[0][0]
        if grid[M - 1][N - 1] ==4: return False
        if grid[0][0] == 5: return False
        if grid[0][0] == 1:
            return walk(0, 0, 0)
        if grid[0][0] == 2:
            return walk(0, 0, 1)
        if grid[0][0] == 3:
            return walk(0, 0, 0)
        if grid[0][0] == 4:
            if walk(0, 0, 2): return True
            return walk(0, 0, 3)
        if grid[0][0] == 6:
            return walk(0, 0, 1)
        
        