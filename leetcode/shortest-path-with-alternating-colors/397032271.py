# title: shortest-path-with-alternating-colors
# detail: https://leetcode.com/submissions/detail/397032271/
# datetime: Thu Sep 17 21:35:16 2020
# runtime: 96 ms
# memory: 14 MB

class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        g = collections.defaultdict(list)
        for a, b in red_edges:
            g[a].append([b, 0])
        for a, b in blue_edges:
            g[a].append([b, 1])
        
        q = [(0, 0, -1)]
        visited = [[10 ** 9, 10 ** 9] for i in range(n)]
        visited[0] = [0, 0]
        while q:
            p, i, c = heapq.heappop(q)
            for j, c_ in g[i]:
                if c_ != c and p + 1 < visited[j][c_]:
                    visited[j][c_] = p + 1
                    heapq.heappush(q, (p + 1, j, c_))
        return [min(i, j) if i < 10 ** 9 or j < 10 ** 9 else -1 for i, j in visited]        