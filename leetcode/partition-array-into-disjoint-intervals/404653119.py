# title: partition-array-into-disjoint-intervals
# detail: https://leetcode.com/submissions/detail/404653119/
# datetime: Mon Oct  5 11:31:57 2020
# runtime: 164 ms
# memory: 18.1 MB

class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        n = len(A)
        left_max = curr_max = A[0]
        j = 1
        for i in range(1, n - 1):
            if left_max > A[i]:
                left_max = curr_max
                j = i + 1
            else:
                curr_max = max(curr_max, A[i])
        return j 