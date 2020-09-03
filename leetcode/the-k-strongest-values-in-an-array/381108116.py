# title: the-k-strongest-values-in-an-array
# detail: https://leetcode.com/submissions/detail/381108116/
# datetime: Sat Aug 15 14:46:51 2020
# runtime: 1492 ms
# memory: 30.6 MB

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        median = arr[(n - 1) // 2]
        return heapq.nlargest(k, arr, key=lambda a: (abs(a - median), a))
