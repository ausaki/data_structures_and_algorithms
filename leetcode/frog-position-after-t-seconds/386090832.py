# title: frog-position-after-t-seconds
# detail: https://leetcode.com/submissions/detail/386090832/
# datetime: Tue Aug 25 17:01:25 2020
# runtime: 100 ms
# memory: 14 MB

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        visited = {1}
        g = collections.defaultdict(list)
        for i, j in edges:
            g[i].append(j)
            g[j].append(i)
        def jump(i, p, t):
            l = len(g[i]) - (i != 1)
            if i == target:
                if l == 0 or t == 0:
                    return 1
                else:
                    return 0
            if t == 0:
                return 0
            for j in g[i]:
                if j == p:
                    continue
                prop = jump(j, i, t - 1)
                if prop:
                    return prop / l
            return 0
        return jump(1, 0, t)