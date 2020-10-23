# title: all-paths-from-source-to-target
# detail: https://leetcode.com/submissions/detail/411786850/
# datetime: Thu Oct 22 15:11:24 2020
# runtime: 100 ms
# memory: 17.2 MB

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        @lru_cache(None)
        def dp(i):
            if i == n - 1:
                return [[n - 1]]
            path = []
            for j in graph[i]:
                path.extend([i] + p for p in dp(j))
            return path
        n = len(graph)
        return dp(0)