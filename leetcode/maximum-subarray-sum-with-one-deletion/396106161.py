# title: maximum-subarray-sum-with-one-deletion
# detail: https://leetcode.com/submissions/detail/396106161/
# datetime: Tue Sep 15 22:08:22 2020
# runtime: 456 ms
# memory: 23.9 MB

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return arr[0]
        maxsum = [0]
        for i in reversed(range(1, n)):
            if maxsum[-1] > 0:
                maxsum.append(maxsum[-1] + arr[i])
            else:
                maxsum.append(arr[i])
        s = 0
        result = -10 ** 6
        for i, a in enumerate(arr):
            r = maxsum.pop()
            if 0 < i < n - 1:
                result = max(result, s + r)
            if s > 0:
                s += a
            else:
                s = a
            result = max(result, s)
        return result