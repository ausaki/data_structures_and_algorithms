# title: find-k-closest-elements
# detail: https://leetcode.com/submissions/detail/287489165/
# datetime: Sat Dec 21 15:16:27 2019
# runtime: 388 ms
# memory: 14.9 MB

import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        y = sorted([(abs(n - x), i) for i, n in enumerate(arr)])
        return sorted([arr[i] for _, i in y[:k]])