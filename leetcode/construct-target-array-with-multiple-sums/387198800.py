# title: construct-target-array-with-multiple-sums
# detail: https://leetcode.com/submissions/detail/387198800/
# datetime: Fri Aug 28 01:30:53 2020
# runtime: 280 ms
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
            s -= m
            if m <= s:
                return False
            m = m % s
            if m == 0:
                if s == 1:
                    return True
                return False
            s += m
            bisect.insort(target, m)
        return True