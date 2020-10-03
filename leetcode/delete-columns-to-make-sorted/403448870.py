# title: delete-columns-to-make-sorted
# detail: https://leetcode.com/submissions/detail/403448870/
# datetime: Fri Oct  2 16:06:35 2020
# runtime: 164 ms
# memory: 14.5 MB

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        D = 0
        for col in zip(*A):
            if not all(col[i] <= col[i + 1] for i in range(len(col) - 1)):
                D += 1
        return D