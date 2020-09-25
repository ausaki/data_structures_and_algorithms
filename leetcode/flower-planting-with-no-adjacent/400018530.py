# title: flower-planting-with-no-adjacent
# detail: https://leetcode.com/submissions/detail/400018530/
# datetime: Thu Sep 24 14:50:48 2020
# runtime: 688 ms
# memory: 20.3 MB

class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        g = collections.defaultdict(list)
        for a, b in paths:
            g[a - 1].append(b - 1)
            g[b - 1].append(a - 1)
        C = {1, 2, 3, 4}
        color = [0] * N
        for i in range(N):
            if color[i]:
                continue
            s = C - set(color[j] for j in g[i])
            color[i] = s.pop()
        return color
                