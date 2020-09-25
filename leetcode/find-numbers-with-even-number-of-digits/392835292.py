# title: find-numbers-with-even-number-of-digits
# detail: https://leetcode.com/submissions/detail/392835292/
# datetime: Tue Sep  8 22:50:53 2020
# runtime: 44 ms
# memory: 14 MB

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum((len(str(num)) % 2 + 1) % 2 for num in nums)
            