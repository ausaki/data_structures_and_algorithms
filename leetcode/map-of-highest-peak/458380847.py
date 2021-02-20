# title: map-of-highest-peak
# detail: https://leetcode.com/submissions/detail/458380847/
# datetime: Sat Feb 20 23:04:25 2021
# runtime: 4060 ms
# memory: 79.4 MB

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
        mh = 0
        while q:
            i, j = q.popleft()
            for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                ii, jj = i + di, j + dj
                if 0 <= ii < n and 0 <= jj < m and res[ii][jj] == -1:
                    res[ii][jj] = h = res[i][j] + 1
                    q.append((ii, jj))
                    mh = max(mh, h)
        return res