# title: number-of-restricted-paths-from-first-to-last-node
# detail: https://leetcode.com/submissions/detail/464517070/
# datetime: Sun Mar  7 11:22:26 2021
# runtime: 1740 ms
# memory: 62.2 MB

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))
        
        q = [(0, n)]
        dist = [math.inf] * (n + 1)
        dist[n] = 0
        while q:
            w, j = heapq.heappop(q)
            if w > dist[j]:
                continue
            for k, w_ in g[j]:
                d = w + w_
                if d < dist[k]:
                    heapq.heappush(q, (d, k))
                    dist[k] = d
        MOD = 10 ** 9 + 7
        
        @lru_cache(None)
        def dfs(i):
            if i == n:
                return 1
            d = dist[i]
            res = 0
            for j, w in g[i]:
                if dist[j] < d:
                    res = (res + dfs(j)) % MOD
            return res
        
        return dfs(1)