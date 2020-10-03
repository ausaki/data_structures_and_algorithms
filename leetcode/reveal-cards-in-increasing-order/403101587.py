# title: reveal-cards-in-increasing-order
# detail: https://leetcode.com/submissions/detail/403101587/
# datetime: Thu Oct  1 21:20:37 2020
# runtime: 44 ms
# memory: 14.4 MB

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort(reverse=True)
        result = [0] * n
        q = collections.deque(range(n))
        while q:
            result[q.popleft()] = deck.pop()
            if q: q.append(q.popleft())
        return result