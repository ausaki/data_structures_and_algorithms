# title: circular-permutation-in-binary-representation
# detail: https://leetcode.com/submissions/detail/394621260/
# datetime: Sat Sep 12 22:35:58 2020
# runtime: 204 ms
# memory: 21.7 MB

class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        p = [0, 1]
        for m in range(1, n):
            for i in reversed(range(len(p))):
                p.append(p[i] | (1 << m))
        i = p.index(start)
        return p[i:] + p[:i]