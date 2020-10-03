# title: minimum-number-of-k-consecutive-bit-flips
# detail: https://leetcode.com/submissions/detail/401726243/
# datetime: Mon Sep 28 15:24:58 2020
# runtime: 788 ms
# memory: 14.9 MB

class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        result = 0
        flips = 0
        for i in range(n):
            if A[i] & 2:
                flips -= 1
            j = ((A[i] & 1) + flips % 2) % 2
            if j == 0:
                result += 1
                if i + K > n:
                    return -1
                flips += 1
                if i + K < n:
                    A[i + K] |= 2
        return result