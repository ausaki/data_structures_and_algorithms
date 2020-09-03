# title: find-the-distance-value-between-two-arrays
# detail: https://leetcode.com/submissions/detail/385487623/
# datetime: Mon Aug 24 11:59:14 2020
# runtime: 100 ms
# memory: 14.1 MB

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        result = 0
        arr2.sort()
        m = len(arr2)
        for a in arr1:
            i = bisect.bisect(arr2, a)
            if i == 0 and arr2[0] - a > d:
                result += 1
            if i == m and a - arr2[-1] > d:
                result += 1
            if 0 < i < m and a - arr2[i - 1] > d and arr2[i] - a > d:
                result += 1
        return result