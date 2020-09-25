# title: divide-array-in-sets-of-k-consecutive-numbers
# detail: https://leetcode.com/submissions/detail/392852884/
# datetime: Tue Sep  8 23:41:03 2020
# runtime: 444 ms
# memory: 28.7 MB

class Solution:
    def isPossibleDivide(self, A, k):
        c = collections.Counter(A)
        for i in sorted(c):
            if c[i] > 0:
                for j in range(k)[::-1]:
                    c[i + j] -= c[i]
                    if c[i + j] < 0:
                        return False
        return True
            