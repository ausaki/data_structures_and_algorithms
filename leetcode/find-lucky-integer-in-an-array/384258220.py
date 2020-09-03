# title: find-lucky-integer-in-an-array
# detail: https://leetcode.com/submissions/detail/384258220/
# datetime: Sat Aug 22 00:33:25 2020
# runtime: 92 ms
# memory: 14 MB

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = collections.Counter(arr)
        m = max(filter(lambda a: a[0] == a[1], c.items()), default=-1)
        if m == -1:
            return -1
        return m[0]
        