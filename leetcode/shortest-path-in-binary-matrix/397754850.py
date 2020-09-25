# title: shortest-path-in-binary-matrix
# detail: https://leetcode.com/submissions/detail/397754850/
# datetime: Sat Sep 19 15:17:35 2020
# runtime: 720 ms
# memory: 14.2 MB

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1:
            return -1
        q = collections.deque([0])
        steps = 1
        while q:
            for i in range(len(q)):
                p = q.popleft()
                i, j = divmod(p, n)
                if i == j == n - 1:
                    return steps
                for di, dj in itertools.product([-1, 0, 1], [-1, 0, 1]):
                    if di == dj == 0:
                        continue
                    ii, jj = i + di, j + dj
                    if 0 <= ii < n and 0 <= jj < n and grid[ii][jj] == 0:
                        if ii == jj == n - 1:
                            return steps + 1
                        grid[ii][jj] = 1
                        q.append(ii * n + jj)
            steps += 1
        return -1