# title: find-eventual-safe-states
# detail: https://leetcode.com/submissions/detail/411405206/
# datetime: Wed Oct 21 17:10:42 2020
# runtime: 672 ms
# memory: 21.2 MB

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        g = [[] for i in range(n)]
        indegrees = [0] * n
        for i, neighbors in enumerate(graph):
            for j in neighbors:
                g[j].append(i)
                indegrees[i] += 1
        q = collections.deque([i for i, deg in enumerate(indegrees) if deg == 0])
        result = []
        while q:
            i = q.popleft()
            result.append(i)
            for j in g[i]:
                indegrees[j] -= 1
                if indegrees[j] == 0:
                    q.append(j)
        result.sort()
        return result
        