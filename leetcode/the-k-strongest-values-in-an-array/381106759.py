# title: the-k-strongest-values-in-an-array
# detail: https://leetcode.com/submissions/detail/381106759/
# datetime: Sat Aug 15 14:43:09 2020
# runtime: 1576 ms
# memory: 30.5 MB

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        median = arr[(n - 1) // 2]
        nl = heapq.nlargest(k, ((abs(a - median), a) for a in arr))
        return [a[1] for a in nl]