# title: valid-mountain-array
# detail: https://leetcode.com/submissions/detail/403446520/
# datetime: Fri Oct  2 15:57:35 2020
# runtime: 196 ms
# memory: 15.4 MB

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        i, n = 0, len(A)
        while i + 1 < n and A[i] < A[i + 1]:
            i += 1
        if i >= n - 1 or i == 0:
            return False
        while i + 1 < n and A[i] > A[i + 1]:
            i += 1
        return i == n - 1