# title: element-appearing-more-than-25%-in-sorted-array
# detail: https://leetcode.com/submissions/detail/393240286/
# datetime: Wed Sep  9 19:13:54 2020
# runtime: 92 ms
# memory: 15.2 MB

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        q = n // 4
        if q == 0:
            return arr[0]
        cnt = 0
        a = -1
        for i in range(q, n, q):
            l = bisect.bisect_left(arr, arr[i], 0, i)
            r = bisect.bisect(arr, arr[i], i + 1, n)
            if r - l > q:
                return arr[i]
        
        