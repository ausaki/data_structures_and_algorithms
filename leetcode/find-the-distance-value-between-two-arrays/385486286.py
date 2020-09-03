# title: find-the-distance-value-between-two-arrays
# detail: https://leetcode.com/submissions/detail/385486286/
# datetime: Mon Aug 24 11:55:32 2020
# runtime: 180 ms
# memory: 14 MB

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        result = 0
        for a in arr1:
            for b in arr2:
                if abs(a - b) <= d:
                    break
            else:
                result += 1
        return result