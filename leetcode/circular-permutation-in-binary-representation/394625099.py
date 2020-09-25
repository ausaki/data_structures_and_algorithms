# title: circular-permutation-in-binary-representation
# detail: https://leetcode.com/submissions/detail/394625099/
# datetime: Sat Sep 12 22:48:22 2020
# runtime: 236 ms
# memory: 21.7 MB

class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        p = [0]
        while len(p) < 1 << n:
            p.append(p[-1] ^ 1)
            p.append(p[-1] ^ ((p[-1] & -p[-1]) << 1))
        p.pop()
        i = p.index(start)
        return p[i:] + p[:i]