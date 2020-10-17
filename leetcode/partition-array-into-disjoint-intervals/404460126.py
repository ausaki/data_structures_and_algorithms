# title: partition-array-into-disjoint-intervals
# detail: https://leetcode.com/submissions/detail/404460126/
# datetime: Mon Oct  5 01:56:11 2020
# runtime: 176 ms
# memory: 18.1 MB

class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        n = len(A)
        max_ = -1
        mins = [n - 1]
        for i in range(n - 2, 0, -1):
            if A[i] < A[mins[-1]]:
                mins.append(i)
        for i in range(n - 1):
            a = A[i]
            if mins[-1] <= i:
                mins.pop()
            max_= max(max_, a)
            if max_ <= A[mins[-1]]:
                return i + 1
        