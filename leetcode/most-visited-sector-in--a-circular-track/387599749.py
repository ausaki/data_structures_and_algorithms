# title: most-visited-sector-in--a-circular-track
# detail: https://leetcode.com/submissions/detail/387599749/
# datetime: Fri Aug 28 22:50:26 2020
# runtime: 36 ms
# memory: 13.9 MB

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        s = 0
        m = len(rounds)
        for i in range(1, m):
            s += (rounds[i] - rounds[i - 1] + n) % n
        s += 1
        s %= n
        if s == 0:
            return list(range(1, n + 1))
        result = [(rounds[0] - 1 + i) % n + 1 for i in range(s)]
        result.sort()
        return result