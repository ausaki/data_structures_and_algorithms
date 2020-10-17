# title: shortest-path-to-get-all-keys
# detail: https://leetcode.com/submissions/detail/407235370/
# datetime: Sun Oct 11 13:29:53 2020
# runtime: 2540 ms
# memory: 14.1 MB

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        si, sj = -1, -1
        n_keys = 0
        all_keys = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    si, sj = i, j
                if grid[i][j].islower():
                    n_keys += 1
                    all_keys.append(grid[i][j])
                    
        def test(i, j, keys):
            if 0 <= i < m and 0 <= j < n and grid[i][j] != '#':
                if grid[i][j].isupper():
                    return keys & (1 << (ord(grid[i][j].lower()) - 97))
                return True
            return False
        @lru_cache(None)
        def bfs(start, find_key, collected_keys):
            q = collections.deque([start])
            moves = 0 
            visited = [0] * (m * n)
            visited[start] = 1
            while q:
                for _ in range(len(q)):
                    p = q.popleft()
                    i, j = divmod(p, n)
                    if grid[i][j] == find_key:
                        return p, moves
                    for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                        ii, jj = i + di, j + dj
                        pp = ii * n + jj
                        if test(ii, jj, collected_keys) and not visited[pp]:
                            q.append(pp)
                            visited[pp] = 1
                moves += 1
            return -1, math.inf
        
        result = math.inf
        for keys in itertools.permutations(all_keys):
            collected_keys = 0
            start = si * n + sj
            moves = 0
            for k in keys:
                start, mo = bfs(start, k, collected_keys)
                moves += mo
                collected_keys |= 1 << (ord(k) - 97)
                if start == -1:
                    moves = math.inf
                    break
            result = min(result, moves)
        return result if not math.isinf(result) else -1 