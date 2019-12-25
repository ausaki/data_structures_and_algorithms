# title: permutations
# detail: https://leetcode.com/submissions/detail/142765438/
# datetime: Wed Feb 28 15:36:43 2018
# runtime: 78 ms
# memory: N/A

class Solution(object):
    def permute(self, iterable, r=None):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        pool = tuple(iterable)
        n = len(pool)
        r = n if r is None else r
        if r > n:
            return result
        indices = range(n)
        cycles = range(n, n-r, -1)
        result.append(list(pool[i] for i in indices[:r]))
        while n:
            for i in reversed(range(r)):
                cycles[i] -= 1
                if cycles[i] == 0:
                    indices[i:] = indices[i+1:] + indices[i:i+1]
                    cycles[i] = n - i
                else:
                    j = cycles[i]
                    indices[i], indices[-j] = indices[-j], indices[i]
                    result.append(list(pool[i] for i in indices[:r]))
                    break
            else:
                return result
        