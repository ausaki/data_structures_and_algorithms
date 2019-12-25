# title: smallest-sufficient-team
# detail: https://leetcode.com/submissions/detail/280350764/
# datetime: Wed Nov 20 22:23:56 2019
# runtime: 260 ms
# memory: 51.9 MB

from functools import lru_cache
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        encoding = {}
        for i, sk in enumerate(req_skills):
            encoding[sk] = 1 << i
        
        skills = (1 << len(req_skills)) - 1
        
        people_skills = {}
        for i, sks in enumerate(people):
            enc = 0
            for sk in sks:
                enc |= encoding[sk]
            if enc == 0:
                continue
            people_skills[enc] = i
        people_skills = list(people_skills.items())
        # N = len(people_skills)
        # dp = [[[] for _ in range(N + 1)] for _ in range(skills + 1)]
        # sk = 0
        # for i in range(1, skills + 1):
        #     dp[i][N] = -1
        #     for j in reversed(range(N)):
        #         s = people_skills[j][0] & i
        #         if s:
        #             a = dp[i ^ s][j + 1]
        #             b = dp[i][j + 1]
        #             if a == -1:
        #                 if b == -1:
        #                     dp[i][j] = -1
        #                 else:
        #                     dp[i][j] = list(b)
        #             else:
        #                 if b == -1:
        #                     dp[i][j] = a + [people_skills[j][1]]
        #                 else:
        #                     if len(a) + 1 < len(b):
        #                         dp[i][j] = a + [people_skills[j][1]]
        #                     else:
        #                         dp[i][j] = list(b)
        #         else:
        #             dp[i][j] = list(dp[i][j + 1]) if dp[i][j + 1] != -1 else -1
        # return dp[skills][0]
        
        @lru_cache(None)
        def _dfs(skill, i):
            if skill == 0:
                return []
            if i >= len(people_skills):
                return -1
            a = skill & people_skills[i][0]
            if a:
                s1 = _dfs(skill ^ a, i + 1)
                s2 = _dfs(skill, i + 1)
                if s1 == -1:
                    if s2 == -1:
                        return -1
                    else:
                        return s2
                else:
                    if s2 == -1:
                        return s1 + [people_skills[i][1]]
                    else:
                        if len(s1) + 1 < len(s2):
                            return s1 +  [people_skills[i][1]]
                        else:
                            return s2
            else:
                return _dfs(skill, i + 1)
        
        return _dfs(skills, 0)
        
        