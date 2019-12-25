# title: minimum-height-trees
# detail: https://leetcode.com/submissions/detail/282473334/
# datetime: Fri Nov 29 21:07:59 2019
# runtime: 328 ms
# memory: 24 MB

from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        path = defaultdict(list)
        for v1, v2 in edges:
            path[v1].append([v2, -1])
            path[v2].append([v1, -1])
        
        def _dfs(p, i):
            m = 0
            for j in path[i]:
                if j[0] == p:
                    continue
                if j[1] > 0:
                    h = j[1]
                else:
                    h = _dfs(i, j[0])
                    j[1] = h
                if h > m:
                    m = h
            return m + 1
        
        res = []
        mh = n
        for i in range(n):
            h = _dfs(-1, i)
            if h < mh:
                mh = h
                res = [i]
            elif h == mh:
                res.append(i)
        return res