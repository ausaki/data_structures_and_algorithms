# title: minimum-number-of-vertices-to-reach-all-nodes
# detail: https://leetcode.com/submissions/detail/389389924/
# datetime: Tue Sep  1 19:12:05 2020
# runtime: 1268 ms
# memory: 51.6 MB

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegrees = [0] * n
        for f, t in edges:
            indegrees[t] += 1
        result = [i for i, j in enumerate(indegrees) if j == 0]
        return result