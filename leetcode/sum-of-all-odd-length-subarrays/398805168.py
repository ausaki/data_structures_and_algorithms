# title: sum-of-all-odd-length-subarrays
# detail: https://leetcode.com/submissions/detail/398805168/
# datetime: Tue Sep 22 00:43:51 2020
# runtime: 28 ms
# memory: 13.7 MB

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        return sum(a * (i * (n - i) // 2 + (n - i - 1) // 2 + 1) for i, a in enumerate(arr))
