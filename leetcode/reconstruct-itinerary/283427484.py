# title: reconstruct-itinerary
# detail: https://leetcode.com/submissions/detail/283427484/
# datetime: Tue Dec  3 19:02:33 2019
# runtime: 84 ms
# memory: 13.1 MB

from collections import defaultdict
class Solution:
    def findItinerary(self, tickets):
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []
        def visit(airport):
            print(airport)
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]
        