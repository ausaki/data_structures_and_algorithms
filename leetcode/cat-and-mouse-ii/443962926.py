# title: cat-and-mouse-ii
# detail: https://leetcode.com/submissions/detail/443962926/
# datetime: Sun Jan 17 12:34:02 2021
# runtime: 1080 ms
# memory: 26.9 MB

class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        '''
        这个和 https://leetcode.com/problems/cat-and-mouse/ 非常类似.
        
        我在比赛时直接复制上面那个题目的代码, 然后在修改代码时漏掉一个变量没有修改, 导致一直算不出正确答案.
        花了好多时间反复浏览代码才发现错误的地方, 代码中变量 m 表示 grid 的列宽, 但是复制的代码中 m 表示 mouse, 修改正确后提交成功了.
        
        会出现这个问题主要是代码没有注释和变量命名太过简单(m, n, c 之类的).
        '''
        m, n = len(grid), len(grid[0])
        encode = lambda p, c, m: (p, c, m)
        cat, mouse, food = -1, -1, -1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'C':
                    cat = i * n + j
                elif grid[i][j] == 'M':
                    mouse = i * n + j
                elif grid[i][j] == 'F':
                    food = i * n + j
        g = collections.defaultdict(list)
        outcomes = {}
        degrees = collections.Counter()
        for c in range(m * n):
            ci, cj = divmod(c, n)
            if grid[ci][cj] == '#':
                continue
            for ms in range(m * n):
                mi, mj = divmod(ms, n)
                if grid[mi][mj] == '#':
                    continue
                for p in range(2):
                    status = encode(p, c, ms)
                    if p == 0:
                        if c == ms or c == food:
                            outcomes[status] = 1
                        elif ms == food:
                            outcomes[status] = -1
                    else:
                        if ms == food:
                            outcomes[status] = 1
                        elif c == ms or c == food:
                            outcomes[status] = -1
                    if outcomes.get(status, 0):
                        continue
                    if p == 0:
                        st = encode((p + 1) % 2, c, ms)
                        g[st].append(status)
                        degrees[status] += 1
                        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                            cii, cjj = ci, cj
                            for i in range(catJump):
                                cii += di
                                cjj += dj
                                if not (0 <= cii < m and 0 <= cjj < n):
                                    break
                                if grid[cii][cjj] == '#':
                                    break
                                st = encode((p + 1) % 2, cii * n + cjj , ms)
                                g[st].append(status)
                                degrees[status] += 1
                                
                    else:
                        st = encode((p + 1) % 2, c, ms)
                        g[st].append(status)
                        degrees[status] += 1
                        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                            mii, mjj = mi, mj
                            for i in range(mouseJump):
                                mii += di
                                mjj += dj
                                if not (0 <= mii < m and 0 <= mjj < n):
                                    break
                                if grid[mii][mjj] == '#':
                                    break
                                st = encode((p + 1) % 2, c, mii * n + mjj)
                                g[st].append(status)
                                degrees[status] += 1
        def dfs(status, d):
            visited[status] = d
            for st in g[status]:
                if st in visited:
                    continue
                if outcomes[status] == -1:
                    outcomes[st] = 1
                else:
                    degrees[st] -= 1
                    if degrees[st] == 0:
                        outcomes[st] = -1
                    else:
                        continue
                dfs(st, d + 1)
        visited = {}
        for c in range(m * n):
            ci, cj = divmod(c, n)
            if grid[ci][cj] == '#':
                continue
            for ms in range(m * n):
                mi, mj = divmod(ms, n)
                if grid[mi][mj] == '#':
                    continue
                for p in range(2):
                    st = encode(p, c, ms)
                    if outcomes.get(st, 0) and st not in visited:
                        dfs(st, 0)
        init = encode(1, cat, mouse)
        o = outcomes.get(init, 0)
        return o == 1 and visited.get(init, 1001) <= 1000