# title: x-of-a-kind-in-a-deck-of-cards
# detail: https://leetcode.com/submissions/detail/404455051/
# datetime: Mon Oct  5 01:41:56 2020
# runtime: 128 ms
# memory: 14.6 MB

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        return functools.reduce(math.gcd, collections.Counter(deck).values()) >= 2
        