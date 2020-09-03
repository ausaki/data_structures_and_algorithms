# title: find-the-distance-value-between-two-arrays
# detail: https://leetcode.com/submissions/detail/385488528/
# datetime: Mon Aug 24 12:01:44 2020
# runtime: 72 ms
# memory: 13.9 MB

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        result = 0
        arr1.sort()
        arr2.sort()
        m = len(arr2)
        i = 0
        for a in arr1:
            i = bisect.bisect(arr2, a, i, m)
            if i == 0 and arr2[0] - a > d:
                result += 1
            if i == m and a - arr2[-1] > d:
                result += 1
            if 0 < i < m and a - arr2[i - 1] > d and arr2[i] - a > d:
                result += 1
        return result