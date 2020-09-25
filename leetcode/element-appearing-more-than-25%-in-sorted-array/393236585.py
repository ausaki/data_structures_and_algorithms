# title: element-appearing-more-than-25%-in-sorted-array
# detail: https://leetcode.com/submissions/detail/393236585/
# datetime: Wed Sep  9 18:56:59 2020
# runtime: 92 ms
# memory: 15.1 MB

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        q = len(arr) // 4
        cnt = 0
        a = -1
        for b in arr:
            if a == b:
                cnt += 1
            else:
                cnt = 1
                a = b
            if cnt > q:
                return b
        