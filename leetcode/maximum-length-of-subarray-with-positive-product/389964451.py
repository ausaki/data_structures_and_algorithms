# title: maximum-length-of-subarray-with-positive-product
# detail: https://leetcode.com/submissions/detail/389964451/
# datetime: Wed Sep  2 22:08:03 2020
# runtime: 664 ms
# memory: 28.1 MB

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        p = n = 0
        result = 0
        for num in nums:
            if num > 0:
                p += 1
                n += n > 0
            elif num == 0:
                p = n = 0
            else:
                p, n = n + (n > 0), p + (p >= 0)
            result = max(result, p)
        return result
