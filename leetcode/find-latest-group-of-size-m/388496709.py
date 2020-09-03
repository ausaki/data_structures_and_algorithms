# title: find-latest-group-of-size-m
# detail: https://leetcode.com/submissions/detail/388496709/
# datetime: Sun Aug 30 23:00:15 2020
# runtime: 1956 ms
# memory: 27.8 MB

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