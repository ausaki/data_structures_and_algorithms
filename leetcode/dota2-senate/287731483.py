# title: dota2-senate
# detail: https://leetcode.com/submissions/detail/287731483/
# datetime: Sun Dec 22 18:27:44 2019
# runtime: 68 ms
# memory: 12.8 MB

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = collections.deque(senate)
        votes = {'R': 0, 'D': 0}
        left = {'R': senate.count('R'), 'D': senate.count('D')}
        while True:
            s = queue.popleft()
            o = 'D' if s == 'R' else 'R'
            if votes[o] > 0:
                votes[o] -= 1
                left[s] -= 1
            else:
                votes[s] += 1
                queue.append(s)
            if left['R'] == 0:
                return 'Dire'
            if left['D'] == 0:
                return 'Radiant'