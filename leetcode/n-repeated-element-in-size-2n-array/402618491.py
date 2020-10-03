# title: n-repeated-element-in-size-2n-array
# detail: https://leetcode.com/submissions/detail/402618491/
# datetime: Wed Sep 30 16:40:00 2020
# runtime: 176 ms
# memory: 15.3 MB

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for i in range(1, len(A)):
            if A[i] == A[i - 1] or (i - 2 >= 0 and A[i] == A[i - 2]):
                return A[i]
        return A[0]