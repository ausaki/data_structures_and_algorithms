# title: circular-permutation-in-binary-representation
# detail: https://leetcode.com/submissions/detail/394628253/
# datetime: Sat Sep 12 22:57:51 2020
# runtime: 260 ms
# memory: 21.7 MB

class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        p = [i ^ (i >> 1) for i in range(1 << n)]
        # print(p)
        i = p.index(start)
        return p[i:] + p[:i]
            