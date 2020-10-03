# title: reveal-cards-in-increasing-order
# detail: https://leetcode.com/submissions/detail/403101162/
# datetime: Thu Oct  1 21:18:48 2020
# runtime: 44 ms
# memory: 14.5 MB

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort(reverse=True)
        result = [0] * n
        q = collections.deque(range(n))
        while q:
            i = q.popleft()
            if q:
                q.append(q.popleft())
            result[i] = deck.pop()
        return result