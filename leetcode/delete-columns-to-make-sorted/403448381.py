# title: delete-columns-to-make-sorted
# detail: https://leetcode.com/submissions/detail/403448381/
# datetime: Fri Oct  2 16:04:35 2020
# runtime: 144 ms
# memory: 14.6 MB

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        D = 0
        for col in zip(*A):
            p = chr(0)
            for c in col:
                if c < p:
                    D += 1
                    break
                p = c
        return D