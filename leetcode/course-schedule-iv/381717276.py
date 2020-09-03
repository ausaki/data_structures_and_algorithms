# title: course-schedule-iv
# detail: https://leetcode.com/submissions/detail/381717276/
# datetime: Sun Aug 16 21:06:30 2020
# runtime: 1076 ms
# memory: 16.9 MB

class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        g = collections.defaultdict(list)
        for c1, c2 in prerequisites:
            g[c2].append(c1)
        result = []
        cache = [[0] * n for i in range(n)]
        
        def build_cache(c):
            if c not in g:
                return
            if cache[c][c]:
                return 
            cache[c][c] = 1
            for c_ in g[c]:
                build_cache(c_)
                for i in range(n):
                    if cache[c_][i]:
                        cache[c][i] = 1
                cache[c][c_] = 1
        for c in g:
            build_cache(c)
        # print(cache)
#         def query(c1, c2):
#             if c1 == c2:
#                 return True
#             if c2 not in g:
#                 return False
#             for c in g[c2]:
#                 if query(c1, c):
#                     return True
#             return False
        
        for c1, c2 in queries:
            result.append(cache[c2][c2] and cache[c2][c1])
        return result