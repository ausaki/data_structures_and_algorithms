# title: card-flipping-game
# detail: https://leetcode.com/submissions/detail/409082351/
# datetime: Thu Oct 15 23:14:16 2020
# runtime: 96 ms
# memory: 14.4 MB

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        idx = {f for f, b in zip(fronts, backs) if f == b}
        res = 2001
        for f, b in zip(fronts, backs):
            if f == b:
                continue
            if f not in idx:
                res = min(res, f)
            if b not in idx:
                res = min(res, b)
        return res if res < 2001 else 0