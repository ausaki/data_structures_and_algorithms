# title: most-visited-sector-in--a-circular-track
# detail: https://leetcode.com/submissions/detail/387603646/
# datetime: Fri Aug 28 23:02:38 2020
# runtime: 36 ms
# memory: 14 MB

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        a, b = rounds[0], rounds[-1]
        if b >= a:
            return list(range(a, b + 1))
        return list(range(1, b + 1)) + list(range(a, n + 1))