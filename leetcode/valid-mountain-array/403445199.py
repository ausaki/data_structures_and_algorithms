# title: valid-mountain-array
# detail: https://leetcode.com/submissions/detail/403445199/
# datetime: Fri Oct  2 15:53:03 2020
# runtime: 328 ms
# memory: 15.2 MB

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] < A[i + 1]:
                i += 1
            if A[j] < A[j - 1]:
                j -= 1
            elif i + 1 >= len(A) or A[i] >= A[i + 1]:
                break
        return i == j and 0 < i < len(A) - 1