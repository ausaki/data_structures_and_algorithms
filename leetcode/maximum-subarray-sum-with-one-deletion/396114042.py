# title: maximum-subarray-sum-with-one-deletion
# detail: https://leetcode.com/submissions/detail/396114042/
# datetime: Tue Sep 15 22:29:29 2020
# runtime: 268 ms
# memory: 23.8 MB

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        a, b = arr[0], 0
        result = a
        for i in range(1, n):
            a, b = max(arr[i], arr[i] + a), max(a, b + arr[i])
            result = max(result, a, b)
        return result