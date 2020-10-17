# title: sort-array-by-parity
# detail: https://leetcode.com/submissions/detail/405146323/
# datetime: Tue Oct  6 13:54:05 2020
# runtime: 76 ms
# memory: 14.7 MB

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return sorted(A, key=lambda a: a % 2)