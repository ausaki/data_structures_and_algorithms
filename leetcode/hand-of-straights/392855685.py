# title: hand-of-straights
# detail: https://leetcode.com/submissions/detail/392855685/
# datetime: Tue Sep  8 23:48:48 2020
# runtime: 188 ms
# memory: 15.3 MB

class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        counter = collections.Counter(hand)
        keys = sorted(counter)
        for i in keys:
            if counter[i] <= 0:
                continue
            for j in reversed(range(W)):
                counter[i + j] -= counter[i]
                if counter[i + j] < 0:
                    return False
        return True 