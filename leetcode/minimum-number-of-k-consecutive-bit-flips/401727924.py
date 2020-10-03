# title: minimum-number-of-k-consecutive-bit-flips
# detail: https://leetcode.com/submissions/detail/401727924/
# datetime: Mon Sep 28 15:30:33 2020
# runtime: 796 ms
# memory: 14.9 MB

class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        result = 0
        flips = 0
        for i in range(n):
            j = ((A[i] & 1) + flips % 2) % 2
            if j == 0:
                result += 1
                if i + K - 1 >= n:
                    return -1
                flips += 1
                A[i + K - 1] |= 2
            if A[i] & 2:
                flips -= 1
        return result