# title: dota2-senate
# detail: https://leetcode.com/submissions/detail/287730759/
# datetime: Sun Dec 22 18:20:40 2019
# runtime: 76 ms
# memory: 13 MB

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = collections.deque(map(lambda s: 1 if s == 'R' else 0, senate))
        counter = {1: 0, 0: 0}
        while senate:
            for i in range(len(senate)):
                s = senate.popleft()
                o = (s + 1) % 2
                if counter[o] > 0:
                    counter[o] -= 1
                else:
                    counter[s] += 1
                    senate.append(s)
            if senate.count(1) == 0:
                return 'Dire'
            if senate.count(0) == 0:
                return 'Radiant'
            
            
