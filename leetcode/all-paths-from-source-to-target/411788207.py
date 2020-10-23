# title: all-paths-from-source-to-target
# detail: https://leetcode.com/submissions/detail/411788207/
# datetime: Thu Oct 22 15:15:23 2020
# runtime: 96 ms
# memory: 17.2 MB

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        @lru_cache(None)
        def dp(i):
            if i == len(graph) - 1:
                return [[i]]
            return [[i] + p for j in graph[i] for p in dp(j)]
        return dp(0)