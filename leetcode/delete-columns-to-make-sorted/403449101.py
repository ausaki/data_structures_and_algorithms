# title: delete-columns-to-make-sorted
# detail: https://leetcode.com/submissions/detail/403449101/
# datetime: Fri Oct  2 16:07:24 2020
# runtime: 168 ms
# memory: 14.4 MB

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        return sum(any(col[i] > col[i + 1] for i in range(len(col) - 1)) for col in zip(*A))
