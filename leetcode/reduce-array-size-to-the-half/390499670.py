# title: reduce-array-size-to-the-half
# detail: https://leetcode.com/submissions/detail/390499670/
# datetime: Thu Sep  3 23:09:07 2020
# runtime: 648 ms
# memory: 30.5 MB

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr) // 2
        q = [-v for v in collections.Counter(arr).values()]
        heapq.heapify(q)
        cnt = 0
        m = 0
        while q and m < n:
            m -= heapq.heappop(q)
            cnt += 1
        return cnt