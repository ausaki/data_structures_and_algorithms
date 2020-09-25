# title: convert-integer-to-the-sum-of-two-no-zero-integers
# detail: https://leetcode.com/submissions/detail/391383173/
# datetime: Sat Sep  5 23:42:58 2020
# runtime: 48 ms
# memory: 13.8 MB

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n // 2 + 1):
            if '0' not in str(i) + str(n - i):
                return [i, n - i]
        