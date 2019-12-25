# title: dota2-senate
# detail: https://leetcode.com/submissions/detail/287730932/
# datetime: Sun Dec 22 18:22:19 2019
# runtime: 64 ms
# memory: 12.9 MB

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = collections.deque(senate)
        counter = {'R': 0, 'D': 0}
        while senate:
            for i in range(len(senate)):
                s = senate.popleft()
                o = 'D' if s == 'R' else 'R'
                if counter[o] > 0:
                    counter[o] -= 1
                else:
                    counter[s] += 1
                    senate.append(s)
            if senate.count('R') == 0:
                return 'Dire'
            if senate.count('D') == 0:
                return 'Radiant'
            
            
