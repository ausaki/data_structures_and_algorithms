# title: longest-mountain-in-array
# detail: https://leetcode.com/submissions/detail/408238826/
# datetime: Tue Oct 13 22:02:20 2020
# runtime: 160 ms
# memory: 14.9 MB

class Solution:
    def longestMountain(self, A: List[int]) -> int:
        i = 0
        n = len(A)
        result = 0
        while i < n - 1:
            while i < n - 1 and A[i] >= A[i + 1]:
                i += 1
            j = i
            while j < n - 1 and A[j] < A[j + 1]:
                j += 1
            if j >= n - 1:
                break
            while j < n - 1 and A[j] > A[j + 1]:
                j += 1
            if A[j] < A[j - 1]:
                result = max(result, j - i + 1)
            i = j
        return result