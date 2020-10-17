# title: positions-of-large-groups
# detail: https://leetcode.com/submissions/detail/408954918/
# datetime: Thu Oct 15 14:26:15 2020
# runtime: 24 ms
# memory: 14.2 MB

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        intervals = [[0, 0]]
        for i, c in enumerate(s):
            it = intervals[-1]
            if c == s[it[1]]:
                it[1] = i
            else:
                if it[1] - it[0] + 1 < 3:
                    intervals.pop()
                intervals.append([i, i])
        if intervals[-1][1] - intervals[-1][0] + 1 < 3:
            intervals.pop()
        intervals.sort()
        return intervals