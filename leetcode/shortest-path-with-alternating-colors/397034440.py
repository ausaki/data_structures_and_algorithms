# title: shortest-path-with-alternating-colors
# detail: https://leetcode.com/submissions/detail/397034440/
# datetime: Thu Sep 17 21:43:14 2020
# runtime: 80 ms
# memory: 13.8 MB

class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        g = collections.defaultdict(lambda: [[], []])
        for a, b in red_edges:
            g[a][0].append(b)
        for a, b in blue_edges:
            g[a][1].append(b)
        
        q = collections.deque([(0, 0, 0), (0, 0, 1)])
        visited = [[10 ** 9, 10 ** 9] for i in range(n)]
        visited[0] = [0, 0]
        while q:
            p, i, c = q.popleft()
            c = (c + 1) % 2
            for j in g[i][c]:
                if p + 1 < visited[j][c]:
                    visited[j][c] = p + 1
                    q.append((p + 1, j, c))
        return [min(i, j) if i < 10 ** 9 or j < 10 ** 9 else -1 for i, j in visited]        