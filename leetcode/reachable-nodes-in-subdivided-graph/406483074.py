# title: reachable-nodes-in-subdivided-graph
# detail: https://leetcode.com/submissions/detail/406483074/
# datetime: Fri Oct  9 15:26:31 2020
# runtime: 508 ms
# memory: 21.1 MB

class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        g = collections.defaultdict(dict)
        for u, v, w in edges:
            g[u][v] = w
            g[v][u] = w
        q = [(0, 0)]
        visited = [10 ** 9 + 1 for i in range(N)]
        visited[0] = 0
        edges2 = set()
        edges3 = {}
        while q:
            m, u = heapq.heappop(q)
            if m > visited[u]:
                continue
            for v, w in g[u].items():
                mm = m + w + 1
                t = (min(u, v), max(u, v))
                if mm <= M:
                    edges2.add(t)
                else:
                    if t not in edges3:
                        edges3[t] = [0, 0]
                    if u < v:
                        edges3[t][0] = max(edges3[t][0], M - m)
                    else:
                        edges3[t][1] = max(edges3[t][1], M - m)
                if mm <= M and mm < visited[v]:
                    visited[v] = mm
                    heapq.heappush(q, (mm, v))
        result = 0
        nodes = set()
        for u, v in edges2:
            result += g[v].get(u, 0)
            nodes.add(u)
            nodes.add(v)
        result += len(nodes)
        if result == 0:
            result += 1
        for k, v in edges3.items():
            if k in edges2:
                continue
            result += min(sum(v), g[k[0]][k[1]])
        return result
