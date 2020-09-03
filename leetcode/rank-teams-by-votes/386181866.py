# title: rank-teams-by-votes
# detail: https://leetcode.com/submissions/detail/386181866/
# datetime: Tue Aug 25 22:38:28 2020
# runtime: 76 ms
# memory: 14.1 MB

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes)
        if n == 1:
            return votes[0]
        m = len(votes[0])
        teams = {}
        for v in votes:
            for i, t in enumerate(v):
                if t not in teams:
                    teams[t] = [0] * m
                teams[t][i] += 1
        return ''.join(sorted(teams, key=lambda t: (teams[t], -ord(t)), reverse=True))
