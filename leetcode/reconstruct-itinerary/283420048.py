# title: reconstruct-itinerary
# detail: https://leetcode.com/submissions/detail/283420048/
# datetime: Tue Dec  3 17:50:44 2019
# runtime: 104 ms
# memory: 13.5 MB

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        N = len(tickets)
        for f, t in tickets:
            if f not in graph:
                graph[f] = {}
            if t not in graph[f]:
                graph[f][t] = 0
            graph[f][t] += 1
        def dfs(node, n):
            if n == 0:
                return True
            next_node = sorted(filter(lambda item: item[1] > 0, graph.get(node, {}).items()), key=lambda item: item[0])
            if not next_node:
                return False
            for to, _ in next_node:
                graph[node][to] -= 1
                path.append(to)
                p = dfs(to, n - 1)
                graph[node][to] += 1
                if p:
                    return True
                path.pop()
            return False
        
        path = ['JFK']
        dfs('JFK', N)
        return path
        