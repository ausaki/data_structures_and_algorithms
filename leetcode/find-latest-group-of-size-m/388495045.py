# title: find-latest-group-of-size-m
# detail: https://leetcode.com/submissions/detail/388495045/
# datetime: Sun Aug 30 22:55:06 2020
# runtime: 1168 ms
# memory: 27.7 MB

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
                if l + 1 == m:
                    cnt += 1
                if l == m:
                    cnt -= 1
            else:
                groups[a] = 1
                if m == 1:
                    cnt += 1
            c = a + 1
            if c in groups:
                l = groups.pop(a)
                r = groups.pop(c)
                groups[a - l + 1] = l + r
                groups[c + r - 1] = l + r
                if l + r == m:
                    cnt += 1
                if l == m :
                    cnt -= 1
                if r == m:
                    cnt -= 1
            if cnt != 0:
                result = i + 1
        return result