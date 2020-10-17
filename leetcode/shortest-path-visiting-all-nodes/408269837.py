# title: shortest-path-visiting-all-nodes
# detail: https://leetcode.com/submissions/detail/408269837/
# datetime: Tue Oct 13 23:47:27 2020
# runtime: 664 ms
# memory: 14.7 MB

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        def bfs(i):
            initial = (1 << i) * n + i
            q = collections.deque([initial])
            visited = [0] * ((1 << n) * n)
            visited[initial] = 1
            steps = 0
            while q:
                for _ in range(len(q)):
                    state = q.popleft()
                    m, j = divmod(state, n)
                    if m == (1 << n) - 1:
                        return steps
                    for k in graph[j]:
                        st = (m | (1 << k)) * n + k
                        if m | (1 << k) == (1 << n) - 1:
                            return steps + 1
                        if not visited[st]:
                            visited[st] = 1
                            q.append(st)
                steps += 1
        return min(bfs(i) for i in range(n))
        