# title: hamming-distance
# detail: https://leetcode.com/submissions/detail/280086683/
# datetime: Tue Nov 19 18:20:20 2019
# runtime: 20 ms
# memory: 12.7 MB

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        n = x ^ y
        result = 0
        while n:
            n &= n - 1
            result += 1
        return result