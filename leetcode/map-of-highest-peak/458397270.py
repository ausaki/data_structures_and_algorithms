# title: map-of-highest-peak
# detail: https://leetcode.com/submissions/detail/458397270/
# datetime: Sat Feb 20 23:41:23 2021
# runtime: 3700 ms
# memory: 79.6 MB

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n, m = len(isWater), len(isWater[0])
        q = collections.deque()
        res = [[-1] * m for i in range(n)]
        for i in range(n):
            for j in range(m):
                if isWater[i][j]:
                    res[i][j] = 0
                    q.append((i, j))
        while q:
            i, j = q.popleft()
            for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                ii, jj = i + di, j + dj
                if 0 <= ii < n and 0 <= jj < m and res[ii][jj] == -1:
                    res[ii][jj] = h = res[i][j] + 1
                    q.append((ii, jj))
        return res