# title: circular-permutation-in-binary-representation
# detail: https://leetcode.com/submissions/detail/394630203/
# datetime: Sat Sep 12 23:03:59 2020
# runtime: 224 ms
# memory: 21.9 MB

class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        return [start ^ i ^ (i >> 1) for i in range(1 << n)]
            