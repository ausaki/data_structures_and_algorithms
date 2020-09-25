# title: minimum-absolute-difference
# detail: https://leetcode.com/submissions/detail/395536203/
# datetime: Mon Sep 14 17:57:08 2020
# runtime: 480 ms
# memory: 27.8 MB

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        n = len(arr)
        result = []
        v = 10 ** 8
        for i in range(n - 1):
            a = arr[i + 1] - arr[i]
            if a > v:
                continue
            if a < v:
                v = a
                result.clear()
            result.append([arr[i], arr[i + 1]])
        return result