# title: dota2-senate
# detail: https://leetcode.com/submissions/detail/287728919/
# datetime: Sun Dec 22 18:02:32 2019
# runtime: 52 ms
# memory: 12.7 MB

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        while True:
            r = 0
            d = 0
            new_senate = []
            for s in senate:
                if s == 'R':
                    if d > 0:
                        d -= 1
                    else:
                        r += 1
                        new_senate.append(s)
                else:
                    if r > 0:
                        r -= 1
                    else:
                        d += 1
                        new_senate.append(s)
            # print(new_senate)
            if r > 0:
                for i in range(r):
                    try:
                        new_senate.remove('D')
                    except:
                        return 'Radiant'
                
            if d > 0:
                for i in range(d):
                    try:
                        new_senate.remove('R')
                    except:
                        return 'Dire'
            senate = new_senate