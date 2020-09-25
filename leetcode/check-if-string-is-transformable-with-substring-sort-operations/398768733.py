# title: check-if-string-is-transformable-with-substring-sort-operations
# detail: https://leetcode.com/submissions/detail/398768733/
# datetime: Mon Sep 21 22:55:20 2020
# runtime: 808 ms
# memory: 18.1 MB

class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        n = len(s)
        pos = collections.defaultdict(collections.deque)
        for i, c in enumerate(s):
            pos[int(c)].append(i)
        i, j = 0, 0
        while i < n and j < n:
            a = int(s[i])
            b = int(t[j])
            if not pos[a] or i < pos[a][0]:
                i += 1
                continue
            if a == b:
                i += 1
                j += 1
                pos[a].popleft()
            elif a > b:
                if b not in pos or not pos[b]:
                    return False
                l = pos[b][0]
                h = 0
                for k in range(b):
                    if k not in pos:
                        continue
                    x = bisect.bisect(pos[k], l) - 1
                    if x >= 0:
                        x = pos[k][x] + 1
                    else:
                        x = -1
                    h = max(h, x)
                if h <= i:
                    j += 1
                    pos[b].popleft()
                else:
                    return False
            else:
                return False
        return True