# title: construct-target-array-with-multiple-sums
# detail: https://leetcode.com/submissions/detail/387200731/
# datetime: Fri Aug 28 01:36:09 2020
# runtime: 264 ms
# memory: 19.6 MB

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        n = len(target)
        if n == 1 and target[0] != 1:
            return False
        s = sum(target)
        target.sort()
        while s != n:
            m = target.pop()
            s -= m
            if m <= s:
                return False
            m %= s
            if m == 0:
                return s == 1
            s += m
            bisect.insort(target, m)
        return True