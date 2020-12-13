# title: stone-game-vi
# detail: https://leetcode.com/submissions/detail/429897122/
# datetime: Sun Dec 13 00:24:14 2020
# runtime: 1268 ms
# memory: 25.9 MB

class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        pairs = sorted(zip(aliceValues, bobValues), key=sum, reverse=True)
        v = 0
        for i, (a, b) in enumerate(pairs):
            if i % 2 == 0:
                v += a
            else:
                v -= b
        return 1 if v > 0 else (-1 if v < 0 else 0)
    