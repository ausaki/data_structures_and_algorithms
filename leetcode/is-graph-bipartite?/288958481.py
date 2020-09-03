# title: is-graph-bipartite?
# detail: https://leetcode.com/submissions/detail/288958481/
# datetime: Fri Dec 27 21:33:18 2019
# runtime: 184 ms
# memory: 13.2 MB

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        A = set()
        B = set()
        queue = collections.deque()
        nodes = {i for i in range(len(graph)) if graph[i]}
        while nodes:
            node = nodes.pop()
            queue.append(node)
            A.add(node)
            while queue:
                i = queue.popleft()
                S, T = (A, B) if i in A else (B, A)
                for j in graph[i]:
                    if j in S:
                        return False
                    if j not in T:
                        T.add(j)
                        nodes.remove(j)
                        queue.append(j)
        return True