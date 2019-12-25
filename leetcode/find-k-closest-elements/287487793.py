# title: find-k-closest-elements
# detail: https://leetcode.com/submissions/detail/287487793/
# datetime: Sat Dec 21 15:07:20 2019
# runtime: 376 ms
# memory: 14 MB

import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        N = len(arr)
        i = bisect.bisect_left(arr, x)
        if i == N or (i != 0 and arr[i] != x):
            i -= 1
        j = i + 1
        res = collections.deque()
        while k > 0:
            if j >= len(arr) or (i >= 0 and x - arr[i] <= arr[j] - x):
                res.appendleft(arr[i])
                i -= 1
            else:
                res.append(arr[j])
                j += 1
            k -= 1
        return res