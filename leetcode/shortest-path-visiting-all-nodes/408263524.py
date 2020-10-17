# title: shortest-path-visiting-all-nodes
# detail: https://leetcode.com/submissions/detail/408263524/
# datetime: Tue Oct 13 23:26:45 2020
# runtime: 2856 ms
# memory: 14.9 MB

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        def bfs(i):
            q = collections.deque([i])
            visited = [0] * n
            visited[i] = 1
            steps = 0
            neighbors = []
            while q:
                for _ in range(len(q)):
                    j = q.popleft()
                    if j != i:
                        neighbors.append([j, steps])
                    for k in graph[j]:
                        if not visited[k]:
                            visited[k] = 1
                            q.append(k)
                steps += 1
            return neighbors
        n = len(graph)
        g = [bfs(i) for i in range(n)]
        def dijkstra(i):
            result = 0
            initial = (1 << i) * n + i
            q = [(0, initial)]
            dist = [math.inf] * ((1 << n) * n)
            dist[initial] = 0
            while q:
                d, state = heapq.heappop(q)
                if d > dist[state]:
                    continue
                m, j = divmod(state, n)
                if m == (1 << n) - 1:
                    return d
                for k, w in g[j]:
                    if (m >> k) & 1:
                        continue
                    st = (m | (1 << k)) * n + k
                    if d + w < dist[st]:
                        dist[st] = d + w
                        heapq.heappush(q, (d + w, st))
        
        return min(dijkstra(i) for i in range(n))
        