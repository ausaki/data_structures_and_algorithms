# title: construct-target-array-with-multiple-sums
# detail: https://leetcode.com/submissions/detail/387194040/
# datetime: Fri Aug 28 01:18:02 2020
# runtime: 272 ms
# memory: 19.4 MB

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        n = len(target)
        if n == 1 and target[0] != 1:
            return False
        s = sum(target)
        target.sort()
        while s != n:
            m = target.pop()
            if m == 1:
                break
            l = s - m
            if m <= l:
                return False
            m = m % l
            if m == 0:
                m = l
            s = m + l
            bisect.insort(target, m)
        return True