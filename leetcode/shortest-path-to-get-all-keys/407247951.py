# title: shortest-path-to-get-all-keys
# detail: https://leetcode.com/submissions/detail/407247951/
# datetime: Sun Oct 11 14:09:26 2020
# runtime: 2548 ms
# memory: 14.6 MB

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        si, sj = -1, -1
        n_keys = 0
        all_keys = [0] * 6
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    si, sj = i, j
                if grid[i][j].islower():
                    n_keys += 1
                    all_keys[ord(grid[i][j]) - 97] = i * n + j
                    
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
                    if ord(grid[i][j]) - 97 == find_key:
                        return moves
                    for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                        ii, jj = i + di, j + dj
                        pp = ii * n + jj
                        if test(ii, jj, collected_keys) and not visited[pp]:
                            if ord(grid[ii][jj]) - 97 == find_key:
                                return moves + 1
                            q.append(pp)
                            visited[pp] = 1
                moves += 1
            return math.inf
        
        @lru_cache(None)
        def dp(key, collected_keys):
            c_keys = collected_keys & ~(1 << key)
            if c_keys == 0:
                return bfs(si * n + sj, key, c_keys)
            result = math.inf
            for i in range(n_keys):
                if (c_keys >> i) & 1:
                    mo1 = dp(i, c_keys)
                    mo2 = bfs(all_keys[i], key, c_keys)
                    result = min(result, mo1 + mo2)
            return result
        
        result = min(dp(i, (1 << n_keys) - 1) for i in range(n_keys))
        return result if not math.isinf(result) else -1
            