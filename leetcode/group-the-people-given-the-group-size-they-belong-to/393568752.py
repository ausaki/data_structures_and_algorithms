# title: group-the-people-given-the-group-size-they-belong-to
# detail: https://leetcode.com/submissions/detail/393568752/
# datetime: Thu Sep 10 11:59:13 2020
# runtime: 76 ms
# memory: 13.7 MB

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        g = {}
        result = []
        for i, sz in enumerate(groupSizes):
            gp = None
            if sz not in g:
                gp = []
                g[sz] = gp
                result.append(gp)
            else:
                gp = g[sz]
            gp.append(i)
            if len(gp) == sz:
                g.pop(sz)
        return result