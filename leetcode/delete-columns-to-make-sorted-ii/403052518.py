# title: delete-columns-to-make-sorted-ii
# detail: https://leetcode.com/submissions/detail/403052518/
# datetime: Thu Oct  1 17:28:05 2020
# runtime: 40 ms
# memory: 14.3 MB

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        m, n = len(A), len(A[0])
        relations = [0] * m
        deletions = 0
        for i in range(n):
            new = relations[:]
            for j in range(m - 1):
                if A[j][i] < A[j + 1][i]:
                    new[j] = -1
                if A[j][i] > A[j + 1][i] and relations[j] == 0:
                    deletions += 1
                    break
            else:
                relations = new
        return deletions