# title: sequential-digits
# detail: https://leetcode.com/submissions/detail/393129750/
# datetime: Wed Sep  9 13:05:09 2020
# runtime: 32 ms
# memory: 13.8 MB

class Solution:
    NUMS = [12, 23, 34, 45, 56, 67, 78, 89, 123, 234, 345, 456, 567, 678, 789, 1234, 2345, 3456, 4567, 5678, 6789, 12345, 23456, 34567, 45678, 56789, 123456, 234567, 345678, 456789, 1234567, 2345678, 3456789, 12345678, 23456789, 123456789]
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        i = bisect.bisect_left(self.NUMS, low)
        j = bisect.bisect(self.NUMS, high)
        return self.NUMS[i:j]