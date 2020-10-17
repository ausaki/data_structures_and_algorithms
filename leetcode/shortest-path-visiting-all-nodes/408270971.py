# title: shortest-path-visiting-all-nodes
# detail: https://leetcode.com/submissions/detail/408270971/
# datetime: Tue Oct 13 23:51:07 2020
# runtime: 124 ms
# memory: 14.8 MB

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        q = collections.deque()
        visited = [0] * ((1 << n) * n)
        for i in range(n):
            state = (1 << i) * n + i 
            q.append(state)
            visited[state] = 1
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
        