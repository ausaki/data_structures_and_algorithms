# title: delete-columns-to-make-sorted-ii
# detail: https://leetcode.com/submissions/detail/282676305/
# datetime: Sat Nov 30 21:13:40 2019
# runtime: 40 ms
# memory: 13 MB

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        deletion = set()
        while True:
            N = len(A)
            old = len(deletion)
            for i in range(N - 1):
                a = A[i]
                b = A[i + 1]
                for j in range(len(a)):
                    if j in deletion:
                        continue
                    if a[j] < b[j]:
                        break
                    if a[j] == b[j]:
                        continue
                    deletion.add(j)
            if len(deletion) == old:
                break
        return len(deletion)