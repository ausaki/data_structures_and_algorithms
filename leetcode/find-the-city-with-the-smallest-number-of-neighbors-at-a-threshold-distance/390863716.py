# title: find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance
# detail: https://leetcode.com/submissions/detail/390863716/
# datetime: Fri Sep  4 16:42:28 2020
# runtime: 1816 ms
# memory: 14.9 MB

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        g = collections.defaultdict(list)
        for f, t, w in edges:
            g[f].append((t, w))
            g[t].append((f, w))
        
        def bfs(i):
            q = [(0, i)]
            visited = {i}
            while q:
                w, j = heapq.heappop(q)
                visited.add(j)
                for k, w_ in g[j]:
                    if k not in visited and w + w_ <= distanceThreshold:
                        heapq.heappush(q, (w + w_, k))
            return visited
        
        return -min([(len(bfs(i)), -i) for i in range(n)])[1]