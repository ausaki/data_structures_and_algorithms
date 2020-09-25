# title: strange-printer-ii
# detail: https://leetcode.com/submissions/detail/399122860/
# datetime: Tue Sep 22 16:25:38 2020
# runtime: 1128 ms
# memory: 15 MB

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        grid = targetGrid
        m, n = len(grid), len(grid[0])
        colors = {}
        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                if c not in colors:
                    colors[c] = [i, j, i, j, 1]
                    continue
                l = colors[c]
                l[0] = min(l[0], i)
                l[1] = min(l[1], j)
                l[2] = max(l[2], i)
                l[3] = max(l[3], j)
                l[4] += 1
        q = collections.deque()
        g = collections.defaultdict(list)
        indeg = collections.Counter()
        for c, (t, l, b, r, cnt) in colors.items():
            if cnt == (b - t + 1) * (r - l + 1):
                q.append(c)
            else:
                for i in range(t, b + 1):
                    for j in range(l, r + 1):
                        if grid[i][j] != c:
                            # g[c].append(grid[i][j])
                            g[grid[i][j]].append(c)
                            indeg[c] += 1
        n = len(colors)
        while q:
            c = q.popleft()
            n -= 1
            for cc in g[c]:
                indeg[cc] -= 1
                if indeg[cc] == 0:
                    q.append(cc)
        return n == 0