# title: check-if-string-is-transformable-with-substring-sort-operations
# detail: https://leetcode.com/submissions/detail/398773113/
# datetime: Mon Sep 21 23:08:58 2020
# runtime: 672 ms
# memory: 18.5 MB

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        idx, pos = [[] for _ in range(10)], [0 for _ in range(10)]
        for i, ch in enumerate(s):
            idx[int(ch)].append(i)
        for ch in t:
            d = int(ch)
            if pos[d] >= len(idx[d]):
                return False
            for i in range(d):
                if pos[i] < len(idx[i]) and idx[i][pos[i]] < idx[d][pos[d]]:
                    return False
            pos[d] += 1
        return True
