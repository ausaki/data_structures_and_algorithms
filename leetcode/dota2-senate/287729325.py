# title: dota2-senate
# detail: https://leetcode.com/submissions/detail/287729325/
# datetime: Sun Dec 22 18:06:43 2019
# runtime: 48 ms
# memory: 12.7 MB

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        r = 0
        d = 0
        while True:
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
#             # print(new_senate)
#             if r > 0:
#                 for i in range(r):
#                     try:
#                         new_senate.remove('D')
#                     except:
#                         return 'Radiant'
                
#             if d > 0:
#                 for i in range(d):
#                     try:
#                         new_senate.remove('R')
#                     except:
#                         return 'Dire'
            if new_senate.count('R') == 0:
                return 'Dire'
            if new_senate.count('D') == 0:
                return 'Radiant'
            senate = new_senate