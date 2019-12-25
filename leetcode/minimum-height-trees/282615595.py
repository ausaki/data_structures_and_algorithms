# title: minimum-height-trees
# detail: https://leetcode.com/submissions/detail/282615595/
# datetime: Sat Nov 30 13:18:39 2019
# runtime: 232 ms
# memory: 17.4 MB

from collections import defaultdict, deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        path = defaultdict(set)
        for v1, v2 in edges:
            path[v1].add(v2)
            path[v2].add(v1)
        leaves = [v for v, w in path.items() if len(w) == 1]
        while n > 2:
            n -= len(leaves)
            new = []
            for i in leaves:
                j = path[i].pop()
                path[j].remove(i)
                if len(path[j]) == 1:
                    new.append(j)
            leaves = new
        return leaves