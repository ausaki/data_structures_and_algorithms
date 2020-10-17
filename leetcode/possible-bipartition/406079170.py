# title: possible-bipartition
# detail: https://leetcode.com/submissions/detail/406079170/
# datetime: Thu Oct  8 16:38:32 2020
# runtime: 692 ms
# memory: 22 MB

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        g = collections.defaultdict(list)
        for a, b in dislikes:
            g[a - 1].append(b - 1)
            g[b - 1].append(a - 1)
            
        def dfs(i, parent, k):
            visited[i] = k
            for j in g[i]:
                if j == parent:
                    continue
                if visited[j]:
                    if (k - visited[j] + 1) % 2:
                        return True
                    continue
                if dfs(j, i, k + 1):
                    return True
            return False
        
        visited = [0] * N
        for i in range(N):
            if not visited[i]:
                if dfs(i, -1, 1):
                    return False
        return True