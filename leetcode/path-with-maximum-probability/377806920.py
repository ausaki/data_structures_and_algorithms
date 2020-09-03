# title: path-with-maximum-probability
# detail: https://leetcode.com/submissions/detail/377806920/
# datetime: Sat Aug  8 17:48:21 2020
# runtime: 772 ms
# memory: 25.9 MB

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = {}
        for i, edge in enumerate(edges):
            if edge[0] not in graph:
                graph[edge[0]] = []
            if edge[1] not in graph:
                graph[edge[1]] = []
            graph[edge[0]].append((edge[1], succProb[i]))
            graph[edge[1]].append((edge[0], succProb[i]))
        
        heap = [(-1, start)]
        visited = set()
        while heap:
            p, v = heapq.heappop(heap)
            if v == end:
                return -p
            visited.add(v)
            for vv, prob in graph.get(v, []):
                if vv in visited:
                    continue
                heapq.heappush(heap, (p * prob, vv))
        return 0
        