# title: minimum-absolute-difference
# detail: https://leetcode.com/submissions/detail/395536904/
# datetime: Mon Sep 14 17:59:48 2020
# runtime: 520 ms
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
                result = []
            result.append([arr[i], arr[i + 1]])
        return result