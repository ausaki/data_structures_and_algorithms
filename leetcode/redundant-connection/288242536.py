# title: redundant-connection
# detail: https://leetcode.com/submissions/detail/288242536/
# datetime: Tue Dec 24 22:58:13 2019
# runtime: 52 ms
# memory: 13.2 MB

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)
        degree = collections.Counter()
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            degree[u] += 1
            degree[v] += 1
        queue = collections.deque()
        for v in degree:
            if degree[v] == 1:
                queue.append(v)
        while queue:
            v = queue.popleft()
            degree.pop(v)
            u = graph[v].pop()
            graph.pop(v)
            graph[u].remove(v)
            degree[u] -= 1
            if degree[u] == 1:
                queue.append(u)
        for i in range(len(edges) - 1, -1, -1):
            u, v = edges[i]
            if u in degree and v in degree:
                return [u, v]
        