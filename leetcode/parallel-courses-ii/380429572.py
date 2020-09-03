# title: parallel-courses-ii
# detail: https://leetcode.com/submissions/detail/380429572/
# datetime: Fri Aug 14 01:44:24 2020
# runtime: 376 ms
# memory: 14.3 MB

from functools import lru_cache

class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        graph = collections.defaultdict(set)
        indegrees = {i: 0 for i in range(1, n + 1)}
        for c1, c2 in dependencies:
            graph[c1].add(c2)
            indegrees[c2] += 1
        
        @lru_cache(None)
        def plan(finished):
            result = n
            if not indegrees:
                return 0
            in0 = [c for c, d in indegrees.items() if d == 0]
            if len(in0) == len(indegrees):
                return (len(in0) + k - 1) // k
            combs = itertools.combinations(in0, k) if k < len(in0) else [in0]
            for nodes in combs:
                # print(nodes)
                for node in nodes:
                    indegrees.pop(node)
                    finished |= 1 << node
                    for nb in graph[node]:
                        indegrees[nb] -= 1
                result = min(result, plan(finished))
                for node in nodes:
                    indegrees[node] = 0
                    finished &= ~(1 << node)
                    for nb in graph[node]:
                        indegrees[nb] += 1
            # print(result + 1)
            return result + 1
        
        return plan(0)
                
        