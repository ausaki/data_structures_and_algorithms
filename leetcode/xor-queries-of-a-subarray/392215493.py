# title: xor-queries-of-a-subarray
# detail: https://leetcode.com/submissions/detail/392215493/
# datetime: Mon Sep  7 16:17:48 2020
# runtime: 408 ms
# memory: 28.4 MB

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xor = [0]
        for a in arr:
            xor.append(xor[-1] ^ a)
        return [xor[j + 1] ^ xor[i] for i, j in queries]
