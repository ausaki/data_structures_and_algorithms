# title: find-in-mountain-array
# detail: https://leetcode.com/submissions/detail/397500377/
# datetime: Fri Sep 18 23:28:26 2020
# runtime: 28 ms
# memory: 14.6 MB

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        class Wrap:
            def __init__(self, l, r, rev=False):
                self.l = l
                self.r = r
                self.rev = rev
            def __getitem__(self, i):
                return A.get(self.l + i) if not self.rev else A.get(self.r - i)
            def __len__(self):
                return self.r - self.l + 1
            
        A = mountain_arr
        L = A.length()
        i, j = 0, L - 1
        while i <= j:
            m = (i + j) // 2
            v = A.get(m)
            w = A.get(m - 1) if m else -1
            if w < v:
                i = m + 1
            else:
                j = m - 1
        # print(i, j)
        i = j
        l = Wrap(0, i)
        k = bisect.bisect_left(l, target)
        if k >= len(l):
            return -1
        if l[k] == target:
            return k
        r = Wrap(i + 1, L - 1, True)
        k = bisect.bisect_left(r, target)
        if k >= len(r):
            return -1
        if r[k] == target:
            return L - 1 - k
        return -1