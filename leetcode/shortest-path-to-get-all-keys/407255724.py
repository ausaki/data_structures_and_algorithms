# title: shortest-path-to-get-all-keys
# detail: https://leetcode.com/submissions/detail/407255724/
# datetime: Sun Oct 11 14:33:46 2020
# runtime: 2156 ms
# memory: 14.9 MB

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
                        return p, moves
                    for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                        ii, jj = i + di, j + dj
                        pp = ii * n + jj
                        if test(ii, jj, collected_keys) and not visited[pp]:
                            if ord(grid[ii][jj]) - 97 == find_key:
                                return pp, moves + 1
                            q.append(pp)
                            visited[pp] = 1
                moves += 1
            return -1, math.inf
        
        def encode_state(p, keys):
            return keys * m * n + p
        
        def decode_state(state):
            keys, p = divmod(state, m * n)
            return p, keys
        
        initial = encode_state(si * n + sj, 0)
        q = [(0, initial)]
        dist = [math.inf] * ((1 << n_keys) * m * n)
        dist[initial] = 0
        
        while q:
            moves, state = heapq.heappop(q)
            p, keys = decode_state(state)
            if keys == (1 << n_keys) - 1:
                return moves
            if moves > dist[state]:
                continue
            for k in range(n_keys):
                if (keys >> k) & 1 == 0:
                    pp, mo = bfs(p, k, keys)
                    st = encode_state(pp, keys | (1 << k))
                    if moves + mo < dist[st]:
                        dist[st] = moves + mo
                        heapq.heappush(q, (moves + mo, st))
        return -1
            