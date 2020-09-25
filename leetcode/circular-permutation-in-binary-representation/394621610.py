# title: circular-permutation-in-binary-representation
# detail: https://leetcode.com/submissions/detail/394621610/
# datetime: Sat Sep 12 22:37:08 2020
# runtime: 224 ms
# memory: 21.8 MB

class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        p = [0, 1]
        for m in range(1, n):
            p.extend(p[i] | (1 << m) for i in reversed(range(len(p))))
        i = p.index(start)
        return p[i:] + p[:i]