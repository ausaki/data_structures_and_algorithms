# title: rank-transform-of-an-array
# detail: https://leetcode.com/submissions/detail/390959735/
# datetime: Fri Sep  4 23:32:27 2020
# runtime: 452 ms
# memory: 33.7 MB

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = [0] * n
        r = [(a, i) for i, a in enumerate(arr)]
        r.sort()
        k = 0
        b = 1e9 + 1
        for a, i in r:
            if a != b:
                k += 1
                b = a
            result[i] = k
        return result