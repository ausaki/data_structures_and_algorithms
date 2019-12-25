# title: smallest-sufficient-team
# detail: https://leetcode.com/submissions/detail/280359451/
# datetime: Wed Nov 20 23:25:45 2019
# runtime: 228 ms
# memory: 20.6 MB

from functools import lru_cache
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
#         encoding = {}
#         for i, sk in enumerate(req_skills):
#             encoding[sk] = 1 << i
        
#         skills = (1 << len(req_skills)) - 1
        
#         people_skills = {}
#         for i, sks in enumerate(people):
#             enc = 0
#             for sk in sks:
#                 enc |= encoding[sk]
#             if enc == 0:
#                 continue
#             people_skills[enc] = i
#         people_skills = list(people_skills.items())
        
#         @lru_cache(None)
#         def _dfs(skill, i):
#             if skill == 0:
#                 return []
#             if i >= len(people_skills):
#                 return -1
#             a = skill & people_skills[i][0]
#             if a:
#                 s1 = _dfs(skill ^ a, i + 1)
#                 s2 = _dfs(skill, i + 1)
#                 if s1 == -1:
#                     if s2 == -1:
#                         return -1
#                     else:
#                         return s2
#                 else:
#                     if s2 == -1:
#                         return s1 + [people_skills[i][1]]
#                     else:
#                         if len(s1) + 1 < len(s2):
#                             return s1 +  [people_skills[i][1]]
#                         else:
#                             return s2
#             else:
#                 return _dfs(skill, i + 1)
        
#         return _dfs(skills, 0)
        n, m = len(req_skills), len(people)
        key = {v: i for i, v in enumerate(req_skills)}
        dp = {0: []}
        for i, p in enumerate(people):
            his_skill = 0
            for skill in p:
                if skill in key:
                    his_skill |= 1 << key[skill]
            for skill_set, need in list(dp.items()):
                with_him = skill_set | his_skill
                if with_him == skill_set: continue
                if with_him not in dp or len(dp[with_him]) > len(need) + 1:
                    dp[with_him] = need + [i]
        return dp[(1 << n) - 1]
        
    