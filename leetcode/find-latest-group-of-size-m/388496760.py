# title: find-latest-group-of-size-m
# detail: https://leetcode.com/submissions/detail/388496760/
# datetime: Sun Aug 30 23:00:26 2020
# runtime: 1156 ms
# memory: 27.9 MB

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        groups = {}
        cnt = 0
        result = -1
        for i, a in enumerate(arr):
            b = a - 1
            if b in groups:
                l = groups.pop(b)
                groups[a] = groups[b - l + 1] = l + 1
            else:
                groups[a] = 1
            if groups[a] == m:
                cnt += 1
            elif groups[a] - 1 == m:
                cnt -= 1
            c = a + 1
            if c in groups:
                l = groups.pop(a)
                r = groups.pop(c)
                groups[c + r - 1] = groups[a - l + 1] = l + r
                cnt += (l + r) == m
                cnt -= (l == m) + (r == m)
            if cnt != 0:
                result = i + 1
        return result