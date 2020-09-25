# title: find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance
# detail: https://leetcode.com/submissions/detail/390864833/
# datetime: Fri Sep  4 16:47:07 2020
# runtime: 404 ms
# memory: 14.9 MB

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        g = collections.defaultdict(list)
        for f, t, w in edges:
            g[f].append((t, w))
            g[t].append((f, w))
        
        def bfs(i):
            q = [(0, i)]
            dist = [distanceThreshold + 1] * n
            visited = {i}
            while q:
                w, j = heapq.heappop(q)
                visited.add(j)
                for k, w_ in g[j]:
                    d = w + w_
                    if k not in visited and d <= distanceThreshold and d < dist[k]:
                        heapq.heappush(q, (d, k))
                        dist[k] = d
            return len(visited)
        
        return -min([(bfs(i), -i) for i in range(n)])[1]