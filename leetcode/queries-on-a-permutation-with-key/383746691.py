# title: queries-on-a-permutation-with-key
# detail: https://leetcode.com/submissions/detail/383746691/
# datetime: Thu Aug 20 23:26:01 2020
# runtime: 152 ms
# memory: 13.8 MB

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = list(range(1, m + 1))
        result = []
        for q in queries:
            i = p.index(q)
            result.append(i)
            for j in range(i, 0, -1):
                p[j] = p[j - 1]
            p[0] = q
        return result