# title: sort-array-by-parity
# detail: https://leetcode.com/submissions/detail/405145948/
# datetime: Tue Oct  6 13:53:01 2020
# runtime: 72 ms
# memory: 14.6 MB

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i = -1
        for j, a in enumerate(A):
            if a % 2:
                continue
            i += 1
            A[i], A[j] = a, A[i]
        return A