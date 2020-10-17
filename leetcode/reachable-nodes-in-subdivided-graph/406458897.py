# title: reachable-nodes-in-subdivided-graph
# detail: https://leetcode.com/submissions/detail/406458897/
# datetime: Fri Oct  9 14:09:12 2020
# runtime: 528 ms
# memory: 21.3 MB

class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        g = collections.defaultdict(dict)
        for u, v, w in edges:
            g[u][v] = w
            g[v][u] = w
        q = [(0, 0, 0)]
        visited = [[10 ** 9 + 1, -1] for i in range(N)]
        visited[0] = [0, -1]
        while q:
            m, u, p = heapq.heappop(q)
            if m > visited[u][0]:
                continue
            for v, w in g[u].items():
                if v == p:
                    continue
                mm = m + w + 1
                if mm <= M and mm < visited[v][0]:
                    visited[v][0] = mm
                    visited[v][1] = u
                    heapq.heappush(q, (mm, v, u))
        edges2 = set()
        edges3 = {}
        for u, (m, v) in enumerate(visited):
            if m > M:
                continue
            edges2.add((min(u, v), max(u, v)))
            for k, w in g[u].items():
                if k == v:
                    continue
                t = (min(u, k), max(u, k))
                if m + w + 1 <= M:
                    edges2.add(t)
                else:
                    if t not in edges3:
                        edges3[t] = [0, 0]
                    if u < k:
                        edges3[t][0] = max(edges3[t][0], M - m)
                    else:
                        edges3[t][1] = max(edges3[t][1], M - m)
        result = 0
        nodes = set()
        for u, v in edges2:
            result += g[v].get(u, 0)
            nodes.add(u)
            nodes.add(v)
        result += len(nodes) - 1
        for k, v in edges3.items():
            if k in edges2:
                continue
            result += min(sum(v), g[k[0]][k[1]])
        return result
