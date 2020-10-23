# title: count-subtrees-with-max-distance-between-cities
# detail: https://leetcode.com/submissions/detail/410251657/
# datetime: Sun Oct 18 22:29:39 2020
# runtime: 164 ms
# memory: 14.5 MB

class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        g = collections.defaultdict(list)
        for u, v in edges:
            g[u - 1].append(v - 1)
            g[v - 1].append(u - 1)
        dist = [[0] * n for i in range(n)]
        def bfs(start):
            visited = [0] * n
            q = collections.deque([start])
            visited[start] = 1
            d = 0
            while q:
                for _ in range(len(q)):
                    i = q.popleft()
                    dist[start][i] = d
                    for j in g[i]:
                        if not visited[j]:
                            visited[j] = 1
                            q.append(j)
                d += 1
        for i in range(n):
            bfs(i)
        result = [0] * (n - 1)
        subtrees = collections.deque()
        subtrees_dist = [0] * (1 << n)
        for i in range(n):
            sub = (1 << i)
            subtrees.append(sub)
        while subtrees:
            sub = subtrees.popleft()
            for j in range(n):
                if sub & (1 << j) == 0:
                    continue
                for k in g[j]:
                    if sub & (1 << k):
                        continue
                    sub2 = sub | (1 << k)
                    if subtrees_dist[sub2] > 0:
                        continue
                    d = max(dist[k][l] for l in range(n) if (1 << l) & sub)
                    d = max(d, subtrees_dist[sub])
                    subtrees_dist[sub2] = d
                    subtrees.append(sub2)
                    result[d - 1] += 1
        return result
            
                