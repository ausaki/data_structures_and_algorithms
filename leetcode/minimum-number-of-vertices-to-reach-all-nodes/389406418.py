# title: minimum-number-of-vertices-to-reach-all-nodes
# detail: https://leetcode.com/submissions/detail/389406418/
# datetime: Tue Sep  1 20:19:08 2020
# runtime: 1840 ms
# memory: 52.8 MB

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes = {i for i in range(n)}
        for f, t in edges:
            nodes.discard(t)
        return nodes