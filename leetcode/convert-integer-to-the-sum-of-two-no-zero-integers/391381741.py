# title: convert-integer-to-the-sum-of-two-no-zero-integers
# detail: https://leetcode.com/submissions/detail/391381741/
# datetime: Sat Sep  5 23:40:25 2020
# runtime: 44 ms
# memory: 13.8 MB

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n // 2 + 1):
            j = n - i
            if '0' not in str(i) and '0' not in str(j):
                return [i, j]
        